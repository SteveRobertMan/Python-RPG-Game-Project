import time
import random
import copy 
from rich.panel import Panel
from rich.table import Table
from rich.layout import Layout
from rich.columns import Columns
import config 

from ui_components import clear_screen, get_player_input
from entities import ELEMENT_NAMES, get_element_color, get_tier_roman, to_subscript, StatusEffect

DURATION_ONLY_EFFECTS = ["Bind", "Haste", "Pierce Affinity", "Riposte"]
DUAL_STACK_EFFECTS =  ["Bleed", "Rupture", "Fairylight", "Poise"]

"""
--------------------------------------------------------------------------------
CORE DATA STRUCTURES & BATTLE SYSTEM PROPERTIES
--------------------------------------------------------------------------------
The Battle System heavily relies on the 'Entity' class from entities.py.
Below is a breakdown of the essential properties used during combat logic:
1. ENTITY STATE
   self.hp            -> Current Health. If <= 0, unit is dead/incapacitated.
   self.max_hp        -> Cap for healing effects.
   self.resistances   -> List of 7 floats (0.0 to 2.0+). 
                         Matches ELEMENT_NAMES indices (Eros, Philia, etc.).
                         Used in execute_skill to multiply incoming elemental damage.
2. CARD/DECK MANAGEMENT
   self.hand          -> List of Skill objects currently available to play.
   self.deck          -> Draw pile. Refilled from discard_pile when empty.
   self.discard_pile  -> Used Skill objects go here.
   self.intent        -> (Enemy Only) Tuple of (Skill, TargetUnit, HandIndex).
                         Determined at start of turn, executed on Enemy Turn.
3. TEMPORARY MODIFIERS (Reset every turn in battle_loop)
   self.temp_modifiers = {
       "final_dmg_reduction": (int) Flat damage subtraction at the very end of calculation.
                                    Used by: Defend, Flail Around, Rally.
       "outgoing_dmg_mult":   (float) Multiplier for damage dealt BY this unit.
                                    Default 1.0. Altered by Buffs/Debuffs.
       "incoming_dmg_mult":   (float) Multiplier for damage TAKEN by this unit.
                                    Default 1.0. >1.0 means vulnerability.
       "incoming_dmg_flat":   (int) Flat damage added to incoming hits (before defense).
                                    Used for "Fragile" type effects.
   }
4. SPECIAL MECHANICS (Persistent or Specific Triggers)
   self.next_hit_taken_flat_bonus -> (int) Added damage to the NEXT single hit this unit receives.
                                     Consumed immediately upon taking damage.
                                     Used by: Benikawa's Skill I.
   self.next_hit_deal_flat_bonus  -> (int) Added damage to the NEXT single hit this unit deals.
                                     Consumed immediately upon dealing damage.
                                     Used by: Bulky Delinquent's Skill I.
   self.nerve_disruption_turns    -> (int) Hidden Flag. If > 0, unit deals -80% damage.
                                     Decrements at end of turn.
                                     Used by: Benikawa (ninja)'s Nerve Disruption.
   self.status_effects            -> List of StatusEffect objects.
                                     Handled in 'process_turn_end_effects' and 'execute_skill'.
                                     Common Effects: Bleed (Logic in execute_skill), Bind, Regen.
   self.pending_bind              -> (int) DYNAMIC ATTRIBUTE (Added by BattleManager).
                                     Stores Bind count to be applied next turn to prevent
                                     immediate decay or immediate penalty on the same turn.
    How does adding status effects with both potency and count for the ‘first time’ work?
    1. When adding 'potency' while the target has no ‘count’, the duration/count inflicted always starts at +1 count.
    2. When adding ‘count' while the target has no ‘potency’, the potency inflicted always starts at 1.
    ! Whether or not this debuff can be stacked well by the attacker of the target is up to them. If the effect runs out easily, then that is the result.
--------------------------------------------------------------------------------
"""

