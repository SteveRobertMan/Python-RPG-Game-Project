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
DUAL_STACK_EFFECTS =  ["Bleed", "Rupture", "Fairylight", "Poise", "Sinking"]

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
            # Draw Pace * 2 at the start of battle
            unit.draw_skills(unit.pace * 2)
            unit.status_effects = []
            unit.nerve_disruption_turns = 0 
            unit.pending_bind = 0
            unit.pending_haste = 0
            unit.pending_ls = 0
            unit.active_ls = 0
            
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
                    unit.apply_next_turn_modifiers()
                
                self.apply_status_modifiers(unit)
                
                # --- BUG FIX: CLEAN HAND BEFORE DRAWING ---
                # Remove any 'None' placeholders left over from the previous command phase
                unit.hand = [s for s in unit.hand if s is not None]
                
                # REFILL HAND TO FULL PACE (Pace * 2)
                skills_to_draw = (unit.pace * 2) - len(unit.hand)
                if skills_to_draw > 0:
                    unit.draw_skills(skills_to_draw)

            # Assign targets and enemy intents SLOT BY SLOT
            self.assign_round_targets()

            # --- COMMAND PHASE ---
            self.handle_player_command_phase()
            if self.check_win_condition(): return
            if self.is_battle_over: return
            
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
                
                # Use the new Pace-based staggered execution
                self.execute_enemy_actions()
                if self.check_loss_condition(): return
                
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
                return True
            # ---------------------------------------------------------
            
    def apply_status_modifiers(self, unit):
        for effect in unit.status_effects:
            if effect.name in DUAL_STACK_EFFECTS:
                if effect.potency > 99: effect.potency = 99
                if effect.duration > 99: effect.duration = 99
            elif effect.name == "Bind":
                if effect.duration > 5: effect.duration = 5
        
        for effect in unit.status_effects:
            if effect.name == "Bind":
                penalty = 1.0 - (0.1 * effect.duration)
                unit.temp_modifiers["outgoing_dmg_mult"] *= max(0.1, penalty)
            elif effect.name == "Haste":
                bonus = 1.0 + (0.1 * effect.duration)
                unit.temp_modifiers["outgoing_dmg_mult"] *= bonus
        
        if getattr(unit, "nerve_disruption_turns", 0) > 0:
            unit.temp_modifiers["outgoing_dmg_mult"] *= 0.2

    def resolve_combat_start_effects(self):
        activated_any = False
        
        for ally, skill, target in self.ally_action_queue:
            if ally.hp > 0 and "[Combat Start]" in skill.description:
                self.apply_combat_start_logic(ally, skill)
                activated_any = True

        for enemy in self.enemies:
            if enemy.hp > 0 and enemy.intents:
                # We check all intents of the enemy for [Combat Start]
                for skill, _, _ in enemy.intents:
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

        elif skill.effect_type == "HISAYUKI_SPECIAL_2":
            if any(s.name == "Bind" for s in unit.status_effects):
                unit.temp_modifiers["incoming_dmg_mult"] *= 1.50
        
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
        
        elif skill.effect_type == "JOKE_SKILL":
            if hasattr(unit, "kata"):
                unit.kata.rift_aptitude = 0
        
        elif skill.effect_type == "COUNTER_SKILL_TYPE1":
            unit.counter_active = True
            unit.counter_potency = 0.20  # +20% damage
        elif skill.effect_type == "COUNTER_SKILL_SPECIAL_TYPE1":
            unit.counter_active = True
            unit.counter_potency = 0.40  # +40% damage
        elif skill.effect_type == "COUNTER_SKILL_SPECIAL_TYPE3":
            unit.counter_active = True
            unit.counter_potency = 0.30  # +30% damage
        
        elif skill.effect_type in ["BENIKAWA_CLAN_SPECIAL_1", "BENIKAWA_CLAN_SPECIAL_3"]:
            unit.temp_modifiers["incoming_dmg_mult"] *= 1.30
            
        elif skill.effect_type == "BENIKAWA_CLAN_SPECIAL_2":
            unit.temp_modifiers["incoming_dmg_mult"] *= 0.70
            unit.next_turn_modifiers["incoming_dmg_mult"] = unit.next_turn_modifiers.get("incoming_dmg_mult", 1.0) * 0.50

        elif skill.effect_type == "LIGHTWEIGHT_SPECIAL":
            unit.temp_modifiers["final_dmg_reduction"] += skill.effect_val
            haste_eff = StatusEffect("Haste", "[yellow1]🢙[/yellow1]", 0, "Deal +(10*Count)% base damage with skills. Lose 1 count every new turn. Max count: 5", duration=skill.effect_val)
            self.apply_status_logic(unit, haste_eff)

        elif skill.effect_type == "GOLDEN_FIST_SPECIAL":
            unit.temp_modifiers["final_dmg_reduction"] += 8
            team = self.allies if unit in self.allies else self.enemies
            for member in team:
                # The prompt specified allies FROM "Golden Fist Union"
                if member.hp > 0 and "Golden Fist Union" in member.name:
                    member.temp_modifiers["outgoing_dmg_flat"] = member.temp_modifiers.get("outgoing_dmg_flat", 0) + 4

    def process_turn_end_effects(self):
        effects_triggered = False
        all_units = self.allies + self.enemies
        
        for unit in all_units:
            if unit.hp <= 0: continue
            
            if getattr(unit, "counter_active", False):
                unit.counter_active = False
                unit.counter_potency = 0
            if getattr(unit, "nerve_disruption_turns", 0) > 0:
                unit.nerve_disruption_turns -= 1

            for i in range(len(unit.status_effects) - 1, -1, -1):
                effect = unit.status_effects[i]
                triggered_this_loop = False

                if effect.name == "Bleed":
                    pass 
                elif effect.name in ["Bind", "Poise", "Haste"]:
                    effect.duration -= 1
                elif effect.name == "Fairylight":
                    old_duration = effect.duration
                    effect.duration = effect.duration // 2 
                    reduced_amount = old_duration - effect.duration
                    if reduced_amount > 0:
                        rupture_eff = next((s for s in unit.status_effects if s.name == "Rupture"), None)
                        if rupture_eff:
                            rupture_eff.potency = min(99, rupture_eff.potency + reduced_amount)
                            self.log(f"[spring_green1]Fairylight decay granted {unit.name} +{reduced_amount} Rupture Potency![/spring_green1]")
                elif effect.name == "Riposte":
                    reduction = int(effect.duration * 0.25)
                    effect.duration = max(0, effect.duration - max(1, reduction))
                
                elif effect.type == "DOT":
                    dmg = effect.potency
                    unit.hp -= dmg
                    self.log(f"[bold magenta]{effect.name}[/bold magenta] deals {dmg} dmg to {unit.name}!")
                    effect.duration -= 1
                    effects_triggered = True
                elif effect.type == "REGEN":
                    heal = effect.potency
                    unit.hp = min(unit.max_hp, unit.hp + heal)
                    self.log(f"[bold green]{effect.name}[/bold green] heals {unit.name} for {heal}!")
                    effect.duration -= 1
                    effects_triggered = True
                
                if unit.hp <= 0:
                    unit.hp = 0
                    self.log(f"[bold red]{unit.name} succumbed to {effect.name}![/bold red]")
                    effects_triggered = True
                    break 
                
                if effect.duration <= 0:
                    self.log(f"{unit.name}'s [dim]{effect.name}[/dim] expired.")
                    unit.status_effects.pop(i)
                    effects_triggered = True

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

            for effect in list(unit.status_effects):
                if effect.name in DUAL_STACK_EFFECTS:
                    if effect.potency <= 0 or effect.duration <= 0:
                        unit.status_effects.remove(effect)
                        effects_triggered = True

            # --- End of Unit Loop: Transfer Sinking Tally ---
            unit.active_ls = getattr(unit, "pending_ls", 0)
            unit.pending_ls = 0

        if effects_triggered:
            self.render_battle_screen()
            time.sleep(1.0)
            self.battle_log = [] 

    def assign_round_targets(self):
        # Reset tracking
        for u in self.allies + self.enemies:
            u.slot_targets = []
            u.intents = []
            u.turn_committed_skills = [] # Clear committed skills for the new round

        target_counts_allies = {a: 0 for a in self.allies if a.hp > 0}
        target_counts_enemies = {e: 0 for e in self.enemies if e.hp > 0}

        max_ally_pace = max([a.pace for a in self.allies if a.hp > 0], default=0)
        max_enemy_pace = max([e.pace for e in self.enemies if e.hp > 0], default=0)
        max_pace = max(max_ally_pace, max_enemy_pace)

        for slot_idx in range(max_pace):
            # ALLIES PICK TARGETS
            for ally in self.allies:
                if ally.hp > 0 and slot_idx < ally.pace:
                    living_enemies = [e for e in self.enemies if e.hp > 0]
                    if living_enemies:
                        min_c = min(target_counts_enemies[e] for e in living_enemies)
                        least = [e for e in living_enemies if target_counts_enemies[e] == min_c]
                        t = random.choice(least)
                        ally.slot_targets.append(t)
                        target_counts_enemies[t] += 1
                    else:
                        ally.slot_targets.append(None)
            
            # ENEMIES PICK TARGETS & GENERATE INTENTS
            for enemy in self.enemies:
                if enemy.hp > 0 and slot_idx < enemy.pace:
                    living_allies = [a for a in self.allies if a.hp > 0]
                    if living_allies:
                        min_c = min(target_counts_allies[a] for a in living_allies)
                        least = [a for a in living_allies if target_counts_allies[a] == min_c]
                        t = random.choice(least)
                        enemy.slot_targets.append(t)
                        target_counts_allies[t] += 1
                        
                        # Generate intent for this specific slot (Picks from the 2 cards meant for this slot)
                        opt1 = slot_idx * 2
                        opt2 = slot_idx * 2 + 1
                        valid_opts = []
                        if opt1 < len(enemy.hand): valid_opts.append(opt1)
                        if opt2 < len(enemy.hand): valid_opts.append(opt2)
                        
                        if valid_opts:
                            chosen_idx = random.choice(valid_opts)
                            enemy.intents.append((enemy.hand[chosen_idx], t, chosen_idx))
                    else:
                        enemy.slot_targets.append(None)

    def handle_player_command_phase(self):
        self.ally_action_queue = []
        # Track how many unassigned slots each ally has remaining
        self.ally_slots_pending = {a: a.pace for a in self.allies if a.hp > 0}
        
        if self.auto_battle:
            self.run_auto_battler()
            return

        while any(slots > 0 for slots in self.ally_slots_pending.values()):
            self.render_battle_screen(active_unit=None)
            config.console.print("[bold yellow]COMMAND PHASE[/bold yellow]")
            config.console.print("Select an ally to command:")
            valid_choices = []
            idx = 1
            for ally, slots in self.ally_slots_pending.items():
                if slots > 0 and ally.hp > 0:
                    config.console.print(f"[{idx}] {ally.name}")
                    valid_choices.append(ally)
                    idx += 1
            config.console.print("[V] View Unit Details")
            auto_status = "[bold green]ON[/bold green]" if self.auto_battle else "[dim]OFF[/dim]"
            config.console.print(f"[A] Toggle Auto Battle ({auto_status})")
            config.console.print("[R] Retreat")
            
            choice = get_player_input("Select Unit > ").upper()

            if choice == "BLOWUNIVERSE":
                self.log("[bold magenta]*** AUTHOR CHEAT: THE UNIVERSE IMPLODES ***[/bold magenta]")
                self.log("[dim]All enemy HP set to 1.[/dim]")
                for enemy in self.enemies:
                    if enemy.hp > 0:
                        enemy.hp = 1
                self.render_battle_screen()
                time.sleep(0.5)
                continue 
            
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
                    self.run_auto_battler()
                    return
                else:
                    self.log("[dim]Auto Battle Disabled.[/dim]")
                    continue
            if choice.isdigit():
                c_idx = int(choice) - 1
                if 0 <= c_idx < len(valid_choices):
                    selected_ally = valid_choices[c_idx]
                    if self.select_skill_for_ally(selected_ally):
                        self.ally_slots_pending[selected_ally] -= 1
                else: self.log("[red]Invalid Selection![/red]")
            else:
                pass

    def run_auto_battler(self):
        def get_priority(unit):
            if "Akasuke" in unit.name: return 0
            if "Yuri" in unit.name: return 1
            if "Benikawa" in unit.name: return 2
            if "Shigemura" in unit.name: return 3
            return 10 + self.allies.index(unit) 
            
        while any(slots > 0 for slots in self.ally_slots_pending.values()):
            available_options = []
            for ally, slots_left in self.ally_slots_pending.items():
                if slots_left > 0 and ally.hp > 0:
                    slot_idx = ally.pace - slots_left
                    opt1_idx = slot_idx * 2
                    opt2_idx = slot_idx * 2 + 1
                    
                    if opt1_idx < len(ally.hand) and ally.hand[opt1_idx] is not None:
                        available_options.append((ally, ally.hand[opt1_idx], opt1_idx, slot_idx))
                    if opt2_idx < len(ally.hand) and ally.hand[opt2_idx] is not None:
                        available_options.append((ally, ally.hand[opt2_idx], opt2_idx, slot_idx))
            
            if not available_options:
                break
                
            global_max_tier = max(opt[1].tier for opt in available_options)
            best_options = [opt for opt in available_options if opt[1].tier == global_max_tier]
            best_options.sort(key=lambda x: get_priority(x[0]))
            
            winner, skill_to_use, h_idx, slot_idx = best_options[0]
            winner.hand[h_idx] = None
            self.ally_slots_pending[winner] -= 1
            
            target = winner.slot_targets[slot_idx] if slot_idx < len(winner.slot_targets) else None
            if not target or target.hp <= 0:
                living = [e for e in self.enemies if e.hp > 0]
                if living: target = random.choice(living)
                
            if target:
                self.ally_action_queue.append((winner, skill_to_use, target))
            
            self.render_battle_screen(active_unit=winner)
            config.console.print(f"[bold yellow]AUTO:[/bold yellow] {winner.name} selects {skill_to_use.name} (Tier {get_tier_roman(skill_to_use.tier)})")
            time.sleep(0.3)

    def select_skill_for_ally(self, ally):
        while True:
            self.render_battle_screen(active_unit=ally)
            
            slot_idx = ally.pace - self.ally_slots_pending[ally]
            slot_sym = "".join(["⬢" if i == slot_idx else "⬡" for i in range(ally.pace)]) if ally.pace > 1 else ""
            target = ally.slot_targets[slot_idx] if slot_idx < len(ally.slot_targets) else None
            t_name = target.name if target else "None"
            
            if ally.pace == 1: config.console.print(f"[bold cyan]Commanding {ally.name} -> {t_name}[/bold cyan]")
            else: config.console.print(f"[bold cyan]Commanding {ally.name} {slot_sym} -> {t_name}[/bold cyan]")
            
            config.console.print("Select a skill to use:")
            
            opt1_idx = slot_idx * 2
            opt2_idx = slot_idx * 2 + 1
            available_options = []
            
            display_idx = 1
            if opt1_idx < len(ally.hand) and ally.hand[opt1_idx]:
                available_options.append((display_idx, opt1_idx, ally.hand[opt1_idx]))
                display_idx += 1
            if opt2_idx < len(ally.hand) and ally.hand[opt2_idx]:
                available_options.append((display_idx, opt2_idx, ally.hand[opt2_idx]))

            for d_idx, h_idx, skill in available_options:
                 c = get_element_color(skill.element)
                 t = get_tier_roman(skill.tier)
                 config.console.print(f"[{d_idx}] [{c}]{skill.name}[/{c}] ({t})")
                 if skill.description: config.console.print(f"      [light_green]{skill.description}[/light_green]")
                 
            config.console.print("[0] Cancel")
            choice = get_player_input("Skill > ")
            if choice == "0": return False
            if choice.isdigit():
                c_idx = int(choice)
                matched_option = next((opt for opt in available_options if opt[0] == c_idx), None)
                if matched_option:
                    h_idx = matched_option[1]
                    selected_skill = ally.hand[h_idx]
                    ally.hand[h_idx] = None 
                    
                    if not target or target.hp <= 0:
                        living = [e for e in self.enemies if e.hp > 0]
                        if living: target = min(living, key=lambda e: e.target_count if hasattr(e, 'target_count') else 0)
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
                
                ally.turn_committed_skills.append(skill)
                self.execute_skill(ally, skill, target)
                if self.check_win_condition(): return

    def execute_enemy_actions(self):
        max_enemy_pace = max([e.pace for e in self.enemies if e.hp > 0], default=0)
        for slot_idx in range(max_enemy_pace):
            for enemy in self.enemies:
                if enemy.hp > 0 and slot_idx < len(enemy.intents):
                    skill, target, _ = enemy.intents[slot_idx]
                    
                    if target.hp <= 0:
                        living = [a for a in self.allies if a.hp > 0]
                        if living: target = random.choice(living)
                        else: break
                        
                    enemy.turn_committed_skills.append(skill)
                    self.execute_skill(enemy, skill, target)

    def get_avg_defense_tier(self, unit):
        if not unit.turn_committed_skills: return 0
        import math
        total = sum(s.tier for s in unit.turn_committed_skills)
        return math.ceil(total / len(unit.turn_committed_skills))

    def execute_skill(self, attacker, skill, target):
        attacker.discard_pile.append(skill)
        
        # Log Action
        self.log(f"{attacker.name} uses [bold]{skill.name}[/bold]!")
        self.render_battle_screen() 
        time.sleep(0.8) 

        # Initialize specific variable for Shigemura's Sadism to avoid scope errors
        sadism_bind_to_apply = 0
        
        # --- [STEP 1] [On Use] EFFECTS (Uses Parent Skill) ---
        if "[On Use]" in skill.description:
            if skill.effect_type == "BUFF_DEF_FLAT":
                 attacker.temp_modifiers["final_dmg_reduction"] = attacker.temp_modifiers.get("final_dmg_reduction", 0) + skill.effect_val
            
            elif skill.effect_type == "DEF_BUFF_BASE_PER":
                reduction_pct = skill.effect_val / 10.0
                if attacker in self.enemies:
                    if not hasattr(attacker, "next_turn_modifiers"): attacker.next_turn_modifiers = {}
                    attacker.next_turn_modifiers["incoming_dmg_mult"] = attacker.next_turn_modifiers.get("incoming_dmg_mult", 1.0) * (1.0 - reduction_pct)
                else:
                    attacker.temp_modifiers["incoming_dmg_mult"] *= (1.0 - reduction_pct)
                    
            elif skill.effect_type == "BLEED_POTENCY_DEF_BUFF":
                attacker.temp_modifiers["final_dmg_reduction"] += skill.effect_val
                
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

            # Check Skill Condition
            if skill.effect_type == "BLEED_RUPTURE_BUFF_FLAT_TYPE1":
                if any(s.name == "Rupture" for s in target.status_effects):
                    attacker.temp_modifiers["outgoing_dmg_flat"] = attacker.temp_modifiers.get("outgoing_dmg_flat", 0) + skill.effect_val
            elif skill.effect_type == "RUPTURE_BUFF_AND_COUNT_SPECIAL":
                if any(s.name == "Rupture" for s in target.status_effects):
                    attacker.temp_modifiers["outgoing_dmg_flat"] = attacker.temp_modifiers.get("outgoing_dmg_flat", 0) + skill.effect_val

        # --- PREPARE MULTI-HIT LOGIC ---
        chips_to_execute = getattr(skill, "chips", [skill])

        for chip_idx, chip in enumerate(chips_to_execute):
            
            # FIZZLE MECHANIC: If target died on previous hit, abort remaining hits
            if target.hp <= 0:
                if len(chips_to_execute) > 1 and chip_idx > 0:
                    self.log(f"[dim]Remaining hits fizzled out...[/dim]")
                break 

            damage = 0
            is_crit = False

            # --- [STEP 2] DAMAGE CALCULATION (Per Chip) ---
            if chip.base_damage > 0:
                # 1. Base Damage & Variance
                base_dmg_val = float(chip.base_damage)
                base_dmg_val += attacker.temp_modifiers.get("outgoing_base_dmg_flat", 0)
                
                if chip.effect_type == "HISAYUKI_SPECIAL_3":
                    haste = next((s for s in attacker.status_effects if s.name == "Haste"), None)
                    if haste:
                        bonus_pct = min(0.50, haste.duration * 0.10)
                        base_dmg_val *= (1.0 + bonus_pct)
                        attacker.status_effects.remove(haste)

                # PIERCE AFFINITY BASE DAMAGE MANIPULATION
                pierce_eff = next((s for s in target.status_effects if s.name == "Pierce Affinity"), None)
                if pierce_eff:
                    p_count = min(5, pierce_eff.duration)
                    # Support checking description of either the parent skill or the chip
                    desc_to_check = getattr(chip, "description", "") or skill.description
                    if "Pierce Affinity" in desc_to_check:
                        base_dmg_val += p_count

                # RIPOSTE UNIQUE DAMAGE BUFFS
                if chip.effect_type == "NAGANOHARA_RIPOSTE_CEDE":
                    riposte_eff = next((s for s in attacker.status_effects if s.name == "Riposte"), None)
                    if riposte_eff and riposte_eff.duration >= 20:
                        base_dmg_val *= 1.40
                        attacker.temp_modifiers["incoming_dmg_mult"] *= 1.50
                        self.log(f"[bold red]{attacker.name} cedes their defense for a heavy strike![/bold red]")
                if chip.effect_type == "AKASUKE_RIPOSTE_PRISEDEFER":
                    riposte_eff = next((s for s in attacker.status_effects if s.name == "Riposte"), None)
                    if riposte_eff:
                        bonus_pct = min(1.0, riposte_eff.duration * 0.02)
                        base_dmg_val *= (1.0 + bonus_pct)

                # SHIGEMURA INFILTRATOR
                infiltrator_recoil = 0
                if chip.effect_type == "SHIGEMURA_INFILTRATOR_SPECIAL_1":
                    haste = next((s for s in attacker.status_effects if s.name == "Haste"), None)
                    if haste:
                        bonus_base = base_dmg_val * 0.20
                        base_dmg_val += bonus_base
                        infiltrator_recoil = int(bonus_base) 

                if chip.effect_type == "COND_REAPER_BIND_CONVERT_SPECIAL":
                    total_bleed = sum(s.potency + s.duration for s in target.status_effects if s.name == "Bleed")
                    steps = min(3, total_bleed // 3)
                    if steps > 0:
                        base_dmg_val = max(0, base_dmg_val - (steps * 3))
                        sadism_bind_to_apply = steps

                # RUPTURE FLAT BONUS
                if chip.effect_type == "RUPTURE_DAMAGE_BUFF_TYPE2":
                    if any(s.name in ["Rupture", "Fairylight"] for s in target.status_effects):
                        base_dmg_val += chip.effect_val

                # --- NATSUME STRANGE KATA (ON USE) ---
                if chip.effect_type in ["NATSUME_STRANGE_SPECIAL_1", "NATSUME_STRANGE_SPECIAL_2", "NATSUME_STRANGE_SPECIAL_3", "NATSUME_STRANGE_SPECIAL_4"]:
                    base_dmg_val *= 0.20
                elif chip.effect_type in ["NATSUME_STRANGE_SPECIAL_5", "NATSUME_STRANGE_SPECIAL_6"]:
                    base_dmg_val *= 0.15

                if chip.effect_type == "NATSUME_STRANGE_SPECIAL_1":
                    self.apply_status_logic(attacker, StatusEffect("Poise", "[light_cyan1]༄[/light_cyan1]", 0, "Boost Critical Hit chance by (Potency*5)% for the next 'Count' amount of hits. Max potency or count: 99", duration=2))
                elif chip.effect_type == "NATSUME_STRANGE_SPECIAL_2":
                    self.apply_status_logic(attacker, StatusEffect("Poise", "[light_cyan1]༄[/light_cyan1]", 0, "Boost Critical Hit chance by (Potency*5)% for the next 'Count' amount of hits. Max potency or count: 99", duration=1))
                elif chip.effect_type == "NATSUME_STRANGE_SPECIAL_3":
                    self.apply_status_logic(attacker, StatusEffect("Bind", "[dim gold1]⛓[/dim gold1]", 1, "Deal -(10*Count)% base damage with skills. Lose 1 count every new turn. Max Count: 5", duration=1))
                elif chip.effect_type == "NATSUME_STRANGE_SPECIAL_5":
                    self.apply_status_logic(attacker, StatusEffect("Bind", "[dim gold1]⛓[/dim gold1]", 1, "Deal -(10*Count)% base damage with skills. Lose 1 count every new turn. Max Count: 5", duration=1))
                    self.apply_status_logic(attacker, StatusEffect("Poise", "[light_cyan1]༄[/light_cyan1]", 2, "Boost Critical Hit chance by (Potency*5)% for the next 'Count' amount of hits. Max potency or count: 99", duration=2))
                elif chip.effect_type == "NATSUME_STRANGE_SPECIAL_6":
                    self.apply_status_logic(attacker, StatusEffect("Poise", "[light_cyan1]༄[/light_cyan1]", 2, "Boost Critical Hit chance by (Potency*5)% for the next 'Count' amount of hits. Max potency or count: 99", duration=2))

                # Check Passive Condition
                active_passives = getattr(attacker, "passives", [])
                if not active_passives and getattr(attacker, "kata", None):
                    active_passives = getattr(attacker.kata, "passives", [])

                if active_passives:
                    for p in active_passives:
                        if p.effect_type == "PASSIVE_GOLDEN_FIST":
                            if any(s.name == "Bleed" for s in target.status_effects):
                                attacker.temp_modifiers["outgoing_dmg_flat"] = attacker.temp_modifiers.get("outgoing_dmg_flat", 0) + p.effect_val
                                self.log(f"[bold yellow][Passive][/bold yellow] {p.name} activated! (+{p.effect_val} Dmg)")

                # 2. Bind Penalty
                bind_effect = next((s for s in attacker.status_effects if s.name == "Bind"), None)
                if bind_effect:
                    b_count = min(5, bind_effect.duration) 
                    base_dmg_val *= max(0.0, 1.0 - (0.10 * b_count))

                # 3. Random Variance
                dmg = base_dmg_val * random.uniform(1.0, 1.5)

                # 4. Handle [On Use] Status (Pre-Hit Application)
                if chip.effect_type == "GAIN_STATUS":
                    self.apply_status_logic(attacker, copy.deepcopy(chip.status_effect))
                elif chip.effect_type == "GAIN_POISE_SPECIAL_1":
                    self.apply_status_logic(attacker, StatusEffect("Poise", "[light_cyan1]༄[/light_cyan1]", 2, "Boost Critical Hit chance by (Potency*5)% for the next 'Count' amount of hits. Max potency or count: 99", duration=0))

                # 5. Critical Hit Roll (POISE CHECK - DECREMENTS PER CHIP)
                poise = next((se for se in attacker.status_effects if se.name == "Poise"), None)
                if poise and poise.potency > 0 and poise.duration > 0:
                    crit_chance = min(100, poise.potency * 5)
                    if random.randint(1, 100) <= crit_chance:
                        is_crit = True
                        dmg *= 1.2  # 20% Crit Multiplier
                        # Consume Poise Count immediately on this chip
                        poise.duration -= 1
                        if poise.duration <= 0:
                            attacker.status_effects.remove(poise)
                            poise = None # Clear reference

                # 6. Elemental & Global Multipliers (Uses PARENT skill element)
                res_mult = target.resistances[skill.element]
                nbd = dmg * res_mult
                nbd *= attacker.temp_modifiers.get("outgoing_dmg_mult", 1.0)
                nbd *= target.temp_modifiers.get("incoming_dmg_mult", 1.0)
                
                # 7. Flat Modifiers
                final_dmg = nbd + target.temp_modifiers.get("incoming_dmg_flat", 0)
                final_dmg += attacker.temp_modifiers.get("outgoing_dmg_flat", 0)
                final_dmg -= target.temp_modifiers["final_dmg_reduction"]
                # --- SINKING LS CHECK (Attacker Penalty) ---
                if getattr(attacker, "active_ls", 0) > 0:
                    if random.randint(1, 100) <= attacker.active_ls:
                        reduction_pct = (attacker.active_ls / 2.0) / 100.0
                        final_dmg = final_dmg * (1.0 - reduction_pct)
                        self.log(f"[blue3]Sinking[/blue3] disrupted {attacker.name}'s attack! Damage reduced by {int(reduction_pct*100)}%.")

                # Consume Hit Bonuses
                if target.next_hit_taken_flat_bonus > 0:
                    final_dmg += target.next_hit_taken_flat_bonus
                    target.next_hit_taken_flat_bonus = 0 
                if attacker.next_hit_deal_flat_bonus > 0:
                    final_dmg += attacker.next_hit_deal_flat_bonus
                    attacker.next_hit_deal_flat_bonus = 0

                # NAGANOHARA CONDITIONAL FLATS
                target_has_bleed = any(s.name == "Bleed" and s.duration > 0 for s in target.status_effects)
                if chip.effect_type == "COND_TARGET_HAS_BLEED_DMG":
                    if target_has_bleed: final_dmg += chip.effect_val
                if chip.effect_type == "COND_BLEED_DMG_AND_APPLY":
                    if target_has_bleed: final_dmg += chip.effect_val

                # DEFENSE TIER REDUCTION (Uses Parent skill tier)
                def_max_tier = self.get_avg_defense_tier(target)
                if skill.tier > def_max_tier:
                    final_dmg -= (final_dmg * min(0.60, 0.15 * (skill.tier - def_max_tier)))

                damage = int(final_dmg)

                # FINAL CHECKS
                if chip.effect_type == "COND_HP_ABOVE_50_FLAT" and target.hp >= (target.max_hp * 0.5): damage += int(chip.effect_val)
                if chip.effect_type == "COND_LOW_HP_MERCY" and target.hp <= (target.max_hp * 0.7): damage -= int(chip.effect_val)
                if chip.effect_type == "COND_HP_BELOW_80_FLAT" and target.hp <= (target.max_hp * 0.8): damage += int(chip.effect_val)
                
                # RIPOSTE DAMAGE MITIGATION
                riposte_eff = next((s for s in target.status_effects if s.name == "Riposte"), None)
                if riposte_eff:
                    reduction_pct = min(0.25, (riposte_eff.duration // 10) * 0.05)
                    damage = damage * (1.0 - reduction_pct)

                damage = max(1, int(damage)) # Minimum 1 damage if hit connects

                if "Golden Fist Union" in target.name:
                    target_team = self.allies if target in self.allies else self.enemies
                    for ally in target_team:
                        if ally.hp > 0:
                            ap = getattr(ally, "passives", [])
                            if not ap and getattr(ally, "kata", None): ap = getattr(ally.kata, "passives", [])
                            for p in ap:
                                if p.effect_type == "PASSIVE_CRUDE_COMMAND":
                                    final_dmg -= p.effect_val
                                    break # Only apply the reduction once, even if multiple units with the passive are alive

                # CONVERT DAMAGE TO HEAL
                if chip.effect_type == "SPECIAL_CONVERT_DMG_TO_HEAL_LOWEST":
                    team = self.allies if attacker in self.allies else self.enemies
                    living_teammates = [u for u in team if u.hp > 0]
                    if living_teammates:
                        lowest_unit = min(living_teammates, key=lambda u: u.hp / u.max_hp)
                        heal_amt = damage
                        lowest_unit.hp = min(lowest_unit.max_hp, lowest_unit.hp + heal_amt)
                        self.log(f"[light_green]-> {attacker.name} Heals {lowest_unit.name} for {heal_amt}.[/light_green]")
                    damage = 0

                # CUSTOM NON-DAMAGE & HEALING SKILLS
                if chip.effect_type in ["SELF_HEAL_TYPE1", "EAGLE_SPECIAL_3", "JOKE_SKILL"]:
                    if chip.effect_type == "SELF_HEAL_TYPE1":
                        heal_amt = damage
                        attacker.hp = min(attacker.max_hp, attacker.hp + heal_amt)
                        self.log(f"[light_green]-> {attacker.name} Heals self for {heal_amt}.[/light_green]")
                        damage = 0
                    elif chip.effect_type == "EAGLE_SPECIAL_3":
                        team = self.allies if attacker in self.allies else self.enemies
                        living_teammates = [u for u in team if u.hp > 0]
                        if living_teammates:
                            lowest_unit = min(living_teammates, key=lambda u: u.hp / u.max_hp)
                            heal_amt = damage
                            lowest_unit.hp = min(lowest_unit.max_hp, lowest_unit.hp + heal_amt)
                            self.log(f"[light_green]-> {attacker.name} Heals {lowest_unit.name} for {heal_amt}.[/light_green]")
                            for a in living_teammates:
                                if a != lowest_unit: a.hp = min(a.max_hp, a.hp + (heal_amt // 2))
                                self.apply_status_logic(a, StatusEffect("Haste", "[yellow1]🢙[/yellow1]", 0, "Deal +(10*Count)% base damage with skills. Lose 1 count every new turn. Max count: 5", duration=3))
                        damage = 0
                    elif chip.effect_type == "JOKE_SKILL":
                        damage = 0

                # --- APPLY DAMAGE ---
                if damage > 0:
                    target.hp -= damage
                    el_color = get_element_color(skill.element)
                    eff_text = " [bold yellow](WEAK!)[/]" if res_mult > 1.0 else (" [dim](Resist)[/]" if res_mult < 1.0 else "")
                    crit_text = "[khaki1]Critical![/] " if is_crit else ""
                    
                    self.log(f"-> {crit_text}Hit {target.name} for [bold {el_color}]{damage}[/bold {el_color}]!{eff_text}")
                    
                    # COUNTER TRIGGER
                    if getattr(target, "counter_active", False):
                        if not hasattr(target, "next_turn_modifiers"): target.next_turn_modifiers = {}
                        current_mult = target.next_turn_modifiers.get("outgoing_dmg_mult", 1.0)
                        target.next_turn_modifiers["outgoing_dmg_mult"] = current_mult + target.counter_potency
                        target.counter_active = False 
                    
                    # ON HIT POISE
                    if chip.effect_type == "GAIN_POISE_SPECIAL_1":
                        self.apply_status_logic(attacker, StatusEffect("Poise", "[light_cyan1]༄[/light_cyan1]", 4, "Boost Critical Hit chance by (Potency*5)% for the next 'Count' amount of hits. Max potency or count: 99", duration=0))
                    
                    # BLEED RECOIL ON ATTACKER
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
                        if attacker.hp <= 0: attacker.hp = 0
                        if bleed_eff and bleed_eff.duration <= 0 and bleed_idx < len(attacker.status_effects):
                            try:
                                attacker.status_effects.remove(bleed_eff)
                            except ValueError: pass

                    # ON HIT HEAL
                    if chip.effect_type == "ON_HIT_HEAL_LOWEST_BY_DMG":
                        team = self.allies if attacker in self.allies else self.enemies
                        living_teammates = [u for u in team if u.hp > 0]
                        if living_teammates:
                            lowest_unit = min(living_teammates, key=lambda u: u.hp / u.max_hp)
                            heal_amt = damage 
                            lowest_unit.hp = min(lowest_unit.max_hp, lowest_unit.hp + heal_amt)
                            self.log(f"[light_green]-> {attacker.name} Heals {lowest_unit.name} for {heal_amt}.[/light_green]")

                    # RIPOSTE REDUCTION & HASTE GAIN
                    if riposte_eff:
                        stacks_lost = min(random.randint(1, 4), riposte_eff.duration)
                        riposte_eff.duration -= stacks_lost
                        target.riposte_loss_tracker += stacks_lost
                        while target.riposte_loss_tracker >= 10:
                            target.riposte_loss_tracker -= 10
                            haste_eff = StatusEffect("Haste", "[yellow1]🢙[/yellow1]", 0, "Deal +(10*Count)% base damage with skills. Lose 1 count every new turn. Max count: 5", duration=1, type="BUFF")
                            self.apply_status_logic(target, haste_eff)
                            self.log(f"[yellow1]{target.name} gained Haste from Riposte![/yellow1]")
                        if riposte_eff.duration <= 0: target.status_effects.remove(riposte_eff)

                    # RUPTURE & FAIRYLIGHT TRIGGERS
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

                    # PIERCE AFFINITY TRIGGER
                    pierce_target_eff = next((s for s in target.status_effects if s.name == "Pierce Affinity"), None)
                    if pierce_target_eff:
                        pierce_target_eff.duration -= 1
                        if pierce_target_eff.duration <= 0: target.status_effects.remove(pierce_target_eff)
                        
                    # INFILTRATOR RECOIL
                    if infiltrator_recoil > 0:
                        attacker.hp -= infiltrator_recoil
                        self.log(f"[bold red]{attacker.name} takes {infiltrator_recoil} Recoil Damage from momentum![/bold red]")

                    # POISE SUPPORT LOGIC
                    if chip.effect_type == "ON_HIT_PROVIDE_POISE_TYPE1":
                        team = self.allies if attacker in self.allies else self.enemies
                        for member in team:
                            poise_effect = next((e for e in member.status_effects if e.name == "Poise"), None)
                            if poise_effect: poise_effect.duration = min(99, poise_effect.duration + chip.effect_val)
                    elif chip.effect_type == "ON_HIT_PROVIDE_POISE_TYPE2":
                        team = self.allies if attacker in self.allies else self.enemies
                        for member in team:
                            poise_effect = next((e for e in member.status_effects if e.name == "Poise"), None)
                            if poise_effect:
                                poise_effect.potency = min(99, poise_effect.potency + chip.effect_val)
                                poise_effect.duration = min(99, poise_effect.duration + chip.effect_val)
                    elif chip.effect_type == "ON_HIT_PROVIDE_POISE_TYPE3":
                        team = self.allies if attacker in self.allies else self.enemies
                        for member in team:
                            poise_effect = next((e for e in member.status_effects if e.name == "Poise"), None)
                            if poise_effect: poise_effect.potency = min(99, poise_effect.potency + chip.effect_val)
                    elif chip.effect_type == "ON_HIT_PROVIDE_POISE_TYPE4":
                        team = self.allies if attacker in self.allies else self.enemies
                        for member in team:
                            poise_effect = next((e for e in member.status_effects if e.name == "Poise"), None)
                            if poise_effect: poise_effect.duration = min(99, poise_effect.duration + chip.effect_val)
                            else: self.apply_status_logic(member, StatusEffect("Poise", "[light_cyan1]༄[/light_cyan1]", chip.effect_val, "Boost Critical Hit chance by (Potency*5)% for the next 'Count' amount of hits. Max potency or count: 99", duration=0))
                    elif chip.effect_type == "ON_HIT_CONVERT_POISE_TYPE1":
                        team = self.allies if attacker in self.allies else self.enemies
                        for member in team:
                            poise_effect = next((e for e in member.status_effects if e.name == "Poise"), None)
                            if poise_effect and poise_effect.potency >= 2:
                                poise_effect.potency -= 1
                                poise_effect.duration = min(99, poise_effect.duration + 1)
                                if poise_effect.potency <= 0 or poise_effect.duration <= 0: member.status_effects.remove(poise_effect)
                    elif chip.effect_type == "ON_HIT_CONVERT_POISE_TYPE2":
                        team = self.allies if attacker in self.allies else self.enemies
                        for member in team:
                            poise_effect = next((e for e in member.status_effects if e.name == "Poise"), None)
                            if poise_effect and poise_effect.potency >= 4:
                                poise_effect.potency -= chip.effect_val
                                poise_effect.duration = min(99, poise_effect.duration + chip.effect_val)
                                if poise_effect.potency <= 0 or poise_effect.duration <= 0: member.status_effects.remove(poise_effect)
                    
                    # SINKING TRIGGER
                    sinking_eff = next((s for s in target.status_effects if s.name == "Sinking"), None)
                    if sinking_eff:
                        if not hasattr(target, "pending_ls"): target.pending_ls = 0
                        target.pending_ls = min(90, target.pending_ls + sinking_eff.potency)
                        sinking_eff.duration -= 1
                        #self.log(f"[blue3]Sinking[/blue3] disrupted {target.name}'s mind! LS Tally +{sinking_eff.potency} (Total: {target.pending_ls}).")
                        if sinking_eff.duration <= 0: target.status_effects.remove(sinking_eff)

                    # NEXT HIT BONUSES
                    elif chip.effect_type == "ON_HIT_NEXT_TAKEN_FLAT": target.next_hit_taken_flat_bonus += chip.effect_val
                    elif chip.effect_type == "ON_HIT_NEXT_DEAL_FLAT": attacker.next_hit_deal_flat_bonus += chip.effect_val
                    elif chip.effect_type == "SELF_NEXT_TAKEN_FLAT": attacker.next_hit_taken_flat_bonus += chip.effect_val
                    elif chip.effect_type == "DEBUFF_INCOMING_DMG_FLAT": target.temp_modifiers["incoming_dmg_flat"] += chip.effect_val

            else:
                if chip.effect_type != "SPECIAL_CONVERT_DMG_TO_HEAL_LOWEST":
                    self.log(f"-> The move dealt no damage.")

            # --- [STEP 3] STATUS EFFECT / SPECIAL APPLICATION (Per Chip) ---
            
            # AOE BUFF
            if chip.effect_type == "AOE_BUFF_DEF_FLAT":
                team = self.allies if attacker in self.allies else self.enemies
                for member in team:
                    if member.hp > 0: member.temp_modifiers["final_dmg_reduction"] = member.temp_modifiers.get("final_dmg_reduction", 0) + chip.effect_val
                    
            # AKASUKE SKILLS
            elif chip.effect_type == "BLEED_COUNT_OPENER":
                has_bleed = any(s.name == "Bleed" for s in target.status_effects)
                if not has_bleed and hasattr(chip, "status_effect") and chip.status_effect:
                    self.apply_status_logic(target, copy.deepcopy(chip.status_effect))
                elif has_bleed and hasattr(chip, "alt_status_effect") and chip.alt_status_effect:
                    self.apply_status_logic(target, copy.deepcopy(chip.alt_status_effect))
            elif chip.effect_type == "BLEED_POTENCY_STACKER":
                has_bleed = any(s.name == "Bleed" for s in target.status_effects)
                if has_bleed and hasattr(chip, "status_effect") and chip.status_effect:
                    self.apply_status_logic(target, copy.deepcopy(chip.status_effect))
            elif chip.effect_type == "HEIWA_RALLY_EFFECT":
                team = self.allies if attacker in self.allies else self.enemies
                for member in team:
                    if member.hp > 0:
                        member.temp_modifiers["outgoing_dmg_flat"] = member.temp_modifiers.get("outgoing_dmg_flat", 0) + chip.effect_val
                        if hasattr(member, "kata") and "Heiwa" in member.kata.name:
                            member.temp_modifiers["final_dmg_reduction"] += chip.effect_val
            elif chip.effect_type == "BLEED_POTENCY_DEF_BUFF":
                if hasattr(chip, "status_effect") and chip.status_effect:
                    self.apply_status_logic(target, copy.deepcopy(chip.status_effect))
            
            # BENIKAWA
            elif chip.effect_type == "COND_TARGET_HAS_BLEED_DMG_PER":
                has_bleed = any(s.name == "Bleed" for s in target.status_effects)
                if has_bleed:
                    bonus_dmg = int(chip.base_damage * (chip.effect_val / 10.0))
                    target.hp -= bonus_dmg
                    if 'sadism_bind_to_apply' in locals() and sadism_bind_to_apply > 0:
                        self.apply_status_logic(target, StatusEffect("Bind", "[dim gold1]⛓[/dim gold1]", 1, "Deal -(10*Count)% base damage with skills. Lose 1 count every new turn. Max Count: 5", duration=sadism_bind_to_apply))

            # KUROGANE & GENERIC EFFECTS
            elif chip.effect_type == "APPLY_BLEED_HEAVY_STACKS":
                self.apply_status_logic(target, StatusEffect("Bleed", "[red]💧︎[/red]", 2, "Upon dealing damage, Take fixed damage equal to Potency, then reduce count by 1 Max potency or count: 99", duration=2, type="DEBUFF"))
            elif chip.effect_type == "APPLY_BLEED_AND_BIND":
                self.apply_status_logic(target, StatusEffect("Bleed", "[red]💧︎[/red]", 3, "Upon dealing damage, Take fixed damage equal to Potency, then reduce count by 1 Max potency or count: 99", duration=1, type="DEBUFF"))
                self.apply_status_logic(target, StatusEffect("Bind", "[dim gold1]⛓[/dim gold1]", 1, "Deal -(10*Count)% base damage with skills. Lose 1 count every new turn. Max Count: 5", duration=1, type="DEBUFF"))
            elif chip.effect_type == "APPLY_BLEED_AND_BIND_HEAVY":
                self.apply_status_logic(target, StatusEffect("Bleed", "[red]💧︎[/red]", 3, "Upon dealing damage, Take fixed damage equal to Potency, then reduce count by 1 Max potency or count: 99", duration=1, type="DEBUFF"))
                self.apply_status_logic(target, StatusEffect("Bind", "[dim gold1]⛓[/dim gold1]", 1, "Deal -(10*Count)% base damage with skills. Lose 1 count every new turn. Max Count: 5", duration=2, type="DEBUFF"))
            elif (chip.effect_type == "APPLY_STATUS" or chip.effect_type == "COND_BLEED_DMG_AND_APPLY") and hasattr(chip, "status_effect") and chip.status_effect:
                if chip.status_effect.name == "Nerve Disruption": target.nerve_disruption_turns = chip.status_effect.duration
                else: self.apply_status_logic(target, copy.deepcopy(chip.status_effect))

            elif chip.effect_type == "HASTE_BIND_SPECIAL_TYPE1":
                team = self.allies if attacker in self.allies else self.enemies
                enemy_team = self.enemies if attacker in self.allies else self.allies
                valid_allies = [u for u in team if u.hp > 0 and u != attacker]
                valid_enemies = [u for u in enemy_team if u.hp > 0]
                chosen_allies = random.sample(valid_allies, min(2, len(valid_allies)))
                chosen_enemies = random.sample(valid_enemies, min(2, len(valid_enemies)))
                for a in chosen_allies: self.apply_status_logic(a, StatusEffect("Haste", "[yellow1]🢙[/yellow1]", 0, "Deal +(10*Count)% base damage with skills. Lose 1 count every new turn. Max count: 5", duration=chip.effect_val))
                for e in chosen_enemies: self.apply_status_logic(e, StatusEffect("Bind", "[dim gold1]⛓[/dim gold1]", 1, "Deal -(10*Count)% base damage with skills. Lose 1 count every new turn. Max Count: 5", duration=chip.effect_val))
                
            elif chip.effect_type == "HANA_SPECIAL_RAGE":
                if not hasattr(attacker, "next_turn_modifiers"): attacker.next_turn_modifiers = {}
                attacker.next_turn_modifiers["outgoing_dmg_mult"] = 0.6
                target.temp_modifiers["outgoing_dmg_mult"] *= 0.85
                
            elif chip.effect_type == "BLEED_RUPTURE_SPECIAL_TYPE1":
                self.apply_status_logic(target, StatusEffect("Bleed", "[red]💧︎[/red]", chip.effect_val, "Upon dealing damage, Take fixed damage equal to Potency, then reduce count by 1. Max Potency or Count: 99", duration=1))
                self.apply_status_logic(target, StatusEffect("Rupture", "[medium_spring_green]✧[/medium_spring_green]", chip.effect_val, "Upon getting hit by a skill, Take extra fixed damage equal to the amount of Potency, then reduce count by 1. Max Potency or Count: 99", duration=1))
                
            elif chip.effect_type == "SPECIAL_CONVERT_DMG_TO_HEAL_RANDOM":
                team = self.allies if attacker in self.allies else self.enemies
                valid_allies = [u for u in team if u.hp > 0 and u != attacker]
                chosen_allies = random.sample(valid_allies, min(chip.effect_val, len(valid_allies)))
                targets_to_heal = [attacker] + chosen_allies
                for a in targets_to_heal:
                    a.hp = min(a.max_hp, a.hp + damage)
                    self.log(f"[light_green]-> {attacker.name} Heals {a.name} for {damage}.[/light_green]")
                damage = 0

            elif chip.effect_type == "NAGANOHARA_KIRYOKU_SPECIAL":
                team = self.allies if attacker in self.allies else self.enemies
                valid_allies = [u for u in team if u.hp > 0 and u != attacker]
                for a in random.sample(valid_allies, min(2, len(valid_allies))):
                    self.apply_status_logic(a, StatusEffect("Haste", "[yellow1]🢙[/yellow1]", 0, "Deal +(10*Count)% base damage with skills. Lose 1 count every new turn. Max count: 5", duration=1))
                has_rupture = any(s.name in ["Rupture", "Fairylight"] for s in target.status_effects)
                if has_rupture: self.apply_status_logic(target, StatusEffect("Rupture", "[medium_spring_green]✧[/medium_spring_green]", 1, "Upon getting hit by a skill, Take extra fixed damage equal to the amount of Potency, then reduce count by 1. Max Potency or Count: 99", duration=2))
                else: self.apply_status_logic(target, StatusEffect("Rupture", "[medium_spring_green]✧[/medium_spring_green]", 3, "Upon getting hit by a skill, Take extra fixed damage equal to the amount of Potency, then reduce count by 1. Max Potency or Count: 99", duration=1))   
                    
            elif chip.effect_type == "RUPTURE_DAMAGE_BUFF_TYPE1":
                has_rupture = any(s.name in ["Rupture", "Fairylight"] for s in target.status_effects)
                if has_rupture and damage > 0:
                    bonus = int(damage * 0.25)
                    target.hp -= bonus
                    self.log(f"[medium_spring_green]Bonus Rupture Execute: {bonus} damage![/medium_spring_green]")

            elif chip.effect_type == "SHIGEMURA_INFILTRATOR_SPECIAL_2":
                haste = next((s for s in attacker.status_effects if s.name == "Haste"), None)
                if haste and damage > 0:
                    bonus_pct = min(0.75, haste.duration * 0.15)
                    bonus_dmg = int(damage * bonus_pct)
                    target.hp -= bonus_dmg
                    self.log(f"[bold yellow]Maximized Ram! +{bonus_dmg} Bonus Damage![/bold yellow]")
                    attacker.status_effects.remove(haste)

            elif chip.effect_type == "KIRYOKU_COUNCIL_SPECIAL":
                self.apply_status_logic(target, StatusEffect("Rupture", "[medium_spring_green]✧[/medium_spring_green]", 0, "Upon getting hit by a skill, Take extra fixed damage equal to the amount of Potency, then reduce count by 1. Max Potency or Count: 99", duration=2))
                self.apply_status_logic(target, StatusEffect("Fairylight", "[spring_green1]𒀭[/spring_green1]", 2, "Unique Rupture (Counts As Rupture)\nUpon getting hit by a skill, Take extra fixed damage equal to the amount of Potency. On turn end, reduce Count by half, and if this unit has Rupture, gain Rupture Potency based on Count lost this way. Max Potency or Count: 99", duration=1))
            elif chip.effect_type == "AYAKO_SPECIAL":
                self.apply_status_logic(target, StatusEffect("Rupture", "[medium_spring_green]✧[/medium_spring_green]", 0, "Upon getting hit by a skill, Take extra fixed damage equal to the amount of Potency, then reduce count by 1. Max Potency or Count: 99", duration=3))
                self.apply_status_logic(target, StatusEffect("Fairylight", "[spring_green1]𒀭[/spring_green1]", 4, "Unique Rupture (Counts As Rupture)\nUpon getting hit by a skill, Take extra fixed damage equal to the amount of Potency. On turn end, reduce Count by half, and if this unit has Rupture, gain Rupture Potency based on Count lost this way. Max Potency or Count: 99", duration=1))
            elif chip.effect_type == "SUMIKO_SPECIAL_1":
                self.apply_status_logic(attacker, StatusEffect("Haste", "[yellow1]🢙[/yellow1]", 0, "Deal +(10*Count)% base damage with skills. Lose 1 count every new turn. Max count: 5", duration=2))
            elif chip.effect_type == "SUMIKO_SPECIAL_2":
                self.apply_status_logic(target, StatusEffect("Rupture", "[medium_spring_green]✧[/medium_spring_green]", 5, "Upon getting hit by a skill, Take extra fixed damage equal to the amount of Potency, then reduce count by 1. Max Potency or Count: 99", duration=4))
                self.apply_status_logic(attacker, StatusEffect("Haste", "[yellow1]🢙[/yellow1]", 0, "Deal +(10*Count)% base damage with skills. Lose 1 count every new turn. Max count: 5", duration=2))
            elif chip.effect_type == "APPLY_RUPTURE_HEAVY_STACKS":
                self.apply_status_logic(target, StatusEffect("Rupture", "[medium_spring_green]✧[/medium_spring_green]", 2, "Upon getting hit by a skill, Take extra fixed damage equal to the amount of Potency, then reduce count by 1. Max Potency or Count: 99", duration=2))
            
            elif chip.effect_type == "HISAYUKI_SPECIAL_1":
                if any(s.name == "Haste" for s in attacker.status_effects): self.apply_status_logic(attacker, StatusEffect("Bind", "[dim gold1]⛓[/dim gold1]", 1, "Deal -(10*Count)% base damage with skills. Lose 1 count every new turn. Max Count: 5", duration=1))
                else: self.apply_status_logic(attacker, StatusEffect("Haste", "[yellow1]🢙[/yellow1]", 0, "Deal +(10*Count)% base damage with skills. Lose 1 count every new turn. Max count: 5", duration=1))
            elif chip.effect_type == "BIND_RUPTURE_SPECIAL_TYPE1":
                self.apply_status_logic(target, StatusEffect("Bind", "[dim gold1]⛓[/dim gold1]", 1, "Deal -(10*Count)% base damage with skills. Lose 1 count every new turn. Max Count: 5", duration=2))
                self.apply_status_logic(target, StatusEffect("Rupture", "[medium_spring_green]✧[/medium_spring_green]", 2, "Upon getting hit by a skill, Take extra fixed damage equal to the amount of Potency, then reduce count by 1. Max Potency or Count: 99", duration=1))
            
            elif chip.effect_type == "RAVEN_SPECIAL_1":
                target.next_hit_taken_flat_bonus += 6
                self.apply_status_logic(attacker, StatusEffect("Poise", "[light_cyan1]༄[/light_cyan1]", 4, "Boost Critical Hit chance by (Potency*5)% for the next 'Count' amount of hits. Max potency or count: 99", duration=4))
            elif chip.effect_type == "RAVEN_SPECIAL_2":
                if not hasattr(target, "next_turn_modifiers"): target.next_turn_modifiers = {}
                target.next_turn_modifiers["outgoing_dmg_mult"] = target.next_turn_modifiers.get("outgoing_dmg_mult", 1.0) * 0.30
                self.apply_status_logic(attacker, StatusEffect("Poise", "[light_cyan1]༄[/light_cyan1]", 6, "Boost Critical Hit chance by (Potency*5)% for the next 'Count' amount of hits. Max potency or count: 99", duration=1))
            elif chip.effect_type == "FALCON_SPECIAL_1":
                self.apply_status_logic(target, StatusEffect("Rupture", "[medium_spring_green]✧[/medium_spring_green]", 4, "Upon getting hit by a skill, Take extra fixed damage equal to the amount of Potency, then reduce count by 1. Max Potency or Count: 99", duration=1))
            elif chip.effect_type == "FALCON_SPECIAL_2":
                if not hasattr(target, "next_turn_modifiers"): target.next_turn_modifiers = {}
                target.next_turn_modifiers["outgoing_dmg_mult"] = target.next_turn_modifiers.get("outgoing_dmg_mult", 1.0) * 0.30
                self.apply_status_logic(attacker, StatusEffect("Haste", "[yellow1]🢙[/yellow1]", 0, "Deal +(10*Count)% base damage with skills. Lose 1 count every new turn. Max count: 5", duration=2))
                self.apply_status_logic(target, StatusEffect("Bind", "[dim gold1]⛓[/dim gold1]", 1, "Deal -(10*Count)% base damage with skills. Lose 1 count every new turn. Max Count: 5", duration=2))
            elif chip.effect_type == "EAGLE_SPECIAL_1":
                target.next_hit_taken_flat_bonus += 5
                if not hasattr(target, "next_turn_modifiers"): target.next_turn_modifiers = {}
                target.next_turn_modifiers["outgoing_dmg_mult"] = target.next_turn_modifiers.get("outgoing_dmg_mult", 1.0) * 0.50
            elif chip.effect_type == "EAGLE_SPECIAL_2":
                self.apply_status_logic(target, StatusEffect("Rupture", "[medium_spring_green]✧[/medium_spring_green]", 2, "Upon getting hit by a skill, Take extra fixed damage equal to the amount of Potency, then reduce count by 1. Max Potency or Count: 99", duration=5))

            # Riposte Gang
            elif chip.effect_type == "RIPOSTE_GAIN_SPECIAL_1":
                if any(s.name == "Pierce Affinity" for s in target.status_effects):
                    self.apply_status_logic(attacker, StatusEffect("Riposte", "[cyan1]➲[/cyan1]", 0, "Take -5% damage for every 10 stacks owned (max -25%). When taking damage, reduce stack count by 1-4 stacks. For every 10 cumulative stacks reduced this way, gain 1 Haste next turn, then reset the count. At end of turn, reduce stack count by 25%. Max Count: 50", duration=10))
            elif chip.effect_type == "PIERCE_AFFINITY_INFLICT_SPECIAL_1":
                if any(s.name == "Pierce Affinity" for s in target.status_effects): self.apply_status_logic(target, StatusEffect("Pierce Affinity", "[light_yellow3]➾[/light_yellow3]", 0, "Take +Base Damage from any skill related to Pierce Affinity based on stack amount. Upon getting hit by a skill, reduce count by 1. Max Count: 5", duration=2))
                else: self.apply_status_logic(target, StatusEffect("Pierce Affinity", "[light_yellow3]➾[/light_yellow3]", 0, "Take +Base Damage from any skill related to Pierce Affinity based on stack amount. Upon getting hit by a skill, reduce count by 1. Max Count: 5", duration=1))
            elif chip.effect_type == "RIPOSTE_SQUAD_LEADER_SPECIAL_1":
                self.apply_status_logic(target, StatusEffect("Pierce Affinity", "[light_yellow3]➾[/light_yellow3]", 0, "Take +Base Damage from any skill related to Pierce Affinity based on stack amount. Upon getting hit by a skill, reduce count by 1. Max Count: 5", duration=2))
            elif chip.effect_type == "RIPOSTE_SQUAD_LEADER_SPECIAL_2":
                self.apply_status_logic(target, StatusEffect("Pierce Affinity", "[light_yellow3]➾[/light_yellow3]", 0, "Take +Base Damage from any skill related to Pierce Affinity based on stack amount. Upon getting hit by a skill, reduce count by 1. Max Count: 5", duration=3))
            elif chip.effect_type == "ADAM_SPECIAL_1":
                self.apply_status_logic(target, StatusEffect("Pierce Affinity", "[light_yellow3]➾[/light_yellow3]", 0, "Take +Base Damage from any skill related to Pierce Affinity based on stack amount. Upon getting hit by a skill, reduce count by 1. Max Count: 5", duration=2))
                self.apply_status_logic(attacker, StatusEffect("Riposte", "[cyan1]➲[/cyan1]", 0, "Take -5% damage for every 10 stacks owned (max -25%). When taking damage, reduce stack count by 1-4 stacks. For every 10 cumulative stacks reduced this way, gain 1 Haste next turn, then reset the count. At end of turn, reduce stack count by 25%. Max Count: 50", duration=10))
            elif chip.effect_type == "ADAM_SPECIAL_2":
                pierce_target_eff = next((s for s in target.status_effects if s.name == "Pierce Affinity"), None)
                if pierce_target_eff: self.apply_status_logic(attacker, StatusEffect("Riposte", "[cyan1]➲[/cyan1]", 0, "Take -5% damage for every 10 stacks owned (max -25%). When taking damage, reduce stack count by 1-4 stacks. For every 10 cumulative stacks reduced this way, gain 1 Haste next turn, then reset the count. At end of turn, reduce stack count by 25%. Max Count: 50", duration=5 * pierce_target_eff.duration))
                self.apply_status_logic(target, StatusEffect("Pierce Affinity", "[light_yellow3]➾[/light_yellow3]", 0, "Take +Base Damage from any skill related to Pierce Affinity based on stack amount. Upon getting hit by a skill, reduce count by 1. Max Count: 5", duration=3))
            elif chip.effect_type == "ADAM_SPECIAL_3":
                self.apply_status_logic(target, StatusEffect("Pierce Affinity", "[light_yellow3]➾[/light_yellow3]", 0, "Take +Base Damage from any skill related to Pierce Affinity based on stack amount. Upon getting hit by a skill, reduce count by 1. Max Count: 5", duration=5))
                riposte_eff = next((s for s in attacker.status_effects if s.name == "Riposte"), None)
                if riposte_eff: riposte_eff.duration = 50
                else: self.apply_status_logic(attacker, StatusEffect("Riposte", "[cyan1]➲[/cyan1]", 0, "Take -5% damage for every 10 stacks owned (max -25%). When taking damage, reduce stack count by 1-4 stacks. For every 10 cumulative stacks reduced this way, gain 1 Haste next turn, then reset the count. At end of turn, reduce stack count by 25%. Max Count: 50", duration=50))
            
            # COUNTER SKILLS
            elif chip.effect_type == "COUNTER_SKILL_SPECIAL_TYPE1":
                self.apply_status_logic(target, StatusEffect("Pierce Affinity", "[light_yellow3]➾[/light_yellow3]", 0, "Take +Base Damage from any skill related to Pierce Affinity based on stack amount. Upon getting hit by a skill, reduce count by 1. Max Count: 5", duration=2))
            elif chip.effect_type == "COUNTER_SKILL_SPECIAL_TYPE3":
                self.apply_status_logic(target, StatusEffect("Pierce Affinity", "[light_yellow3]➾[/light_yellow3]", 0, "Take +Base Damage from any skill related to Pierce Affinity based on stack amount. Upon getting hit by a skill, reduce count by 1. Max Count: 5", duration=3))

            # RIPOSTE KATAS EFFECTS
            elif chip.effect_type in ["NAGANOHARA_RIPOSTE_APPEL", "NAGANOHARA_RIPOSTE_CEDE", "NAGANOHARA_RIPOSTE_COUNTERPARRY", "AKASUKE_RIPOSTE_ENGARDE", "AKASUKE_RIPOSTE_FEINT", "AKASUKE_RIPOSTE_PRISEDEFER"]:
                riposte_eff = next((s for s in attacker.status_effects if s.name == "Riposte"), None)
                if chip.effect_type == "NAGANOHARA_RIPOSTE_APPEL":
                    self.apply_status_logic(attacker, StatusEffect("Riposte", "[cyan1]➲[/cyan1]", 0, "Take -5% damage for every 10 stacks owned (max -25%). When taking damage, reduce stack count by 1-4 stacks. For every 10 cumulative stacks reduced this way, gain 1 Haste next turn, then reset the count. At end of turn, reduce stack count by 25%. Max Count: 50", duration=5))
                    self.apply_status_logic(target, StatusEffect("Pierce Affinity", "[light_yellow3]➾[/light_yellow3]", 0, "Take +Base Damage from any skill related to Pierce Affinity based on stack amount. Upon getting hit by a skill, reduce count by 1. Max Count: 5", duration=1))
                elif chip.effect_type == "NAGANOHARA_RIPOSTE_CEDE":
                    self.apply_status_logic(attacker, StatusEffect("Riposte", "[cyan1]➲[/cyan1]", 0, "Take -5% damage for every 10 stacks owned (max -25%). When taking damage, reduce stack count by 1-4 stacks. For every 10 cumulative stacks reduced this way, gain 1 Haste next turn, then reset the count. At end of turn, reduce stack count by 25%. Max Count: 50", duration=10))
                    self.apply_status_logic(target, StatusEffect("Pierce Affinity", "[light_yellow3]➾[/light_yellow3]", 0, "Take +Base Damage from any skill related to Pierce Affinity based on stack amount. Upon getting hit by a skill, reduce count by 1. Max Count: 5", duration=2))
                elif chip.effect_type == "NAGANOHARA_RIPOSTE_COUNTERPARRY":
                    if riposte_eff and riposte_eff.duration >= 25:
                        riposte_eff.duration = 50
                        self.log(f"[cyan1]{attacker.name} maxes out their Riposte Stance![/cyan1]")
                    else: self.apply_status_logic(attacker, StatusEffect("Riposte", "[cyan1]➲[/cyan1]", 0, "Take -5% damage for every 10 stacks owned (max -25%). When taking damage, reduce stack count by 1-4 stacks. For every 10 cumulative stacks reduced this way, gain 1 Haste next turn, then reset the count. At end of turn, reduce stack count by 25%. Max Count: 50", duration=20))
                    self.apply_status_logic(target, StatusEffect("Pierce Affinity", "[light_yellow3]➾[/light_yellow3]", 0, "Take +Base Damage from any skill related to Pierce Affinity based on stack amount. Upon getting hit by a skill, reduce count by 1. Max Count: 5", duration=3))
                elif chip.effect_type == "AKASUKE_RIPOSTE_ENGARDE":
                    if not riposte_eff or riposte_eff.duration <= 0: self.apply_status_logic(attacker, StatusEffect("Riposte", "[cyan1]➲[/cyan1]", 0, "Take -5% damage for every 10 stacks owned (max -25%). When taking damage, reduce stack count by 1-4 stacks. For every 10 cumulative stacks reduced this way, gain 1 Haste next turn, then reset the count. At end of turn, reduce stack count by 25%. Max Count: 50", duration=10))
                    else: self.apply_status_logic(attacker, StatusEffect("Riposte", "[cyan1]➲[/cyan1]", 0, "Take -5% damage for every 10 stacks owned (max -25%). When taking damage, reduce stack count by 1-4 stacks. For every 10 cumulative stacks reduced this way, gain 1 Haste next turn, then reset the count. At end of turn, reduce stack count by 25%. Max Count: 50", duration=5))
                    self.apply_status_logic(target, StatusEffect("Pierce Affinity", "[light_yellow3]➾[/light_yellow3]", 0, "Take +Base Damage from any skill related to Pierce Affinity based on stack amount. Upon getting hit by a skill, reduce count by 1. Max Count: 5", duration=1))
                elif chip.effect_type == "AKASUKE_RIPOSTE_FEINT":
                    self.apply_status_logic(attacker, StatusEffect("Haste", "[yellow1]🢙[/yellow1]", 0, "Deal +(10*Count)% base damage with skills. Lose 1 count every new turn. Max count: 5", duration=1))
                    if riposte_eff and riposte_eff.duration >= 10: self.apply_status_logic(attacker, StatusEffect("Haste", "[yellow1]🢙[/yellow1]", 0, "Deal +(10*Count)% base damage with skills. Lose 1 count every new turn. Max count: 5", duration=1))
                    target_pierce = next((s for s in target.status_effects if s.name == "Pierce Affinity"), None)
                    if target_pierce and target_pierce.duration > 0: self.apply_status_logic(attacker, StatusEffect("Riposte", "[cyan1]➲[/cyan1]", 0, "Take -5% damage for every 10 stacks owned (max -25%). When taking damage, reduce stack count by 1-4 stacks. For every 10 cumulative stacks reduced this way, gain 1 Haste next turn, then reset the count. At end of turn, reduce stack count by 25%. Max Count: 50", duration=10))
                    self.apply_status_logic(target, StatusEffect("Pierce Affinity", "[light_yellow3]➾[/light_yellow3]", 0, "Take +Base Damage from any skill related to Pierce Affinity based on stack amount. Upon getting hit by a skill, reduce count by 1. Max Count: 5", duration=2))
                elif chip.effect_type == "AKASUKE_RIPOSTE_PRISEDEFER":
                    self.apply_status_logic(attacker, StatusEffect("Riposte", "[cyan1]➲[/cyan1]", 0, "Take -5% damage for every 10 stacks owned (max -25%). When taking damage, reduce stack count by 1-4 stacks. For every 10 cumulative stacks reduced this way, gain 1 Haste next turn, then reset the count. At end of turn, reduce stack count by 25%. Max Count: 50", duration=10))
                    self.apply_status_logic(target, StatusEffect("Pierce Affinity", "[light_yellow3]➾[/light_yellow3]", 0, "Take +Base Damage from any skill related to Pierce Affinity based on stack amount. Upon getting hit by a skill, reduce count by 1. Max Count: 5", duration=3))

            # KIRYOKU FAIRY & INFILTRATOR
            elif chip.effect_type == "RUPTURE_SPECIAL1":
                has_rupture = any(s.name in ["Rupture", "Fairylight"] for s in target.status_effects)
                if has_rupture: self.apply_status_logic(target, StatusEffect("Rupture", "[medium_spring_green]✧[/medium_spring_green]", 1, "Upon getting hit by a skill, Take extra fixed damage equal to the amount of Potency, then reduce count by 1. Max Potency or Count: 99", duration=chip.effect_val))
                else: self.apply_status_logic(target, StatusEffect("Rupture", "[medium_spring_green]✧[/medium_spring_green]", chip.effect_val, "Upon getting hit by a skill, Take extra fixed damage equal to the amount of Potency, then reduce count by 1. Max Potency or Count: 99", duration=1))
            elif chip.effect_type == "FAIRYLIGHT_APPLY":
                has_rupture = any(s.name in ["Rupture", "Fairylight"] for s in target.status_effects)
                if has_rupture: self.apply_status_logic(target, StatusEffect("Fairylight", "[spring_green1]𒀭[/spring_green1]", chip.effect_val, "Unique Rupture (Counts As Rupture)\nUpon getting hit by a skill, Take extra fixed damage equal to the amount of Potency. On turn end, reduce Count by half, and if this unit has Rupture, gain Rupture Potency based on Count lost this way. Max Potency or Count: 99", duration=1))
            elif chip.effect_type == "BENIKAWA_KIRYOKU_SPECIAL":
                has_rupture = any(s.name in ["Rupture", "Fairylight"] for s in target.status_effects)
                if has_rupture: self.apply_status_logic(target, StatusEffect("Fairylight", "[spring_green1]𒀭[/spring_green1]", 3, "Unique Rupture (Counts As Rupture)\nUpon getting hit by a skill, Take extra fixed damage equal to the amount of Potency. On turn end, reduce Count by half, and if this unit has Rupture, gain Rupture Potency based on Count lost this way. Max Potency or Count: 99", duration=1))
            elif chip.effect_type == "FAIRYLIGHT_SPECIAL1":
                has_fairylight = any(s.name == "Fairylight" for s in target.status_effects)
                if has_fairylight: self.apply_status_logic(target, StatusEffect("Rupture", "[medium_spring_green]✧[/medium_spring_green]", chip.effect_val, "Upon getting hit by a skill, Take extra fixed damage equal to the amount of Potency, then reduce count by 1. Max Potency or Count: 99", duration=1))
            elif chip.effect_type == "HANA_KIRYOKU_SPECIAL":
                has_fairylight = any(s.name == "Fairylight" for s in target.status_effects)
                if has_fairylight:
                    self.apply_status_logic(target, StatusEffect("Rupture", "[medium_spring_green]✧[/medium_spring_green]", 1, "Upon getting hit by a skill, Take extra fixed damage equal to the amount of Potency, then reduce count by 1. Max Potency or Count: 99", duration=2))
                    attacker.temp_modifiers["incoming_dmg_mult"] *= 0.70
            elif chip.effect_type == "HASTE_GAIN_SPECIAL_TYPE1":
                has_haste = any(s.name == "Haste" for s in attacker.status_effects)
                if has_haste: self.apply_status_logic(attacker, StatusEffect("Haste", "[yellow1]🢙[/yellow1]", 0, "Deal +(10*Count)% base damage with skills. Lose 1 count every new turn. Max count: 5", duration=1))
                self.apply_status_logic(attacker, StatusEffect("Haste", "[yellow1]🢙[/yellow1]", 0, "Deal +(10*Count)% base damage with skills. Lose 1 count every new turn. Max count: 5", duration=chip.effect_val))
            elif chip.effect_type == "DEBUFF_ATK_MULT":
                target.temp_modifiers["outgoing_dmg_mult"] *= chip.effect_val

            # BENIKAWA NINJA CLAN
            elif chip.effect_type == "BENIKAWA_CLAN_SPECIAL_1":
                target.temp_modifiers["final_dmg_reduction"] -= 4
                has_bleed = any(s.name == "Bleed" for s in target.status_effects)
                if has_bleed: self.apply_status_logic(target, StatusEffect("Bleed", "[red]💧︎[/red]", 3, "", duration=1))
                self.apply_status_logic(target, StatusEffect("Pierce Affinity", "[light_yellow3]⇴[/light_yellow3]", 0, "", duration=1))
            elif chip.effect_type == "BENIKAWA_CLAN_SPECIAL_2":
                has_poise = any(s.name == "Poise" for s in attacker.status_effects)
                if not has_poise: self.apply_status_logic(attacker, StatusEffect("Poise", "[light_cyan1]༄[/light_cyan1]", 1, "", duration=4))
                self.apply_status_logic(attacker, StatusEffect("Poise", "[light_cyan1]༄[/light_cyan1]", 3, "", duration=1))
                self.apply_status_logic(attacker, StatusEffect("Haste", "[yellow1]🢙[/yellow1]", 0, "", duration=2))
            elif chip.effect_type == "BENIKAWA_CLAN_SPECIAL_3":
                target.temp_modifiers["outgoing_dmg_mult"] *= 0.85
                target.next_turn_modifiers["outgoing_dmg_mult"] = target.next_turn_modifiers.get("outgoing_dmg_mult", 1.0) * 0.75
                has_bleed = any(s.name == "Bleed" for s in target.status_effects)
                if has_bleed:
                    self.apply_status_logic(target, StatusEffect("Bleed", "[red]💧︎[/red]", 3, "", duration=3))
                    self.apply_status_logic(attacker, StatusEffect("Haste", "[yellow1]🢙[/yellow1]", 0, "", duration=2))
                has_pierce = any(s.name == "Pierce Affinity" for s in target.status_effects)
                if has_pierce:
                    self.apply_status_logic(target, StatusEffect("Pierce Affinity", "[light_yellow3]⇴[/light_yellow3]", 0, "", duration=2))
                    self.apply_status_logic(attacker, StatusEffect("Poise", "[light_cyan1]༄[/light_cyan1]", 3, "", duration=2))

            # --- LUOXIA MARTIAL ARTS STUDENT ---
            elif chip.effect_type == "RUPTURE_BUFF_DEF_SPECIAL_1":
                self.apply_status_logic(target, StatusEffect("Rupture", "[medium_spring_green]✧[/medium_spring_green]", 2, "Upon getting hit by a skill, Take extra fixed damage equal to the amount of Potency, then reduce count by 1. Max Potency or Count: 99", duration=0))
                if not hasattr(attacker, "next_turn_modifiers"): attacker.next_turn_modifiers = {}
                attacker.next_turn_modifiers["final_dmg_reduction"] = attacker.next_turn_modifiers.get("final_dmg_reduction", 0) + 1
            elif chip.effect_type == "RUPTURE_BUFF_DEF_SPECIAL_2":
                self.apply_status_logic(target, StatusEffect("Rupture", "[medium_spring_green]✧[/medium_spring_green]", 0, "Upon getting hit by a skill, Take extra fixed damage equal to the amount of Potency, then reduce count by 1. Max Potency or Count: 99", duration=2))
                if not hasattr(attacker, "next_turn_modifiers"): attacker.next_turn_modifiers = {}
                attacker.next_turn_modifiers["final_dmg_reduction"] = attacker.next_turn_modifiers.get("final_dmg_reduction", 0) + 1
            elif chip.effect_type == "POISE_RUPTURE_SPECIAL_TYPE1":
                self.apply_status_logic(attacker, StatusEffect("Poise", "[light_cyan1]༄[/light_cyan1]", chip.effect_val, "Boost Critical Hit chance by (Potency*5)% for the next 'Count' amount of hits. Max potency or count: 99", duration=chip.effect_val))
                self.apply_status_logic(target, StatusEffect("Rupture", "[medium_spring_green]✧[/medium_spring_green]", chip.effect_val, "Upon getting hit by a skill, Take extra fixed damage equal to the amount of Potency, then reduce count by 1. Max Potency or Count: 99", duration=0))
    
            # --- NATSUME STRANGE KATA (ON HIT) ---
            elif chip.effect_type == "NATSUME_STRANGE_SPECIAL_1":
                self.apply_status_logic(target, StatusEffect("Rupture", "[medium_spring_green]✧[/medium_spring_green]", 0, "Upon getting hit by a skill, Take extra fixed damage equal to the amount of Potency, then reduce count by 1. Max Potency or Count: 99", duration=3))
            elif chip.effect_type == "NATSUME_STRANGE_SPECIAL_2":
                self.apply_status_logic(target, StatusEffect("Rupture", "[medium_spring_green]✧[/medium_spring_green]", 1, "Upon getting hit by a skill, Take extra fixed damage equal to the amount of Potency, then reduce count by 1. Max Potency or Count: 99", duration=0))
            elif chip.effect_type == "NATSUME_STRANGE_SPECIAL_3":
                self.apply_status_logic(target, StatusEffect("Sinking", "[blue3]♆[/blue3]", 0, "Upon getting hit by a skill, add Potency to an 'LS' (Low Sanity) tally and reduce Count by 1. Next turn, before attacking, each hit has an LS% chance to deal -(LS/2)% Final Damage. LS resets to 0 at turn end. Max LS: 90. Max Potency or Count: 99", duration=5, type="DEBUFF"))
            elif chip.effect_type == "NATSUME_STRANGE_SPECIAL_4":
                self.apply_status_logic(target, StatusEffect("Sinking", "[blue3]♆[/blue3]", 1, "Upon getting hit by a skill, add Potency to an 'LS' (Low Sanity) tally and reduce Count by 1. Next turn, before attacking, each hit has an LS% chance to deal -(LS/2)% Final Damage. LS resets to 0 at turn end. Max LS: 90. Max Potency or Count: 99", duration=0, type="DEBUFF"))
            elif chip.effect_type == "NATSUME_STRANGE_SPECIAL_5":
                self.apply_status_logic(target, StatusEffect("Sinking", "[blue3]♆[/blue3]", 2, "Upon getting hit by a skill, add Potency to an 'LS' (Low Sanity) tally and reduce Count by 1. Next turn, before attacking, each hit has an LS% chance to deal -(LS/2)% Final Damage. LS resets to 0 at turn end. Max LS: 90. Max Potency or Count: 99", duration=0, type="DEBUFF"))
            elif chip.effect_type == "NATSUME_STRANGE_SPECIAL_6":
                self.apply_status_logic(target, StatusEffect("Rupture", "[medium_spring_green]✧[/medium_spring_green]", 2, "Upon getting hit by a skill, Take extra fixed damage equal to the amount of Potency, then reduce count by 1. Max Potency or Count: 99", duration=0))

            # --- GOLDEN FIST UNION ---
            elif skill.effect_type == "GOLDEN_FIST_SPECIAL":
                self.apply_status_logic(attacker, StatusEffect("Bind", "[dim gold1]⛓[/dim gold1]", 0, "Deal -(10*Count)% base damage with skills. Lose 1 count every new turn. Max Count: 5", duration=5))
            elif chip.effect_type == "APPLY_BLEED_RUPTURE_HEAVY_STACKS":
                self.apply_status_logic(target, StatusEffect("Bleed", "[red]🩸[/red]", 2, "Take (Potency) damage on turn end, then reduce count by 1. Max Potency or Count: 99", duration=2))
                self.apply_status_logic(target, StatusEffect("Rupture", "[medium_spring_green]✧[/medium_spring_green]", 2, "Upon getting hit by a skill, Take extra fixed damage equal to the amount of Potency, then reduce count by 1. Max Potency or Count: 99", duration=2))
            elif chip.effect_type == "RUPTURE_BUFF_AND_COUNT_SPECIAL":
                self.apply_status_logic(target, StatusEffect("Rupture", "[medium_spring_green]✧[/medium_spring_green]", 0, "Upon getting hit by a skill, Take extra fixed damage equal to the amount of Potency, then reduce count by 1. Max Potency or Count: 99", duration=3))

            if target.hp <= 0:
                target.hp = 0
                self.log(f"[bold red]{target.name} was defeated![/bold red]")

            # --- DELAY BETWEEN CHIP HITS ---
            # If this is a multi-hit skill and not the last chip, render the current state and pause
            if len(chips_to_execute) > 1 and chip_idx < len(chips_to_execute) - 1:
                self.render_battle_screen()
                time.sleep(0.75)

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
            if new_status.name in DUAL_STACK_EFFECTS:
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
            if new_status.name in DUAL_STACK_EFFECTS:
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
                kata_info_str = str(unit.kata.rift_aptitude) if unit.kata else "None"
            else:
                kata_label = "Kata"
                kata_info_str = unit.kata.name if unit.kata else "None"

            pool_text = ""
            if unit.kata and hasattr(unit.kata, 'skill_pool_def'):
                sorted_pool = sorted(unit.kata.skill_pool_def, key=lambda x: x[0].tier)
                for skill, count in sorted_pool:
                    c = get_element_color(skill.element)
                    t_r = get_tier_roman(skill.tier)
                    
                    # --- CHIP SKILL / DETAILED DESCRIPTION LOGIC ---
                    if hasattr(skill, "inspect_description") and skill.inspect_description:
                        desc = skill.inspect_description
                    else:
                        desc = skill.description if skill.description else ""
                        
                    dmg_str = f"[bold]Dmg: {skill.base_damage}[/bold]"
                    
                    # Format newlines so multi-line inspect descriptions indent perfectly
                    formatted_desc = desc.replace("\n", "\n")
                    
                    pool_text += f"x{count} [{c}]{skill.name}[/{c}] ({t_r}) {dmg_str}\n       [light_green]{formatted_desc}[/light_green]\n"
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
                se_text = "No active status effects.\n"

            # --- PASSIVE TEXT LOGIC ---
            passives_text = ""
            active_passives = getattr(unit, "passives", [])
            if not active_passives and getattr(unit, "kata", None):
                active_passives = getattr(unit.kata, "passives", [])

            if active_passives:
                for i, p in enumerate(active_passives):
                    # The color tag now wraps the entire line, keeping the Px bolded!
                    passives_text += f"[{p.color}][bold]P{i+1}[/bold]: {p.name}[/{p.color}]\n"
            else:
                passives_text = "No active passives.\n"

            content = f"""
[bold]{unit.name}[/bold]
HP: {unit.hp}/{unit.max_hp}
{kata_label}: {kata_info_str}
Modifiers: {status_str}

[bold]Status Effects:[/bold]
{se_text}
[bold]Passives:[/bold]
{passives_text}
[bold]Full Skill Pool:[/bold]
{pool_text}
            """
            layout = Layout()
            layout.split_row(Layout(Panel(content)), Layout(Panel(res_table)))
            config.console.print(layout)
            config.console.print("\nType [bold]SE#[/bold] to view status details, [bold]P#[/bold] to view passive details, or [Enter] to return.")
            
            choice = get_player_input("Input > ").upper()
            if choice == "": break
                
            if choice.startswith("SE") and choice[2:].isdigit():
                idx = int(choice[2:]) - 1
                if 0 <= idx < len(unit.status_effects):
                    eff = unit.status_effects[idx]
                    
                    # --- Ensure Fairylight and Rupture always display correct descriptions ---
                    disp_name = eff.name
                    disp_desc = eff.description
                    
                    if disp_name == "Fairylight":
                        disp_desc = "Unique Rupture (Counts As Rupture)\nUpon getting hit by a skill, Take extra fixed damage equal to the amount of Potency. On turn end, reduce Count by half, and if this unit has Rupture, gain Rupture Potency based on Count lost this way. Max Potency or Count: 99"
                    elif disp_name == "Rupture":
                        disp_desc = "Upon getting hit by a skill, Take extra fixed damage equal to the amount of Potency, then reduce count by 1. Max Potency or Count: 99"
                    
                    config.console.print(Panel(f"[bold]{disp_name}[/bold]\n\n{disp_desc}", title="Status Effect", style="green"))
                    get_player_input("Press Enter...")
                    
            # --- PASSIVE EXPANSION INPUT ---
            elif choice.startswith("P") and choice[1:].isdigit():
                idx = int(choice[1:]) - 1
                
                active_passives = getattr(unit, "passives", [])
                if not active_passives and getattr(unit, "kata", None):
                    active_passives = getattr(unit.kata, "passives", [])
                    
                if active_passives and 0 <= idx < len(active_passives):
                    p = active_passives[idx]
                    # Uses dynamic p.color for the Panel style boundary!
                    config.console.print(Panel(f"[bold]{p.name}[/bold]\n\n{p.description}", title="Passive", style=p.color))
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
            # Prepare intended skills first
            intent_lines = []
            if e.hp > 0 and getattr(e, "intents", []):
                for idx, (skill, target, _) in enumerate(e.intents):
                    c = get_element_color(skill.element)
                    t_r = get_tier_roman(skill.tier)
                    slot_sym = "".join(["⬢" if i == idx else "⬡" for i in range(e.pace)]) if e.pace > 1 else "⬢"
                    
                    intent_lines.append(f"   {slot_sym} -> [{c}]{skill.name}[/{c}] ({t_r}) -> {target.name}")
                    if skill.description:
                        intent_lines.append(f"       [light_green]{skill.description}[/light_green]")
                        
            elif e.hp > 0 and getattr(e, "intent", None): # Fallback for old system if missed
                skill, target, _ = e.intent
                c = get_element_color(skill.element)
                t_r = get_tier_roman(skill.tier)
                
                intent_lines.append(f"   -> [{c}]{skill.name}[/{c}] ({t_r}) -> {target.name}")
                if skill.description:
                    intent_lines.append(f"       [light_green]{skill.description}[/light_green]")

            # Prepare HP and Status Effects
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
                    
            # --- STRICT PRINTING ORDER ---
            
            # 1. Print Name and HP
            config.console.print(f"[bold red]{e.name}[/bold red] {status}")
            
            # 2. Print Status Effects right underneath the name
            if se_display.strip(): 
                config.console.print(f"   {se_display}")
                
            # 3. Print the intended skill(s) and description(s) last
            for line in intent_lines:
                config.console.print(line)

        config.console.print("\n" + "-"*30 + "\n")
        
        # Two-panel ally display (left: 1-4, right: 5-8)
        ally_displays = []
        for a in self.allies:
            active_marker = ">>" if a == active_unit else "  "
            hp_style = "green" if a.hp > a.max_hp/2 else "red"
            
            target_str = ""
            if a.hp > 0 and getattr(a, "slot_targets", []):
                # Only show target string if it's Pace 1, otherwise command phase handles showing targets
                if a.pace == 1 and len(a.slot_targets) > 0 and a.slot_targets[0]:
                    target_str = f"-> {a.slot_targets[0].name}"
            
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
                # Need to check for None because the new command phase replaces played skills with None
                for i, s in enumerate(a.hand):
                    if s is not None:
                        c = get_element_color(s.element)
                        t1 = get_tier_roman(s.tier)
                        
                        # Only visually print indices 1, 2, 3, etc. for what is ACTUALLY selectable
                        # To keep UI clean we won't strictly enforce physical numbers here if some are None,
                        # but for the visual overview, we just print the contents.
                        skill_line = f"   [{i+1}] [{c}]{s.name}[/{c}] ({t1})"
                        ally_lines.append(skill_line)
                        if s.description:
                            ally_lines.append(f"       [light_green]{s.description}[/light_green]")
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