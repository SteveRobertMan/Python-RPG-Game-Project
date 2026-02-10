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
            unit.pending_bind = 0  # <--- NEW: Initialize Pending Bind
            
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
        # Implementation of specific [Combat Start] effects
        if skill.effect_type == "BUFF_DEF_FLAT":
             unit.temp_modifiers["final_dmg_reduction"] += skill.effect_val

    def process_turn_end_effects(self):
        """
        Handles Status Effect ticks.
        Logic updated to support Potency/Count system.
        'duration' attribute in code is treated as 'Count'.
        """
        effects_triggered = False
        all_units = self.allies + self.enemies
        
        for unit in all_units:
            if unit.hp <= 0: continue
            
            # --- HIDDEN FLAGS ---
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

                # 2. Bind Logic (Decay Count by 1 every turn)
                elif effect.name == "Bind":
                    effect.duration -= 1
                # 2. Bind Logic (Decay Count by 1 every turn)
                elif effect.name == "Poise":
                    effect.duration -= 1
                
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
            # This happens AFTER the decay loop above. 
            # This ensures the new Bind is applied fresh for the start of the next turn.
            if getattr(unit, "pending_bind", 0) > 0:
                # Construct the Bind Effect
                # Note: We cap it at 5 here just to be safe, though logic usually caps on add
                actual_duration = min(5, unit.pending_bind)
                
                bind_effect = StatusEffect(
                    name="Bind", 
                    symbol="[dim gold1]⛓[/dim gold1]", 
                    potency=1, 
                    duration=actual_duration, 
                    description="Deal -(10%*Count) of base damage with skills. Lose 1 count every new turn. Max count: 5"
                )
                #self.log(f"[gold1]{unit.name}! Becomes bound for {bind_effect.duration}[/gold1]")
                #time.sleep(0.5)
                unit.status_effects.append(bind_effect)
                
                # Reset pending to 0
                unit.pending_bind = 0
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