class BattleManager:
    def __init__(self):
        self.allies = []
        self.enemies = []
        self.turn_count = 1
        self.battle_log = []
        self.is_battle_over = False
        self.won = False
        self.ally_action_queue = []
        self.auto_battle = False 

    def start_battle(self, allies, enemies, stage_id=0):
        self.allies = allies
        self.enemies = enemies
        self.turn_count = 1
        self.battle_log = ["Battle Start!"]
        self.is_battle_over = False
        self.won = False
        self.auto_battle = False
        self.stage_id = stage_id
        
        for unit in self.allies + self.enemies:
            unit.refresh_deck()
            unit.draw_skills(2)
            # Reset Statuses
            unit.status_effects = []
            # Reset Hidden Flags
            unit.nerve_disruption_turns = 0 
            unit.pending_bind = 0
            unit.pending_haste = 0
            
            unit.temp_modifiers = {
                "outgoing_dmg_mult": 1.0,
                "incoming_dmg_mult": 1.0,
                "incoming_dmg_flat": 0,
                "final_dmg_reduction": 0
            }

        self.render_battle_screen()
        time.sleep(1.0)
        self.battle_loop()

    def battle_loop(self):
        while not self.is_battle_over:
            # --- START OF TURN PHASE ---
            for unit in self.allies + self.enemies:
                # Modifiers reset at start of turn
                if self.turn_count > 1:
                    unit.reset_turn_modifiers()
                    unit.apply_next_turn_modifiers() # Apply delayed modifiers
                
                # Apply Status Effect Modifiers (Buffs/Debuffs/Hidden Flags)
                self.apply_status_modifiers(unit)
                
                unit.auto_target = None 

            self.assign_auto_targets(self.allies, self.enemies)
            self.assign_auto_targets(self.enemies, self.allies) 
            self.generate_enemy_intents()

            # --- COMMAND PHASE ---
            self.handle_player_command_phase()
            if self.check_win_condition(): return
            if self.is_battle_over: return # Catch retreat
            
            # --- RESOLUTION PHASE ---
            if not self.is_battle_over:
                self.resolve_combat_start_effects()

            if not self.is_battle_over:
                self.execute_player_actions()
                if self.check_win_condition(): return

            if not self.is_battle_over:
                self.render_battle_screen()
                time.sleep(1.0) 
                self.battle_log = [] 
                self.render_battle_screen() 

            if not self.is_battle_over:
                self.log("--- Enemy Turn ---")
                self.render_battle_screen() 
                time.sleep(0.5) 
                
                enemies_acted = False
                for enemy in self.enemies:
                    if enemy.hp > 0:
                        self.execute_enemy_turn(enemy)
                        enemies_acted = True
                        if self.check_loss_condition(): return
                
                if enemies_acted:
                    self.render_battle_screen()
                    if self.auto_battle:
                        config.console.print("[bold yellow]Enemy turn finished.[/bold yellow]")
                        config.console.print("Press [bold]Enter[/bold] to continue, or [bold]A[/bold] to Stop Auto.")
                        choice = get_player_input("> ").upper()
                        if choice == "A":
                            self.auto_battle = False
                            config.console.print("[dim]Auto Battle Disabled.[/dim]")
                            time.sleep(0.6)
                    else:
                        get_player_input("Enemy turn finished. Press Enter...")
                    self.battle_log = [] 
            
            # --- END OF TURN PHASE (Status Effects) ---
            if not self.is_battle_over:
                self.process_turn_end_effects()
                if self.check_win_condition() or self.check_loss_condition(): return

            self.turn_count += 1
            # ---------------------------------------------------------
            # SPECIAL STAGE 2-9 LOGIC: SURVIVE 5 TURNS
            # ---------------------------------------------------------
            if self.stage_id == 20 and self.turn_count == 3:
                self.log("[yellow]The enemy is overwhelming![/yellow]")
                self.log("[yellow]Your objective: survive the encounter...[/yellow]")
                
            if self.stage_id == 20 and self.turn_count == 6:
                self.won = True
                # Return True immediately to signal Player Victory
                return True
            # ---------------------------------------------------------
            
    def apply_status_modifiers(self, unit):
        """
        Calculates stat penalties derived from status effects.
        """
        # --- NEW: SAFETY CLAMP LOGIC ---
        # Ensures that no matter how an effect was added, it never exceeds game limits.
        for effect in unit.status_effects:
            if effect.name in ["Poise", "Bleed"]:
                # Cap Potency and Count at 99
                if effect.potency > 99: effect.potency = 99
                if effect.duration > 99: effect.duration = 99
            elif effect.name == "Bind":
                # Cap Count at 5 (Bind has no potency)
                if effect.duration > 5: effect.duration = 5
        # 1. Reset Modifiers handled elsewhere (reset_turn_modifiers)
        
        # 2. Apply Visible Status Effects
        for effect in unit.status_effects:
            if effect.name == "Bind":
                # Logic: Reduce Damage by 10% per duration, capped (min 10% dmg remaining)
                penalty = 1.0 - (0.1 * effect.duration)
                unit.temp_modifiers["outgoing_dmg_mult"] *= max(0.1, penalty)
            elif effect.name == "Haste":
                # Logic: Deal +10% base damage per count
                bonus = 1.0 + (0.1 * effect.duration)
                unit.temp_modifiers["outgoing_dmg_mult"] *= bonus
        
        # 1. Apply Hidden Flags (Invisible to Player UI, but affects logic)
        # Check for Nerve Disruption (Dynamic attribute)
        if getattr(unit, "nerve_disruption_turns", 0) > 0:
            # Effect: Target deals -80% damage (so they deal 20%)
            unit.temp_modifiers["outgoing_dmg_mult"] *= 0.2

        # 2. Apply Visible Status Effects
        pass

    def resolve_combat_start_effects(self):
        """
        Scans queued actions (Ally Queue & Enemy Intents).
        If a skill has [Combat Start], activate its effect immediately.
        """
        activated_any = False
        
        # 1. Check Allies
        for ally, skill, target in self.ally_action_queue:
            if ally.hp > 0 and "[Combat Start]" in skill.description:
                self.apply_combat_start_logic(ally, skill)
                activated_any = True

        # 2. Check Enemies
        for enemy in self.enemies:
            if enemy.hp > 0 and enemy.intent:
                skill, target, _ = enemy.intent
                if "[Combat Start]" in skill.description:
                    self.apply_combat_start_logic(enemy, skill)
                    activated_any = True
        
        if activated_any:
            self.render_battle_screen()
            time.sleep(0.8)

    def apply_combat_start_logic(self, unit, skill):
        # Existing Base Buff
        if skill.effect_type == "BUFF_DEF_FLAT":
             unit.temp_modifiers["final_dmg_reduction"] += skill.effect_val

        # --- HISAYUKI ---
        elif skill.effect_type == "HISAYUKI_SPECIAL_2":
            if any(s.name == "Bind" for s in unit.status_effects):
                unit.temp_modifiers["incoming_dmg_mult"] *= 1.50
        
        # --- RIPOSTE GANG / ADAM ---
        elif skill.effect_type == "RIPOSTE_SQUAD_LEADER_SPECIAL_1":
            team = self.allies if unit in self.allies else self.enemies
            for a in team:
                if a.hp > 0: 
                    a.temp_modifiers["outgoing_dmg_flat"] = a.temp_modifiers.get("outgoing_dmg_flat", 0) + 4
                    
        elif skill.effect_type == "ADAM_SPECIAL_2":
            team = self.allies if unit in self.allies else self.enemies
            for a in team:
                if a.hp > 0:
                    a.temp_modifiers["outgoing_dmg_flat"] = a.temp_modifiers.get("outgoing_dmg_flat", 0) + 3
                    a.temp_modifiers["final_dmg_reduction"] = a.temp_modifiers.get("final_dmg_reduction", 0) + 2
                    
        elif skill.effect_type == "ADAM_SPECIAL_3":
            unit.temp_modifiers["incoming_dmg_flat"] = unit.temp_modifiers.get("incoming_dmg_flat", 0) + 3
            unit.temp_modifiers["outgoing_base_dmg_flat"] = unit.temp_modifiers.get("outgoing_base_dmg_flat", 0) - 20
        
        # --- MASCOT JOKE SKILL ---
        elif skill.effect_type == "JOKE_SKILL":
            if hasattr(unit, "kata"):
                unit.kata.rift_aptitude = 0
        
        # --- COUNTER SKILL FLAGS (Hidden Tracking) ---
        elif skill.effect_type == "COUNTER_SKILL_TYPE1":
            unit.counter_active = True
            unit.counter_potency = 0.20  # +20% damage
        elif skill.effect_type == "COUNTER_SKILL_SPECIAL_TYPE1":
            unit.counter_active = True
            unit.counter_potency = 0.40  # +40% damage
        elif skill.effect_type == "COUNTER_SKILL_SPECIAL_TYPE3":
            unit.counter_active = True
            unit.counter_potency = 0.30  # +30% damage
        
        # --- BENIKAWA NINJA CLAN ---
        elif skill.effect_type in ["BENIKAWA_CLAN_SPECIAL_1", "BENIKAWA_CLAN_SPECIAL_3"]:
            unit.temp_modifiers["incoming_dmg_mult"] *= 1.30
            #self.log(f"[dim]{unit.name} assumes a reckless stance, taking +30% damage this turn![/dim]")
            
        elif skill.effect_type == "BENIKAWA_CLAN_SPECIAL_2":
            unit.temp_modifiers["incoming_dmg_mult"] *= 0.70
            # Set the next turn's incoming damage multiplier safely
            unit.next_turn_modifiers["incoming_dmg_mult"] = unit.next_turn_modifiers.get("incoming_dmg_mult", 1.0) * 0.50
            #self.log(f"[dim]{unit.name} nullifies their pain receptors, reducing incoming damage significantly![/dim]")

    def process_turn_end_effects(self):
        """
        Handles Status Effect ticks.
        Logic supports Potency/Count system.
        'duration' attribute in code is treated as 'Count'.
        """
        effects_triggered = False
        all_units = self.allies + self.enemies
        
        for unit in all_units:
            if unit.hp <= 0: continue
            
            # --- HIDDEN FLAGS CLEANUP ---
            if getattr(unit, "counter_active", False):
                unit.counter_active = False
                unit.counter_potency = 0
            if getattr(unit, "nerve_disruption_turns", 0) > 0:
                unit.nerve_disruption_turns -= 1
                if unit.nerve_disruption_turns == 0:
                    pass

            # --- VISIBLE STATUS EFFECTS ---
            # Iterate backwards to allow safe removal
            for i in range(len(unit.status_effects) - 1, -1, -1):
                effect = unit.status_effects[i]
                triggered_this_loop = False

                # 1. Bleed Logic: handled in execute_skill (Upon dealing damage)
                # Bleed DOES NOT decay at end of turn. It persists until triggered.
                if effect.name == "Bleed":
                    pass 

                # 2. Decay Logic (Decay Count by a certain value every turn)
                elif effect.name in ["Bind", "Poise", "Haste"]:
                    effect.duration -= 1
                elif effect.name == "Fairylight":
                    old_duration = effect.duration
                    # Halve the duration rounding down
                    effect.duration = effect.duration // 2 
                    # Calculate how much was lost
                    reduced_amount = old_duration - effect.duration
                    # If duration was reduced and they have Rupture, boost the Rupture Potency
                    if reduced_amount > 0:
                        rupture_eff = next((s for s in unit.status_effects if s.name == "Rupture"), None)
                        if rupture_eff:
                            rupture_eff.potency = min(99, rupture_eff.potency + reduced_amount)
                            # Optional: A log to show the conversion happened!
                            self.log(f"[spring_green1]Fairylight decay granted {unit.name} +{reduced_amount} Rupture Potency![/spring_green1]")
                elif effect.name == "Riposte":
                    # Reduce by 25% at end of turn
                    reduction = int(effect.duration * 0.25)
                    effect.duration = max(0, effect.duration - max(1, reduction))
                
                # 3. Standard DOT / Regen (Legacy support)
                elif effect.type == "DOT":
                    dmg = effect.potency
                    unit.hp -= dmg
                    self.log(f"[bold magenta]{effect.name}[/bold magenta] deals {dmg} dmg to {unit.name}!")
                    effect.duration -= 1
                    effects_triggered = True
                    triggered_this_loop = True
                elif effect.type == "REGEN":
                    heal = effect.potency
                    unit.hp = min(unit.max_hp, unit.hp + heal)
                    self.log(f"[bold green]{effect.name}[/bold green] heals {unit.name} for {heal}!")
                    effect.duration -= 1
                    effects_triggered = True
                    triggered_this_loop = True
                
                # Check Death
                if unit.hp <= 0:
                    unit.hp = 0
                    self.log(f"[bold red]{unit.name} succumbed to {effect.name}![/bold red]")
                    effects_triggered = True
                    break 
                
                # Remove if Count/Duration is 0
                if effect.duration <= 0:
                    self.log(f"{unit.name}'s [dim]{effect.name}[/dim] expired.")
                    unit.status_effects.pop(i)
                    effects_triggered = True

            # --- PROCESS PENDING BIND (Hidden -> Visible) ---
            if getattr(unit, "pending_bind", 0) > 0:
                actual_duration = min(5, unit.pending_bind)
                existing_bind = next((s for s in unit.status_effects if s.name == "Bind"), None)
                
                if existing_bind:
                    existing_bind.duration = min(5, existing_bind.duration + actual_duration)
                else:
                    bind_effect = StatusEffect("Bind", "[dim gold1]⛓[/dim gold1]", 1, "Deal -(10*Count)% base damage with skills. Lose 1 count every new turn. Max Count: 5", duration=actual_duration)
                    unit.status_effects.append(bind_effect)
                
                unit.pending_bind = 0
                effects_triggered = True

            # --- PROCESS PENDING HASTE (Hidden -> Visible) ---
            if getattr(unit, "pending_haste", 0) > 0:
                actual_duration = min(5, unit.pending_haste)
                existing_haste = next((s for s in unit.status_effects if s.name == "Haste"), None)
                
                if existing_haste:
                    existing_haste.duration = min(5, existing_haste.duration + actual_duration)
                else:
                    haste_effect = StatusEffect("Haste", "[yellow1]🢙[/yellow1]", 0, "Deal +(10*Count)% base damage with skills. Lose 1 count every new turn. Max count: 5", duration=actual_duration, type="BUFF")
                    unit.status_effects.append(haste_effect)
                
                unit.pending_haste = 0
                effects_triggered = True

            # --- UNIVERSAL DUAL-STACK CLEANUP (POP ON 0) ---
            for effect in list(unit.status_effects):
                if effect.name in DUAL_STACK_EFFECTS:
                    if effect.potency <= 0 or effect.duration <= 0:
                        unit.status_effects.remove(effect)
                        effects_triggered = True

        if effects_triggered:
            self.render_battle_screen()
            time.sleep(1.0)
            self.battle_log = [] 

    def assign_auto_targets(self, sources, targets):
        living_sources = [s for s in sources if s.hp > 0]
        living_targets = [t for t in targets if t.hp > 0]
        if not living_sources or not living_targets: return
        
        # Simple random assignment logic
        temp_sources = list(living_sources) 
        random.shuffle(temp_sources)
        
        temp_targets = list(living_targets)
        random.shuffle(temp_targets)
        
        assigned_count = 0
        for source in temp_sources:
            if assigned_count < len(temp_targets):
                source.auto_target = temp_targets[assigned_count]
                assigned_count += 1
            else:
                source.auto_target = random.choice(living_targets)

    def generate_enemy_intents(self):
        for enemy in self.enemies:
            enemy.draw_skills(1)
            enemy.intent = None
            if enemy.hand and enemy.auto_target and enemy.auto_target.hp > 0:
                skill_idx = random.randint(0, len(enemy.hand)-1)
                skill = enemy.hand[skill_idx]
                enemy.intent = (skill, enemy.auto_target, skill_idx) 

    def handle_player_command_phase(self):
        self.ally_action_queue = []
        pending_allies = [a for a in self.allies if a.hp > 0]
        
        if self.auto_battle:
            self.run_auto_battler(pending_allies)
            return

        while pending_allies:
            self.render_battle_screen(active_unit=None)
            config.console.print("[bold yellow]COMMAND PHASE[/bold yellow]")
            config.console.print("Select an ally to command:")
            for idx, ally in enumerate(pending_allies):
                config.console.print(f"[{idx+1}] {ally.name}")
            config.console.print("[V] View Unit Details")
            auto_status = "[bold green]ON[/bold green]" if self.auto_battle else "[dim]OFF[/dim]"
            config.console.print(f"[A] Toggle Auto Battle ({auto_status})")
            config.console.print("[R] Retreat")
            
            choice = get_player_input("Select Unit > ").upper()

            # --- SECRET DEV COMMAND: BLOWUNIVERSE ---
            if choice == "BLOWUNIVERSE":
                self.log("[bold magenta]*** AUTHOR CHEAT: THE UNIVERSE IMPLODES ***[/bold magenta]")
                self.log("[dim]All enemy HP set to 1.[/dim]")
                for enemy in self.enemies:
                    if enemy.hp > 0:
                        enemy.hp = 1
                self.render_battle_screen()
                time.sleep(0.5)
                continue # Loop back so you can select a unit to finish them off
            
            if choice == "R":
                config.console.print("[bold red]Are you sure you want to retreat? (y/n)[/bold red]")
                confirm = get_player_input("> ").lower()
                if confirm == "y":
                    self.is_battle_over = True
                    self.won = False
                    return
                else:
                    continue

            if choice == "V":
                self.inspect_unit_menu()
                continue
            if choice == "A":
                self.auto_battle = not self.auto_battle
                if self.auto_battle:
                    self.log("[bold yellow]Auto Battle Enabled![/bold yellow]")
                    self.run_auto_battler(pending_allies)
                    return
                else:
                    self.log("[dim]Auto Battle Disabled.[/dim]")
                    continue
            if choice.isdigit():
                idx = int(choice) - 1
                if 0 <= idx < len(pending_allies):
                    selected_ally = pending_allies[idx]
                    if self.select_skill_for_ally(selected_ally):
                        pending_allies.pop(idx)
                else:
                    self.log("[red]Invalid Selection![/red]")
            else:
                pass

    def run_auto_battler(self, pending_allies):
        # Priority: Akasuke > Yuri > Benikawa > Shigemura > Others
        def get_priority(unit):
            if "Akasuke" in unit.name: return 0
            if "Yuri" in unit.name: return 1
            if "Benikawa" in unit.name: return 2
            if "Shigemura" in unit.name: return 3
            return 10 + self.allies.index(unit) 
            
        while pending_allies:
            global_max_tier = -1
            # Find highest available tier across all allies
            for ally in pending_allies:
                for skill in ally.hand:
                    if skill.tier > global_max_tier: global_max_tier = skill.tier
            
            if global_max_tier == -1: break
            
            # Filter allies who have that tier
            candidates = []
            for ally in pending_allies:
                has_tier = any(s.tier == global_max_tier for s in ally.hand)
                if has_tier: candidates.append(ally)
            
            candidates.sort(key=get_priority)
            winner = candidates[0]
            
            skill_to_use = None; skill_idx = -1
            for i, s in enumerate(winner.hand):
                if s.tier == global_max_tier:
                    skill_to_use = s; skill_idx = i; break
            
            if skill_to_use:
                winner.hand.pop(skill_idx)
                target = winner.auto_target
                if not target or target.hp <= 0:
                    living = [e for e in self.enemies if e.hp > 0]
                    if living: target = random.choice(living)
                
                if target:
                    self.ally_action_queue.append((winner, skill_to_use, target))
            
            pending_allies.remove(winner)
            self.render_battle_screen(active_unit=winner)
            config.console.print(f"[bold yellow]AUTO:[/bold yellow] {winner.name} selects {skill_to_use.name} (Tier {get_tier_roman(skill_to_use.tier)})")
            time.sleep(0.3)

    def select_skill_for_ally(self, ally):
        while True:
            self.render_battle_screen(active_unit=ally)
            config.console.print(f"[bold cyan]Commanding {ally.name}[/bold cyan]")
            config.console.print("Select a skill to use:")
            for i, skill in enumerate(ally.hand):
                 c = get_element_color(skill.element)
                 t = get_tier_roman(skill.tier)
                 config.console.print(f"[{i+1}] [{c}]{skill.name}[/{c}] ({t})")
                 if skill.description: config.console.print(f"      [light_green]{skill.description}[/light_green]")
            config.console.print("[0] Cancel")
            choice = get_player_input("Skill > ")
            if choice == "0": return False
            if choice.isdigit():
                idx = int(choice) - 1
                if 0 <= idx < len(ally.hand):
                    selected_skill = ally.hand.pop(idx)
                    target = ally.auto_target
                    if not target or target.hp <= 0:
                        living_enemies = [e for e in self.enemies if e.hp > 0]
                        if living_enemies: target = random.choice(living_enemies)
                    if target:
                        self.ally_action_queue.append((ally, selected_skill, target))
                        return True
                    else: self.log("[red]No valid target![/red]")
                else: self.log("[red]Invalid Skill Selection![/red]")
            else: self.log("[red]Invalid Input![/red]")
            
    def execute_player_actions(self):
        for ally, skill, target in self.ally_action_queue:
            if ally.hp > 0:
                if target.hp <= 0:
                        living = [e for e in self.enemies if e.hp > 0]
                        if living: target = random.choice(living)
                        else: break 
                self.execute_skill(ally, skill, target)
                if ally.hp > 0: ally.draw_skills(1)
                if self.check_win_condition(): return

    def execute_enemy_turn(self, enemy):
        if not enemy.intent: return
        skill, target, skill_idx = enemy.intent
        if target.hp <= 0:
            living_allies = [a for a in self.allies if a.hp > 0]
            if living_allies: target = random.choice(living_allies)
            else: return 
        if skill_idx < len(enemy.hand): enemy.hand.pop(skill_idx)
        else:
            if enemy.hand: enemy.hand.pop(0)
        self.execute_skill(enemy, skill, target)

    def get_max_skill_tier(self, unit):
        if not unit.hand: return 0
        return max(s.tier for s in unit.hand)

    def execute_skill(self, attacker, skill, target):
        attacker.discard_pile.append(skill)
        
        # Log Action
        self.log(f"{attacker.name} uses [bold]{skill.name}[/bold]!")
        self.render_battle_screen() 
        time.sleep(0.8) 

        # Initialize specific variable for Shigemura's Sadism to avoid scope errors
        sadism_bind_to_apply = 0
        is_crit = False
        
        # FIX 4: UnboundLocalError Risk - Default initialize damage to 0 at the start of the function
        damage = 0

        # --- [STEP 1] [On Use] EFFECTS ---
        if "[On Use]" in skill.description:
            if skill.effect_type == "BUFF_DEF_FLAT":
                 attacker.temp_modifiers["final_dmg_reduction"] = attacker.temp_modifiers.get("final_dmg_reduction", 0) + skill.effect_val
            
            # FIX 2 & FIX 5: Moved DEF_BUFF_BASE_PER to Step 1 and handled Enemy phase vulnerability
            elif skill.effect_type == "DEF_BUFF_BASE_PER":
                reduction_pct = skill.effect_val / 10.0
                if attacker in self.enemies:
                    if not hasattr(attacker, "next_turn_modifiers"): attacker.next_turn_modifiers = {}
                    attacker.next_turn_modifiers["incoming_dmg_mult"] = attacker.next_turn_modifiers.get("incoming_dmg_mult", 1.0) * (1.0 - reduction_pct)
                else:
                    attacker.temp_modifiers["incoming_dmg_mult"] *= (1.0 - reduction_pct)
                    
            # FIX 2: Moved BLEED_POTENCY_DEF_BUFF's [On Use] defense buff to Step 1
            elif skill.effect_type == "BLEED_POTENCY_DEF_BUFF":
                attacker.temp_modifiers["final_dmg_reduction"] += skill.effect_val
                
            # FIX 2: Moved BENIKAWA_KIRYOKU_SPECIAL's [On Use] self-debuff to Step 1
            elif skill.effect_type == "BENIKAWA_KIRYOKU_SPECIAL":
                attacker.temp_modifiers["incoming_dmg_mult"] *= 1.50

            # KIRYOKU / SUMIKO / FALCON
            elif skill.effect_type == "BASE_DAMAGE_DEBUFF_ALL":
                team = self.allies if attacker in self.allies else self.enemies
                for member in team:
                    if member.hp > 0:
                        member.temp_modifiers["outgoing_base_dmg_flat"] = member.temp_modifiers.get("outgoing_base_dmg_flat", 0) - skill.effect_val
            elif skill.effect_type == "SUMIKO_SPECIAL_1":
                team = self.allies if attacker in self.allies else self.enemies
                for member in team:
                    if member.hp > 0:
                        member.temp_modifiers["outgoing_dmg_flat"] = member.temp_modifiers.get("outgoing_dmg_flat", 0) - 8
            elif skill.effect_type == "FALCON_SPECIAL_1":
                if not any(s.name == "Haste" for s in attacker.status_effects):
                    self.apply_status_logic(attacker, StatusEffect("Haste", "[yellow1]🢙[/yellow1]", 0, "Deal +(10*Count)% base damage with skills. Lose 1 count every new turn. Max count: 5", duration=3))
            
            # HISAYUKI / EAGLE / AOE BUFFS
            elif skill.effect_type == "HISAYUKI_SPECIAL_1":
                if not hasattr(attacker, "next_turn_modifiers"): attacker.next_turn_modifiers = {}
                attacker.next_turn_modifiers["incoming_dmg_mult"] = attacker.next_turn_modifiers.get("incoming_dmg_mult", 1.0) * 0.60
            elif skill.effect_type == "GAIN_POISE_SPECIAL":
                self.apply_status_logic(attacker, StatusEffect("Poise", "[light_cyan1]༄[/light_cyan1]", skill.effect_val, "Boost Critical Hit chance by (Potency*5)% for the next 'Count' amount of hits. Max potency or count: 99", duration=skill.effect_val))
            elif skill.effect_type == "EAGLE_SPECIAL_2":
                self.apply_status_logic(attacker, StatusEffect("Poise", "[light_cyan1]༄[/light_cyan1]", 3, "Boost Critical Hit chance by (Potency*5)% for the next 'Count' amount of hits. Max potency or count: 99", duration=3))
            elif skill.effect_type == "AOE_BUFF_ATK_FLAT":
                team = self.allies if attacker in self.allies else self.enemies
                for member in team:
                    if member.hp > 0:
                        member.temp_modifiers["outgoing_dmg_flat"] = member.temp_modifiers.get("outgoing_dmg_flat", 0) + skill.effect_val
            
            # RIPOSTE GANG
            elif skill.effect_type in ["RIPOSTE_GAIN_SPECIAL_1", "RIPOSTE_SQUAD_LEADER_SPECIAL_1"]:
                self.apply_status_logic(attacker, StatusEffect("Riposte", "[cyan1]➲[/cyan1]", 0, "Take -5% damage for every 10 stacks owned (max -25%). When taking damage, reduce stack count by 1-4 stacks. For every 10 cumulative stacks reduced this way, gain 1 Haste next turn, then reset the count. At end of turn, reduce stack count by 25%. Max Count: 50", duration=10))
            elif skill.effect_type == "RIPOSTE_SQUAD_LEADER_SPECIAL_2":
                riposte_eff = next((s for s in attacker.status_effects if s.name == "Riposte"), None)
                if riposte_eff: riposte_eff.duration = 30
                else: self.apply_status_logic(attacker, StatusEffect("Riposte", "[cyan1]➲[/cyan1]", 0, "Take -5% damage for every 10 stacks owned (max -25%). When taking damage, reduce stack count by 1-4 stacks. For every 10 cumulative stacks reduced this way, gain 1 Haste next turn, then reset the count. At end of turn, reduce stack count by 25%. Max Count: 50", duration=30))
            elif skill.effect_type == "ADAM_SPECIAL_1":
                if not any(s.name == "Haste" for s in attacker.status_effects):
                    self.apply_status_logic(attacker, StatusEffect("Haste", "[yellow1]🢙[/yellow1]", 0, "Deal +(10*Count)% base damage with skills. Lose 1 count every new turn. Max count: 5", duration=2))

        # --- [STEP 2] DAMAGE CALCULATION ---
        if skill.base_damage > 0:
            # 1. Base Damage & Variance
            base_dmg_val = float(skill.base_damage)
            # Apply new Base Damage Debuffs from Step 1
            base_dmg_val += attacker.temp_modifiers.get("outgoing_base_dmg_flat", 0)
            
            # Hisayuki Special 3 Damage calculation
            if skill.effect_type == "HISAYUKI_SPECIAL_3":
                haste = next((s for s in attacker.status_effects if s.name == "Haste"), None)
                if haste:
                    bonus_pct = min(0.50, haste.duration * 0.10)
                    base_dmg_val *= (1.0 + bonus_pct)
                    attacker.status_effects.remove(haste)

            # --- PIERCE AFFINITY BASE DAMAGE MANIPULATION ---
            pierce_eff = next((s for s in target.status_effects if s.name == "Pierce Affinity"), None)
            if pierce_eff:
                p_count = min(5, pierce_eff.duration)
                if "Pierce Affinity" in skill.description:
                    base_dmg_val += p_count

            # --- RIPOSTE UNIQUE DAMAGE BUFFS FOR STEP 2 ---
            if skill.effect_type == "NAGANOHARA_RIPOSTE_CEDE":
                riposte_eff = next((s for s in attacker.status_effects if s.name == "Riposte"), None)
                if riposte_eff and riposte_eff.duration >= 20:
                    # [On Hit] deal +40% damage
                    base_dmg_val *= 1.40
                    # ...then take +50% more damage this turn
                    attacker.temp_modifiers["incoming_dmg_mult"] *= 1.50
                    self.log(f"[bold red]{attacker.name} cedes their defense for a heavy strike![/bold red]")
            if skill.effect_type == "AKASUKE_RIPOSTE_PRISEDEFER":
                riposte_eff = next((s for s in attacker.status_effects if s.name == "Riposte"), None)
                if riposte_eff:
                    # Deals +2% base damage for each stack of Riposte owned (Max +100%)
                    bonus_pct = min(1.0, riposte_eff.duration * 0.02)
                    base_dmg_val *= (1.0 + bonus_pct)

            # --- SHIGEMURA INFILTRATOR SKILL II ---
            infiltrator_recoil = 0
            if skill.effect_type == "SHIGEMURA_INFILTRATOR_SPECIAL_1":
                haste = next((s for s in attacker.status_effects if s.name == "Haste"), None)
                if haste:
                    bonus_base = base_dmg_val * 0.20
                    base_dmg_val += bonus_base
                    infiltrator_recoil = int(bonus_base) # Store the exact numeric increase

            # Shigemura Sadism Pre-Calc
            if skill.effect_type == "COND_REAPER_BIND_CONVERT_SPECIAL":
                total_bleed = sum(s.potency + s.duration for s in target.status_effects if s.name == "Bleed")
                steps = min(3, total_bleed // 3)
                if steps > 0:
                    base_dmg_val = max(0, base_dmg_val - (steps * 3))
                    sadism_bind_to_apply = steps

            # 2. Bind Penalty
            bind_effect = next((s for s in attacker.status_effects if s.name == "Bind"), None)
            if bind_effect:
                b_count = min(5, bind_effect.duration) 
                base_dmg_val *= max(0.0, 1.0 - (0.10 * b_count))

            # 3. Random Variance
            dmg = base_dmg_val * random.uniform(1.0, 1.5)

            # 4. Handle [On Use] Status (Skill I, II, III Poise Gains)
            if skill.effect_type == "GAIN_STATUS":
                self.apply_status_logic(attacker, copy.deepcopy(skill.status_effect))
            # GAIN_POISE_SPECIAL_1 On Use
            elif skill.effect_type == "GAIN_POISE_SPECIAL_1":
                self.apply_status_logic(attacker, StatusEffect("Poise", "[light_cyan1]༄[/light_cyan1]", 2, "Boost Critical Hit chance by (Potency*5)% for the next 'Count' amount of hits. Max potency or count: 99", duration=0))

            # 5. Critical Hit Roll (POISE CHECK)
            poise = next((se for se in attacker.status_effects if se.name == "Poise"), None)
            if poise and poise.potency > 0 and poise.duration > 0:
                crit_chance = min(100, poise.potency * 5)
                if random.randint(1, 100) <= crit_chance:
                    is_crit = True
                    dmg *= 1.2  # 20% Crit Multiplier

            # 6. Elemental & Global Multipliers
            res_mult = target.resistances[skill.element]
            nbd = dmg * res_mult
            nbd *= attacker.temp_modifiers.get("outgoing_dmg_mult", 1.0)
            nbd *= target.temp_modifiers.get("incoming_dmg_mult", 1.0)
            
            # 7. Flat Modifiers
            final_dmg = nbd + target.temp_modifiers.get("incoming_dmg_flat", 0)
            final_dmg += attacker.temp_modifiers.get("outgoing_dmg_flat", 0)

            # Consume Hit Bonuses
            if target.next_hit_taken_flat_bonus > 0:
                final_dmg += target.next_hit_taken_flat_bonus
                target.next_hit_taken_flat_bonus = 0 
            if attacker.next_hit_deal_flat_bonus > 0:
                final_dmg += attacker.next_hit_deal_flat_bonus
                attacker.next_hit_deal_flat_bonus = 0

            # --- NAGANOHARA CONDITIONAL FLATS ---
            target_has_bleed = any(s.name == "Bleed" and s.duration > 0 for s in target.status_effects)
            
            # Skill II: Simmer Down (+2 Dmg if Bleed)
            if skill.effect_type == "COND_TARGET_HAS_BLEED_DMG":
                if target_has_bleed:
                    final_dmg += skill.effect_val

            # Skill III: One-Handed Throw Down (+4 Dmg if Bleed)
            if skill.effect_type == "COND_BLEED_DMG_AND_APPLY":
                if target_has_bleed:
                    final_dmg += skill.effect_val

            # --- DEFENSE TIER REDUCTION ---
            def_max_tier = self.get_max_skill_tier(target)
            if skill.tier > def_max_tier:
                final_dmg -= (final_dmg * min(0.80, 0.20 * (skill.tier - def_max_tier)))

            damage = int(final_dmg)

            # --- FINAL CHECKS ---
            if skill.effect_type == "COND_HP_ABOVE_50_FLAT":
                if target.hp >= (target.max_hp * 0.5): 
                    damage += int(skill.effect_val)

            if skill.effect_type == "COND_LOW_HP_MERCY":
                if target.hp <= (target.max_hp * 0.7): 
                    damage -= int(skill.effect_val)

            if skill.effect_type == "COND_HP_BELOW_80_FLAT":
                if target.hp <= (target.max_hp * 0.8): 
                    damage += int(skill.effect_val)

            # ... Final Defense Reduction (Armor)
            flat_def = target.temp_modifiers["final_dmg_reduction"]
            damage = damage - flat_def
            
            # --- RIPOSTE DAMAGE MITIGATION ---
            riposte_eff = next((s for s in target.status_effects if s.name == "Riposte"), None)
            if riposte_eff:
                reduction_pct = min(0.25, (riposte_eff.duration // 10) * 0.05)
                damage = damage * (1.0 - reduction_pct)

            damage = max(1, int(damage)) # Minimum 1 damage if hit connects

            # [MECHANIC] CONVERT DAMAGE TO HEAL
            if skill.effect_type == "SPECIAL_CONVERT_DMG_TO_HEAL_LOWEST":
                team = self.allies if attacker in self.allies else self.enemies
                living_teammates = [u for u in team if u.hp > 0]
                if living_teammates:
                    lowest_unit = min(living_teammates, key=lambda u: u.hp / u.max_hp)
                    heal_amt = damage
                    lowest_unit.hp = min(lowest_unit.max_hp, lowest_unit.hp + heal_amt)
                    self.log(f"[light_green]-> {attacker.name} Heals {lowest_unit.name} for {heal_amt}.[/light_green]")
                damage = 0

            # --- CUSTOM NON-DAMAGE & HEALING SKILLS ---
            if skill.effect_type in ["SELF_HEAL_TYPE1", "EAGLE_SPECIAL_3", "JOKE_SKILL"]:
                if skill.effect_type == "SELF_HEAL_TYPE1":
                    heal_amt = damage
                    attacker.hp = min(attacker.max_hp, attacker.hp + heal_amt)
                    self.log(f"[light_green]-> {attacker.name} Heals self for {heal_amt}.[/light_green]")
                    damage = 0
                
                elif skill.effect_type == "EAGLE_SPECIAL_3":
                    team = self.allies if attacker in self.allies else self.enemies
                    living_teammates = [u for u in team if u.hp > 0]
                    if living_teammates:
                        lowest_unit = min(living_teammates, key=lambda u: u.hp / u.max_hp)
                        heal_amt = damage
                        lowest_unit.hp = min(lowest_unit.max_hp, lowest_unit.hp + heal_amt)
                        self.log(f"[light_green]-> {attacker.name} Heals {lowest_unit.name} for {heal_amt}.[/light_green]")
                        for a in living_teammates:
                            if a != lowest_unit:
                                a.hp = min(a.max_hp, a.hp + (heal_amt // 2))
                            # Haste Gain Next Turn
                            self.apply_status_logic(a, StatusEffect("Haste", "[yellow1]🢙[/yellow1]", 0, "Deal +(10*Count)% base damage with skills. Lose 1 count every new turn. Max count: 5", duration=3))
                    damage = 0
                
                elif skill.effect_type == "JOKE_SKILL":
                    damage = 0

            # --- APPLY DAMAGE ---
            if damage > 0:
                target.hp -= damage
                el_color = get_element_color(skill.element)
                eff_text = " [bold yellow](WEAK!)[/]" if res_mult > 1.0 else (" [dim](Resist)[/]" if res_mult < 1.0 else "")
                crit_text = "[khaki1]Critical![/] " if is_crit else ""
                
                self.log(f"-> {crit_text}Hit {target.name} for [bold {el_color}]{damage}[/bold {el_color}]!{eff_text}")
                
                # --- [HIDDEN MECHANIC] COUNTER TRIGGER ---
                if getattr(target, "counter_active", False):
                    # Ensure the next_turn_modifiers dictionary exists
                    if not hasattr(target, "next_turn_modifiers"): 
                        target.next_turn_modifiers = {}
                        
                    # Add the potency to next turn's outgoing damage multiplier
                    current_mult = target.next_turn_modifiers.get("outgoing_dmg_mult", 1.0)
                    target.next_turn_modifiers["outgoing_dmg_mult"] = current_mult + target.counter_potency
                    
                    # Deactivate so multi-hit skills don't stack the counter infinitely
                    target.counter_active = False 
                
                # GAIN_POISE_SPECIAL_1 On Hit
                if skill.effect_type == "GAIN_POISE_SPECIAL_1":
                    self.apply_status_logic(attacker, StatusEffect("Poise", "[light_cyan1]༄[/light_cyan1]", 4, "Boost Critical Hit chance by (Potency*5)% for the next 'Count' amount of hits. Max potency or count: 99", duration=0))
                
                # Consume Poise Count on Crit
                if is_crit and poise:
                    poise.duration -= 1
                    if poise.duration <= 0:
                        attacker.status_effects.remove(poise)
                
                # --- [MECHANIC] BLEED TRIGGER (Recoil on Attacker) ---
                bleed_idx = -1
                for i, se in enumerate(attacker.status_effects):
                    if se.name == "Bleed":
                        bleed_idx = i
                        break
                
                if bleed_idx != -1:
                    bleed_eff = next((se for se in attacker.status_effects if se.name == "Bleed"), None)
                    if bleed_eff:
                        recoil = bleed_eff.potency
                        attacker.hp -= recoil
                        bleed_eff.duration -= 1
                        self.log(f"[bold dim red]{attacker.name} took {recoil} Bleed damage.[/bold dim red]")
                        if bleed_eff.duration <= 0: attacker.status_effects.remove(bleed_eff)

                    if attacker.hp <= 0:
                        attacker.hp = 0
                    
                    if bleed_eff.duration <= 0 and bleed_idx in attacker.status_effects:
                        attacker.status_effects.pop(bleed_idx)

                # --- [MECHANIC] ON HIT HEAL LOWEST ---
                if skill.effect_type == "ON_HIT_HEAL_LOWEST_BY_DMG":
                    team = self.allies if attacker in self.allies else self.enemies
                    living_teammates = [u for u in team if u.hp > 0]
                    if living_teammates:
                        lowest_unit = min(living_teammates, key=lambda u: u.hp / u.max_hp)
                        heal_amt = damage 
                        lowest_unit.hp = min(lowest_unit.max_hp, lowest_unit.hp + heal_amt)
                        self.log(f"[light_green]-> {attacker.name} Heals {lowest_unit.name} for {heal_amt}.[/light_green]")

                # --- RIPOSTE STACK REDUCTION & HASTE GAIN ---
                if riposte_eff:
                    stacks_lost = random.randint(1, 4)
                    stacks_lost = min(stacks_lost, riposte_eff.duration)
                    riposte_eff.duration -= stacks_lost
                    target.riposte_loss_tracker += stacks_lost
                    
                    while target.riposte_loss_tracker >= 10:
                        target.riposte_loss_tracker -= 10
                        haste_eff = StatusEffect("Haste", "[yellow1]🢙[/yellow1]", 0, "Deal +(10*Count)% base damage with skills. Lose 1 count every new turn. Max count: 5", duration=1, type="BUFF")
                        self.apply_status_logic(target, haste_eff)
                        self.log(f"[yellow1]{target.name} gained Haste from Riposte![/yellow1]")
                    
                    if riposte_eff.duration <= 0: target.status_effects.remove(riposte_eff)

                # --- RUPTURE & FAIRYLIGHT TRIGGERS ---
                rupture_eff = next((s for s in target.status_effects if s.name == "Rupture"), None)
                if rupture_eff:
                    target.hp -= rupture_eff.potency
                    rupture_eff.duration -= 1
                    self.log(f"[medium_spring_green]Rupture dealt {rupture_eff.potency} damage to {target.name}![/medium_spring_green]")
                    if rupture_eff.duration <= 0: target.status_effects.remove(rupture_eff)
                    
                fairylight_eff = next((s for s in target.status_effects if s.name == "Fairylight"), None)
                if fairylight_eff:
                    target.hp -= fairylight_eff.potency
                    fairylight_eff.duration -= 1
                    self.log(f"[spring_green1]Fairylight dealt {fairylight_eff.potency} damage to {target.name}![/spring_green1]")
                    if fairylight_eff.duration <= 0: target.status_effects.remove(fairylight_eff)

                # --- PIERCE AFFINITY TRIGGER (STACK REDUCTION) ---
                pierce_target_eff = next((s for s in target.status_effects if s.name == "Pierce Affinity"), None)
                if pierce_target_eff:
                    pierce_target_eff.duration -= 1
                    if pierce_target_eff.duration <= 0: target.status_effects.remove(pierce_target_eff)
                    
                # --- APPLY INFILTRATOR RECOIL ---
                if infiltrator_recoil > 0:
                    attacker.hp -= infiltrator_recoil
                    self.log(f"[bold red]{attacker.name} takes {infiltrator_recoil} Recoil Damage from momentum![/bold red]")

                # FIX 1: Optimization - Chained the [On Hit] conditional checks with elif
                # --- LOGIC: POISE SUPPORT ---
                if skill.effect_type == "ON_HIT_PROVIDE_POISE_TYPE1":
                    # Logic: Grant +1 Poise Count to all allies who already have Poise
                    team = self.allies if attacker in self.allies else self.enemies
                    for member in team:
                        poise_effect = next((e for e in member.status_effects if e.name == "Poise"), None)
                        if poise_effect:
                            poise_effect.duration = min(99, poise_effect.duration + skill.effect_val)
                elif skill.effect_type == "ON_HIT_PROVIDE_POISE_TYPE2":
                    # Logic: Grant +2 Potency AND +2 Count to allies with Poise
                    team = self.allies if attacker in self.allies else self.enemies
                    for member in team:
                        poise_effect = next((e for e in member.status_effects if e.name == "Poise"), None)
                        if poise_effect:
                            poise_effect.potency = min(99, poise_effect.potency + skill.effect_val)
                            poise_effect.duration = min(99, poise_effect.duration + skill.effect_val)
                elif skill.effect_type == "ON_HIT_PROVIDE_POISE_TYPE3":
                    # Logic: Grant +2 Poise Potency to all allies who already have Poise
                    team = self.allies if attacker in self.allies else self.enemies
                    for member in team:
                        poise_effect = next((e for e in member.status_effects if e.name == "Poise"), None)
                        if poise_effect:
                            poise_effect.potency = min(99, poise_effect.potency + skill.effect_val)
                elif skill.effect_type == "ON_HIT_PROVIDE_POISE_TYPE4":
                    # Logic: If they have Poise, grant x Count. Else, grant x Potency.
                    team = self.allies if attacker in self.allies else self.enemies
                    for member in team:
                        poise_effect = next((e for e in member.status_effects if e.name == "Poise"), None)
                        if poise_effect:
                            poise_effect.duration = min(99, poise_effect.duration + skill.effect_val)
                        else:
                            new_poise = StatusEffect("Poise", "[light_cyan1]༄[/light_cyan1]", skill.effect_val, "Boost Critical Hit chance by (Potency*5)% for the next 'Count' amount of hits. Max potency or count: 99", duration=0)
                            self.apply_status_logic(member, new_poise)
                elif skill.effect_type == "ON_HIT_CONVERT_POISE_TYPE1":
                    # Logic: Convert 1 Potency -> 1 Count if Potency >= 2
                    team = self.allies if attacker in self.allies else self.enemies
                    for member in team:
                        poise_effect = next((e for e in member.status_effects if e.name == "Poise"), None)
                        if poise_effect and poise_effect.potency >= 2:
                            poise_effect.potency -= 1
                            poise_effect.duration = min(99, poise_effect.duration + 1)
                            if poise_effect.potency <= 0 or poise_effect.duration <= 0:
                                member.status_effects.remove(poise_effect)
                # --- KAGAKU DISCIPLINARY COMMITTEE POISE FLAGS ---
                elif skill.effect_type == "ON_HIT_CONVERT_POISE_TYPE2":
                    # Logic: Convert x Potency -> x Count if Potency >= 4
                    team = self.allies if attacker in self.allies else self.enemies
                    for member in team:
                        poise_effect = next((e for e in member.status_effects if e.name == "Poise"), None)
                        if poise_effect and poise_effect.potency >= 4:
                            poise_effect.potency -= skill.effect_val
                            poise_effect.duration = min(99, poise_effect.duration + skill.effect_val)
                            if poise_effect.potency <= 0 or poise_effect.duration <= 0:
                                member.status_effects.remove(poise_effect)

                # --- NEXT HIT BONUSES ---
                elif skill.effect_type == "ON_HIT_NEXT_TAKEN_FLAT":
                    target.next_hit_taken_flat_bonus += skill.effect_val
                elif skill.effect_type == "ON_HIT_NEXT_DEAL_FLAT":
                    attacker.next_hit_deal_flat_bonus += skill.effect_val
                elif skill.effect_type == "SELF_NEXT_TAKEN_FLAT":
                    attacker.next_hit_taken_flat_bonus += skill.effect_val
                elif skill.effect_type == "DEBUFF_INCOMING_DMG_FLAT":
                    target.temp_modifiers["incoming_dmg_flat"] += skill.effect_val

            else:
                if skill.effect_type != "SPECIAL_CONVERT_DMG_TO_HEAL_LOWEST":
                    self.log(f"-> The move dealt no damage.")

        # --- [STEP 3] STATUS EFFECT / SPECIAL APPLICATION ---
        
        # AOE BUFF
        if skill.effect_type == "AOE_BUFF_DEF_FLAT":
            team = self.allies if attacker in self.allies else self.enemies
            for member in team:
                if member.hp > 0:
                    member.temp_modifiers["final_dmg_reduction"] = member.temp_modifiers.get("final_dmg_reduction", 0) + skill.effect_val
                    
        # --- AKASUKE SKILLS ---

        # Skill I: Jab Flurry (Bleed Count Opener)
        elif skill.effect_type == "BLEED_COUNT_OPENER":
            has_bleed = any(s.name == "Bleed" for s in target.status_effects)
            
            if not has_bleed:
                # Target has NO Bleed -> Apply Primary Effect (Count 3, Pot 1)
                if hasattr(skill, "status_effect"):
                      self.apply_status_logic(target, copy.deepcopy(skill.status_effect))
            else:
                # Target HAS Bleed -> Apply Alternative Effect (Pot 1, Count 1)
                if hasattr(skill, "alt_status_effect"):
                      self.apply_status_logic(target, copy.deepcopy(skill.alt_status_effect))

        # Skill II: Cheap Nose Shot (Bleed Potency Stacker)
        elif skill.effect_type == "BLEED_POTENCY_STACKER":
            has_bleed = any(s.name == "Bleed" for s in target.status_effects)
            if has_bleed:
                 # Only apply if target already bleeds
                 if hasattr(skill, "status_effect"):
                     self.apply_status_logic(target, copy.deepcopy(skill.status_effect))

        # Skill III: Rally (Heiwa Rally Effect)
        elif skill.effect_type == "HEIWA_RALLY_EFFECT":
            team = self.allies if attacker in self.allies else self.enemies
            for member in team:
                if member.hp > 0:
                    # 1. Universal Buff: All allies deal +2 Final Dmg (Outgoing Flat)
                    current_bonus = member.temp_modifiers.get("outgoing_dmg_flat", 0)
                    member.temp_modifiers["outgoing_dmg_flat"] = current_bonus + skill.effect_val
                    
                    # 2. Conditional Buff: "Heiwa" allies take -2 Final Dmg (Incoming Reduction)
                    if hasattr(member, "kata") and "Heiwa" in member.kata.name:
                        member.temp_modifiers["final_dmg_reduction"] += skill.effect_val

        # BLEED_POTENCY_DEF_BUFF (Yuri Heiwa S3)
        # FIX 2: Removed the self-buff segment of this block as it was properly placed in Step 1
        elif skill.effect_type == "BLEED_POTENCY_DEF_BUFF":
            if skill.status_effect:
                # Apply deepcopy of status to prevent template corruption
                effect_instance = copy.deepcopy(skill.status_effect)
                self.apply_status_logic(target, effect_instance)
        
        # --- BENIKAWA SKILL LOGIC ---
        # FIX 2: DEF_BUFF_BASE_PER (Benikawa S2) removed entirely from Step 3 and shifted to Step 1

        # COND_TARGET_HAS_BLEED_DMG_PER (Benikawa S3)
        elif skill.effect_type == "COND_TARGET_HAS_BLEED_DMG_PER":
            has_bleed = any(s.name == "Bleed" for s in target.status_effects)
            if has_bleed:
                bonus_dmg = int(skill.base_damage * (skill.effect_val / 10.0))
                target.hp -= bonus_dmg
                
                # --- SADISM BIND APPLY ---
                if 'sadism_bind_to_apply' in locals() and sadism_bind_to_apply > 0:
                    bind_eff = StatusEffect(
                        "Bind", "[dim gold1]⛓[/dim gold1]", 1, 
                        "Deal -(10*Count)% base damage with skills. Lose 1 count every new turn. Max Count: 5", 
                        duration=sadism_bind_to_apply
                    )
                    self.apply_status_logic(target, bind_eff)

        # --- EXISTING KUROGANE & GENERIC EFFECTS ---
        elif skill.effect_type == "APPLY_BLEED_HEAVY_STACKS":
            bleed = StatusEffect("Bleed", "[red]💧︎[/red]", 2, "Upon dealing damage, Take fixed damage equal to Potency, then reduce count by 1 Max potency or count: 99", duration=2, type="DEBUFF")
            self.apply_status_logic(target, bleed)
        elif skill.effect_type == "APPLY_BLEED_AND_BIND":
            bleed = StatusEffect("Bleed", "[red]💧︎[/red]", 3, "Upon dealing damage, Take fixed damage equal to Potency, then reduce count by 1 Max potency or count: 99", duration=1, type="DEBUFF")
            self.apply_status_logic(target, bleed)
            bind = StatusEffect("Bind", "[dim gold1]⛓[/dim gold1]", 1, "Deal -(10*Count)% base damage with skills. Lose 1 count every new turn. Max Count: 5", duration=1, type="DEBUFF")
            self.apply_status_logic(target, bind)
        elif skill.effect_type == "APPLY_BLEED_AND_BIND_HEAVY":
            bleed = StatusEffect("Bleed", "[red]💧︎[/red]", 3, "Upon dealing damage, Take fixed damage equal to Potency, then reduce count by 1 Max potency or count: 99", duration=1, type="DEBUFF")
            self.apply_status_logic(target, bleed)
            bind = StatusEffect("Bind", "[dim gold1]⛓[/dim gold1]", 1, "Deal -(10*Count)% base damage with skills. Lose 1 count every new turn. Max Count: 5", duration=2, type="DEBUFF")
            self.apply_status_logic(target, bind)

        # Generic Status + Naganohara Skill III Dual Type
        elif (skill.effect_type == "APPLY_STATUS" or skill.effect_type == "COND_BLEED_DMG_AND_APPLY") and hasattr(skill, "status_effect"):
                if skill.status_effect.name == "Nerve Disruption":
                    target.nerve_disruption_turns = skill.status_effect.duration
                else:
                    new_status = copy.deepcopy(skill.status_effect)
                    self.apply_status_logic(target, new_status)

        elif skill.effect_type == "HASTE_BIND_SPECIAL_TYPE1":
            team = self.allies if attacker in self.allies else self.enemies
            enemy_team = self.enemies if attacker in self.allies else self.allies
            
            valid_allies = [u for u in team if u.hp > 0 and u != attacker]
            valid_enemies = [u for u in enemy_team if u.hp > 0]
            
            chosen_allies = random.sample(valid_allies, min(2, len(valid_allies)))
            chosen_enemies = random.sample(valid_enemies, min(2, len(valid_enemies)))
            
            for a in chosen_allies: self.apply_status_logic(a, StatusEffect("Haste", "[yellow1]🢙[/yellow1]", 0, "Deal +(10*Count)% base damage with skills. Lose 1 count every new turn. Max count: 5", duration=skill.effect_val))
            for e in chosen_enemies: self.apply_status_logic(e, StatusEffect("Bind", "[dim gold1]⛓[/dim gold1]", 1, "Deal -(10*Count)% base damage with skills. Lose 1 count every new turn. Max Count: 5", duration=skill.effect_val))
            
        elif skill.effect_type == "HANA_SPECIAL_RAGE":
            # FIX 3: Safety logic check injected
            if not hasattr(attacker, "next_turn_modifiers"): attacker.next_turn_modifiers = {}
            attacker.next_turn_modifiers["outgoing_dmg_mult"] = 0.6
            target.temp_modifiers["outgoing_dmg_mult"] *= 0.85
            
        elif skill.effect_type == "BLEED_RUPTURE_SPECIAL_TYPE1":
            self.apply_status_logic(target, StatusEffect("Bleed", "[red]💧︎[/red]", skill.effect_val, "Upon dealing damage, Take fixed damage equal to Potency, then reduce count by 1. Max Potency or Count: 99", duration=1))
            self.apply_status_logic(target, StatusEffect("Rupture", "[medium_spring_green]✧[/medium_spring_green]", skill.effect_val, "Upon getting hit by a skill, Take extra fixed damage equal to the amount of Potency, then reduce count by 1. Max Potency or Count: 99", duration=1))
            
        elif skill.effect_type == "SPECIAL_CONVERT_DMG_TO_HEAL_RANDOM":
            team = self.allies if attacker in self.allies else self.enemies
            valid_allies = [u for u in team if u.hp > 0 and u != attacker]
            chosen_allies = random.sample(valid_allies, min(skill.effect_val, len(valid_allies)))
            
            targets_to_heal = [attacker] + chosen_allies
            for a in targets_to_heal:
                a.hp = min(a.max_hp, a.hp + damage)
                self.log(f"[light_green]-> {attacker.name} Heals {a.name} for {damage}.[/light_green]")
            damage = 0

        elif skill.effect_type == "NAGANOHARA_KIRYOKU_SPECIAL":
            team = self.allies if attacker in self.allies else self.enemies
            valid_allies = [u for u in team if u.hp > 0 and u != attacker]
            for a in random.sample(valid_allies, min(2, len(valid_allies))):
                self.apply_status_logic(a, StatusEffect("Haste", "[yellow1]🢙[/yellow1]", 0, "Deal +(10*Count)% base damage with skills. Lose 1 count every new turn. Max count: 5", duration=1))
                
            has_rupture = any(s.name in ["Rupture", "Fairylight"] for s in target.status_effects)
            if has_rupture:
                self.apply_status_logic(target, StatusEffect("Rupture", "[medium_spring_green]✧[/medium_spring_green]", 1, "Upon getting hit by a skill, Take extra fixed damage equal to the amount of Potency, then reduce count by 1. Max Potency or Count: 99", duration=2))
            else:
                self.apply_status_logic(target, StatusEffect("Rupture", "[medium_spring_green]✧[/medium_spring_green]", 3, "Upon getting hit by a skill, Take extra fixed damage equal to the amount of Potency, then reduce count by 1. Max Potency or Count: 99", duration=1))   
                
        elif skill.effect_type == "RUPTURE_DAMAGE_BUFF_TYPE1":
            has_rupture = any(s.name in ["Rupture", "Fairylight"] for s in target.status_effects)
            if has_rupture and damage > 0:
                bonus = int(damage * 0.25)
                target.hp -= bonus
                self.log(f"[medium_spring_green]Bonus Rupture Execute: {bonus} damage![/medium_spring_green]")

        elif skill.effect_type == "SHIGEMURA_INFILTRATOR_SPECIAL_2":
            haste = next((s for s in attacker.status_effects if s.name == "Haste"), None)
            if haste and damage > 0:
                bonus_pct = min(0.75, haste.duration * 0.15)
                bonus_dmg = int(damage * bonus_pct)
                target.hp -= bonus_dmg
                self.log(f"[bold yellow]Maximized Ram! +{bonus_dmg} Bonus Damage![/bold yellow]")
                attacker.status_effects.remove(haste)

        # Kiryoku / Fairylight / Rupture
        elif skill.effect_type == "KIRYOKU_COUNCIL_SPECIAL":
            self.apply_status_logic(target, StatusEffect("Rupture", "[medium_spring_green]✧[/medium_spring_green]", 0, "Upon getting hit by a skill, Take extra fixed damage equal to the amount of Potency, then reduce count by 1. Max Potency or Count: 99", duration=2))
            self.apply_status_logic(target, StatusEffect("Fairylight", "[spring_green1]𒀭[/spring_green1]", 2, "Unique Rupture (Counts As Rupture)\nUpon getting hit by a skill, Take extra fixed damage equal to the amount of Potency. On turn end, reduce Count by half, and if this unit has Rupture, gain Rupture Potency based on Count lost this way. Max Potency or Count: 99", duration=1))
        elif skill.effect_type == "AYAKO_SPECIAL":
            self.apply_status_logic(target, StatusEffect("Rupture", "[medium_spring_green]✧[/medium_spring_green]", 0, "Upon getting hit by a skill, Take extra fixed damage equal to the amount of Potency, then reduce count by 1. Max Potency or Count: 99", duration=3))
            self.apply_status_logic(target, StatusEffect("Fairylight", "[spring_green1]𒀭[/spring_green1]", 4, "Unique Rupture (Counts As Rupture)\nUpon getting hit by a skill, Take extra fixed damage equal to the amount of Potency. On turn end, reduce Count by half, and if this unit has Rupture, gain Rupture Potency based on Count lost this way. Max Potency or Count: 99", duration=1))
        elif skill.effect_type == "SUMIKO_SPECIAL_1":
            self.apply_status_logic(attacker, StatusEffect("Haste", "[yellow1]🢙[/yellow1]", 0, "Deal +(10*Count)% base damage with skills. Lose 1 count every new turn. Max count: 5", duration=2))
        elif skill.effect_type == "SUMIKO_SPECIAL_2":
            self.apply_status_logic(target, StatusEffect("Rupture", "[medium_spring_green]✧[/medium_spring_green]", 5, "Upon getting hit by a skill, Take extra fixed damage equal to the amount of Potency, then reduce count by 1. Max Potency or Count: 99", duration=4))
            self.apply_status_logic(attacker, StatusEffect("Haste", "[yellow1]🢙[/yellow1]", 0, "Deal +(10*Count)% base damage with skills. Lose 1 count every new turn. Max count: 5", duration=2))
        elif skill.effect_type == "APPLY_RUPTURE_HEAVY_STACKS":
            self.apply_status_logic(target, StatusEffect("Rupture", "[medium_spring_green]✧[/medium_spring_green]", 2, "Upon getting hit by a skill, Take extra fixed damage equal to the amount of Potency, then reduce count by 1. Max Potency or Count: 99", duration=2))
        
        # Hisayuki / Infiltrators / Disciplinary
        elif skill.effect_type == "HISAYUKI_SPECIAL_1":
            if any(s.name == "Haste" for s in attacker.status_effects):
                self.apply_status_logic(attacker, StatusEffect("Bind", "[dim gold1]⛓[/dim gold1]", 1, "Deal -(10*Count)% base damage with skills. Lose 1 count every new turn. Max Count: 5", duration=1))
            else:
                self.apply_status_logic(attacker, StatusEffect("Haste", "[yellow1]🢙[/yellow1]", 0, "Deal +(10*Count)% base damage with skills. Lose 1 count every new turn. Max count: 5", duration=1))
        elif skill.effect_type == "BIND_RUPTURE_SPECIAL_TYPE1":
            self.apply_status_logic(target, StatusEffect("Bind", "[dim gold1]⛓[/dim gold1]", 1, "Deal -(10*Count)% base damage with skills. Lose 1 count every new turn. Max Count: 5", duration=2))
            self.apply_status_logic(target, StatusEffect("Rupture", "[medium_spring_green]✧[/medium_spring_green]", 2, "Upon getting hit by a skill, Take extra fixed damage equal to the amount of Potency, then reduce count by 1. Max Potency or Count: 99", duration=1))
        
        # Ninjas (Raven, Falcon, Eagle)
        elif skill.effect_type == "RAVEN_SPECIAL_1":
            target.next_hit_taken_flat_bonus += 6
            self.apply_status_logic(attacker, StatusEffect("Poise", "[light_cyan1]༄[/light_cyan1]", 4, "Boost Critical Hit chance by (Potency*5)% for the next 'Count' amount of hits. Max potency or count: 99", duration=4))
        elif skill.effect_type == "RAVEN_SPECIAL_2":
            if not hasattr(target, "next_turn_modifiers"): target.next_turn_modifiers = {}
            target.next_turn_modifiers["outgoing_dmg_mult"] = target.next_turn_modifiers.get("outgoing_dmg_mult", 1.0) * 0.30
            self.apply_status_logic(attacker, StatusEffect("Poise", "[light_cyan1]༄[/light_cyan1]", 6, "Boost Critical Hit chance by (Potency*5)% for the next 'Count' amount of hits. Max potency or count: 99", duration=1))
        elif skill.effect_type == "FALCON_SPECIAL_1":
            self.apply_status_logic(target, StatusEffect("Rupture", "[medium_spring_green]✧[/medium_spring_green]", 4, "Upon getting hit by a skill, Take extra fixed damage equal to the amount of Potency, then reduce count by 1. Max Potency or Count: 99", duration=1))
        elif skill.effect_type == "FALCON_SPECIAL_2":
            if not hasattr(target, "next_turn_modifiers"): target.next_turn_modifiers = {}
            target.next_turn_modifiers["outgoing_dmg_mult"] = target.next_turn_modifiers.get("outgoing_dmg_mult", 1.0) * 0.30
            self.apply_status_logic(attacker, StatusEffect("Haste", "[yellow1]🢙[/yellow1]", 0, "Deal +(10*Count)% base damage with skills. Lose 1 count every new turn. Max count: 5", duration=2))
            self.apply_status_logic(target, StatusEffect("Bind", "[dim gold1]⛓[/dim gold1]", 1, "Deal -(10*Count)% base damage with skills. Lose 1 count every new turn. Max Count: 5", duration=2))
        elif skill.effect_type == "EAGLE_SPECIAL_1":
            target.next_hit_taken_flat_bonus += 5
            if not hasattr(target, "next_turn_modifiers"): target.next_turn_modifiers = {}
            target.next_turn_modifiers["outgoing_dmg_mult"] = target.next_turn_modifiers.get("outgoing_dmg_mult", 1.0) * 0.50
        elif skill.effect_type == "EAGLE_SPECIAL_2":
            self.apply_status_logic(target, StatusEffect("Rupture", "[medium_spring_green]✧[/medium_spring_green]", 2, "Upon getting hit by a skill, Take extra fixed damage equal to the amount of Potency, then reduce count by 1. Max Potency or Count: 99", duration=5))

        # Riposte Gang / Adam
        elif skill.effect_type == "RIPOSTE_GAIN_SPECIAL_1":
            if any(s.name == "Pierce Affinity" for s in target.status_effects):
                self.apply_status_logic(attacker, StatusEffect("Riposte", "[cyan1]➲[/cyan1]", 0, "Take -5% damage for every 10 stacks owned (max -25%). When taking damage, reduce stack count by 1-4 stacks. For every 10 cumulative stacks reduced this way, gain 1 Haste next turn, then reset the count. At end of turn, reduce stack count by 25%. Max Count: 50", duration=10))
        elif skill.effect_type == "PIERCE_AFFINITY_INFLICT_SPECIAL_1":
            if any(s.name == "Pierce Affinity" for s in target.status_effects):
                self.apply_status_logic(target, StatusEffect("Pierce Affinity", "[light_yellow3]➾[/light_yellow3]", 0, "Take +Base Damage from any skill related to Pierce Affinity based on stack amount. Upon getting hit by a skill, reduce count by 1. Max Count: 5", duration=2))
            else:
                self.apply_status_logic(target, StatusEffect("Pierce Affinity", "[light_yellow3]➾[/light_yellow3]", 0, "Take +Base Damage from any skill related to Pierce Affinity based on stack amount. Upon getting hit by a skill, reduce count by 1. Max Count: 5", duration=1))
        elif skill.effect_type == "RIPOSTE_SQUAD_LEADER_SPECIAL_1":
            self.apply_status_logic(target, StatusEffect("Pierce Affinity", "[light_yellow3]➾[/light_yellow3]", 0, "Take +Base Damage from any skill related to Pierce Affinity based on stack amount. Upon getting hit by a skill, reduce count by 1. Max Count: 5", duration=2))
        elif skill.effect_type == "RIPOSTE_SQUAD_LEADER_SPECIAL_2":
            self.apply_status_logic(target, StatusEffect("Pierce Affinity", "[light_yellow3]➾[/light_yellow3]", 0, "Take +Base Damage from any skill related to Pierce Affinity based on stack amount. Upon getting hit by a skill, reduce count by 1. Max Count: 5", duration=3))
        elif skill.effect_type == "ADAM_SPECIAL_1":
            self.apply_status_logic(target, StatusEffect("Pierce Affinity", "[light_yellow3]➾[/light_yellow3]", 0, "Take +Base Damage from any skill related to Pierce Affinity based on stack amount. Upon getting hit by a skill, reduce count by 1. Max Count: 5", duration=2))
            self.apply_status_logic(attacker, StatusEffect("Riposte", "[cyan1]➲[/cyan1]", 0, "Take -5% damage for every 10 stacks owned (max -25%). When taking damage, reduce stack count by 1-4 stacks. For every 10 cumulative stacks reduced this way, gain 1 Haste next turn, then reset the count. At end of turn, reduce stack count by 25%. Max Count: 50", duration=10))
        elif skill.effect_type == "ADAM_SPECIAL_2":
            pierce_target_eff = next((s for s in target.status_effects if s.name == "Pierce Affinity"), None)
            if pierce_target_eff:
                self.apply_status_logic(attacker, StatusEffect("Riposte", "[cyan1]➲[/cyan1]", 0, "Take -5% damage for every 10 stacks owned (max -25%). When taking damage, reduce stack count by 1-4 stacks. For every 10 cumulative stacks reduced this way, gain 1 Haste next turn, then reset the count. At end of turn, reduce stack count by 25%. Max Count: 50", duration=5 * pierce_target_eff.duration))
            self.apply_status_logic(target, StatusEffect("Pierce Affinity", "[light_yellow3]➾[/light_yellow3]", 0, "Take +Base Damage from any skill related to Pierce Affinity based on stack amount. Upon getting hit by a skill, reduce count by 1. Max Count: 5", duration=3))
        elif skill.effect_type == "ADAM_SPECIAL_3":
            self.apply_status_logic(target, StatusEffect("Pierce Affinity", "[light_yellow3]➾[/light_yellow3]", 0, "Take +Base Damage from any skill related to Pierce Affinity based on stack amount. Upon getting hit by a skill, reduce count by 1. Max Count: 5", duration=5))
            riposte_eff = next((s for s in attacker.status_effects if s.name == "Riposte"), None)
            if riposte_eff: riposte_eff.duration = 50
            else: self.apply_status_logic(attacker, StatusEffect("Riposte", "[cyan1]➲[/cyan1]", 0, "Take -5% damage for every 10 stacks owned (max -25%). When taking damage, reduce stack count by 1-4 stacks. For every 10 cumulative stacks reduced this way, gain 1 Haste next turn, then reset the count. At end of turn, reduce stack count by 25%. Max Count: 50", duration=50))
        
        # --- COUNTER SKILLS [ON HIT] EFFECTS ---
        elif skill.effect_type == "COUNTER_SKILL_SPECIAL_TYPE1":
            self.apply_status_logic(target, StatusEffect("Pierce Affinity", "[light_yellow3]➾[/light_yellow3]", 0, "Take +Base Damage from any skill related to Pierce Affinity based on stack amount. Upon getting hit by a skill, reduce count by 1. Max Count: 5", duration=2))
            
        elif skill.effect_type == "COUNTER_SKILL_SPECIAL_TYPE3":
            self.apply_status_logic(target, StatusEffect("Pierce Affinity", "[light_yellow3]➾[/light_yellow3]", 0, "Take +Base Damage from any skill related to Pierce Affinity based on stack amount. Upon getting hit by a skill, reduce count by 1. Max Count: 5", duration=3))

        # --- RIPOSTE GANG KATAS SKILL EFFECTS ---
        elif skill.effect_type in [
            "NAGANOHARA_RIPOSTE_APPEL", "NAGANOHARA_RIPOSTE_CEDE", "NAGANOHARA_RIPOSTE_COUNTERPARRY", 
            "AKASUKE_RIPOSTE_ENGARDE", "AKASUKE_RIPOSTE_FEINT", "AKASUKE_RIPOSTE_PRISEDEFER"
        ]:
            riposte_eff = next((s for s in attacker.status_effects if s.name == "Riposte"), None)
            
            # --- NAGANOHARA SKILLS ---
            if skill.effect_type == "NAGANOHARA_RIPOSTE_APPEL":
                self.apply_status_logic(attacker, StatusEffect("Riposte", "[cyan1]➲[/cyan1]", 0, "Take -5% damage for every 10 stacks owned (max -25%). When taking damage, reduce stack count by 1-4 stacks. For every 10 cumulative stacks reduced this way, gain 1 Haste next turn, then reset the count. At end of turn, reduce stack count by 25%. Max Count: 50", duration=5))
                self.apply_status_logic(target, StatusEffect("Pierce Affinity", "[light_yellow3]➾[/light_yellow3]", 0, "Take +Base Damage from any skill related to Pierce Affinity based on stack amount. Upon getting hit by a skill, reduce count by 1. Max Count: 5", duration=1))
                
            elif skill.effect_type == "NAGANOHARA_RIPOSTE_CEDE":
                self.apply_status_logic(attacker, StatusEffect("Riposte", "[cyan1]➲[/cyan1]", 0, "Take -5% damage for every 10 stacks owned (max -25%). When taking damage, reduce stack count by 1-4 stacks. For every 10 cumulative stacks reduced this way, gain 1 Haste next turn, then reset the count. At end of turn, reduce stack count by 25%. Max Count: 50", duration=10))
                self.apply_status_logic(target, StatusEffect("Pierce Affinity", "[light_yellow3]➾[/light_yellow3]", 0, "Take +Base Damage from any skill related to Pierce Affinity based on stack amount. Upon getting hit by a skill, reduce count by 1. Max Count: 5", duration=2))
                # Damage and debuff logic is handled in Step 2!
                
            elif skill.effect_type == "NAGANOHARA_RIPOSTE_COUNTERPARRY":
                if riposte_eff and riposte_eff.duration >= 25:
                    riposte_eff.duration = 50
                    self.log(f"[cyan1]{attacker.name} maxes out their Riposte Stance![/cyan1]")
                else:
                    self.apply_status_logic(attacker, StatusEffect("Riposte", "[cyan1]➲[/cyan1]", 0, "Take -5% damage for every 10 stacks owned (max -25%). When taking damage, reduce stack count by 1-4 stacks. For every 10 cumulative stacks reduced this way, gain 1 Haste next turn, then reset the count. At end of turn, reduce stack count by 25%. Max Count: 50", duration=20))
                self.apply_status_logic(target, StatusEffect("Pierce Affinity", "[light_yellow3]➾[/light_yellow3]", 0, "Take +Base Damage from any skill related to Pierce Affinity based on stack amount. Upon getting hit by a skill, reduce count by 1. Max Count: 5", duration=3))
                
            # --- AKASUKE SKILLS ---
            elif skill.effect_type == "AKASUKE_RIPOSTE_ENGARDE":
                if not riposte_eff or riposte_eff.duration <= 0:
                    self.apply_status_logic(attacker, StatusEffect("Riposte", "[cyan1]➲[/cyan1]", 0, "Take -5% damage for every 10 stacks owned (max -25%). When taking damage, reduce stack count by 1-4 stacks. For every 10 cumulative stacks reduced this way, gain 1 Haste next turn, then reset the count. At end of turn, reduce stack count by 25%. Max Count: 50", duration=10))
                else:
                    self.apply_status_logic(attacker, StatusEffect("Riposte", "[cyan1]➲[/cyan1]", 0, "Take -5% damage for every 10 stacks owned (max -25%). When taking damage, reduce stack count by 1-4 stacks. For every 10 cumulative stacks reduced this way, gain 1 Haste next turn, then reset the count. At end of turn, reduce stack count by 25%. Max Count: 50", duration=5))
                self.apply_status_logic(target, StatusEffect("Pierce Affinity", "[light_yellow3]➾[/light_yellow3]", 0, "Take +Base Damage from any skill related to Pierce Affinity based on stack amount. Upon getting hit by a skill, reduce count by 1. Max Count: 5", duration=1))
                
            elif skill.effect_type == "AKASUKE_RIPOSTE_FEINT":
                # [On Use] Gain 1 Haste
                self.apply_status_logic(attacker, StatusEffect("Haste", "[yellow1]🢙[/yellow1]", 0, "Deal +(10*Count)% base damage with skills. Lose 1 count every new turn. Max count: 5", duration=1))
                # [On Use] If this unit has 10+ Riposte, Gain 1 Haste
                if riposte_eff and riposte_eff.duration >= 10:
                    self.apply_status_logic(attacker, StatusEffect("Haste", "[yellow1]🢙[/yellow1]", 0, "Deal +(10*Count)% base damage with skills. Lose 1 count every new turn. Max count: 5", duration=1))
                    
                # [On Hit] If target has Pierce Affinity, gain 10 Riposte
                target_pierce = next((s for s in target.status_effects if s.name == "Pierce Affinity"), None)
                if target_pierce and target_pierce.duration > 0:
                    self.apply_status_logic(attacker, StatusEffect("Riposte", "[cyan1]➲[/cyan1]", 0, "Take -5% damage for every 10 stacks owned (max -25%). When taking damage, reduce stack count by 1-4 stacks. For every 10 cumulative stacks reduced this way, gain 1 Haste next turn, then reset the count. At end of turn, reduce stack count by 25%. Max Count: 50", duration=10))
                    
                # [On Hit] Inflict 2 Pierce Affinity
                self.apply_status_logic(target, StatusEffect("Pierce Affinity", "[light_yellow3]➾[/light_yellow3]", 0, "Take +Base Damage from any skill related to Pierce Affinity based on stack amount. Upon getting hit by a skill, reduce count by 1. Max Count: 5", duration=2))
                
            elif skill.effect_type == "AKASUKE_RIPOSTE_PRISEDEFER":
                self.apply_status_logic(attacker, StatusEffect("Riposte", "[cyan1]➲[/cyan1]", 0, "Take -5% damage for every 10 stacks owned (max -25%). When taking damage, reduce stack count by 1-4 stacks. For every 10 cumulative stacks reduced this way, gain 1 Haste next turn, then reset the count. At end of turn, reduce stack count by 25%. Max Count: 50", duration=10))
                self.apply_status_logic(target, StatusEffect("Pierce Affinity", "[light_yellow3]➾[/light_yellow3]", 0, "Take +Base Damage from any skill related to Pierce Affinity based on stack amount. Upon getting hit by a skill, reduce count by 1. Max Count: 5", duration=3))
                # Base damage increase handled in Step 2!
            
        # --- KIRYOKU FAIRY & INFILTRATOR ---
        elif skill.effect_type == "RUPTURE_SPECIAL1":
            # Yuri Kiryoku S1: If target has Rupture (or Fairylight), +Count. Else, +Potency.
            has_rupture = any(s.name in ["Rupture", "Fairylight"] for s in target.status_effects)
            if has_rupture:
                self.apply_status_logic(target, StatusEffect("Rupture", "[medium_spring_green]✧[/medium_spring_green]", 1, "Upon getting hit by a skill, Take extra fixed damage equal to the amount of Potency, then reduce count by 1. Max Potency or Count: 99", duration=skill.effect_val))
            else:
                self.apply_status_logic(target, StatusEffect("Rupture", "[medium_spring_green]✧[/medium_spring_green]", skill.effect_val, "Upon getting hit by a skill, Take extra fixed damage equal to the amount of Potency, then reduce count by 1. Max Potency or Count: 99", duration=1))

        elif skill.effect_type == "FAIRYLIGHT_APPLY":
            # Benikawa Kiryoku S2 / Hana Kiryoku S1: If target has Rupture (or Fairylight), apply Fairylight
            has_rupture = any(s.name in ["Rupture", "Fairylight"] for s in target.status_effects)
            if has_rupture:
                self.apply_status_logic(target, StatusEffect("Fairylight", "[spring_green1]𒀭[/spring_green1]", skill.effect_val, "Unique Rupture (Counts As Rupture)\nUpon getting hit by a skill, Take extra fixed damage equal to the amount of Potency. On turn end, reduce Count by half, and if this unit has Rupture, gain Rupture Potency based on Count lost this way. Max Potency or Count: 99", duration=1))

        # FIX 2: Removed [On Use] self modifier portion from BENIKAWA_KIRYOKU_SPECIAL entirely since it is in Step 1
        elif skill.effect_type == "BENIKAWA_KIRYOKU_SPECIAL":
            has_rupture = any(s.name in ["Rupture", "Fairylight"] for s in target.status_effects)
            if has_rupture:
                self.apply_status_logic(target, StatusEffect("Fairylight", "[spring_green1]𒀭[/spring_green1]", 3, "Unique Rupture (Counts As Rupture)\nUpon getting hit by a skill, Take extra fixed damage equal to the amount of Potency. On turn end, reduce Count by half, and if this unit has Rupture, gain Rupture Potency based on Count lost this way. Max Potency or Count: 99", duration=1))

        elif skill.effect_type == "FAIRYLIGHT_SPECIAL1":
            # Hana Kiryoku S2: If target has Fairylight (specifically), inflict Rupture Potency
            has_fairylight = any(s.name == "Fairylight" for s in target.status_effects)
            if has_fairylight:
                self.apply_status_logic(target, StatusEffect("Rupture", "[medium_spring_green]✧[/medium_spring_green]", skill.effect_val, "Upon getting hit by a skill, Take extra fixed damage equal to the amount of Potency, then reduce count by 1. Max Potency or Count: 99", duration=1))

        elif skill.effect_type == "HANA_KIRYOKU_SPECIAL":
            # Hana Kiryoku S3: If target has Fairylight (specifically), inflict 2 Rupture Count, then take -30% dmg this turn
            has_fairylight = any(s.name == "Fairylight" for s in target.status_effects)
            if has_fairylight:
                self.apply_status_logic(target, StatusEffect("Rupture", "[medium_spring_green]✧[/medium_spring_green]", 1, "Upon getting hit by a skill, Take extra fixed damage equal to the amount of Potency, then reduce count by 1. Max Potency or Count: 99", duration=2))
                attacker.temp_modifiers["incoming_dmg_mult"] *= 0.70

        elif skill.effect_type == "HASTE_GAIN_SPECIAL_TYPE1":
            # Shigemura Infiltrator S1: [On Use] If has Haste, gain 1 Haste. [On Hit] Gain 1 Haste.
            has_haste = any(s.name == "Haste" for s in attacker.status_effects)
            if has_haste:
                self.apply_status_logic(attacker, StatusEffect("Haste", "[yellow1]🢙[/yellow1]", 0, "Deal +(10*Count)% base damage with skills. Lose 1 count every new turn. Max count: 5", duration=1))
            self.apply_status_logic(attacker, StatusEffect("Haste", "[yellow1]🢙[/yellow1]", 0, "Deal +(10*Count)% base damage with skills. Lose 1 count every new turn. Max count: 5", duration=skill.effect_val))

        elif skill.effect_type == "DEBUFF_ATK_MULT":
            # Target deals reduced damage for the rest of the turn
            target.temp_modifiers["outgoing_dmg_mult"] *= skill.effect_val

        # --- BENIKAWA NINJA CLAN ---
        elif skill.effect_type == "BENIKAWA_CLAN_SPECIAL_1":
            # Target takes +4 Final Damage from other attacks this turn (by reducing their flat defense by 4)
            target.temp_modifiers["final_dmg_reduction"] -= 4
            
            # If target has Bleed, Inflict 3 Bleed Potency
            has_bleed = any(s.name == "Bleed" for s in target.status_effects)
            if has_bleed:
                self.apply_status_logic(target, StatusEffect("Bleed", "[red]💧︎[/red]", 3, "", duration=1))
                
            # Inflict 1 Pierce Affinity
            self.apply_status_logic(target, StatusEffect("Pierce Affinity", "[light_yellow3]⇴[/light_yellow3]", 0, "", duration=1))

        elif skill.effect_type == "BENIKAWA_CLAN_SPECIAL_2":
            # If this unit does not have Poise, gain 4 Poise Count (we assign 1 Potency to obey the minimum rule)
            has_poise = any(s.name == "Poise" for s in attacker.status_effects)
            if not has_poise:
                self.apply_status_logic(attacker, StatusEffect("Poise", "[light_cyan1]༄[/light_cyan1]", 1, "", duration=4))
                
            # Gain 3 Poise Potency
            self.apply_status_logic(attacker, StatusEffect("Poise", "[light_cyan1]༄[/light_cyan1]", 3, "", duration=1))
            
            # Gain 2 Haste next turn (Auto-intercepted by our delayed application queue!)
            self.apply_status_logic(attacker, StatusEffect("Haste", "[yellow1]🢙[/yellow1]", 0, "", duration=2))

        elif skill.effect_type == "BENIKAWA_CLAN_SPECIAL_3":
            # Target deals -15% damage this turn, then deals -25% damage next turn
            target.temp_modifiers["outgoing_dmg_mult"] *= 0.85
            target.next_turn_modifiers["outgoing_dmg_mult"] = target.next_turn_modifiers.get("outgoing_dmg_mult", 1.0) * 0.75
            
            # If target has Bleed, inflict 3 Bleed Count and 3 Bleed Potency, then this unit gains 2 Haste next turn
            has_bleed = any(s.name == "Bleed" for s in target.status_effects)
            if has_bleed:
                self.apply_status_logic(target, StatusEffect("Bleed", "[red]💧︎[/red]", 3, "", duration=3))
                self.apply_status_logic(attacker, StatusEffect("Haste", "[yellow1]🢙[/yellow1]", 0, "", duration=2))
                
            # If target has Pierce Affinity, inflict 2 Pierce Affinity, then this unit gains 3 Poise Potency and 2 Poise Count
            has_pierce = any(s.name == "Pierce Affinity" for s in target.status_effects)
            if has_pierce:
                self.apply_status_logic(target, StatusEffect("Pierce Affinity", "[light_yellow3]⇴[/light_yellow3]", 0, "", duration=2))
                self.apply_status_logic(attacker, StatusEffect("Poise", "[light_cyan1]༄[/light_cyan1]", 3, "", duration=2))

        if target.hp <= 0:
            target.hp = 0
            self.log(f"[bold red]{target.name} was defeated![/bold red]")

        self.render_battle_screen()
        time.sleep(0.5)

    def apply_status_logic(self, target, new_status):
        """
        Handles stacking logic (Potency vs Count).
        Implements 'First Time' Application rules for Bleed.
        """
        
        # --- PRE-PROCESS: DELAYED APPLICATION (Bind & Haste) ---
        if new_status.name == "Bind":
            if not hasattr(target, "pending_bind"): target.pending_bind = 0
            target.pending_bind = min(5, target.pending_bind + new_status.duration)
            return
            
        if new_status.name == "Haste":
            if not hasattr(target, "pending_haste"): target.pending_haste = 0
            target.pending_haste = min(5, target.pending_haste + new_status.duration)
            return

        if new_status.name == "Pierce Affinity":
            new_status.duration = min(5, new_status.duration)

        # --- PRE-PROCESS: DUAL-STACK MINIMUM 1 RULE ---
        if new_status.name in DUAL_STACK_EFFECTS:
            if new_status.duration > 0 and new_status.potency <= 0:
                new_status.potency = 1
            elif new_status.potency > 0 and new_status.duration <= 0:
                new_status.duration = 1

        # --- FIND EXISTING ---
        existing = next((s for s in target.status_effects if s.name == new_status.name), None)
        
        if existing:
            # --- MERGE LOGIC ---
            if new_status.name in ["Bleed", "Poise", "Rupture", "Fairylight"]:
                existing.duration = min(99, existing.duration + new_status.duration)
                existing.potency = min(99, existing.potency + new_status.potency)
            elif new_status.name in ["Bind", "Haste", "Pierce Affinity"]:
                existing.duration = min(5, existing.duration + new_status.duration)
            
            else:
                # Generic Stacking
                existing.duration += new_status.duration
                existing.potency += new_status.potency
        else:
            # --- NEW APPLICATION (FIRST TIME LOGIC) ---
            if new_status.name in ["Bleed", "Poise", "Rupture", "Fairylight"]:
                # Rule 1: Ensure Duration starts at least 1.
                if new_status.duration < 1:
                    new_status.duration = 1
                # Rule 2: Ensure Potency starts at least 1.
                if new_status.potency < 1:
                    new_status.potency = 1
                # Cap Checks
                new_status.duration = min(99, new_status.duration)
                new_status.potency = min(99, new_status.potency)
            target.status_effects.append(new_status)
            

            """
            End of execute_skill()
            """

    def inspect_unit_menu(self):
        clear_screen()
        config.console.print(Panel("[bold]INSPECT MODE[/bold]", style="white on blue"))
        
        all_units = self.allies + self.enemies
        for idx, unit in enumerate(all_units):
            config.console.print(f"[{idx+1}] {unit.name}")
        
        config.console.print("[Enter] Back")
        choice = get_player_input("Inspect > ")
        
        if choice == "":
            return
            
        if choice.isdigit():
            idx = int(choice) - 1
            if 0 <= idx < len(all_units):
                self.show_unit_details(all_units[idx])
    
    def show_unit_details(self, unit):
        while True:
            clear_screen()
            res_table = Table(title="Elemental Weaknesses", box=None)
            res_table.add_column("Element"); res_table.add_column("Mult")
            for i, name in enumerate(ELEMENT_NAMES):
                color = get_element_color(i)
                val = unit.resistances[i]
                style = "green" if val < 1.0 else ("red" if val > 1.0 else "white")
                res_table.add_row(f"[{color}]{name}[/{color}]", f"[{style}]{val}x[/{style}]")

            # --- KATA / RIFT APTITUDE DISPLAY ---
            if unit in self.enemies:
                kata_label = "Rift Aptitude"
                kata_info_str = unit.kata.rift_aptitude
            else:
                kata_label = "Kata"
                kata_info_str = unit.kata.name if unit.kata else "None"

            pool_text = ""
            if unit.kata and hasattr(unit.kata, 'skill_pool_def'):
                sorted_pool = sorted(unit.kata.skill_pool_def, key=lambda x: x[0].tier)
                for skill, count in sorted_pool:
                    c = get_element_color(skill.element)
                    t_r = get_tier_roman(skill.tier)
                    desc = skill.description if skill.description else ""
                    dmg_str = f"[bold]Dmg: {skill.base_damage}[/bold]"
                    pool_text += f"x{count} [{c}]{skill.name}[/{c}] ({t_r}) {dmg_str}\n       [light_green]{desc}[/light_green]\n"
            else:
                pool_text = "No Kata / Skill info available."

            status_list = []
            if unit.temp_modifiers["final_dmg_reduction"] > 0:
                 status_list.append(f"Defense +{unit.temp_modifiers['final_dmg_reduction']}")
            if unit.temp_modifiers["outgoing_dmg_mult"] != 1.0:
                 pct = int((unit.temp_modifiers["outgoing_dmg_mult"] * 100))
                 status_list.append(f"Damage Output: {pct}%")
            if unit.temp_modifiers["incoming_dmg_mult"] != 1.0:
                 pct = int((unit.temp_modifiers["incoming_dmg_mult"] * 100))
                 status_list.append(f"Damage Taken: {pct}%")
            if unit.temp_modifiers["incoming_dmg_flat"] != 0:
                 val = unit.temp_modifiers["incoming_dmg_flat"]
                 sign = "+" if val > 0 else ""
                 status_list.append(f"Incoming Dmg: {sign}{val}")

            status_str = ", ".join(status_list) if status_list else "None"
            
            se_text = ""
            if unit.status_effects:
                for i, effect in enumerate(unit.status_effects):
                    if effect.name in DURATION_ONLY_EFFECTS:
                        # Bind and some others don't show potency, only count
                        se_text += f"[bold cyan]SE{i+1}[/bold cyan]: {effect.symbol} {effect.name} (Count: {effect.duration})\n"
                    else:
                        se_text += f"[bold cyan]SE{i+1}[/bold cyan]: {effect.symbol} {effect.name} (Potency: {effect.potency}, Count: {effect.duration})\n"
            else:
                se_text = "No active status effects."

            content = f"""
[bold]{unit.name}[/bold]
HP: {unit.hp}/{unit.max_hp}
{kata_label}: {kata_info_str}
Modifiers: {status_str}

[bold]Status Effects:[/bold]
{se_text}

[bold]Full Skill Pool:[/bold]
{pool_text}
            """
            layout = Layout()
            layout.split_row(Layout(Panel(content)), Layout(Panel(res_table)))
            config.console.print(layout)
            config.console.print("\nType [bold]SE#[/bold] (e.g. SE1) to view status details, or [Enter] to return.")
            
            choice = get_player_input("Input > ").upper()
            if choice == "": break
                
            if choice.startswith("SE") and choice[2:].isdigit():
                idx = int(choice[2:]) - 1
                if 0 <= idx < len(unit.status_effects):
                    eff = unit.status_effects[idx]
                    
                    # --- FIX: Ensure Fairylight and Rupture always display correct descriptions ---
                    disp_name = eff.name
                    disp_desc = eff.description
                    
                    if disp_name == "Fairylight":
                        disp_desc = "Unique Rupture (Counts As Rupture)\nUpon getting hit by a skill, Take extra fixed damage equal to the amount of Potency. On turn end, reduce Count by half, and if this unit has Rupture, gain Rupture Potency based on Count lost this way. Max Potency or Count: 99"
                    elif disp_name == "Rupture":
                        disp_desc = "Upon getting hit by a skill, Take extra fixed damage equal to the amount of Potency, then reduce count by 1. Max Potency or Count: 99"
                    
                    config.console.print(Panel(f"[bold]{disp_name}[/bold]\n\n{disp_desc}", title="Status Effect", style="green"))
                    get_player_input("Press Enter...")

    def check_win_condition(self):
        if all(e.hp <= 0 for e in self.enemies):
            self.is_battle_over = True; self.won = True; return True
        return False

    def check_loss_condition(self):
        if all(a.hp <= 0 for a in self.allies):
            self.is_battle_over = True; self.won = False; return True
        return False

    def log(self, message):
        # PAGING LOGIC: 
        # If the log has reached the panel height limit, 
        # clear the entire list so the new message starts fresh at the top.
        if len(self.battle_log) >= 11:
            self.battle_log = []
            self.battle_log.append(message)
        else:
            self.battle_log.append(message)

    def render_battle_screen(self, active_unit=None):
        clear_screen()
        config.console.print(Panel(f"TURN {self.turn_count}", style="white on blue", width=20))
        
        for e in self.enemies:
            intent_str = ""
            intended_skill = None
            if e.hp > 0 and e.intent:
                skill, target, _ = e.intent
                intended_skill = skill
                c = get_element_color(skill.element)
                tier_r = get_tier_roman(skill.tier)
                intent_str = f"-> [{c}]{skill.name}[/{c}] ({tier_r}) -> {target.name}"
            hp_style = "green" if e.hp > e.max_hp/2 else "red"
            status = "Defeated" if e.hp <= 0 else f"[{hp_style}]{e.hp}/{e.max_hp}[/{hp_style}]"
            se_display = ""
            for se in e.status_effects:
                # Visual distinction: Bind and many more status effects don't show potency
                if se.name in DURATION_ONLY_EFFECTS:
                    se_display += f"{se.symbol} x{se.duration} "
                else:
                    sub = to_subscript(se.potency)
                    se_display += f"{se.symbol}{sub}/{se.duration} "
            config.console.print(f"[bold red]{e.name}[/bold red] {status} {intent_str}")
            if se_display: config.console.print(f"   {se_display}")
            
            # SHOW ENEMY SKILL DESCRIPTION
            if intended_skill and intended_skill.description:
                config.console.print(f"      [light_green]{intended_skill.description}[/light_green]")

        config.console.print("\n" + "-"*30 + "\n")
        
        # Two-panel ally display (left: 1-4, right: 5-8)
        ally_displays = []
        for a in self.allies:
            active_marker = ">>" if a == active_unit else "  "
            hp_style = "green" if a.hp > a.max_hp/2 else "red"
            target_str = ""
            if a.hp > 0 and a.auto_target and a.auto_target.hp > 0:
                target_str = f"-> {a.auto_target.name}"
            auto_badge = "[bold yellow][AUTO][/bold yellow] " if self.auto_battle else ""
            se_display = ""
            for se in a.status_effects:
                if se.name in DURATION_ONLY_EFFECTS:
                    se_display += f"{se.symbol} x{se.duration} "
                else:
                    sub = to_subscript(se.potency)
                    se_display += f"{se.symbol}{sub}/{se.duration} "
            
            name_line = f"{active_marker} {auto_badge}[bold cyan]{a.name}[/bold cyan] [{hp_style}]{a.hp}/{a.max_hp}[/{hp_style}] {target_str}"
            ally_lines = [name_line]
            if se_display.strip():
                ally_lines.append(f"   {se_display}")
            if a.hand:
                for i, s in enumerate(a.hand):
                    c = get_element_color(s.element)
                    t1 = get_tier_roman(s.tier)
                    skill_line = f"   [{i+1}] [{c}]{s.name}[/{c}] ({t1})"
                    ally_lines.append(skill_line)
                    if s.description:
                        ally_lines.append(f"      [light_green]{s.description}[/light_green]")
            ally_lines.append("")  # Empty line separator between allies
            ally_displays.append(ally_lines)

        # Flatten into left (1-4) and right (5-8)
        left_text_lines = []
        for ad in ally_displays[:4]:
            left_text_lines.extend(ad)
        right_text_lines = []
        for ad in ally_displays[4:]:
            right_text_lines.extend(ad)

        left_text = "\n".join(left_text_lines).rstrip("\n")
        right_text = "\n".join(right_text_lines).rstrip("\n")

        # Create panels
        left_panel = Panel(left_text, title="[bold cyan]Party[/]", padding=(0, 1), width=84, border_style="cyan")
        panels = [left_panel]
        if right_text_lines:
            right_panel = Panel(right_text, title="[bold cyan]Party[/]", padding=(0, 1), width=84, border_style="cyan")
            panels.append(right_panel)

        config.console.print(Columns(panels, expand=True))
        config.console.print(Panel("\n".join(self.battle_log), title="Battle Log", height=14))

battle_manager = BattleManager()