# --- [STEP 1] [On Use] EFFECTS ---
        if "[On Use]" in skill.description:
            if skill.effect_type == "BUFF_DEF_FLAT":
                 attacker.temp_modifiers["final_dmg_reduction"] = attacker.temp_modifiers.get("final_dmg_reduction", 0) + skill.effect_val

        # --- [STEP 2] DAMAGE CALCULATION ---
        if skill.base_damage > 0:
            # 1. Base Damage & Variance
            base_dmg_val = float(skill.base_damage)

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
            elif skill.effect_type == "GAIN_POISE_SPECIAL_1":
                self.apply_status_logic(attacker, StatusEffect("Poise", "[light_cyan1]༄[/light_cyan1]", 2, "", duration=0))

            # 5. Critical Hit Roll (POISE CHECK)
            poise = next((se for se in attacker.status_effects if se.name == "Poise"), None)
            if poise and poise.potency > 0 and poise.duration > 0:
                crit_chance = min(100, poise.potency * 5)
                if random.randint(1, 100) <= crit_chance:
                    is_crit = True
                    dmg *= 1.2  # 20% Crit Multiplier

            # 6. Elemental & Global Multipliers (CRASH PROTECTION: Added .get())
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

            damage = int(final_dmg) - target.temp_modifiers.get("final_dmg_reduction", 0)

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

            # Final Defense Reduction (Armor)
            flat_def = target.temp_modifiers["final_dmg_reduction"]
            damage = damage - flat_def
            damage = max(1, damage) # Minimum 1 damage if hit connects

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

            # --- APPLY DAMAGE ---
            if damage > 0:
                target.hp -= damage
                el_color = get_element_color(skill.element)
                eff_text = " [bold yellow](WEAK!)[/]" if res_mult > 1.0 else (" [dim](Resist)[/]" if res_mult < 1.0 else "")
                crit_text = "[khaki1]Critical![/] " if is_crit else ""
                
                self.log(f"-> {crit_text}Hit {target.name} for [bold {el_color}]{damage}[/bold {el_color}]!{eff_text}")
                
                # Skill III On Hit
                if skill.effect_type == "GAIN_POISE_SPECIAL_1":
                    self.apply_status_logic(attacker, StatusEffect("Poise", "[light_cyan1]༄[/light_cyan1]", 4, "", duration=0))
                
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

                # --- LOGIC: POISE SUPPORT ---
                if skill.effect_type == "ON_HIT_PROVIDE_POISE_TYPE1":
                    # Logic: Grant +1 Poise Count to all allies who already have Poise
                    team = self.allies if attacker in self.allies else self.enemies
                    for member in team:
                        poise_effect = next((e for e in member.status_effects if e.name == "Poise"), None)
                        if poise_effect:
                            # Increase Duration (Count) by val (1), cap at 99
                            poise_effect.duration = min(99, poise_effect.duration + skill.effect_val)
                            # if self.console: self.console.print(f"   [cyan]>{member.name}'s Poise Count +{skill.effect_val}![/cyan]")
                if skill.effect_type == "ON_HIT_PROVIDE_POISE_TYPE2":
                    # Logic: Grant +2 Potency AND +2 Count to allies with Poise
                    team = self.allies if attacker in self.allies else self.enemies
                    for member in team:
                        poise_effect = next((e for e in member.status_effects if e.name == "Poise"), None)
                        if poise_effect:
                            # Increase Potency and Duration, cap at 99
                            poise_effect.potency = min(99, poise_effect.potency + skill.effect_val)
                            poise_effect.duration = min(99, poise_effect.duration + skill.effect_val)
                            # if self.console: self.console.print(f"   [cyan]>{member.name}'s Poise Strengthened![/cyan]")
                if skill.effect_type == "ON_HIT_PROVIDE_POISE_TYPE3":
                            # Logic: Grant +2 Poise Potency to all allies who already have Poise
                    team = self.allies if attacker in self.allies else self.enemies
                    for member in team:
                        poise_effect = next((e for e in member.status_effects if e.name == "Poise"), None)
                        if poise_effect:
                            # Increase Potency by val (2), cap at 99
                            poise_effect.potency = min(99, poise_effect.potency + skill.effect_val)
                            #if self.console: self.console.print(f"   [cyan]>{member.name}'s Poise Potency +{skill.effect_val}![/cyan]")
                if skill.effect_type == "ON_HIT_CONVERT_POISE_TYPE1":
                    # Logic: Convert 1 Potency -> 1 Count if Potency >= 2
                    team = self.allies if attacker in self.allies else self.enemies
                    for member in team:
                        poise_effect = next((e for e in member.status_effects if e.name == "Poise"), None)
                        # Check condition: Must have at least 2 Potency (to afford the cost of 1)
                        if poise_effect and poise_effect.potency >= 2:
                            poise_effect.potency -= 1
                            poise_effect.duration = min(99, poise_effect.duration + 1)
                            #if self.console: self.console.print(f"   [cyan]>{member.name} converted Poise Potency to Count![/cyan]")

                # --- NEXT HIT BONUSES ---
                if skill.effect_type == "ON_HIT_NEXT_TAKEN_FLAT":
                    target.next_hit_taken_flat_bonus += skill.effect_val
                if skill.effect_type == "ON_HIT_NEXT_DEAL_FLAT":
                    attacker.next_hit_deal_flat_bonus += skill.effect_val
                if skill.effect_type == "SELF_NEXT_TAKEN_FLAT":
                    attacker.next_hit_taken_flat_bonus += skill.effect_val
                if skill.effect_type == "DEBUFF_INCOMING_DMG_FLAT":
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
            
            #self.log(f"[bold gold1]{attacker.name} rallies the team![/bold gold1]")

        # BLEED_POTENCY_DEF_BUFF (Yuri Heiwa S3)
        elif skill.effect_type == "BLEED_POTENCY_DEF_BUFF":
            if skill.status_effect:
                # Apply deepcopy of status to prevent template corruption
                effect_instance = copy.deepcopy(skill.status_effect)
                self.apply_status_logic(target, effect_instance)
            
            # Apply Defense Buff to User
            attacker.temp_modifiers["final_dmg_reduction"] += skill.effect_val
        
        # --- BENIKAWA SKILL LOGIC ---
        
        # DEF_BUFF_BASE_PER (Benikawa S2)
        elif skill.effect_type == "DEF_BUFF_BASE_PER":
            reduction_pct = skill.effect_val / 10.0
            attacker.temp_modifiers["incoming_dmg_mult"] *= (1.0 - reduction_pct)
            #self.log(f"[bold cyan]{attacker.name} presence reduces incoming damage by {int(reduction_pct*100)}%![/bold cyan]")

        # COND_TARGET_HAS_BLEED_DMG_PER (Benikawa S3)
        elif skill.effect_type == "COND_TARGET_HAS_BLEED_DMG_PER":
            has_bleed = any(s.name == "Bleed" for s in target.status_effects)
            if has_bleed:
                bonus_dmg = int(skill.base_damage * (skill.effect_val / 10.0))
                target.hp -= bonus_dmg
                #self.log(f"[bold red]CRUSHER! The wound is exploited for +{bonus_dmg} Bonus Damage![/bold red]")
                
        # --- SADISM BIND APPLY ---
        # Checks the variable we set back in Phase 1
        if 'sadism_bind_to_apply' in locals() and sadism_bind_to_apply > 0:
            # Create Bind Effect manually based on calculation
            bind_eff = StatusEffect(
                "Bind", "[dim gold1]⛓[/dim gold1]", 1, 
                "Deal -(10%*Count) of base damage. Lose 1 count/turn. Max: 5", 
                duration=sadism_bind_to_apply
            )
            # Use existing logic to stack it (Handles the Max 5 Cap and Duration merging)
            self.apply_status_logic(target, bind_eff)
            self.log(f"[bold violet]Sadism inflicts {sadism_bind_to_apply} Bind![/bold violet]")

        # --- EXISTING KUROGANE & GENERIC EFFECTS ---
        elif skill.effect_type == "APPLY_BLEED_HEAVY_STACKS":
            bleed = StatusEffect("Bleed", "[red]💧︎[/red]", 2, "Upon dealing damage, Take fixed damage equal to amount of Potency, then reduce count by 1 Max potency or count: 99", duration=2)
            self.apply_status_logic(target, bleed)
        elif skill.effect_type == "APPLY_BLEED_AND_BIND":
            bleed = StatusEffect("Bleed", "[red]💧︎[/red]", 3, "Upon dealing damage, Take fixed damage equal to amount of Potency, then reduce count by 1 Max potency or count: 99", duration=1)
            self.apply_status_logic(target, bleed)
            bind = StatusEffect("Bind", "[dim gold1]⛓[/dim gold1]", 1, "Deal -(10%*Count) of base damage with skills. Lose 1 count every new turn. Max count: 5", duration=1)
            self.apply_status_logic(target, bind)
        elif skill.effect_type == "APPLY_BLEED_AND_BIND_HEAVY":
            bleed = StatusEffect("Bleed", "[red]💧︎[/red]", 3, "Upon dealing damage, Take fixed damage equal to amount of Potency, then reduce count by 1 Max potency or count: 99", duration=1)
            self.apply_status_logic(target, bleed)
            bind = StatusEffect("Bind", "[dim gold1]⛓[/dim gold1]", 1, "Deal -(10%*Count) of base damage with skills. Lose 1 count every new turn. Max count: 5", duration=2)
            self.apply_status_logic(target, bind)

        # Generic Status + Naganohara Skill III Dual Type
        elif (skill.effect_type == "APPLY_STATUS" or skill.effect_type == "COND_BLEED_DMG_AND_APPLY") and hasattr(skill, "status_effect"):
                if skill.status_effect.name == "Nerve Disruption":
                    target.nerve_disruption_turns = skill.status_effect.duration
                else:
                    new_status = copy.deepcopy(skill.status_effect)
                    self.apply_status_logic(target, new_status)

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
        
        # --- PRE-PROCESS: FIX BIND POTENCY ---
        if new_status.name == "Bind":
            new_status.potency = 1 
            existing_bind = next((s for s in target.status_effects if s.name == "Bind"), None)
            if existing_bind:
                existing_bind.duration = min(5, existing_bind.duration + new_status.duration)
            else:
                # Handles pending_bind if target doesn't have it yet (delayed application)
                if not hasattr(target, "pending_bind"): target.pending_bind = 0
                target.pending_bind = min(5, target.pending_bind + new_status.duration)
            return

        # --- FIND EXISTING ---
        existing = next((s for s in target.status_effects if s.name == new_status.name), None)
        
        if existing:
            # --- MERGE LOGIC ---
            if new_status.name == "Bleed":
                # Stack Duration (Count)
                existing.duration = min(99, existing.duration + new_status.duration)
                # Stack Potency
                existing.potency = min(99, existing.potency + new_status.potency)
            
            else:
                # Generic Stacking
                existing.duration += new_status.duration
                existing.potency += new_status.potency
        else:
            # --- NEW APPLICATION (FIRST TIME LOGIC) ---
            if new_status.name in ["Bleed", "Poise"]:
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
                    if effect.name == "Bind":
                        # Bind doesn't show potency, only count
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
                    config.console.print(Panel(f"[bold]{eff.name}[/bold]\n\n{eff.description}", title="Status Effect", style="green"))
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
        # If the log has reached the panel height limit (14 lines), 
        # clear the entire list so the new message starts fresh at the top.
        if len(self.battle_log) >= 13:
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
                # Visual distinction: Bind doesn't show potency
                if se.name == "Bind":
                    se_display += f"{se.symbol}x{se.duration} "
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
                if se.name == "Bind":
                    se_display += f"{se.symbol}x{se.duration} "
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

battle_manager = BattleManager()#