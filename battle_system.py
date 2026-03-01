import time
import random
import copy 
from rich.panel import Panel
from rich.table import Table
from rich.layout import Layout
from rich.columns import Columns
import config 

from ui_components import clear_screen, get_player_input
from entities import ELEMENT_NAMES, STATUS_DESCS, get_element_color, get_tier_roman, to_subscript, StatusEffect

DURATION_ONLY_EFFECTS = ["Bind", "Haste", "Pierce Fragility", "Riposte", "Paralysis", "Overheat", "Cloud Sword [云]", "Invisibility", "Blossom", "Malice", "Flickering Invisibility", "Leaking Bloodlust"]
DUAL_STACK_EFFECTS =  ["Bleed", "Rupture", "Fairylight", "Poise", "Sinking", "Acceleration"]
RUPTURE_LIST = ["Rupture", "Fairylight"]
POISE_LIST = ["Poise", "Acceleration"]

"""
--------------------------------------------------------------------------------
CORE DATA STRUCTURES, BATTLE SYSTEM PROPERTIES, & ACT 4 DEV GUIDE
--------------------------------------------------------------------------------
The Battle System heavily relies on the 'Entity' class from entities.py.
Below is a breakdown of the essential properties and new Act 4 mechanics used during combat logic:

1. ENTITY STATE & MULTI-ACTION (PACE)
   self.hp               -> Current Health. If <= 0, unit is dead/incapacitated.
   self.max_hp           -> Cap for healing effects.
   self.pace             -> (int) Determines how many skill slots/actions a unit gets per turn.
   self.resistances      -> List of 7 floats (0.0 to 2.0+). 
                            Matches ELEMENT_NAMES indices (Eros, Philia, Storge, Agape, Ludus, Pragma, Philautia).

2. DECK, INTENTS, & TARGETING
   self.hand             -> List of Skill/ChipSkill objects currently available to play.
   self.deck             -> Draw pile. Refilled from discard_pile when empty.
   self.discard_pile     -> Used Skill objects go here.
   self.intents          -> (Enemy Only) List of Tuples: (Skill, TargetUnit, HandIndex). 
                            Now a list instead of a single tuple to support Pace > 1.
   self.target_priority  -> (Skill Property) Used in `assign_round_targets()` to force enemies to prioritize 
                            specific targets (e.g., "NOT_BENI_SHIGE" or "IS_BENI_SHIGE").

3. SKILLS vs CHIP SKILLS
   Normal Skills         -> Execute as a single hit. Base damage is handled directly.
   Chip Skills           -> Execute as multiple hits. Contains a list of `Chip` objects.
                            Each `Chip` has its own `base_damage`, `effect_type`, and `effect_val`.
                            Iterated through in `execute_skill` [STEP 2] & [STEP 3].

4. TEMPORARY MODIFIERS (Hidden Flags - Reset Accordingly)
   These are HIDDEN flags used for quick damage calculation adjustments without cluttering the UI.
   self.temp_modifiers = {
       "final_dmg_reduction": (int) Flat damage subtraction at the very end of calculation.
       "outgoing_dmg_flat":   (int) Flat Final Damage ADDED to hits dealt by this unit.
       "incoming_dmg_flat":   (int) Flat Final Damage ADDED to hits taken by this unit.
       "outgoing_dmg_mult":   (float) Multiplier for damage dealt BY this unit (Default 1.0).
       "incoming_dmg_mult":   (float) Multiplier for damage TAKEN by this unit (Default 1.0).
                              *Note: Standard % damage reduction (e.g., "Takes -20% Final Damage") 
                               is applied here: incoming_dmg_mult *= (1.0 - 0.20)
   }
   self.next_turn_modifiers -> Same dictionary structure as above, but applied to `temp_modifiers` 
                               at the start of the NEXT turn, then wiped.

5. STATUS EFFECTS (Visible UI Buffs/Debuffs)
   Must be carefully managed in 'process_turn_end_effects', 'execute_skill', and 'apply_status_logic'.
   - Dual Stack (Potency + Count): Bleed, Rupture, Fairylight, Poise, Sinking, Acceleration.
     * Rule: When adding 'potency' while target has no 'count', count starts at 1. 
             When adding 'count' while target has no 'potency', potency starts at 1.
   - Duration Only (Count = Potency/Duration): Bind, Haste, Pierce Fragility, Riposte, Paralysis, 
                                               Overheat, Cloud Sword [云], Invisibility.
   - Subsets: Unique statuses can count as core statuses (e.g., "Fairylight" is checked alongside "Rupture" 
              via `RUPTURE_LIST = ["Rupture", "Fairylight"]`).

6. PASSIVES
   Checked via: `getattr(unit, "passives", []) or (getattr(unit.kata, "passives", []) if getattr(unit, "kata", None) else [])`
   Handles constant state checks (like Intangible Form reducing Base Damage by 50%), start-of-turn buffs, 
   or unique triggers (like "First to take damage" tracked via `self.first_ally_to_take_damage` and `self.first_enemy_to_take_damage`).

7. TIPS & TRICKS FOR ACT 4 UPDATES
   - DO NOT create new status effects for simple one-turn "+3 Damage" buffs. Ride along the existing 
     `temp_modifiers["outgoing_dmg_flat"]` flag.
   - Check `effect_type` strings closely. If it ends in `_FLAT`, it applies to Final Damage. 
   - `base_dmg_val` is modified BEFORE resistances. `final_dmg` is modified AFTER resistances.
   - Extremely specific + important terminology: When a skill description mentions "all_allies" in this game, it ONLY refers to the player's allies. When a skill description mentions "this unit's allies / all of this unit's allies / an ally of this unit", it refers to the team / allies of the effect's owner. Both enemies and allies can use the latter wording, but only enemies can use "this unit's allies (etc.)" when referring to THEIR OWN allies / team!!
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
            self.first_ally_to_take_damage = None
            self.first_enemy_to_take_damage = None
            self.ally_attacker_order = []      # Tracks damage order
            self.enemy_attacker_order = []     # Tracks damage order
            self.brotherhood_triggered_allies = [] # Tracks distinct allied units (max 3)
            self.camaraderie_trigger_count = 0     # Tracks damage instances (max 3)
            
            for unit in self.allies + self.enemies:
                unit.fading_form_stacks_this_turn = 0 # Stack tracker
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

            # --- PASSIVE: BLIND SPOTS (GLOBAL CHECK) ---
            has_blind_spots = any(
                any(p.effect_type == "PASSIVE_BLIND_SPOTS" for p in (getattr(e, "passives", []) or (getattr(e.kata, "passives", []) if getattr(e, "kata", None) else [])))
                for e in self.enemies if e.hp > 0
            )
            if has_blind_spots and self.turn_count % 2 == 1:
                for ally in self.allies:
                    if ally.hp > 0 and any(s.name == "Bind" for s in ally.status_effects):
                        # Using pending_bind cleanly applies "Bind next turn"
                        ally.pending_bind = min(5, getattr(ally, "pending_bind", 0) + 2)
                self.log("[bold green][Passive][/bold green] Blind Spots prepares to deepen the Bind on your party!")

            # --- ZHAO FENG VANGUARD SUMMON LOGIC ---
            living_enemies = [e for e in self.enemies if e.hp > 0]
            zhao = next((e for e in living_enemies if e.name == "Zhao Feng"), None)
            if zhao:
                # Detect ally death to start the 2-turn cooldown
                if len(living_enemies) == 1 and getattr(self, "zhao_ally_was_alive", False):
                    self.zhao_next_summon_turn = self.turn_count + 2
                    self.zhao_ally_was_alive = False
                elif len(living_enemies) > 1:
                    self.zhao_ally_was_alive = True
                # Check summon conditions
                if len(living_enemies) == 1:
                    can_summon = False
                    # 1. Initial Turn 3 Summon
                    if self.turn_count == 3 and not getattr(self, "zhao_initial_summon_done", False):
                        can_summon = True
                        self.zhao_initial_summon_done = True
                    # 2. Cooldown Summon (2 turns after death)
                    elif getattr(self, "zhao_next_summon_turn", 999) <= self.turn_count:
                        can_summon = True
                    if can_summon:
                        import stages
                        db = stages.get_enemy_database()
                        choices = [e for e in db if e.name in ["Ten Thousand Blossom Brotherhood Linebreaker", "Ten Thousand Blossom Brotherhood Defender"]]
                        if choices:
                            self.enemies = [e for e in self.enemies if e.hp > 0 or e.name == "Zhao Feng"]
                            summon = copy.deepcopy(random.choice(choices))
                            summon.max_hp = 50
                            summon.hp = 50
                            summon.refresh_deck()
                            summon.draw_skills(summon.pace * 2)
                            summon.status_effects = []
                            summon.temp_modifiers = {"outgoing_dmg_mult": 1.0, "incoming_dmg_mult": 1.0, "incoming_dmg_flat": 0, "final_dmg_reduction": 0}
                            self.enemies.append(summon)
                            self.log(f"[hot_pink]The Vanguard calls for reinforcements! {summon.name} joins the fray![/hot_pink]")
                            # Reset states now that an ally is alive
                            self.zhao_ally_was_alive = True
                            self.zhao_next_summon_turn = 999

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

        # --- IMPEDIMENT: SEVERED ARM ---
        active_passives = getattr(unit, "passives", [])
        if not active_passives and getattr(unit, "kata", None): active_passives = getattr(unit.kata, "passives", [])
        for p in active_passives:
            if p.effect_type == "PASSIVE_SEVERED_ARM":
                unit.temp_modifiers["outgoing_dmg_mult"] *= 0.5
                unit.temp_modifiers["incoming_dmg_mult"] *= 2.0
                
        # --- ACCELERATION POISE CONVERSION & PACE LIMIT ---
        has_accel_passive = any(p.effect_type == "PASSIVE_ACCELERATION" for p in active_passives)
        if has_accel_passive:
            poise = next((s for s in unit.status_effects if s.name == "Poise"), None)
            accel = next((s for s in unit.status_effects if s.name == "Acceleration"), None)
            if poise:
                if accel:
                    accel.potency = min(99, accel.potency + poise.potency)
                    accel.duration = min(99, accel.duration + poise.duration)
                else:
                    accel = StatusEffect("Acceleration", "[bold pale_turquoise1]>>[/bold pale_turquoise1]", poise.potency, STATUS_DESCS["Acceleration"], duration=poise.duration, type="UNIQUEBUFF")
                    unit.status_effects.append(accel)
                unit.status_effects.remove(poise)
            
            # 30-Stack Pace Check
            accel_check = next((s for s in unit.status_effects if s.name == "Acceleration"), None)
            if accel_check:
                total_accel = accel_check.potency + accel_check.duration
                if total_accel >= 30:
                    if unit.pace >= 6:
                        # --- 6+ Pace Fallback ---
                        accel_check.potency = max(1, int(accel_check.potency * 0.3))
                        accel_check.duration = max(1, int(accel_check.duration * 0.3))
                        self.apply_status_logic(unit, StatusEffect("Overheat", "[indian_red]>>[/indian_red]", 0, STATUS_DESCS["Overheat"], duration=2, type="DEBUFF"))
                        self.log(f"[indian_red]{unit.name} Overheated at max velocity! Acceleration plummeted.[/indian_red]")
                    else:
                        # --- Normal Pace Up ---
                        unit.status_effects.remove(accel_check)
                        if getattr(unit, "miyu_pace_increases", 0) < 3:
                            unit.pace += 1
                            unit.miyu_pace_increases = getattr(unit, "miyu_pace_increases", 0) + 1
                            self.apply_status_logic(unit, StatusEffect("Overheat", "[indian_red]>>[/indian_red]", 0, STATUS_DESCS["Overheat"], duration=1, type="DEBUFF"))
                            self.log(f"[bold pale_turquoise1]{unit.name} reached velocity limit! Pace permanently increased to {unit.pace}![/bold pale_turquoise1]")
                            self.log(f"[indian_red]{unit.name}'s Systems Overheated![/indian_red]")

        # --- ENFORCEMENT RESET ---
        unit.enforcement_tally = 0
        unit.enforcement_activations = 0
        # --- BREATHING TECHNIQUES & INGRAINED COMMAND ---
        active_passives = getattr(unit, "passives", []) or (getattr(unit.kata, "passives", []) if getattr(unit, "kata", None) else [])
        if any(p.effect_type == "PASSIVE_BREATHING_TECHNIQUES" for p in active_passives):
            poise = next((s for s in unit.status_effects if s.name == "Poise"), None)
            if poise:
                heal_amt = 0
                if poise.potency > 20:
                    heal_amt += (poise.potency - 20)
                    poise.potency = 20
                if poise.duration > 20:
                    heal_amt += (poise.duration - 20)
                    poise.duration = 20
                if heal_amt > 0:
                    unit.hp = min(unit.max_hp, unit.hp + heal_amt)
                    self.log(f"[pale_turquoise1]Breathing Techniques healed {unit.name} for {heal_amt} HP![/pale_turquoise1]")
        if any(p.effect_type == "PASSIVE_INGRAINED_COMMAND" for p in active_passives):
            if self.turn_count % 2 == 0:
                self.apply_status_logic(unit, StatusEffect("Paralysis", "[orange1]ϟ[/orange1]", 1, STATUS_DESCS["Paralysis"], duration=1, type="DEBUFF"))

        # --- FRONTLINE FIGHTER HASTE LOGIC ---
        if any(p.effect_type == "PASSIVE_FRONTLINE_FIGHTER" for p in active_passives):
            if self.turn_count % 2 == 1:
                self.apply_status_logic(unit, StatusEffect("Haste", "[yellow1]🢙[/yellow1]", 0, STATUS_DESCS["Haste"], duration=1))

        # --- IBARA NINJA INVISIBILITY LOGIC ---
        if any(p.effect_type == "PASSIVE_IBARA_INVISIBILITY" for p in active_passives):
            if getattr(unit, "reflect_invis_damage", False): unit.reflect_invis_damage = False # Reset Reflect
            
            if self.turn_count == 1:
                self.apply_status_logic(unit, StatusEffect("Invisibility", "[purple4]⛆[/purple4]", 0, STATUS_DESCS["Invisibility"], duration=4, type="BUFF"))
            
            # Poise Fix
            invis = next((s for s in unit.status_effects if s.name == "Invisibility"), None)
            if invis:
                poise = next((s for s in unit.status_effects if s.name == "Poise"), None)
                if not poise: self.apply_status_logic(unit, StatusEffect("Poise", "[light_cyan1]༄[/light_cyan1]", 0, STATUS_DESCS["Poise"], duration=invis.duration))
                elif poise.duration < invis.duration: poise.duration = invis.duration
            
            # Poise Fix
            invis = next((s for s in unit.status_effects if s.name == "Invisibility"), None)
            if invis:
                poise = next((s for s in unit.status_effects if s.name == "Poise"), None)
                if not poise: self.apply_status_logic(unit, StatusEffect("Poise", "[light_cyan1]༄[/light_cyan1]", 0, STATUS_DESCS["Poise"], duration=invis.duration))
                elif poise.duration < invis.duration: poise.duration = invis.duration
            
        # --- KAGEROU TURN START / POISE FIX ---
        if any(p.effect_type == "PASSIVE_KAGEROU_INVISIBILITY" for p in active_passives):
            if getattr(unit, "reflect_flickering_damage", False): 
                unit.reflect_flickering_damage = False
            if self.turn_count == 1:
                self.apply_status_logic(unit, StatusEffect("Flickering Invisibility", "[thistle3]⛆[/thistle3]", 1, STATUS_DESCS["Flickering Invisibility"], duration=5, type="BUFF"))
            f_invis = next((s for s in unit.status_effects if s.name == "Flickering Invisibility"), None)
            if f_invis:
                poise = next((s for s in unit.status_effects if s.name == "Poise"), None)
                if not poise: self.apply_status_logic(unit, StatusEffect("Poise", "[light_cyan1]༄[/light_cyan1]", 0, STATUS_DESCS["Poise"], duration=1))
                else: poise.duration = 1

    def resolve_combat_start_effects(self):
        activated_any = False

        if self.turn_count == 1:
            zhao = next((e for e in self.enemies if e.name == "Zhao Feng" and e.hp > 0), None)
            if zhao:
                self.log("[hot_pink]Zhao Feng's oppressive aura blankets the battlefield![/hot_pink]")
                for u in self.allies + self.enemies:
                    rup = next((s for s in u.status_effects if s.name in RUPTURE_LIST), None)
                    if rup:
                        rup.potency = int((rup.potency / 2.0) + 0.5)
                        rup.duration = int((rup.duration / 2.0) + 0.5)
        
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

    # Faction Check
    def check_black_water_dock_req(self, unit):
        team = self.allies if unit in self.allies else self.enemies
        count = sum(1 for u in team if "Black Water Dock" in (u.kata.name if hasattr(u, "kata") and u.kata else u.name))
        return count >= 2

    def apply_combat_start_logic(self, unit, skill):
        # Existing Buff
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
            haste_eff = StatusEffect("Haste", "[yellow1]🢙[/yellow1]", 0, STATUS_DESCS["Haste"], duration=skill.effect_val)
            self.apply_status_logic(unit, haste_eff)

        elif skill.effect_type == "GOLDEN_FIST_SPECIAL":
            unit.temp_modifiers["final_dmg_reduction"] += 8
            team = self.allies if unit in self.allies else self.enemies
            for member in team:
                if member.hp > 0 and "Golden Fist Union" in member.name:
                    # Prevent stacking by tracking the turn count it was applied
                    if getattr(member, "golden_fist_buff_turn", 0) != self.turn_count:
                        member.temp_modifiers["outgoing_dmg_flat"] = member.temp_modifiers.get("outgoing_dmg_flat", 0) + 4
                        member.golden_fist_buff_turn = self.turn_count

        elif skill.effect_type == "MIYU_S5_COMBAT_START":
            unit.temp_modifiers["outgoing_base_dmg_pct"] = unit.temp_modifiers.get("outgoing_base_dmg_pct", 0) + ((unit.pace - 2) * 0.10)
            unit.temp_modifiers["final_dmg_reduction"] -= (8 + (unit.pace - 3))

        elif skill.effect_type == "IBARA_ACT4_SPECIAL3":
            invis = next((s for s in unit.status_effects if s.name == "Invisibility"), None)
            if invis and invis.duration >= 2:
                self.apply_status_logic(unit, StatusEffect("Invisibility", "[purple4]⛆[/purple4]", 0, STATUS_DESCS["Invisibility"], duration=1, type="BUFF"))
                
        elif skill.effect_type == "IBARA_ACT4_SPECIAL4":
            unit.reflect_invis_damage = True
    
        elif skill.effect_type == "ZHAOFENG_SPECIAL_1":
            for u in self.allies + self.enemies:
                rup = next((s for s in u.status_effects if s.name in RUPTURE_LIST), None)
                if rup:
                    val = int((rup.potency + rup.duration) / 3)
                    if val > 0:
                        self.apply_status_logic(u, StatusEffect("Blossom", "[hot_pink]❀[/hot_pink]", 0, STATUS_DESCS["Blossom"], duration=min(3, val), type="DEBUFF"))
        elif skill.effect_type == "ZHAOFENG_SPECIAL_2":
            for u in self.allies + self.enemies:
                rup = next((s for s in u.status_effects if s.name in RUPTURE_LIST), None)
                if rup:
                    val = int((rup.potency + rup.duration) / 3)
                    if val > 0:
                        self.apply_status_logic(u, StatusEffect("Malice", "[hot_pink]♨[/hot_pink]", 0, STATUS_DESCS["Malice"], duration=min(3, val), type="DEBUFF"))
        elif skill.effect_type == "ZHAOFENG_SPECIAL_7":
            for u in self.allies + self.enemies:
                if any(s.name == "Blossom" for s in u.status_effects):
                    self.apply_status_logic(u, StatusEffect("Bind", "[gold1]⛓[/gold1]", 1, STATUS_DESCS["Bind"], duration=3))
                rup = next((s for s in u.status_effects if s.name in RUPTURE_LIST), None)
                if rup:
                    val = int((rup.potency + rup.duration) / 3)
                    if val > 0:
                        self.apply_status_logic(u, StatusEffect("Blossom", "[hot_pink]❀[/hot_pink]", 0, STATUS_DESCS["Blossom"], duration=min(5, val), type="DEBUFF"))

        elif skill.effect_type == "KAGEROU_SPECIAL_CS":
            if not getattr(self, "kagerou_s3_cs_triggered", False):
                self.kagerou_s3_cs_triggered = True
                self.apply_status_logic(unit, StatusEffect("Flickering Invisibility", "[thistle3]⛆[/thistle3]", 1, STATUS_DESCS["Flickering Invisibility"], duration=1, type="BUFF"))
        elif skill.effect_type == "KAGEROU_SPECIAL_3":
            self.apply_status_logic(unit, StatusEffect("Poise", "[light_cyan1]༄[/light_cyan1]", 10, STATUS_DESCS["Poise"], duration=0, type="BUFF"))
        elif skill.effect_type == "KAGEROU_SPECIAL_7":
            unit.reflect_flickering_damage = True

        elif skill.effect_type == "YUNHAI_AKASUKE_SPECIAL1":
            team = self.allies if unit in self.allies else self.enemies
            for member in team:
                if member.hp > 0:
                    name_check = member.kata.name if hasattr(member, "kata") and member.kata else member.name
                    if "Yunhai Association" in name_check:
                        member.temp_modifiers["final_dmg_reduction"] += 2
        elif skill.effect_type == "YUNHAI_AKASUKE_SPECIAL2":
            team = self.allies if unit in self.allies else self.enemies
            for member in team:
                if member.hp > 0:
                    name_check = member.kata.name if hasattr(member, "kata") and member.kata else member.name
                    if "Yunhai Association" in name_check:
                        member.temp_modifiers["outgoing_base_dmg_flat"] = member.temp_modifiers.get("outgoing_base_dmg_flat", 0) + 2
        elif skill.effect_type == "YUNHAI_NAGANOHARA_SPECIAL2":
            team = self.allies if unit in self.allies else self.enemies
            for member in team:
                if member.hp > 0:
                    name_check = member.kata.name if hasattr(member, "kata") and member.kata else member.name
                    if "Yunhai Association" in name_check:
                        self.apply_status_logic(member, StatusEffect("Poise", "[light_cyan1]༄[/light_cyan1]", 3, STATUS_DESCS["Poise"], duration=0))
            self.apply_status_logic(unit, StatusEffect("Poise", "[light_cyan1]༄[/light_cyan1]", 0, STATUS_DESCS["Poise"], duration=3))
        elif skill.effect_type == "YUNHAI_NAGANOHARA_SPECIAL3":
            team = self.allies if unit in self.allies else self.enemies
            for member in team:
                if member.hp > 0:
                    name_check = member.kata.name if hasattr(member, "kata") and member.kata else member.name
                    if "Yunhai Association" in name_check:
                        member.temp_modifiers["outgoing_base_dmg_flat"] = member.temp_modifiers.get("outgoing_base_dmg_flat", 0) - 3
                        if not hasattr(member, "next_turn_modifiers"): member.next_turn_modifiers = {}
                        member.next_turn_modifiers["outgoing_base_dmg_flat"] = member.next_turn_modifiers.get("outgoing_base_dmg_flat", 0) + 3
        elif skill.effect_type == "BLACKWATER_SHIGEMURA_TYPE2":
            team = self.allies if unit in self.allies else self.enemies
            valid_allies = [u for u in team if u.hp > 0 and u != unit]
            bwd_allies = [u for u in valid_allies if "Black Water Dock" in (u.kata.name if hasattr(u, "kata") and u.kata else u.name)]
            non_bwd_allies = [u for u in valid_allies if u not in bwd_allies]
            pool = bwd_allies + non_bwd_allies
            chosen = [unit] + pool[:2]
            for c in chosen:
                name_check = c.kata.name if hasattr(c, "kata") and c.kata else c.name
                if "Black Water Dock" in name_check:
                    c.temp_modifiers["outgoing_dmg_flat"] = c.temp_modifiers.get("outgoing_dmg_flat", 0) + 3
                else:
                    c.temp_modifiers["outgoing_dmg_flat"] = c.temp_modifiers.get("outgoing_dmg_flat", 0) + 1
            for member in team:
                if member.hp > 0:
                    name_check = member.kata.name if hasattr(member, "kata") and member.kata else member.name
                    if "Black Water Dock" in name_check or member == unit:
                        self.apply_status_logic(member, StatusEffect("Poise", "[light_cyan1]༄[/light_cyan1]", 0, STATUS_DESCS["Poise"], duration=3))
        elif skill.effect_type == "YUNHAI_YURI_SPECIAL1":
            team = self.allies if unit in self.allies else self.enemies
            for member in team:
                if member.hp > 0 and any(s.name in POISE_LIST for s in member.status_effects):
                    name_check = member.kata.name if hasattr(member, "kata") and member.kata else member.name
                    amt = 3 if "Yunhai Association" in name_check else 2
                    self.apply_status_logic(member, StatusEffect("Poise", "[light_cyan1]༄[/light_cyan1]", 0, STATUS_DESCS["Poise"], duration=amt))
        elif skill.effect_type == "YUNHAI_YURI_CS1":
            team = self.allies if unit in self.allies else self.enemies
            for member in team:
                if member.hp > 0 and any(s.name in POISE_LIST for s in member.status_effects):
                    name_check = member.kata.name if hasattr(member, "kata") and member.kata else member.name
                    amt = 4 if "Yunhai Association" in name_check else 2
                    self.apply_status_logic(member, StatusEffect("Poise", "[light_cyan1]༄[/light_cyan1]", amt, STATUS_DESCS["Poise"], duration=0))

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
                elif effect.name in ["Bind", "Poise", "Haste", "Overheat"]:
                    effect.duration -= 1
                elif effect.name == "Fairylight":
                    old_duration = effect.duration
                    effect.duration = effect.duration // 2 
                    reduced_amount = old_duration - effect.duration
                    if reduced_amount > 0:
                        rupture_eff = next((s for s in unit.status_effects if s.name in RUPTURE_LIST), None)
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
                    bind_effect = StatusEffect("Bind", "[gold1]⛓[/gold1]", 1, STATUS_DESCS["Bind"], duration=actual_duration)
                    unit.status_effects.append(bind_effect)
                unit.pending_bind = 0
                effects_triggered = True

            if getattr(unit, "pending_haste", 0) > 0:
                actual_duration = min(5, unit.pending_haste)
                existing_haste = next((s for s in unit.status_effects if s.name == "Haste"), None)
                if existing_haste:
                    existing_haste.duration = min(5, existing_haste.duration + actual_duration)
                else:
                    haste_effect = StatusEffect("Haste", "[yellow1]🢙[/yellow1]", 0, STATUS_DESCS["Haste"], duration=actual_duration, type="BUFF")
                    unit.status_effects.append(haste_effect)
                unit.pending_haste = 0
                effects_triggered = True

            for effect in list(unit.status_effects):
                if effect.name in DUAL_STACK_EFFECTS:
                    if effect.potency <= 0 or effect.duration <= 0:
                        unit.status_effects.remove(effect)
                        effects_triggered = True

            # --- IBARA NINJA END TURN POISE FIX ---
            active_passives = getattr(unit, "passives", []) or (getattr(unit.kata, "passives", []) if getattr(unit, "kata", None) else [])
            if any(p.effect_type == "PASSIVE_IBARA_INVISIBILITY" for p in active_passives):
                invis = next((s for s in unit.status_effects if s.name == "Invisibility"), None)
                if invis:
                    poise = next((s for s in unit.status_effects if s.name == "Poise"), None)
                    if not poise: self.apply_status_logic(unit, StatusEffect("Poise", "[light_cyan1]༄[/light_cyan1]", 0, STATUS_DESCS["Poise"], duration=invis.duration))
                    elif poise.duration < invis.duration: poise.duration = invis.duration

            # --- End of Unit Loop: Transfer Sinking Tally ---
            unit.active_ls = getattr(unit, "pending_ls", 0)
            unit.pending_ls = 0

        if effects_triggered:
            self.render_battle_screen()
            time.sleep(1.0)
            self.battle_log = []

        # --- ZHAO FENG TALLY & APPEND LOGIC ---
        zhao = next((e for e in self.enemies if e.hp > 0 and e.name == "Zhao Feng"), None)
        if zhao:
            if not hasattr(zhao, 'zf_tally'): zhao.zf_tally = 0
            if not hasattr(zhao, 'zf_hp_dropped'): zhao.zf_hp_dropped = False
            if zhao.hp <= 280: zhao.zf_hp_dropped = True
            
            zhao.zf_tally += 1
            if zhao.zf_tally == 2:
                if not zhao.zf_hp_dropped:
                    zhao.deck.insert(random.randint(0, len(zhao.deck)), copy.deepcopy(zhao.appendable_skills["EX1"]))
                    self.log(f"[hot_pink]Zhao Feng draws 'Liao' [撩] into his deck![/hot_pink]")
                else:
                    zhao.deck.insert(random.randint(0, len(zhao.deck)), copy.deepcopy(zhao.appendable_skills["EX2"]))
                    self.log(f"[hot_pink]Zhao Feng's malice grows... 'Encroaching Malice' appended![/hot_pink]")
            elif zhao.zf_tally == 4:
                if not zhao.zf_hp_dropped:
                    zhao.deck.insert(random.randint(0, len(zhao.deck)), copy.deepcopy(zhao.appendable_skills["EX1"]))
                    self.log(f"[hot_pink]Zhao Feng draws 'Liao' [撩] into his deck![/hot_pink]")
                else:
                    zhao.deck.insert(random.randint(0, len(zhao.deck)), copy.deepcopy(zhao.appendable_skills["EX3"]))
                    self.log(f"[hot_pink]Zhao Feng prepares his ultimate technique: 'Embrace The Moon'![/hot_pink]")
                zhao.zf_tally = 0
                
        self.clamp_akasuke1() # End of turn DOT clamp

    def assign_round_targets(self):
        # Reset tracking
        for u in self.allies + self.enemies:
            u.slot_targets = []
            u.intents = []
            u.turn_committed_skills = [] # Clear committed skills for the new round
            u.chips_used_this_turn = 0   # Reset chip tracker at start of turn
            u.accel_reductions_this_turn = 0 # NEW: Track Acceleration reductions

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
                        # 1. Choose skill first
                        opt1 = slot_idx * 2
                        opt2 = slot_idx * 2 + 1
                        valid_opts = []
                        if opt1 < len(enemy.hand) and enemy.hand[opt1] is not None: valid_opts.append(opt1)
                        if opt2 < len(enemy.hand) and enemy.hand[opt2] is not None: valid_opts.append(opt2)
                        
                        if not valid_opts:
                            used_indices = [intent[2] for intent in enemy.intents]
                            available = [i for i in range(len(enemy.hand)) if i not in used_indices and enemy.hand[i] is not None]
                            if available: valid_opts = available
                        
                        chosen_idx = random.choice(valid_opts) if valid_opts else None
                        chosen_skill = enemy.hand[chosen_idx] if chosen_idx is not None else None
                        
                        # 2. Determine target priority based on chosen skill
                        priority = getattr(chosen_skill, "target_priority", None) if chosen_skill else None
                        target_pool = living_allies
                        if priority == "NOT_BENI_SHIGE":
                            subset = [a for a in living_allies if "Benikawa" not in a.name and "Shigemura" not in a.name]
                            if subset: target_pool = subset
                        elif priority == "IS_BENI_SHIGE":
                            subset = [a for a in living_allies if "Benikawa" in a.name or "Shigemura" in a.name]
                            if subset: target_pool = subset
                            
                        # 3. Finalize target
                        min_c = min(target_counts_allies[a] for a in target_pool)
                        least = [a for a in target_pool if target_counts_allies[a] == min_c]
                        t = random.choice(least)
                        
                        enemy.slot_targets.append(t)
                        target_counts_allies[t] += 1
                        if chosen_skill:
                            enemy.intents.append((chosen_skill, t, chosen_idx))
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
                    # Unpack the specific hand index (h_idx) they planned to use
                    skill, target, h_idx = enemy.intents[slot_idx] 
                    if target.hp <= 0:
                        living = [a for a in self.allies if a.hp > 0]
                        if living: target = random.choice(living)
                        else: break
                    enemy.turn_committed_skills.append(skill)
                    # --- Empty the hand slot so they draw new cards next turn ---
                    if h_idx < len(enemy.hand):
                        enemy.hand[h_idx] = None
                    self.execute_skill(enemy, skill, target)

    def get_avg_defense_tier(self, unit):
        if not unit.turn_committed_skills: return 0
        import math
        total = sum(s.tier for s in unit.turn_committed_skills)
        return math.ceil(total / len(unit.turn_committed_skills))

    def execute_skill(self, attacker, skill, target):
        if getattr(skill, "is_temporary", False) == False:
            attacker.discard_pile.append(skill)
        
        # Log Action
        self.log(f"{attacker.name} uses [bold]{skill.name}[/bold]!")
        self.render_battle_screen() 
        time.sleep(0.8) 

        # Initialize specific variables
        sadism_bind_to_apply = 0
        self.current_skill_flickering_rupture_applied = False
        
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
                    self.apply_status_logic(attacker, StatusEffect("Haste", "[yellow1]🢙[/yellow1]", 0, STATUS_DESCS["Haste"], duration=3))
            
            # HISAYUKI / EAGLE / AOE BUFFS
            if skill.effect_type == "HISAYUKI_SPECIAL_1":
                if not hasattr(attacker, "next_turn_modifiers"): attacker.next_turn_modifiers = {}
                attacker.next_turn_modifiers["incoming_dmg_mult"] = attacker.next_turn_modifiers.get("incoming_dmg_mult", 1.0) * 0.60
            elif skill.effect_type == "GAIN_POISE_SPECIAL":
                self.apply_status_logic(attacker, StatusEffect("Poise", "[light_cyan1]༄[/light_cyan1]", skill.effect_val, STATUS_DESCS["Poise"], duration=skill.effect_val))
            elif skill.effect_type == "EAGLE_SPECIAL_2":
                self.apply_status_logic(attacker, StatusEffect("Poise", "[light_cyan1]༄[/light_cyan1]", 3, STATUS_DESCS["Poise"], duration=3))
            elif skill.effect_type == "AOE_BUFF_ATK_FLAT":
                team = self.allies if attacker in self.allies else self.enemies
                for member in team:
                    if member.hp > 0:
                        member.temp_modifiers["outgoing_dmg_flat"] = member.temp_modifiers.get("outgoing_dmg_flat", 0) + skill.effect_val
            
            # RIPOSTE GANG
            if skill.effect_type in ["RIPOSTE_GAIN_SPECIAL_1", "RIPOSTE_SQUAD_LEADER_SPECIAL_1"]:
                self.apply_status_logic(attacker, StatusEffect("Riposte", "[cyan1]➲[/cyan1]", 0, STATUS_DESCS["Riposte"], duration=10))
            elif skill.effect_type == "RIPOSTE_SQUAD_LEADER_SPECIAL_2":
                riposte_eff = next((s for s in attacker.status_effects if s.name == "Riposte"), None)
                if riposte_eff: riposte_eff.duration = 30
                else: self.apply_status_logic(attacker, StatusEffect("Riposte", "[cyan1]➲[/cyan1]", 0, STATUS_DESCS["Riposte"], duration=30))
            elif skill.effect_type == "ADAM_SPECIAL_1":
                if not any(s.name == "Haste" for s in attacker.status_effects):
                    self.apply_status_logic(attacker, StatusEffect("Haste", "[yellow1]🢙[/yellow1]", 0, STATUS_DESCS["Haste"], duration=2))

            # ACT 4 COMMON
            if skill.effect_type == "BLEED_RUPTURE_BUFF_FLAT_TYPE1":
                if any(s.name in RUPTURE_LIST for s in target.status_effects):
                    attacker.temp_modifiers["outgoing_dmg_flat"] = attacker.temp_modifiers.get("outgoing_dmg_flat", 0) + skill.effect_val
            elif skill.effect_type == "RUPTURE_BUFF_AND_COUNT_SPECIAL":
                if any(s.name in RUPTURE_LIST for s in target.status_effects):
                    attacker.temp_modifiers["outgoing_dmg_flat"] = attacker.temp_modifiers.get("outgoing_dmg_flat", 0) + skill.effect_val
            elif skill.effect_type == "POISE_HASTE_SPECIAL_TYPE1":
                self.apply_status_logic(attacker, StatusEffect("Poise", "[light_cyan1]༄[/light_cyan1]", 2, STATUS_DESCS["Poise"], duration=2))
                self.apply_status_logic(attacker, StatusEffect("Haste", "[yellow1]🢙[/yellow1]", 0, STATUS_DESCS["Haste"], duration=2))
            elif skill.effect_type == "RUPTURE_PARALYSIS_SPECIAL_TYPE2":
                self.apply_status_logic(target, StatusEffect("Rupture", "[medium_spring_green]✧[/medium_spring_green]", skill.effect_val, STATUS_DESCS["Rupture"], duration=skill.effect_val))
                self.apply_status_logic(target, StatusEffect("Paralysis", "[orange1]ϟ[/orange1]", 1, STATUS_DESCS["Paralysis"], duration=skill.effect_val, type="DEBUFF"))
            elif skill.effect_type == "POISE_RUPTURE_SPECIAL_TYPE2":
                if any(s.name in POISE_LIST for s in attacker.status_effects):
                    self.apply_status_logic(attacker, StatusEffect("Poise", "[light_cyan1]༄[/light_cyan1]", skill.effect_val, STATUS_DESCS["Poise"], duration=0))
            elif skill.effect_type == "GOLDEN_FIST_SPECIAL":
                self.apply_status_logic(attacker, StatusEffect("Bind", "[gold1]⛓[/gold1]", 1, STATUS_DESCS["Bind"], duration=5))

            # ACT 4 IBARA NINJA
            if skill.effect_type == "IBARA_ACT4_SPECIAL2":
                invis = next((s for s in attacker.status_effects if s.name == "Invisibility"), None)
                if not invis or invis.duration < 2:
                    if invis: attacker.status_effects.remove(invis)
                    attacker.temp_modifiers["incoming_dmg_flat"] = attacker.temp_modifiers.get("incoming_dmg_flat", 0) + 5
                    if not hasattr(attacker, "next_turn_modifiers"): attacker.next_turn_modifiers = {}
                    attacker.next_turn_modifiers["incoming_dmg_flat"] = attacker.next_turn_modifiers.get("incoming_dmg_flat", 0) + 5
            elif skill.effect_type == "IBARA_ACT4_SPECIAL4":
                self.apply_status_logic(attacker, StatusEffect("Poise", "[light_cyan1]༄[/light_cyan1]", 12, STATUS_DESCS["Poise"], duration=0))

            # ACT 4 COMMON (CONTINUED + NINE ARMIES TYPE ENEMIES)
            if skill.effect_type == "BREAKTHEENEMY_SPECIAL":
                attacker.temp_modifiers["incoming_dmg_flat"] = attacker.temp_modifiers.get("incoming_dmg_flat", 0) + 5
            elif skill.effect_type == "POISE_RUPTURE_SINKING_SPECIAL1":
                val = skill.effect_val if hasattr(skill, "effect_val") and skill.effect_val is not None else 2
                self.apply_status_logic(attacker, StatusEffect("Poise", "[light_cyan1]༄[/light_cyan1]", val, STATUS_DESCS["Poise"], duration=val))
            elif skill.effect_type == "POISE_PARALYSIS_SPECIAL1":
                self.apply_status_logic(attacker, StatusEffect("Poise", "[light_cyan1]༄[/light_cyan1]", 1, STATUS_DESCS["Poise"], duration=3))
            elif skill.effect_type == "FORMALINE_SPECIAL":
                team = self.allies if attacker in self.allies else self.enemies
                ttbb_allies = [u for u in team if u.hp > 0 and "Ten Thousand Blossom Brotherhood" in u.name]
                x = len(ttbb_allies)
                for a in ttbb_allies:
                    self.apply_status_logic(a, StatusEffect("Poise", "[light_cyan1]༄[/light_cyan1]", x, STATUS_DESCS["Poise"], duration=2))
                    a.temp_modifiers["outgoing_dmg_flat"] = a.temp_modifiers.get("outgoing_dmg_flat", 0) + min(4, x)

            # IBARA NINJA KAGEROU
            chips_to_check = getattr(skill, "chips", [skill])
            for chip in chips_to_check:
                eff = getattr(chip, "effect_type", getattr(skill, "effect_type", None))
                if eff == "KAGEROU_SPECIAL_1":
                    self.apply_status_logic(attacker, StatusEffect("Flickering Invisibility", "[violet]⛆[/violet]", 0, "Takes -Count Base Damage from skills (max -5).", duration=1, type="BUFF"))
                elif eff == "KAGEROU_SPECIAL_2":
                    self.apply_status_logic(attacker, StatusEffect("Leaking Bloodlust", "[red3]✹[/red3]", 0, "Deal and take +(Count/11) Final Damage.", duration=5, type="BUFF"))
                elif eff == "KAGEROU_SPECIAL_4":
                    self.apply_status_logic(attacker, StatusEffect("Leaking Bloodlust", "[red3]✹[/red3]", 0, "Deal and take +(Count/11) Final Damage.", duration=3, type="BUFF"))   
            # Skill IV is a normal skill, so it's safely checked on the skill itself
            if skill.effect_type == "KAGEROU_SPECIAL_7":
                self.apply_status_logic(attacker, StatusEffect("Flickering Invisibility", "[violet]⛆[/violet]", 0, "Takes -Count Base Damage from skills (max -5).", duration=1, type="BUFF"))
                self.apply_status_logic(attacker, StatusEffect("Leaking Bloodlust", "[red3]✹[/red3]", 0, "Deal and take +(Count/11) Final Damage.", duration=10, type="BUFF"))
                self.apply_status_logic(attacker, StatusEffect("Poise", "[light_cyan1]༄[/light_cyan1]", 20, "Boost Critical Hit chance.", duration=0))

            # ACT 4 KATAS (FIRST HALF UPDATE)
            elif skill.effect_type == "YUNHAI_AKASUKE_SPECIAL1":
                self.apply_status_logic(attacker, StatusEffect("Poise", "[light_cyan1]༄[/light_cyan1]", 0, STATUS_DESCS["Poise"], duration=3))
            elif skill.effect_type == "YUNHAI_NAGANOHARA_SPECIAL3":
                self.apply_status_logic(attacker, StatusEffect("Poise", "[light_cyan1]༄[/light_cyan1]", 0, STATUS_DESCS["Poise"], duration=3))
            elif skill.effect_type == "LUOXIA_KAGAKU_SPECIAL1":
                team = self.allies if attacker in self.allies else self.enemies
                valid = [u for u in team if u.hp > 0]
                if valid:
                    yh = [u for u in valid if "Yunhai Region" in (u.kata.name if hasattr(u, "kata") and u.kata else u.name)]
                    others = [u for u in valid if u not in yh]
                    pool = sorted(yh, key=lambda x: x.hp/x.max_hp) + sorted(others, key=lambda x: x.hp/x.max_hp)
                    target_to_heal = pool[0]
                    heal_amt = int(attacker.max_hp * 0.10)
                    target_to_heal.hp = min(target_to_heal.max_hp, target_to_heal.hp + heal_amt)
                    self.log(f"[light_green]-> {attacker.name} Heals {target_to_heal.name} for {heal_amt}.[/light_green]")
            elif skill.effect_type == "GAIN_POISE_SPECIAL_4":
                self.apply_status_logic(attacker, StatusEffect("Poise", "[light_cyan1]༄[/light_cyan1]", 2, STATUS_DESCS["Poise"], duration=2))
            elif skill.effect_type == "BLACKWATER_NATSUME_TYPE1":
                if self.check_black_water_dock_req(attacker):
                    self.apply_status_logic(attacker, StatusEffect("Poise", "[light_cyan1]༄[/light_cyan1]", 3, STATUS_DESCS["Poise"], duration=2))

        # --- PREPARE MULTI-HIT LOGIC ---
        chips_to_execute = getattr(skill, "chips", [skill])

        for chip_idx, chip in enumerate(chips_to_execute):
            
            # FIZZLE MECHANIC: If target died on previous hit, abort remaining hits
            if target.hp <= 0:
                # if len(chips_to_execute) > 1 and chip_idx > 0:
                #     self.log(f"[dim]Remaining hits fizzled out...[/dim]")
                break 

            # Increment Chip Tracker
            attacker.chips_used_this_turn = getattr(attacker, "chips_used_this_turn", 0) + 1

            damage = 0
            is_crit = False

            # --- [STEP 2] DAMAGE CALCULATION (Per Chip) ---
            if chip.base_damage > 0:
                # 1. Base Damage & Variance
                base_dmg_val = float(chip.base_damage)
                base_dmg_val += attacker.temp_modifiers.get("outgoing_base_dmg_flat", 0)
                
                # --- S5 BASE PCT BONUS ---
                base_pct_bonus = attacker.temp_modifiers.get("outgoing_base_dmg_pct", 0)
                if base_pct_bonus > 0:
                    base_dmg_val *= (1.0 + base_pct_bonus)

                # --- OVERHEAT BASE DMG LOGIC ---
                atk_overheat = next((s for s in attacker.status_effects if s.name == "Overheat"), None)
                if atk_overheat: base_dmg_val *= 0.75
                tgt_overheat = next((s for s in target.status_effects if s.name == "Overheat"), None)
                if tgt_overheat: base_dmg_val *= 1.30
                
                if chip.effect_type == "HISAYUKI_SPECIAL_3":
                    haste = next((s for s in attacker.status_effects if s.name == "Haste"), None)
                    if haste:
                        bonus_pct = min(0.50, haste.duration * 0.10)
                        base_dmg_val *= (1.0 + bonus_pct)
                        attacker.status_effects.remove(haste)

                # Pierce Fragility BASE DAMAGE MANIPULATION
                pierce_eff = next((s for s in target.status_effects if s.name == "Pierce Fragility"), None)
                if pierce_eff:
                    p_count = min(5, pierce_eff.duration)
                    # Support checking description of either the parent skill or the chip
                    desc_to_check = getattr(chip, "description", "") or skill.description
                    if "Pierce Fragility" in desc_to_check:
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
                        if sadism_bind_to_apply > 0:
                            self.apply_status_logic(target, StatusEffect("Bind", "[gold1]⛓[/gold1]", 1, STATUS_DESCS["Bind"], duration=sadism_bind_to_apply))

                # RUPTURE FLAT BONUS
                if chip.effect_type == "RUPTURE_DAMAGE_BUFF_TYPE2":
                    if any(s.name in RUPTURE_LIST for s in target.status_effects):
                        base_dmg_val += chip.effect_val

                # --- NATSUME STRANGE KATA ---
                if chip.effect_type in ["NATSUME_STRANGE_SPECIAL_1", "NATSUME_STRANGE_SPECIAL_2", "NATSUME_STRANGE_SPECIAL_3", "NATSUME_STRANGE_SPECIAL_4"]:
                    base_dmg_val *= 0.20
                elif chip.effect_type in ["NATSUME_STRANGE_SPECIAL_5", "NATSUME_STRANGE_SPECIAL_6"]:
                    base_dmg_val *= 0.15

                if chip.effect_type == "NATSUME_STRANGE_SPECIAL_1":
                    self.apply_status_logic(attacker, StatusEffect("Poise", "[light_cyan1]༄[/light_cyan1]", 0, STATUS_DESCS["Poise"], duration=2))
                elif chip.effect_type == "NATSUME_STRANGE_SPECIAL_2":
                    self.apply_status_logic(attacker, StatusEffect("Poise", "[light_cyan1]༄[/light_cyan1]", 0, STATUS_DESCS["Poise"], duration=1))
                elif chip.effect_type == "NATSUME_STRANGE_SPECIAL_3":
                    self.apply_status_logic(attacker, StatusEffect("Bind", "[gold1]⛓[/gold1]", 1, STATUS_DESCS["Bind"], duration=1))
                elif chip.effect_type == "NATSUME_STRANGE_SPECIAL_5":
                    self.apply_status_logic(attacker, StatusEffect("Bind", "[gold1]⛓[/gold1]", 1, STATUS_DESCS["Bind"], duration=1))
                    self.apply_status_logic(attacker, StatusEffect("Poise", "[light_cyan1]༄[/light_cyan1]", 2, STATUS_DESCS["Poise"], duration=2))
                elif chip.effect_type == "NATSUME_STRANGE_SPECIAL_6":
                    self.apply_status_logic(attacker, StatusEffect("Poise", "[light_cyan1]༄[/light_cyan1]", 2, STATUS_DESCS["Poise"], duration=2))

                # --- COMMON ACT 4 ENEMIES ---
                if chip.effect_type == "PARALYSIS_SPECIAL_TYPE1":
                    para = next((s for s in target.status_effects if s.name == "Paralysis"), None)
                    if para:
                        bonus = min(15, 3 * para.duration)
                        base_dmg_val += bonus

                # --- ZHAO FENG ---
                if chip.effect_type == "ZHAOFENG_SPECIAL_3":
                    rup = next((s for s in target.status_effects if s.name in RUPTURE_LIST), None)
                    if rup and (rup.potency + rup.duration) >= 5: base_dmg_val *= 1.10
                elif chip.effect_type == "ZHAOFENG_SPECIAL_4":
                    blo = next((s for s in target.status_effects if s.name == "Blossom"), None)
                    mal = next((s for s in target.status_effects if s.name == "Malice"), None)
                    if ((blo.duration if blo else 0) + (mal.duration if mal else 0)) >= 5: base_dmg_val *= 1.10
                elif chip.effect_type == "ZHAOFENG_SPECIAL_5":
                    rup = next((s for s in target.status_effects if s.name in RUPTURE_LIST), None)
                    if rup and (rup.potency + rup.duration) >= 5: base_dmg_val *= 1.20
                active_tgt_passives = getattr(target, "passives", []) or (getattr(target.kata, "passives", []) if getattr(target, "kata", None) else [])
                if any(p.effect_type == "PASSIVE_CRUMBLING_FORM" for p in active_tgt_passives):
                    base_dmg_val *= 0.70

                # --- ACT 4 KATAS (FIRST HALF UPDATE) ---
                if chip.effect_type in ["BLACKWATER_NATSUME_TYPE4", "BLACKWATER_NATSUME_TYPE5", "BLACKWATER_NATSUME_TYPE6"]:
                    if self.check_black_water_dock_req(attacker):
                        base_dmg_val += 3

                # --- SOME BASIC PASSIVE LOOPS ---
                active_passives = getattr(attacker, "passives", [])
                if not active_passives and getattr(attacker, "kata", None):
                    active_passives = getattr(attacker.kata, "passives", [])
                # Crucial Passive Loop
                if active_passives:
                    for p in active_passives:
                        if p.effect_type == "PASSIVE_GOLDEN_FIST":
                            if any(s.name == "Bleed" for s in target.status_effects):
                                attacker.temp_modifiers["outgoing_dmg_flat"] = attacker.temp_modifiers.get("outgoing_dmg_flat", 0) + p.effect_val
                                self.log(f"[bold yellow][Passive][/bold yellow] {p.name} activated! (+{p.effect_val} Dmg)")
                        if p.effect_type == "PASSIVE_DOCK_SPEARPLAY":
                            if any(s.name == "Paralysis" for s in target.status_effects):
                                self.apply_status_logic(target, StatusEffect("Rupture", "[medium_spring_green]✧[/medium_spring_green]", 1, STATUS_DESCS["Rupture"], duration=0))
                                self.log(f"[bold yellow][Passive][/bold yellow] {p.name} activated! (+1 Rupture Potency)")
                        if p.effect_type == "PASSIVE_RUTHLESSNESS":
                            bonus_dmg = getattr(attacker, "chips_used_this_turn", 0)
                            if bonus_dmg > 0:
                                base_dmg_val += bonus_dmg
                                # Note: Logging this per chip can spam the log heavily. Can log if needed.
                        if p.effect_type == "PASSIVE_UNPREDICTABLE":
                            if not hasattr(attacker, "next_turn_modifiers"): attacker.next_turn_modifiers = {}
                            attacker.next_turn_modifiers["final_dmg_reduction"] = attacker.next_turn_modifiers.get("final_dmg_reduction", 0) + 1

                # --- THORN / OUTCAST BASE DAMAGE MODIFIERS ---
                active_atk_passives = getattr(attacker, "passives", []) or (getattr(attacker.kata, "passives", []) if getattr(attacker, "kata", None) else [])
                if any(p.effect_type == "PASSIVE_IBARA_THORN" for p in active_atk_passives):
                    if "Benikawa" in target.name or "Shigemura" in target.name: base_dmg_val *= 0.50
                    else: base_dmg_val *= 1.30
                
                active_tgt_passives = getattr(target, "passives", []) or (getattr(target.kata, "passives", []) if getattr(target, "kata", None) else [])
                if any(p.effect_type == "PASSIVE_IBARA_THORN" for p in active_tgt_passives):
                    if "Benikawa" in attacker.name or "Shigemura" in attacker.name: base_dmg_val *= 1.50

                # --- ISOLATE THE ENEMY DYNAMIC BASE DAMAGE ---
                if chip.effect_type == "ISOLATETHEENEMY_SPECIAL_TYPE1":
                    if any(s.name == "Bind" for s in target.status_effects): base_dmg_val += 3
                    if any(s.name == "Paralysis" for s in target.status_effects): base_dmg_val += 3
                elif chip.effect_type == "ISOLATETHEENEMY_SPECIAL_TYPE2":
                    if any(s.name == "Rupture" for s in target.status_effects): base_dmg_val += 2
                    if any(s.name == "Bind" for s in target.status_effects): base_dmg_val += 2
                    if any(s.name == "Paralysis" for s in target.status_effects): base_dmg_val += 2
                elif chip.effect_type == "ISOLATETHEENEMY_SPECIAL_TYPE3":
                    if any(s.name in RUPTURE_LIST for s in target.status_effects): base_dmg_val += 3
                active_tgt_passives = getattr(target, "passives", []) or (getattr(target.kata, "passives", []) if getattr(target, "kata", None) else [])
                if any(p.effect_type == "PASSIVE_FADING_FORM" for p in active_tgt_passives):
                    base_dmg_val *= 0.50

                # --- PASSIVE: CORNERED THORN & FLICKERING INVISIBILITY BASE DMG MODIFIERS ---
                active_atk_passives = getattr(attacker, "passives", []) or (getattr(attacker.kata, "passives", []) if getattr(attacker, "kata", None) else [])
                active_tgt_passives = getattr(target, "passives", []) or (getattr(target.kata, "passives", []) if getattr(target, "kata", None) else [])
                if any(p.effect_type == "PASSIVE_KAGEROU_THORN" for p in active_atk_passives):
                    if "Benikawa" in target.name or "Shigemura" in target.name: base_dmg_val *= 0.50
                    else: base_dmg_val *= 1.30
                if any(p.effect_type == "PASSIVE_KAGEROU_THORN" for p in active_tgt_passives):
                    is_beni_shige = "Benikawa" in attacker.name or "Shigemura" in attacker.name
                    if is_beni_shige: base_dmg_val *= 1.50
                    elif skill.element == 0 and getattr(target, "kagerou_eros_vuln", False):
                        base_dmg_val += 5
                        target.kagerou_eros_vuln = False
                if any(p.effect_type == "PASSIVE_KAGEROU_INVISIBILITY" for p in active_tgt_passives):
                    f_invis = next((s for s in target.status_effects if s.name == "Flickering Invisibility"), None)
                    if f_invis: base_dmg_val -= min(5, f_invis.duration)

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
                    self.apply_status_logic(attacker, StatusEffect("Poise", "[light_cyan1]༄[/light_cyan1]", 2, STATUS_DESCS["Poise"], duration=0))
                elif chip.effect_type == "BLACKWATER_NATSUME_TYPE4":
                    if self.check_black_water_dock_req(attacker):
                        self.apply_status_logic(attacker, StatusEffect("Poise", "[light_cyan1]༄[/light_cyan1]", 3, STATUS_DESCS["Poise"], duration=0))
                elif chip.effect_type == "BLACKWATER_NATSUME_TYPE5":
                    if self.check_black_water_dock_req(attacker):
                        self.apply_status_logic(attacker, StatusEffect("Poise", "[light_cyan1]༄[/light_cyan1]", 0, STATUS_DESCS["Poise"], duration=3))
                elif chip.effect_type == "LUOXIA_HANA_SPECIAL1":
                    team = self.allies if attacker in self.allies else self.enemies
                    for member in team:
                        if member.hp > 0:
                            name_check = member.kata.name if hasattr(member, "kata") and member.kata else member.name
                            if "Yunhai Region" in name_check:
                                member.temp_modifiers["outgoing_dmg_flat"] = member.temp_modifiers.get("outgoing_dmg_flat", 0) + 1

                # 5. Critical Hit Roll (POISE & ACCELERATION)
                poise_eff = next((se for se in attacker.status_effects if se.name == "Poise"), None)
                accel_eff = next((se for se in attacker.status_effects if se.name == "Acceleration"), None)
                
                poise_pot = 0
                if poise_eff and poise_eff.duration > 0: poise_pot += poise_eff.potency
                if accel_eff and accel_eff.duration > 0: poise_pot += accel_eff.potency

                cloud_sword_finisher_mult = 1.0
                if poise_pot > 0:
                    crit_chance = min(100, poise_pot * 5)
                    if atk_overheat: crit_chance = 0
                    
                    if random.randint(1, 100) <= crit_chance:
                        is_crit = True
                        dmg *= 1.2
                        
                        # --- WING CHUN CRIT TALLY ---
                        active_atk_passives = getattr(attacker, "passives", [])
                        if not active_atk_passives and getattr(attacker, "kata", None): 
                            active_atk_passives = getattr(attacker.kata, "passives", [])
                        if any(p.effect_type == "PASSIVE_WING_CHUN" for p in active_atk_passives):
                            attacker.crit_tally = getattr(attacker, "crit_tally", 0) + 1
                            tally = attacker.crit_tally
                            if tally in getattr(attacker, "appendable_skills", {}):
                                app_skill = copy.deepcopy(attacker.appendable_skills[tally])
                                insert_idx = random.randint(0, len(attacker.deck))
                                attacker.deck.insert(insert_idx, app_skill)
                                self.log(f"[bold grey74]Wing Chun appended '{app_skill.name}' to {attacker.name}'s deck![/bold grey74]")
                            if tally >= 7:
                                attacker.crit_tally = 0
                        # --- CLOUD SWORD [云] ---
                        cloud_sword = next((se for se in attacker.status_effects if se.name == "Cloud Sword [云]"), None)
                        if cloud_sword:
                            dmg = (dmg / 1.2) * 1.4  # Base crit is 1.2x. Cloud Sword grants +20% extra crit damage -> 1.4x
                            if skill.element == 3: #AGAPE
                                cloud_sword_finisher_mult = getattr(attacker, "cloud_sword_tally", 0) + 1
                                attacker.cloud_sword_tally = 0
                                attacker.status_effects.remove(cloud_sword)
                            else:
                                attacker.cloud_sword_tally = min(9, getattr(attacker, "cloud_sword_tally", 0) + 1)
                        # --- ENFORCEMENT PASSIVE ---
                        if any(p.effect_type == "PASSIVE_ENFORCEMENT" for p in active_atk_passives):
                            if getattr(attacker, "enforcement_activations", 0) < 4:
                                attacker.enforcement_tally = min(3, getattr(attacker, "enforcement_tally", 0) + 1)
                                tally = attacker.enforcement_tally
                                if random.choice([True, False]):
                                    attacker.next_turn_modifiers["outgoing_dmg_flat"] = attacker.next_turn_modifiers.get("outgoing_dmg_flat", 0) + tally
                                else:
                                    attacker.next_turn_modifiers["final_dmg_reduction"] = attacker.next_turn_modifiers.get("final_dmg_reduction", 0) + tally
                                attacker.enforcement_activations += 1
                        # --- APPLY_STATUS_CRITICAL HERE (IMPORTANT / COMMON) ---
                        if chip.effect_type == "APPLY_STATUS_CRITICAL" and hasattr(chip, "status_effect"):
                            self.apply_status_logic(target if chip.status_effect.type == "DEBUFF" else attacker, copy.deepcopy(chip.status_effect))

                        # --- MEI EFFECTS ---
                        elif chip.effect_type == "MEI_SPECIAL_1":
                            self.apply_status_logic(attacker, StatusEffect("Haste", "[yellow1]🢙[/yellow1]", 0, "", duration=1))
                            self.apply_status_logic(target, StatusEffect("Rupture", "[medium_spring_green]✧[/medium_spring_green]", 2, "", duration=2))
                        elif chip.effect_type == "MEI_SPECIAL_2":
                            self.apply_status_logic(attacker, StatusEffect("Haste", "[yellow1]🢙[/yellow1]", 0, "", duration=1))
                            self.apply_status_logic(target, StatusEffect("Paralysis", "[orange1]ϟ[/orange1]", 1, "", duration=3, type="DEBUFF"))
                        elif chip.effect_type == "MEI_SPECIAL_3":
                            self.apply_status_logic(target, StatusEffect("Rupture", "[medium_spring_green]✧[/medium_spring_green]", 2, "", duration=2))
                            self.apply_status_logic(target, StatusEffect("Paralysis", "[orange1]ϟ[/orange1]", 1, "", duration=3, type="DEBUFF"))
                        elif chip.effect_type == "MEI_SPECIAL_4":
                            self.apply_status_logic(attacker, StatusEffect("Poise", "[light_cyan1]༄[/light_cyan1]", 4, "", duration=4))
                            self.apply_status_logic(target, StatusEffect("Paralysis", "[orange1]ϟ[/orange1]", 1, "", duration=2, type="DEBUFF"))
                        elif chip.effect_type == "MEI_SPECIAL_5":
                            self.apply_status_logic(attacker, StatusEffect("Poise", "[light_cyan1]༄[/light_cyan1]", 8, "", duration=0))
                            self.apply_status_logic(target, StatusEffect("Paralysis", "[orange1]ϟ[/orange1]", 1, "", duration=3, type="DEBUFF"))
                        elif chip.effect_type == "IBARA_ACT4_SPECIAL3":
                            self.apply_status_logic(target, StatusEffect("Bleed", "[red]💧︎[/red]", 4, STATUS_DESCS["Bleed"], duration=4, type="DEBUFF"))
                            self.apply_status_logic(attacker, StatusEffect("Invisibility", "[purple4]⛆[/purple4]", 0, STATUS_DESCS["Invisibility"], duration=1, type="BUFF"))
                        # --- ACT 4 KATAS (FIRST HALF UPDATE) ---
                        elif chip.effect_type == "GAIN_POISE_SPECIAL_4":
                            self.apply_status_logic(attacker, StatusEffect("Poise", "[light_cyan1]༄[/light_cyan1]", 2, STATUS_DESCS["Poise"], duration=0))
                        elif chip.effect_type == "YUNHAI_YURI_SPECIAL1":
                            self.apply_status_logic(attacker, StatusEffect("Poise", "[light_cyan1]༄[/light_cyan1]", 3, STATUS_DESCS["Poise"], duration=0))
                        elif chip.effect_type == "YUNHAI_YURI_SPECIAL2":
                            team = self.allies if attacker in self.allies else self.enemies
                            for u in team:
                                if "Yunhai Association" in (u.kata.name if hasattr(u, "kata") and u.kata else u.name):
                                    u.temp_modifiers["outgoing_dmg_mult"] *= 1.10
                            self.apply_status_logic(target, StatusEffect("Paralysis", "[orange1]ϟ[/orange1]", 1, STATUS_DESCS["Paralysis"], duration=2, type="DEBUFF"))
                        elif chip.effect_type == "YUNHAI_YURI_SPECIAL3":
                            heal_amt = damage
                            team = self.allies if attacker in self.allies else self.enemies
                            for u in team:
                                if "Yunhai Association" in (u.kata.name if hasattr(u, "kata") and u.kata else u.name):
                                    u.hp = min(u.max_hp, u.hp + heal_amt)
                                    self.log(f"[light_green]-> {attacker.name} Heals {u.name} for {heal_amt}.[/light_green]")
                            self.apply_status_logic(target, StatusEffect("Paralysis", "[orange1]ϟ[/orange1]", 1, STATUS_DESCS["Paralysis"], duration=2, type="DEBUFF"))
                        
                        # Consume Poise Count (But not Acceleration count for crits)
                        if poise_eff and poise_eff.duration > 0:
                            poise_eff.duration -= 1
                            if poise_eff.duration <= 0: attacker.status_effects.remove(poise_eff)

                        # --- INTANGIBLE FORM BASE DAMAGE REDUCTION ---
                        active_tgt_passives = getattr(target, "passives", []) or (getattr(target.kata, "passives", []) if getattr(target, "kata", None) else [])
                        if any(p.effect_type == "PASSIVE_INTANGIBLE_FORM" for p in active_tgt_passives):
                            base_dmg_val *= 0.50

                        # Leaking Bloodlust Crit Modifier
                        lb_atk = next((s for s in attacker.status_effects if s.name == "Leaking Bloodlust"), None)
                        if lb_atk and lb_atk.duration >= 99: dmg *= 1.30
                        lb_tgt = next((s for s in target.status_effects if s.name == "Leaking Bloodlust"), None)
                        if lb_tgt and lb_tgt.duration >= 99: dmg *= 1.30
                        # Kagerou Skill III Crit effects
                        if chip.effect_type == "KAGEROU_SPECIAL_4" or chip.effect_type == "KAGEROU_SPECIAL_6":
                            self.apply_status_logic(target, StatusEffect("Bleed", "[red]💧︎[/red]", 6, STATUS_DESCS["Bleed"], duration=1, type="DEBUFF"))
                        if chip.effect_type == "KAGEROU_SPECIAL_5" or chip.effect_type == "KAGEROU_SPECIAL_6":
                            self.apply_status_logic(attacker, StatusEffect("Leaking Bloodlust", "[red3]✹[/red3]", 1, STATUS_DESCS["Leaking Bloodlust"], duration=6, type="BUFF"))

                # 6. Elemental & Global Multipliers (Uses PARENT skill element)
                res_mult = target.resistances[skill.element]
                nbd = dmg * res_mult
                nbd *= attacker.temp_modifiers.get("outgoing_dmg_mult", 1.0)
                nbd *= target.temp_modifiers.get("incoming_dmg_mult", 1.0)
                
                # 7. Flat Modifiers
                final_dmg = nbd + target.temp_modifiers.get("incoming_dmg_flat", 0)
                final_dmg += attacker.temp_modifiers.get("outgoing_dmg_flat", 0)
                final_dmg -= target.temp_modifiers["final_dmg_reduction"]

                # Acceleration Final Damage Reduction & Count Penalty
                tgt_accel = next((s for s in target.status_effects if s.name == "Acceleration"), None)
                if tgt_accel:
                    red_amount = random.randint(1, 3)
                    final_dmg -= red_amount  # Final damage is ALWAYS reduced
                    # Count reduction penalty (max 2 times per turn)
                    reductions_done = getattr(target, "accel_reductions_this_turn", 0)
                    if reductions_done < 2:
                        max_count_red = max(0, tgt_accel.duration - 1)
                        actual_count_red = min(red_amount, max_count_red)
                        if actual_count_red > 0:
                            tgt_accel.duration -= actual_count_red
                            target.accel_reductions_this_turn = reductions_done + 1
                            
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

                # INGRAINED COMMAND DAMAGE REDUCTION    
                active_tgt_passives = getattr(target, "passives", []) or (getattr(target.kata, "passives", []) if getattr(target, "kata", None) else [])
                if any(p.effect_type == "PASSIVE_INGRAINED_COMMAND" for p in active_tgt_passives):
                    if any(s.name == "Paralysis" for s in target.status_effects):
                        final_dmg *= 0.5
                
                # CLOUD SWORD FINISHER MULTIPLIER
                if cloud_sword_finisher_mult > 1.0:
                    self.log("[bold chartreuse1]Cloud Sword [云] Finisher unleashed![/bold chartreuse1]")
                    final_dmg *= cloud_sword_finisher_mult

                # DEFENSE TIER REDUCTION (Uses Parent skill tier)
                def_max_tier = self.get_avg_defense_tier(target)
                
                # --- PARALYSIS LOGIC ---
                # Debuffed unit (attacker) perceives the target's defense tier as lower, triggering the game's tier penalty system
                para_eff = next((s for s in attacker.status_effects if s.name == "Paralysis"), None)
                if para_eff:
                    def_max_tier -= 1
                    
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
                                self.apply_status_logic(a, StatusEffect("Haste", "[yellow1]🢙[/yellow1]", 0, STATUS_DESCS["Haste"], duration=3))
                        damage = 0
                    elif chip.effect_type == "JOKE_SKILL":
                        damage = 0

                # --- SKILL IV REFLECT / ZERO DAMAGE LOGIC ---
                if getattr(target, "reflect_invis_damage", False):
                    invis = next((s for s in target.status_effects if s.name == "Invisibility"), None)
                    invis_count = invis.duration if invis else 0
                    # Reflect is (Invisibility Count * 50%) * Damage
                    reflect_amt = int((invis_count * 0.50) * damage)
                    if reflect_amt > 0:
                        attacker.hp -= reflect_amt
                        self.log(f"[purple4]Shadows reflect {reflect_amt} damage back to {attacker.name}![/purple4]")
                    damage = 0

                # --- LEAKING BLOODLUST FLAT DAMAGE ---
                lb_atk = next((s for s in attacker.status_effects if s.name == "Leaking Bloodlust"), None)
                if lb_atk: damage += min(5, lb_atk.duration // 11)
                lb_tgt = next((s for s in target.status_effects if s.name == "Leaking Bloodlust"), None)
                if lb_tgt: damage += min(5, lb_tgt.duration // 11)

                # --- APPLY DAMAGE ---
                if damage > 0:
                    target.hp -= damage
                    el_color = get_element_color(skill.element)
                    eff_text = " [bold yellow](WEAK!)[/]" if res_mult > 1.0 else (" [dim](Resist)[/]" if res_mult < 1.0 else "")
                    crit_text = "[khaki1]Critical![/] " if is_crit else ""
                    
                    self.log(f"-> {crit_text}Hit {target.name} for [bold {el_color}]{damage}[/bold {el_color}]!{eff_text}")
                    
                    # SKILL NAMED "COUNTER" TRIGGER
                    if getattr(target, "counter_active", False):
                        if not hasattr(target, "next_turn_modifiers"): target.next_turn_modifiers = {}
                        current_mult = target.next_turn_modifiers.get("outgoing_dmg_mult", 1.0)
                        target.next_turn_modifiers["outgoing_dmg_mult"] = current_mult + target.counter_potency
                        target.counter_active = False 
                    
                    # ON HIT POISE
                    if chip.effect_type == "GAIN_POISE_SPECIAL_1":
                        self.apply_status_logic(attacker, StatusEffect("Poise", "[light_cyan1]༄[/light_cyan1]", 4, STATUS_DESCS["Poise"], duration=0))
                    
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
                            # --- INTANGIBLE FORM BLEED MULTIPLIER ---
                            active_atk_passives_bleed = getattr(attacker, "passives", []) or (getattr(attacker.kata, "passives", []) if getattr(attacker, "kata", None) else [])
                            if any(p.effect_type == "PASSIVE_INTANGIBLE_FORM" for p in active_atk_passives_bleed):
                                recoil *= 2
                            if any(p.effect_type == "PASSIVE_FADING_FORM" for p in active_atk_passives_bleed):
                                recoil *= 3
                            if any(p.effect_type == "PASSIVE_CRUMBLING_FORM" for p in active_atk_passives_bleed):
                                recoil *= 1.5
                            if lb_tgt: recoil *= min(3.0, 1.0 + (lb_tgt.duration // 33)) # Bleed Multiplier Math
                            recoil = int(recoil)
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
                            haste_eff = StatusEffect("Haste", "[yellow1]🢙[/yellow1]", 0, STATUS_DESCS["Haste"], duration=1, type="BUFF")
                            self.apply_status_logic(target, haste_eff)
                            self.log(f"[yellow1]{target.name} gained Haste from Riposte![/yellow1]")
                        if riposte_eff.duration <= 0: target.status_effects.remove(riposte_eff)

                    # RUPTURE & FAIRYLIGHT TRIGGERS (DO NOT USE RUPTURE_LIST)
                    active_tgt_passives_rup = getattr(target, "passives", []) or (getattr(target.kata, "passives", []) if getattr(target, "kata", None) else [])
                    zhao_present = any(e.name == "Zhao Feng" and e.hp > 0 for e in self.enemies)
                    rupture_eff = next((s for s in target.status_effects if s.name == "Rupture"), None)
                    if rupture_eff:
                        if zhao_present and target in self.allies:
                            #self.log(f"[dim]Zhao Feng's aura nullifies {target.name}'s Rupture damage and decay![/dim]")
                            dmg_to_take = 0
                        else:
                            dmg_to_take = rupture_eff.potency
                            if any(p.effect_type == "PASSIVE_INTANGIBLE_FORM" for p in active_tgt_passives_rup): dmg_to_take *= 2
                            if any(p.effect_type == "PASSIVE_FADING_FORM" for p in active_tgt_passives): dmg_to_take *= 3
                            if any(p.effect_type == "PASSIVE_CRUMBLING_FORM" for p in active_tgt_passives): dmg_to_take *= 1.5
                            if not zhao_present:
                                dmg_to_take = int(dmg_to_take)
                            target.hp -= dmg_to_take
                            rupture_eff.duration -= 1
                            self.log(f"[medium_spring_green]Rupture dealt {dmg_to_take} damage to {target.name}![/medium_spring_green]")
                            if rupture_eff.duration <= 0: target.status_effects.remove(rupture_eff)
                        
                    fairylight_eff = next((s for s in target.status_effects if s.name == "Fairylight"), None)
                    if fairylight_eff:
                        if zhao_present and target in self.allies:
                            #self.log(f"[dim]Zhao Feng's aura nullifies {target.name}'s Fairylight damage and decay![/dim]")
                            dmg_to_take = 0
                        else:
                            dmg_to_take = fairylight_eff.potency
                            if any(p.effect_type == "PASSIVE_INTANGIBLE_FORM" for p in active_tgt_passives_rup): dmg_to_take *= 2
                            if any(p.effect_type == "PASSIVE_FADING_FORM" for p in active_tgt_passives): dmg_to_take *= 3
                            if any(p.effect_type == "PASSIVE_CRUMBLING_FORM" for p in active_tgt_passives): dmg_to_take *= 1.5
                            if not zhao_present:
                                dmg_to_take = int(dmg_to_take)
                            target.hp -= dmg_to_take
                            self.log(f"[spring_green1]Fairylight dealt {fairylight_eff.potency} damage to {target.name}![/spring_green1]")
                            if fairylight_eff.duration <= 0: target.status_effects.remove(fairylight_eff)

                    # PIERCE FRAGILITY TRIGGER
                    pierce_target_eff = next((s for s in target.status_effects if s.name == "Pierce Fragility"), None)
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
                            poise_effect = next((e for e in member.status_effects if e.name in POISE_LIST), None)
                            if poise_effect: poise_effect.duration = min(99, poise_effect.duration + chip.effect_val)
                    elif chip.effect_type == "ON_HIT_PROVIDE_POISE_TYPE2":
                        team = self.allies if attacker in self.allies else self.enemies
                        for member in team:
                            poise_effect = next((e for e in member.status_effects if e.name in POISE_LIST), None)
                            if poise_effect:
                                poise_effect.potency = min(99, poise_effect.potency + chip.effect_val)
                                poise_effect.duration = min(99, poise_effect.duration + chip.effect_val)
                    elif chip.effect_type == "ON_HIT_PROVIDE_POISE_TYPE3":
                        team = self.allies if attacker in self.allies else self.enemies
                        for member in team:
                            poise_effect = next((e for e in member.status_effects if e.name in POISE_LIST), None)
                            if poise_effect: poise_effect.potency = min(99, poise_effect.potency + chip.effect_val)
                    elif chip.effect_type == "ON_HIT_PROVIDE_POISE_TYPE4":
                        team = self.allies if attacker in self.allies else self.enemies
                        for member in team:
                            poise_effect = next((e for e in member.status_effects if e.name in POISE_LIST), None)
                            if poise_effect: poise_effect.duration = min(99, poise_effect.duration + chip.effect_val)
                            else: self.apply_status_logic(member, StatusEffect("Poise", "[light_cyan1]༄[/light_cyan1]", chip.effect_val, STATUS_DESCS["Poise"], duration=0))
                    elif chip.effect_type == "ON_HIT_CONVERT_POISE_TYPE1":
                        team = self.allies if attacker in self.allies else self.enemies
                        for member in team:
                            poise_effect = next((e for e in member.status_effects if e.name in POISE_LIST), None)
                            if poise_effect and poise_effect.potency >= 2:
                                poise_effect.potency -= 1
                                poise_effect.duration = min(99, poise_effect.duration + 1)
                                if poise_effect.potency <= 0 or poise_effect.duration <= 0: member.status_effects.remove(poise_effect)
                    elif chip.effect_type == "ON_HIT_CONVERT_POISE_TYPE2":
                        team = self.allies if attacker in self.allies else self.enemies
                        for member in team:
                            poise_effect = next((e for e in member.status_effects if e.name in POISE_LIST), None)
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

                    # --- RETURNING CURRENT PASSIVE ---
                    active_target_passives = getattr(target, "passives", [])
                    if not active_target_passives and getattr(target, "kata", None): 
                        active_target_passives = getattr(target.kata, "passives", [])
                        
                    for p in active_target_passives:
                        if p.effect_type == "PASSIVE_RETURNING_CURRENT":
                            if any(s.name == "Paralysis" for s in attacker.status_effects):
                                self.apply_status_logic(attacker, StatusEffect("Rupture", "[medium_spring_green]✧[/medium_spring_green]", 1, STATUS_DESCS["Rupture"], duration=2))
                                #self.log(f"[bold yellow][Passive][/bold yellow] {p.name} triggered! (+2 Rupture Count to {attacker.name})")

                    # --- FIRST TO TAKE DAMAGE TRIGGERS (PASSIVE_FRONTLINE_FIGHTER), (PASSIVE_BLIND_SPOTS)---
                    if target in self.allies and getattr(self, "first_ally_to_take_damage", None) is None:
                        self.first_ally_to_take_damage = target
                        active_tgt_p = getattr(target, "passives", []) or (getattr(target.kata, "passives", []) if getattr(target, "kata", None) else [])
                        if any(p.effect_type == "PASSIVE_FRONTLINE_FIGHTER" for p in active_tgt_p):
                            target.temp_modifiers["outgoing_dmg_flat"] = target.temp_modifiers.get("outgoing_dmg_flat", 0) + 5
                            self.log(f"[bold red][Passive][/bold red] Frontline Fighter activated! {target.name} deals +5 Final Damage this turn!")
                        if any(p.effect_type == "PASSIVE_BLIND_SPOTS" for p in active_tgt_p):
                            if not hasattr(target, "next_turn_modifiers"): target.next_turn_modifiers = {}
                            target.next_turn_modifiers["final_dmg_reduction"] = target.next_turn_modifiers.get("final_dmg_reduction", 0) + 5
                            self.log(f"[bold green][Passive][/bold green] Blind Spots activated! {target.name} takes -5 Final Damage next turn!")
                    elif target in self.enemies and getattr(self, "first_enemy_to_take_damage", None) is None:
                        self.first_enemy_to_take_damage = target
                        active_tgt_p = getattr(target, "passives", []) or (getattr(target.kata, "passives", []) if getattr(target, "kata", None) else [])
                        if any(p.effect_type == "PASSIVE_FRONTLINE_FIGHTER" for p in active_tgt_p):
                            target.temp_modifiers["outgoing_dmg_flat"] = target.temp_modifiers.get("outgoing_dmg_flat", 0) + 5
                            self.log(f"[bold red][Passive][/bold red] Frontline Fighter activated! {target.name} deals +5 Final Damage this turn!")
                        if any(p.effect_type == "PASSIVE_BLIND_SPOTS" for p in active_tgt_p):
                            if not hasattr(target, "next_turn_modifiers"): target.next_turn_modifiers = {}
                            target.next_turn_modifiers["final_dmg_reduction"] = target.next_turn_modifiers.get("final_dmg_reduction", 0) + 5
                            self.log(f"[bold green][Passive][/bold green] Blind Spots activated! {target.name} takes -5 Final Damage next turn!")

                    # --- IBARA NINJA HIT LOGIC & 500 HP CUTOFF ---
                    active_tgt_passives = getattr(target, "passives", []) or (getattr(target.kata, "passives", []) if getattr(target, "kata", None) else [])
                    
                    if any(p.effect_type == "PASSIVE_IBARA_INVISIBILITY" for p in active_tgt_passives):
                        if "Benikawa" in attacker.name or "Shigemura" in attacker.name:
                            if getattr(target, "invis_loss_guaranteed", False) or random.randint(1, 100) <= 50:
                                target.invis_loss_guaranteed = False
                                invis = next((s for s in target.status_effects if s.name == "Invisibility"), None)
                                if invis:
                                    invis.duration -= 1
                                    #self.log(f"[purple4]{target.name} lost 1 Invisibility from the strike![/purple4]")
                                    if invis.duration <= 0:
                                        target.status_effects.remove(invis)
                                        self.apply_status_logic(target, StatusEffect("Bind", "[gold1]⛓[/gold1]", 1, STATUS_DESCS["Bind"], duration=5))
                                        self.apply_status_logic(target, StatusEffect("Invisibility", "[purple4]⛆[/purple4]", 0, STATUS_DESCS["Invisibility"], duration=4, type="BUFF"))
                                        #self.log(f"[bold gold1]Invisibility broken! {target.name} is severely Bound![/bold gold1]")
                            else:
                                target.invis_loss_guaranteed = True
                                #self.log(f"[dim purple4]The strike grazed {target.name}'s shadows... next hit will break them![/dim purple4]")
                        else:
                            self.apply_status_logic(attacker, StatusEffect("Rupture", "[medium_spring_green]✧[/medium_spring_green]", 4, STATUS_DESCS["Rupture"], duration=1))
                            #self.log(f"[medium_spring_green]Striking the shadows ruptured {attacker.name}![/medium_spring_green]")

                    if any(p.effect_type == "PASSIVE_IBARA_THORN" for p in active_tgt_passives):
                        if target.hp <= 500:
                            # UPDATED: Only ends battle if Invisibility is completely broken
                            has_invis = any(s.name == "Invisibility" for s in target.status_effects)
                            if not has_invis:
                                self.log(f"[purple4]{target.name}'s shadows shatter completely! Battle over![/purple4]")
                                time.sleep(3.00)
                                self.won = True
                                self.is_battle_over = True
                                return

                    # --- ATTACKER ORDER TRACKER ---
                    order_list = self.ally_attacker_order if attacker in self.allies else self.enemy_attacker_order
                    if attacker not in order_list:
                        order_list.append(attacker)
                    order = order_list.index(attacker) + 1

                    # --- FADING FORM REDUCTION TRIGGER ---
                    if any(p.effect_type == "PASSIVE_FADING_FORM" for p in active_tgt_passives):
                        if skill.element not in [0, 3]: # Not Eros or Agape
                            stacks = getattr(target, "fading_form_stacks_this_turn", 0)
                            if stacks < 3:
                                target.fading_form_stacks_this_turn = stacks + 1
                                if not hasattr(target, "next_turn_modifiers"): target.next_turn_modifiers = {}
                                target.next_turn_modifiers["final_dmg_reduction"] = target.next_turn_modifiers.get("final_dmg_reduction", 0) + 1
                    # --- BROTHERHOOD / CAMARADERIE TRIGGER ---
                    if target in self.enemies and "Ten Thousand Blossom Brotherhood" in target.name and attacker in self.allies:  
                        # Brotherhood: Up to 3 distinct allied units per turn
                        if attacker not in getattr(self, "brotherhood_triggered_allies", []) and len(getattr(self, "brotherhood_triggered_allies", [])) < 3:
                            if not hasattr(self, "brotherhood_triggered_allies"): self.brotherhood_triggered_allies = []
                            self.brotherhood_triggered_allies.append(attacker)
                            pot = max(0, 6 - order)
                            if pot > 0:
                                self.apply_status_logic(attacker, StatusEffect("Rupture", "[medium_spring_green]✧[/medium_spring_green]", pot, STATUS_DESCS["Rupture"], duration=1))
                                self.log(f"[hot_pink][Passive][/hot_pink] Nostalgia Of A Brotherhood inflicted {pot} Rupture on {attacker.name}!")
                        # Camaraderie: Up to 3 damage instances (hits) per turn
                        defenders = [e for e in self.enemies if e.hp > 0 and "Defender" in e.name and any(p.effect_type == "PASSIVE_CAMARADERIE" for p in (getattr(e, "passives", []) or (getattr(e.kata, "passives", []) if getattr(e, "kata", None) else [])))]
                        if defenders:
                            if getattr(self, "camaraderie_trigger_count", 0) < 3:
                                self.camaraderie_trigger_count = getattr(self, "camaraderie_trigger_count", 0) + 1
                                heal_amt = max(0, 6 - order)
                                if heal_amt > 0 and "Defender" not in target.name:
                                    target.hp = min(target.max_hp, target.hp + heal_amt)
                                    self.log(f"[hot_pink][Passive][/hot_pink] Nostalgia Of A Camaraderie healed {target.name} for {heal_amt} HP!")

                    blo = next((s for s in target.status_effects if s.name == "Blossom"), None)
                    if blo:
                        gain = int(blo.duration / 3)
                        if gain > 0:
                            self.apply_status_logic(target, StatusEffect("Rupture", "[medium_spring_green]✧[/medium_spring_green]", gain, STATUS_DESCS["Rupture"], duration=1))
                            target.hp -= min(5, gain)
                            self.log(f"[hot_pink]Blossom blooms! {target.name} gains {gain} Rupture Potency and takes damage![/hot_pink]")
                        blo.duration -= 1
                        if blo.duration <= 0: target.status_effects.remove(blo)
                        
                    mal = next((s for s in target.status_effects if s.name == "Malice"), None)
                    if mal:
                        gain = int(mal.duration / 3)
                        if gain > 0:
                            self.apply_status_logic(target, StatusEffect("Sinking", "[blue3]♆[/blue3]", gain, STATUS_DESCS["Sinking"], duration=1, type="DEBUFF"))
                            target.hp -= min(5, gain)
                            self.log(f"[hot_pink]Malice festers! {target.name} gains {gain} Sinking Potency and takes damage![/hot_pink]")
                        mal.duration -= 1
                        if mal.duration <= 0: target.status_effects.remove(mal)

                    # --- HEAT HAZE REFLECT ---
                    if getattr(target, "reflect_flickering_damage", False):
                        f_invis = next((s for s in target.status_effects if s.name == "Flickering Invisibility"), None)
                        if f_invis:
                            reflect_pct = min(3.75, f_invis.duration * 0.75)
                            reflect_amt = int(damage * reflect_pct)
                            if reflect_amt > 0:
                                attacker.hp -= reflect_amt
                                self.log(f"[violet]Heat Haze reflects {reflect_amt} damage back to {attacker.name}![/violet]")
                    # --- KAGEROU HIT LOGIC & STATE MACHINE ---
                    if any(p.effect_type == "PASSIVE_KAGEROU_THORN" for p in active_tgt_passives):
                        is_beni_shige = "Benikawa" in attacker.name or "Shigemura" in attacker.name
                        # Cornered Thorn trigger
                        if is_beni_shige: target.kagerou_eros_vuln = True
                        # Flickering Invis State Machine
                        if is_beni_shige:
                            if getattr(target, "kagerou_invis_guaranteed", False):
                                f_invis = next((s for s in target.status_effects if s.name == "Flickering Invisibility"), None)
                                if f_invis:
                                    f_invis.duration -= 1
                                    self.log(f"[violet]{target.name} lost 1 Flickering Invisibility from the guaranteed break![/violet]")
                                    if f_invis.duration <= 0: target.status_effects.remove(f_invis)
                                target.kagerou_invis_guaranteed = False
                            else:
                                target.kagerou_invis_primed = True
                                self.log(f"[dim violet]{target.name}'s shadows are destabilized by {attacker.name}'s strike...[/dim violet]")
                        else:
                            # Not Beni/Shige
                            if getattr(target, "kagerou_invis_guaranteed", False):
                                f_invis = next((s for s in target.status_effects if s.name == "Flickering Invisibility"), None)
                                if f_invis:
                                    f_invis.duration -= 1
                                    self.log(f"[violet]{target.name} lost 1 Flickering Invisibility from the tag-team strike![/violet]")
                                    if f_invis.duration <= 0: target.status_effects.remove(f_invis)
                                target.kagerou_invis_guaranteed = False
                            elif getattr(target, "kagerou_invis_primed", False):
                                target.kagerou_invis_primed = False
                                if random.randint(1, 100) <= 50:
                                    f_invis = next((s for s in target.status_effects if s.name == "Flickering Invisibility"), None)
                                    if f_invis:
                                        f_invis.duration -= 1
                                        self.log(f"[violet]The tag-team succeeds! {target.name} lost 1 Flickering Invisibility![/violet]")
                                        if f_invis.duration <= 0: target.status_effects.remove(f_invis)
                                else:
                                    target.kagerou_invis_guaranteed = True
                                    self.log(f"[dim violet]The tag-team barely missed the shadows... the next hit is guaranteed to break them![/dim violet]")
                            # Flickering Rupture Reflect
                            if not getattr(self, "current_skill_flickering_rupture_applied", False):
                                f_invis = next((s for s in target.status_effects if s.name == "Flickering Invisibility"), None)
                                if f_invis:
                                    rup = min(5, f_invis.duration)
                                    self.apply_status_logic(attacker, StatusEffect("Rupture", "[medium_spring_green]✧[/medium_spring_green]", rup, STATUS_DESCS["Rupture"], duration=1))
                                    self.current_skill_flickering_rupture_applied = True
                                    self.log(f"[medium_spring_green]Striking the flickering shadows ruptured {attacker.name}![/medium_spring_green]")
                        # Invisibility Break Trigger
                        f_invis = next((s for s in target.status_effects if s.name == "Flickering Invisibility"), None)
                        if not f_invis:
                            self.apply_status_logic(target, StatusEffect("Bind", "[gold1]⛓[/gold1]", 1, STATUS_DESCS["Bind"], duration=5))
                            self.apply_status_logic(target, StatusEffect("Leaking Bloodlust", "[red3]✹[/red3]", 1, STATUS_DESCS["Leaking Bloodlust"], duration=30, type="BUFF"))
                            self.apply_status_logic(target, StatusEffect("Flickering Invisibility", "[thistle3]⛆[/thistle3]", 1, STATUS_DESCS["Flickering Invisibility"], duration=5, type="BUFF"))
                            self.log(f"[bold red3]Invisibility broken! {target.name} leaks bloodlust![/bold red3]")

                    # --- ACT 4 KATAS (FIRST HALF UPDATE) ---
                    if chip.effect_type == "YUNHAI_AKASUKE_SPECIAL1":
                        team = self.allies if attacker in self.allies else self.enemies
                        valid = [u for u in team if u.hp > 0 and u != attacker]
                        yh = [u for u in valid if "Yunhai Association" in (u.kata.name if hasattr(u, "kata") and u.kata else u.name)]
                        others = [u for u in valid if u not in yh]
                        for a in (yh + others)[:2]:
                            self.apply_status_logic(a, StatusEffect("Poise", "[light_cyan1]༄[/light_cyan1]", 0, STATUS_DESCS["Poise"], duration=2))
                    elif chip.effect_type == "YUNHAI_AKASUKE_SPECIAL2":
                        self.apply_status_logic(target, StatusEffect("Rupture", "[medium_spring_green]✧[/medium_spring_green]", 2, STATUS_DESCS["Rupture"], duration=2))
                        team = self.allies if attacker in self.allies else self.enemies
                        valid = [u for u in team if u.hp > 0 and u != attacker]
                        yh = [u for u in valid if "Yunhai Association" in (u.kata.name if hasattr(u, "kata") and u.kata else u.name)]
                        others = [u for u in valid if u not in yh]
                        for a in (yh + others)[:2]:
                            self.apply_status_logic(a, StatusEffect("Poise", "[light_cyan1]༄[/light_cyan1]", 3, STATUS_DESCS["Poise"], duration=0))
                    elif chip.effect_type == "YUNHAI_NAGANOHARA_SPECIAL1":
                        team = self.allies if attacker in self.allies else self.enemies
                        for member in team:
                            if member.hp > 0:
                                name_check = member.kata.name if hasattr(member, "kata") and member.kata else member.name
                                if "Yunhai Association" in name_check:
                                    member.temp_modifiers["outgoing_dmg_flat"] = member.temp_modifiers.get("outgoing_dmg_flat", 0) + 2
                        self.apply_status_logic(target, StatusEffect("Rupture", "[medium_spring_green]✧[/medium_spring_green]", 2, STATUS_DESCS["Rupture"], duration=1))
                    elif chip.effect_type == "LUOXIA_KAGAKU_SPECIAL2":
                        self.apply_status_logic(target, StatusEffect("Rupture", "[medium_spring_green]✧[/medium_spring_green]", 3, STATUS_DESCS["Rupture"], duration=0))
                        attacker.hp = min(attacker.max_hp, attacker.hp + damage)
                        self.log(f"[light_green]-> {attacker.name} Heals self for {damage}.[/light_green]")
                        team = self.allies if attacker in self.allies else self.enemies
                        valid = [u for u in team if u.hp > 0 and u != attacker]
                        if valid:
                            yh = [u for u in valid if "Yunhai Region" in (u.kata.name if hasattr(u, "kata") and u.kata else u.name)]
                            others = [u for u in valid if u not in yh]
                            target_to_heal = (sorted(yh, key=lambda x: x.hp/x.max_hp) + sorted(others, key=lambda x: x.hp/x.max_hp))[0]
                            target_to_heal.hp = min(target_to_heal.max_hp, target_to_heal.hp + damage)
                            self.log(f"[light_green]-> {attacker.name} Heals {target_to_heal.name} for {damage}.[/light_green]")
                    elif chip.effect_type == "LUOXIA_KAGAKU_SPECIAL3":
                        self.apply_status_logic(target, StatusEffect("Rupture", "[medium_spring_green]✧[/medium_spring_green]", 0, STATUS_DESCS["Rupture"], duration=2))
                        attacker.hp = min(attacker.max_hp, attacker.hp + damage)
                        self.log(f"[light_green]-> {attacker.name} Heals self for {damage}.[/light_green]")
                        team = self.allies if attacker in self.allies else self.enemies
                        valid = [u for u in team if u.hp > 0 and u != attacker]
                        if valid:
                            yh = [u for u in valid if "Yunhai Region" in (u.kata.name if hasattr(u, "kata") and u.kata else u.name)]
                            others = [u for u in valid if u not in yh]
                            target_to_heal = (sorted(yh, key=lambda x: x.hp/x.max_hp) + sorted(others, key=lambda x: x.hp/x.max_hp))[0]
                            target_to_heal.hp = min(target_to_heal.max_hp, target_to_heal.hp + damage)
                            self.log(f"[light_green]-> {attacker.name} Heals {target_to_heal.name} for {damage}.[/light_green]")
                    elif chip.effect_type == "LUOXIA_HEAL_TYPE1":
                        team = self.allies if attacker in self.allies else self.enemies
                        valid = [u for u in team if u.hp > 0]
                        if valid:
                            yh = [u for u in valid if "Yunhai Region" in (u.kata.name if hasattr(u, "kata") and u.kata else u.name)]
                            others = [u for u in valid if u not in yh]
                            target_to_heal = (yh + others)[0]
                            target_to_heal.hp = min(target_to_heal.max_hp, target_to_heal.hp + damage)
                            self.log(f"[light_green]-> {attacker.name} Heals {target_to_heal.name} for {damage}.[/light_green]")
                    elif chip.effect_type == "LUOXIA_HEAL_TYPE2":
                        if any(s.name in RUPTURE_LIST for s in target.status_effects):
                            team = self.allies if attacker in self.allies else self.enemies
                            valid = [u for u in team if u.hp > 0]
                            if valid:
                                yh = [u for u in valid if "Yunhai Region" in (u.kata.name if hasattr(u, "kata") and u.kata else u.name)]
                                others = [u for u in valid if u not in yh]
                                target_to_heal = (yh + others)[0]
                                target_to_heal.hp = min(target_to_heal.max_hp, target_to_heal.hp + damage)
                                self.log(f"[light_green]-> {attacker.name} Heals {target_to_heal.name} for {damage}.[/light_green]")
                    elif chip.effect_type == "LUOXIA_HANA_SPECIAL1":
                        if any(s.name in POISE_LIST for s in attacker.status_effects):
                            self.apply_status_logic(target, StatusEffect("Rupture", "[medium_spring_green]✧[/medium_spring_green]", 0, STATUS_DESCS["Rupture"], duration=2))
                    elif chip.effect_type == "LUOXIA_HANA_SPECIAL2":
                        self.apply_status_logic(target, StatusEffect("Rupture", "[medium_spring_green]✧[/medium_spring_green]", 3, STATUS_DESCS["Rupture"], duration=0))
                        if not hasattr(target, "next_turn_modifiers"): target.next_turn_modifiers = {}
                        target.temp_modifiers["outgoing_dmg_mult"] *= 0.90
                    elif chip.effect_type == "BLACKWATER_SHIGEMURA_TYPE1":
                        self.apply_status_logic(attacker, StatusEffect("Poise", "[light_cyan1]༄[/light_cyan1]", 4, STATUS_DESCS["Poise"], duration=0))
                        attacker.temp_modifiers["incoming_dmg_mult"] *= 0.80
                        team = self.allies if attacker in self.allies else self.enemies
                        valid = [u for u in team if u.hp > 0 and u != attacker]
                        if valid:
                            bwd = [u for u in valid if "Black Water Dock" in (u.kata.name if hasattr(u, "kata") and u.kata else u.name)]
                            others = [u for u in valid if u not in bwd]
                            pool = bwd + others
                            a = pool[0]
                            a.temp_modifiers["incoming_dmg_mult"] *= 0.80
                    elif chip.effect_type == "BLACKWATER_SHIGEMURA_TYPE2":
                        self.apply_status_logic(target, StatusEffect("Paralysis", "[orange1]ϟ[/orange1]", 1, STATUS_DESCS["Paralysis"], duration=2, type="DEBUFF"))
                    elif chip.effect_type == "BLACKWATER_NATSUME_TYPE1":
                        if self.check_black_water_dock_req(attacker):
                            team = self.allies if attacker in self.allies else self.enemies
                            for u in team:
                                if "Black Water Dock" in (u.kata.name if hasattr(u, "kata") and u.kata else u.name):
                                    if not hasattr(u, "next_turn_modifiers"): u.next_turn_modifiers = {}
                                    u.next_turn_modifiers["final_dmg_reduction"] = u.next_turn_modifiers.get("final_dmg_reduction", 0) + 2
                    elif chip.effect_type == "BLACKWATER_NATSUME_TYPE2":
                        if self.check_black_water_dock_req(attacker):
                            self.apply_status_logic(target, StatusEffect("Rupture", "[medium_spring_green]✧[/medium_spring_green]", 3, STATUS_DESCS["Rupture"], duration=3))
                    elif chip.effect_type == "BLACKWATER_NATSUME_TYPE3":
                        if self.check_black_water_dock_req(attacker):
                            self.apply_status_logic(target, StatusEffect("Paralysis", "[orange1]ϟ[/orange1]", 1, STATUS_DESCS["Paralysis"], duration=2, type="DEBUFF"))
                            team = self.allies if attacker in self.allies else self.enemies
                            for u in team:
                                if "Black Water Dock" in (u.kata.name if hasattr(u, "kata") and u.kata else u.name):
                                    u.temp_modifiers["incoming_dmg_mult"] *= 0.90
                    elif chip.effect_type in ["BLACKWATER_NATSUME_TYPE4", "YUNHAI_YURI_SPECIAL2", "YUNHAI_YURI_SPECIAL3"]:
                        if chip.effect_type == "BLACKWATER_NATSUME_TYPE4" and self.check_black_water_dock_req(attacker):
                            self.apply_status_logic(target, StatusEffect("Paralysis", "[orange1]ϟ[/orange1]", 1, STATUS_DESCS["Paralysis"], duration=1, type="DEBUFF"))
                        team = self.enemies if target in self.enemies else self.allies
                        living = [u for u in team if u.hp > 0 and u != target]
                        if living:
                            target = random.choice(living)
                            self.log(f"[bold magenta]-> {attacker.name} switches focus to {target.name}![/bold magenta]")
                    elif chip.effect_type == "BLACKWATER_NATSUME_TYPE5":
                        if self.check_black_water_dock_req(attacker):
                            self.apply_status_logic(target, StatusEffect("Paralysis", "[orange1]ϟ[/orange1]", 1, STATUS_DESCS["Paralysis"], duration=1, type="DEBUFF"))
                    elif chip.effect_type == "BLACKWATER_NATSUME_TYPE6":
                        if self.check_black_water_dock_req(attacker):
                            self.apply_status_logic(target, StatusEffect("Paralysis", "[orange1]ϟ[/orange1]", 1, STATUS_DESCS["Paralysis"], duration=2, type="DEBUFF"))
                    elif chip.effect_type == "YUNHAI_YURI_SPECIAL1":
                        self.apply_status_logic(attacker, StatusEffect("Poise", "[light_cyan1]༄[/light_cyan1]", 3, STATUS_DESCS["Poise"], duration=0))

                    # PUT YOUR [On Hit] CHECK LOGICS ABOVE THIS
                    # NEXT HIT BONUSES
                    if chip.effect_type == "ON_HIT_NEXT_TAKEN_FLAT": target.next_hit_taken_flat_bonus += chip.effect_val
                    if chip.effect_type == "ON_HIT_NEXT_DEAL_FLAT": attacker.next_hit_deal_flat_bonus += chip.effect_val
                    if chip.effect_type == "SELF_NEXT_TAKEN_FLAT": attacker.next_hit_taken_flat_bonus += chip.effect_val
                    if chip.effect_type == "DEBUFF_INCOMING_DMG_FLAT": target.temp_modifiers["incoming_dmg_flat"] += chip.effect_val

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

            # KUROGANE & GENERIC EFFECTS
            elif chip.effect_type == "APPLY_BLEED_HEAVY_STACKS":
                self.apply_status_logic(target, StatusEffect("Bleed", "[red]💧︎[/red]", 2, STATUS_DESCS["Bleed"], duration=2, type="DEBUFF"))
            elif chip.effect_type == "APPLY_BLEED_AND_BIND":
                self.apply_status_logic(target, StatusEffect("Bleed", "[red]💧︎[/red]", 3, STATUS_DESCS["Bleed"], duration=1, type="DEBUFF"))
                self.apply_status_logic(target, StatusEffect("Bind", "[gold1]⛓[/gold1]", 1, STATUS_DESCS["Bind"], duration=1, type="DEBUFF"))
            elif chip.effect_type == "APPLY_BLEED_AND_BIND_HEAVY":
                self.apply_status_logic(target, StatusEffect("Bleed", "[red]💧︎[/red]", 3, STATUS_DESCS["Bleed"], duration=1, type="DEBUFF"))
                self.apply_status_logic(target, StatusEffect("Bind", "[gold1]⛓[/gold1]", 1, STATUS_DESCS["Bind"], duration=2, type="DEBUFF"))
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
                for a in chosen_allies: self.apply_status_logic(a, StatusEffect("Haste", "[yellow1]🢙[/yellow1]", 0, STATUS_DESCS["Haste"], duration=chip.effect_val))
                for e in chosen_enemies: self.apply_status_logic(e, StatusEffect("Bind", "[gold1]⛓[/gold1]", 1, STATUS_DESCS["Bind"], duration=chip.effect_val))
                
            elif chip.effect_type == "HANA_SPECIAL_RAGE":
                if not hasattr(attacker, "next_turn_modifiers"): attacker.next_turn_modifiers = {}
                attacker.next_turn_modifiers["outgoing_dmg_mult"] = 0.6
                target.temp_modifiers["outgoing_dmg_mult"] *= 0.85
                
            elif chip.effect_type == "BLEED_RUPTURE_SPECIAL_TYPE1":
                self.apply_status_logic(target, StatusEffect("Bleed", "[red]💧︎[/red]", chip.effect_val, STATUS_DESCS["Bleed"], duration=1))
                self.apply_status_logic(target, StatusEffect("Rupture", "[medium_spring_green]✧[/medium_spring_green]", chip.effect_val, STATUS_DESCS["Rupture"], duration=1))
                
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
                    self.apply_status_logic(a, StatusEffect("Haste", "[yellow1]🢙[/yellow1]", 0, STATUS_DESCS["Haste"], duration=1))
                has_rupture = any(s.name in RUPTURE_LIST for s in target.status_effects)
                if has_rupture: self.apply_status_logic(target, StatusEffect("Rupture", "[medium_spring_green]✧[/medium_spring_green]", 1, STATUS_DESCS["Rupture"], duration=2))
                else: self.apply_status_logic(target, StatusEffect("Rupture", "[medium_spring_green]✧[/medium_spring_green]", 3, STATUS_DESCS["Rupture"], duration=1))   
                    
            elif chip.effect_type == "RUPTURE_DAMAGE_BUFF_TYPE1":
                has_rupture = any(s.name in RUPTURE_LIST for s in target.status_effects)
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
                self.apply_status_logic(target, StatusEffect("Rupture", "[medium_spring_green]✧[/medium_spring_green]", 0, STATUS_DESCS["Rupture"], duration=2))
                self.apply_status_logic(target, StatusEffect("Fairylight", "[spring_green1]𒀭[/spring_green1]", 2, STATUS_DESCS["Fairylight"], duration=1))
            elif chip.effect_type == "AYAKO_SPECIAL":
                self.apply_status_logic(target, StatusEffect("Rupture", "[medium_spring_green]✧[/medium_spring_green]", 0, STATUS_DESCS["Rupture"], duration=3))
                self.apply_status_logic(target, StatusEffect("Fairylight", "[spring_green1]𒀭[/spring_green1]", 4, STATUS_DESCS["Fairylight"], duration=1))
            elif chip.effect_type == "SUMIKO_SPECIAL_1":
                self.apply_status_logic(attacker, StatusEffect("Haste", "[yellow1]🢙[/yellow1]", 0, STATUS_DESCS["Haste"], duration=2))
            elif chip.effect_type == "SUMIKO_SPECIAL_2":
                self.apply_status_logic(target, StatusEffect("Rupture", "[medium_spring_green]✧[/medium_spring_green]", 5, STATUS_DESCS["Rupture"], duration=4))
                self.apply_status_logic(attacker, StatusEffect("Haste", "[yellow1]🢙[/yellow1]", 0, STATUS_DESCS["Haste"], duration=2))
            elif chip.effect_type == "APPLY_RUPTURE_HEAVY_STACKS":
                self.apply_status_logic(target, StatusEffect("Rupture", "[medium_spring_green]✧[/medium_spring_green]", 2, STATUS_DESCS["Rupture"], duration=2))
            
            elif chip.effect_type == "HISAYUKI_SPECIAL_1":
                if any(s.name == "Haste" for s in attacker.status_effects): self.apply_status_logic(attacker, StatusEffect("Bind", "[gold1]⛓[/gold1]", 1, STATUS_DESCS["Bind"], duration=1))
                else: self.apply_status_logic(attacker, StatusEffect("Haste", "[yellow1]🢙[/yellow1]", 0, STATUS_DESCS["Haste"], duration=1))
            elif chip.effect_type == "BIND_RUPTURE_SPECIAL_TYPE1":
                self.apply_status_logic(target, StatusEffect("Bind", "[gold1]⛓[/gold1]", 1, STATUS_DESCS["Bind"], duration=2))
                self.apply_status_logic(target, StatusEffect("Rupture", "[medium_spring_green]✧[/medium_spring_green]", 2, STATUS_DESCS["Rupture"], duration=1))
            
            elif chip.effect_type == "RAVEN_SPECIAL_1":
                target.next_hit_taken_flat_bonus += 6
                self.apply_status_logic(attacker, StatusEffect("Poise", "[light_cyan1]༄[/light_cyan1]", 4, STATUS_DESCS["Poise"], duration=4))
            elif chip.effect_type == "RAVEN_SPECIAL_2":
                if not hasattr(target, "next_turn_modifiers"): target.next_turn_modifiers = {}
                target.next_turn_modifiers["outgoing_dmg_mult"] = target.next_turn_modifiers.get("outgoing_dmg_mult", 1.0) * 0.30
                self.apply_status_logic(attacker, StatusEffect("Poise", "[light_cyan1]༄[/light_cyan1]", 6, STATUS_DESCS["Poise"], duration=1))
            elif chip.effect_type == "FALCON_SPECIAL_1":
                self.apply_status_logic(target, StatusEffect("Rupture", "[medium_spring_green]✧[/medium_spring_green]", 4, STATUS_DESCS["Rupture"], duration=1))
            elif chip.effect_type == "FALCON_SPECIAL_2":
                if not hasattr(target, "next_turn_modifiers"): target.next_turn_modifiers = {}
                target.next_turn_modifiers["outgoing_dmg_mult"] = target.next_turn_modifiers.get("outgoing_dmg_mult", 1.0) * 0.30
                self.apply_status_logic(attacker, StatusEffect("Haste", "[yellow1]🢙[/yellow1]", 0, STATUS_DESCS["Haste"], duration=2))
                self.apply_status_logic(target, StatusEffect("Bind", "[gold1]⛓[/gold1]", 1, STATUS_DESCS["Bind"], duration=2))
            elif chip.effect_type == "EAGLE_SPECIAL_1":
                target.next_hit_taken_flat_bonus += 5
                if not hasattr(target, "next_turn_modifiers"): target.next_turn_modifiers = {}
                target.next_turn_modifiers["outgoing_dmg_mult"] = target.next_turn_modifiers.get("outgoing_dmg_mult", 1.0) * 0.50
            elif chip.effect_type == "EAGLE_SPECIAL_2":
                self.apply_status_logic(target, StatusEffect("Rupture", "[medium_spring_green]✧[/medium_spring_green]", 2, STATUS_DESCS["Rupture"], duration=5))

            # RIPOSTE GANG
            elif chip.effect_type == "RIPOSTE_GAIN_SPECIAL_1":
                if any(s.name == "Pierce Fragility" for s in target.status_effects):
                    self.apply_status_logic(attacker, StatusEffect("Riposte", "[cyan1]➲[/cyan1]", 0, STATUS_DESCS["Riposte"], duration=10))
            elif chip.effect_type == "PIERCE_FRAGILITY_INFLICT_SPECIAL_1":
                if any(s.name == "Pierce Fragility" for s in target.status_effects): self.apply_status_logic(target, StatusEffect("Pierce Fragility", "[light_yellow3]▶[/light_yellow3]", 0, STATUS_DESCS["Pierce Fragility"], duration=2))
                else: self.apply_status_logic(target, StatusEffect("Pierce Fragility", "[light_yellow3]▶[/light_yellow3]", 0, STATUS_DESCS["Pierce Fragility"], duration=1))
            elif chip.effect_type == "RIPOSTE_SQUAD_LEADER_SPECIAL_1":
                self.apply_status_logic(target, StatusEffect("Pierce Fragility", "[light_yellow3]▶[/light_yellow3]", 0, STATUS_DESCS["Pierce Fragility"], duration=2))
            elif chip.effect_type == "RIPOSTE_SQUAD_LEADER_SPECIAL_2":
                self.apply_status_logic(target, StatusEffect("Pierce Fragility", "[light_yellow3]▶[/light_yellow3]", 0, STATUS_DESCS["Pierce Fragility"], duration=3))
            elif chip.effect_type == "ADAM_SPECIAL_1":
                self.apply_status_logic(target, StatusEffect("Pierce Fragility", "[light_yellow3]▶[/light_yellow3]", 0, STATUS_DESCS["Pierce Fragility"], duration=2))
                self.apply_status_logic(attacker, StatusEffect("Riposte", "[cyan1]➲[/cyan1]", 0, STATUS_DESCS["Riposte"], duration=10))
            elif chip.effect_type == "ADAM_SPECIAL_2":
                pierce_target_eff = next((s for s in target.status_effects if s.name == "Pierce Fragility"), None)
                if pierce_target_eff: self.apply_status_logic(attacker, StatusEffect("Riposte", "[cyan1]➲[/cyan1]", 0, STATUS_DESCS["Riposte"], duration=5 * pierce_target_eff.duration))
                self.apply_status_logic(target, StatusEffect("Pierce Fragility", "[light_yellow3]▶[/light_yellow3]", 0, STATUS_DESCS["Pierce Fragility"], duration=3))
            elif chip.effect_type == "ADAM_SPECIAL_3":
                self.apply_status_logic(target, StatusEffect("Pierce Fragility", "[light_yellow3]▶[/light_yellow3]", 0, STATUS_DESCS["Pierce Fragility"], duration=5))
                riposte_eff = next((s for s in attacker.status_effects if s.name == "Riposte"), None)
                if riposte_eff: riposte_eff.duration = 50
                else: self.apply_status_logic(attacker, StatusEffect("Riposte", "[cyan1]➲[/cyan1]", 0, STATUS_DESCS["Riposte"], duration=50))
            
            # SKILLS NAMED "COUNTER"
            elif chip.effect_type == "COUNTER_SKILL_SPECIAL_TYPE1":
                self.apply_status_logic(target, StatusEffect("Pierce Fragility", "[light_yellow3]▶[/light_yellow3]", 0, STATUS_DESCS["Pierce Fragility"], duration=2))
            elif chip.effect_type == "COUNTER_SKILL_SPECIAL_TYPE3":
                self.apply_status_logic(target, StatusEffect("Pierce Fragility", "[light_yellow3]▶[/light_yellow3]", 0, STATUS_DESCS["Pierce Fragility"], duration=3))

            # RIPOSTE KATAS EFFECTS
            elif chip.effect_type in ["NAGANOHARA_RIPOSTE_APPEL", "NAGANOHARA_RIPOSTE_CEDE", "NAGANOHARA_RIPOSTE_COUNTERPARRY", "AKASUKE_RIPOSTE_ENGARDE", "AKASUKE_RIPOSTE_FEINT", "AKASUKE_RIPOSTE_PRISEDEFER"]:
                riposte_eff = next((s for s in attacker.status_effects if s.name == "Riposte"), None)
                if chip.effect_type == "NAGANOHARA_RIPOSTE_APPEL":
                    self.apply_status_logic(attacker, StatusEffect("Riposte", "[cyan1]➲[/cyan1]", 0, STATUS_DESCS["Riposte"], duration=5))
                    self.apply_status_logic(target, StatusEffect("Pierce Fragility", "[light_yellow3]▶[/light_yellow3]", 0, STATUS_DESCS["Pierce Fragility"], duration=1))
                elif chip.effect_type == "NAGANOHARA_RIPOSTE_CEDE":
                    self.apply_status_logic(attacker, StatusEffect("Riposte", "[cyan1]➲[/cyan1]", 0, STATUS_DESCS["Riposte"], duration=10))
                    self.apply_status_logic(target, StatusEffect("Pierce Fragility", "[light_yellow3]▶[/light_yellow3]", 0, STATUS_DESCS["Pierce Fragility"], duration=2))
                elif chip.effect_type == "NAGANOHARA_RIPOSTE_COUNTERPARRY":
                    if riposte_eff and riposte_eff.duration >= 25:
                        riposte_eff.duration = 50
                        self.log(f"[cyan1]{attacker.name} maxes out their Riposte Stance![/cyan1]")
                    else: self.apply_status_logic(attacker, StatusEffect("Riposte", "[cyan1]➲[/cyan1]", 0, STATUS_DESCS["Riposte"], duration=20))
                    self.apply_status_logic(target, StatusEffect("Pierce Fragility", "[light_yellow3]▶[/light_yellow3]", 0, STATUS_DESCS["Pierce Fragility"], duration=3))
                elif chip.effect_type == "AKASUKE_RIPOSTE_ENGARDE":
                    if not riposte_eff or riposte_eff.duration <= 0: self.apply_status_logic(attacker, StatusEffect("Riposte", "[cyan1]➲[/cyan1]", 0, STATUS_DESCS["Riposte"], duration=10))
                    else: self.apply_status_logic(attacker, StatusEffect("Riposte", "[cyan1]➲[/cyan1]", 0, STATUS_DESCS["Riposte"], duration=5))
                    self.apply_status_logic(target, StatusEffect("Pierce Fragility", "[light_yellow3]▶[/light_yellow3]", 0, STATUS_DESCS["Pierce Fragility"], duration=1))
                elif chip.effect_type == "AKASUKE_RIPOSTE_FEINT":
                    self.apply_status_logic(attacker, StatusEffect("Haste", "[yellow1]🢙[/yellow1]", 0, STATUS_DESCS["Haste"], duration=1))
                    if riposte_eff and riposte_eff.duration >= 10: self.apply_status_logic(attacker, StatusEffect("Haste", "[yellow1]🢙[/yellow1]", 0, STATUS_DESCS["Haste"], duration=1))
                    target_pierce = next((s for s in target.status_effects if s.name == "Pierce Fragility"), None)
                    if target_pierce and target_pierce.duration > 0: self.apply_status_logic(attacker, StatusEffect("Riposte", "[cyan1]➲[/cyan1]", 0, STATUS_DESCS["Riposte"], duration=10))
                    self.apply_status_logic(target, StatusEffect("Pierce Fragility", "[light_yellow3]▶[/light_yellow3]", 0, STATUS_DESCS["Pierce Fragility"], duration=2))
                elif chip.effect_type == "AKASUKE_RIPOSTE_PRISEDEFER":
                    self.apply_status_logic(attacker, StatusEffect("Riposte", "[cyan1]➲[/cyan1]", 0, STATUS_DESCS["Riposte"], duration=10))
                    self.apply_status_logic(target, StatusEffect("Pierce Fragility", "[light_yellow3]▶[/light_yellow3]", 0, STATUS_DESCS["Pierce Fragility"], duration=3))

            # KIRYOKU FAIRY & INFILTRATOR
            elif chip.effect_type == "RUPTURE_SPECIAL1":
                has_rupture = any(s.name in RUPTURE_LIST for s in target.status_effects)
                if has_rupture: self.apply_status_logic(target, StatusEffect("Rupture", "[medium_spring_green]✧[/medium_spring_green]", 1, STATUS_DESCS["Rupture"], duration=chip.effect_val))
                else: self.apply_status_logic(target, StatusEffect("Rupture", "[medium_spring_green]✧[/medium_spring_green]", chip.effect_val, STATUS_DESCS["Rupture"], duration=1))
            elif chip.effect_type == "FAIRYLIGHT_APPLY":
                has_rupture = any(s.name in RUPTURE_LIST for s in target.status_effects)
                if has_rupture: self.apply_status_logic(target, StatusEffect("Fairylight", "[spring_green1]𒀭[/spring_green1]", chip.effect_val, STATUS_DESCS["Fairylight"], duration=1))
            elif chip.effect_type == "BENIKAWA_KIRYOKU_SPECIAL":
                has_rupture = any(s.name in RUPTURE_LIST for s in target.status_effects)
                if has_rupture: self.apply_status_logic(target, StatusEffect("Fairylight", "[spring_green1]𒀭[/spring_green1]", 3, STATUS_DESCS["Fairylight"], duration=1))
            elif chip.effect_type == "FAIRYLIGHT_SPECIAL1":
                has_fairylight = any(s.name == "Fairylight" for s in target.status_effects)
                if has_fairylight: self.apply_status_logic(target, StatusEffect("Rupture", "[medium_spring_green]✧[/medium_spring_green]", chip.effect_val, STATUS_DESCS["Rupture"], duration=1))
            elif chip.effect_type == "HANA_KIRYOKU_SPECIAL":
                has_fairylight = any(s.name == "Fairylight" for s in target.status_effects)
                if has_fairylight:
                    self.apply_status_logic(target, StatusEffect("Rupture", "[medium_spring_green]✧[/medium_spring_green]", 1, STATUS_DESCS["Rupture"], duration=2))
                    attacker.temp_modifiers["incoming_dmg_mult"] *= 0.70
            elif chip.effect_type == "HASTE_GAIN_SPECIAL_TYPE1":
                has_haste = any(s.name == "Haste" for s in attacker.status_effects)
                if has_haste: self.apply_status_logic(attacker, StatusEffect("Haste", "[yellow1]🢙[/yellow1]", 0, STATUS_DESCS["Haste"], duration=1))
                self.apply_status_logic(attacker, StatusEffect("Haste", "[yellow1]🢙[/yellow1]", 0, STATUS_DESCS["Haste"], duration=chip.effect_val))
            elif chip.effect_type == "DEBUFF_ATK_MULT":
                target.next_turn_modifiers["outgoing_dmg_mult"]

            # BENIKAWA NINJA CLAN
            elif chip.effect_type == "BENIKAWA_CLAN_SPECIAL_1":
                target.temp_modifiers["final_dmg_reduction"] -= 4
                has_bleed = any(s.name == "Bleed" for s in target.status_effects)
                if has_bleed: self.apply_status_logic(target, StatusEffect("Bleed", "[red]💧︎[/red]", 3, "", duration=1))
                self.apply_status_logic(target, StatusEffect("Pierce Fragility", "[light_yellow3]⇴[/light_yellow3]", 0, "", duration=1))
            elif chip.effect_type == "BENIKAWA_CLAN_SPECIAL_2":
                has_poise = any(s.name in POISE_LIST for s in attacker.status_effects)
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
                has_pierce = any(s.name == "Pierce Fragility" for s in target.status_effects)
                if has_pierce:
                    self.apply_status_logic(target, StatusEffect("Pierce Fragility", "[light_yellow3]⇴[/light_yellow3]", 0, "", duration=2))
                    self.apply_status_logic(attacker, StatusEffect("Poise", "[light_cyan1]༄[/light_cyan1]", 3, "", duration=2))

            # --- LUOXIA MARTIAL ARTS STUDENT ---
            elif chip.effect_type == "RUPTURE_BUFF_DEF_SPECIAL_1":
                self.apply_status_logic(target, StatusEffect("Rupture", "[medium_spring_green]✧[/medium_spring_green]", 2, STATUS_DESCS["Rupture"], duration=0))
                if not hasattr(attacker, "next_turn_modifiers"): attacker.next_turn_modifiers = {}
                attacker.next_turn_modifiers["final_dmg_reduction"] = attacker.next_turn_modifiers.get("final_dmg_reduction", 0) + 1
            elif chip.effect_type == "RUPTURE_BUFF_DEF_SPECIAL_2":
                self.apply_status_logic(target, StatusEffect("Rupture", "[medium_spring_green]✧[/medium_spring_green]", 0, STATUS_DESCS["Rupture"], duration=2))
                if not hasattr(attacker, "next_turn_modifiers"): attacker.next_turn_modifiers = {}
                attacker.next_turn_modifiers["final_dmg_reduction"] = attacker.next_turn_modifiers.get("final_dmg_reduction", 0) + 1
            elif chip.effect_type == "POISE_RUPTURE_SPECIAL_TYPE1":
                self.apply_status_logic(attacker, StatusEffect("Poise", "[light_cyan1]༄[/light_cyan1]", chip.effect_val, STATUS_DESCS["Poise"], duration=chip.effect_val))
                self.apply_status_logic(target, StatusEffect("Rupture", "[medium_spring_green]✧[/medium_spring_green]", chip.effect_val, STATUS_DESCS["Rupture"], duration=0))
    
            # --- NATSUME STRANGE KATA ---
            elif chip.effect_type == "NATSUME_STRANGE_SPECIAL_1":
                self.apply_status_logic(target, StatusEffect("Rupture", "[medium_spring_green]✧[/medium_spring_green]", 0, STATUS_DESCS["Rupture"], duration=3))
            elif chip.effect_type == "NATSUME_STRANGE_SPECIAL_2":
                self.apply_status_logic(target, StatusEffect("Rupture", "[medium_spring_green]✧[/medium_spring_green]", 1, STATUS_DESCS["Rupture"], duration=0))
            elif chip.effect_type == "NATSUME_STRANGE_SPECIAL_3":
                self.apply_status_logic(target, StatusEffect("Sinking", "[blue3]♆[/blue3]", 0, STATUS_DESCS["Sinking"], duration=5, type="DEBUFF"))
            elif chip.effect_type == "NATSUME_STRANGE_SPECIAL_4":
                self.apply_status_logic(target, StatusEffect("Sinking", "[blue3]♆[/blue3]", 1, STATUS_DESCS["Sinking"], duration=0, type="DEBUFF"))
            elif chip.effect_type == "NATSUME_STRANGE_SPECIAL_5":
                self.apply_status_logic(target, StatusEffect("Sinking", "[blue3]♆[/blue3]", 2, STATUS_DESCS["Sinking"], duration=0, type="DEBUFF"))
            elif chip.effect_type == "NATSUME_STRANGE_SPECIAL_6":
                self.apply_status_logic(target, StatusEffect("Rupture", "[medium_spring_green]✧[/medium_spring_green]", 2, STATUS_DESCS["Rupture"], duration=0))

            # --- GOLDEN FIST UNION ENEMIES ---
            elif chip.effect_type == "APPLY_BLEED_RUPTURE_HEAVY_STACKS":
                self.apply_status_logic(target, StatusEffect("Bleed", "[red]💧︎[/red]", 2, STATUS_DESCS["Bleed"], duration=2))
                self.apply_status_logic(target, StatusEffect("Rupture", "[medium_spring_green]✧[/medium_spring_green]", 2, STATUS_DESCS["Rupture"], duration=2))
            elif chip.effect_type == "RUPTURE_BUFF_AND_COUNT_SPECIAL":
                self.apply_status_logic(target, StatusEffect("Rupture", "[medium_spring_green]✧[/medium_spring_green]", 0, STATUS_DESCS["Rupture"], duration=3))

            # --- BLACK WATER DOCK ENEMIES ---
            elif chip.effect_type == "POISE_RUPTURE_SPECIAL_TYPE2":
                self.apply_status_logic(attacker, StatusEffect("Poise", "[light_cyan1]༄[/light_cyan1]", 0, STATUS_DESCS["Poise"], duration=chip.effect_val))
                self.apply_status_logic(target, StatusEffect("Rupture", "[medium_spring_green]✧[/medium_spring_green]", chip.effect_val, STATUS_DESCS["Rupture"], duration=0))
            elif chip.effect_type == "RUPTURE_PARALYSIS_SPECIAL_TYPE1":
                self.apply_status_logic(target, StatusEffect("Rupture", "[medium_spring_green]✧[/medium_spring_green]", 1, STATUS_DESCS["Rupture"], duration=0))
                self.apply_status_logic(target, StatusEffect("Paralysis", "[orange1]ϟ[/orange1]", 1, STATUS_DESCS["Paralysis"], duration=chip.effect_val, type="DEBUFF"))
                if any(s.name in POISE_LIST for s in attacker.status_effects):
                    self.apply_status_logic(target, StatusEffect("Paralysis", "[orange1]ϟ[/orange1]", 1, STATUS_DESCS["Paralysis"], duration=chip.effect_val, type="DEBUFF"))
            elif chip.effect_type == "PARALYSIS_SPECIAL_TYPE1":
                self.apply_status_logic(target, StatusEffect("Paralysis", "[orange1]ϟ[/orange1]", 1, STATUS_DESCS["Paralysis"], duration=3, type="DEBUFF"))

            # --- TWIN MOUNTAIN GATE ENEMIES ---
            elif chip.effect_type == "BLEED_RUPTURE_SPECIAL_TYPE2":
                self.apply_status_logic(target, StatusEffect("Bleed", "[red]💧︎[/red]", 1, STATUS_DESCS["Bleed"], duration=1, type="DEBUFF"))
                self.apply_status_logic(target, StatusEffect("Rupture", "[medium_spring_green]✧[/medium_spring_green]", 1, STATUS_DESCS["Rupture"], duration=2))
            elif chip.effect_type == "RUMBLE_SPECIAL":
                if not hasattr(attacker, "next_turn_modifiers"): attacker.next_turn_modifiers = {}
                attacker.next_turn_modifiers["final_dmg_reduction"] = attacker.next_turn_modifiers.get("final_dmg_reduction", 0) - 5
                self.apply_status_logic(target, StatusEffect("Paralysis", "[orange1]ϟ[/orange1]", 1, STATUS_DESCS["Paralysis"], duration=2, type="DEBUFF"))
            elif chip.effect_type == "BLEED_PARALYSIS_SPECIAL_TYPE1":
                self.apply_status_logic(target, StatusEffect("Bleed", "[red]💧︎[/red]", 1, STATUS_DESCS["Bleed"], duration=2, type="DEBUFF"))
                self.apply_status_logic(target, StatusEffect("Paralysis", "[orange1]ϟ[/orange1]", 1, STATUS_DESCS["Paralysis"], duration=1, type="DEBUFF"))
            elif chip.effect_type == "BLEED_PARALYSIS_SPECIAL_TYPE2":
                if not hasattr(attacker, "next_turn_modifiers"): attacker.next_turn_modifiers = {}
                attacker.next_turn_modifiers["final_dmg_reduction"] = attacker.next_turn_modifiers.get("final_dmg_reduction", 0) - 6
                self.apply_status_logic(target, StatusEffect("Bleed", "[red]💧︎[/red]", 1, STATUS_DESCS["Bleed"], duration=2, type="DEBUFF"))
                self.apply_status_logic(target, StatusEffect("Paralysis", "[orange1]ϟ[/orange1]", 1, STATUS_DESCS["Paralysis"], duration=1, type="DEBUFF"))
            elif chip.effect_type == "SWITCH_RANDOM_TYPE1":
                team = self.enemies if target in self.enemies else self.allies
                living = [u for u in team if u.hp > 0 and u != target]
                if living:
                    target = random.choice(living)
                    self.log(f"[bold magenta]-> {attacker.name} switches focus to {target.name}![/bold magenta]")

            # --- MIYU EFFECTS ---
            elif chip.effect_type == "POISE_RUPTURE_SPECIAL_TYPE3":
                self.apply_status_logic(attacker, StatusEffect("Poise", "[light_cyan1]༄[/light_cyan1]", 0, STATUS_DESCS["Poise"], duration=chip.effect_val))
                self.apply_status_logic(target, StatusEffect("Rupture", "[medium_spring_green]✧[/medium_spring_green]", chip.effect_val, STATUS_DESCS["Rupture"], duration=1))
            elif chip.effect_type == "GAIN_POISE_SPECIAL_2":
                self.apply_status_logic(attacker, StatusEffect("Poise", "[light_cyan1]༄[/light_cyan1]", 3, STATUS_DESCS["Poise"], duration=2))
            elif chip.effect_type == "APPLY_RUPTURE_SPECIAL_1":
                self.apply_status_logic(target, StatusEffect("Rupture", "[medium_spring_green]✧[/medium_spring_green]", 3, STATUS_DESCS["Rupture"], duration=2))
            elif chip.effect_type == "GAIN_POISE_SPECIAL_3":
                self.apply_status_logic(attacker, StatusEffect("Poise", "[light_cyan1]༄[/light_cyan1]", 4, STATUS_DESCS["Poise"], duration=3))
                team = self.enemies if target in self.enemies else self.allies
                living = [u for u in team if u.hp > 0 and u != target]
                if living:
                    target = __import__('random').choice(living)
                    self.log(f"[bold magenta]-> {attacker.name} switches focus to {target.name}![/bold magenta]")
            elif chip.effect_type == "APPLY_RUPTURE_SPECIAL_2":
                self.apply_status_logic(target, StatusEffect("Rupture", "[medium_spring_green]✧[/medium_spring_green]", 4, STATUS_DESCS["Rupture"], duration=2))
                team = self.enemies if target in self.enemies else self.allies
                living = [u for u in team if u.hp > 0 and u != target]
                if living:
                    target = __import__('random').choice(living)
                    self.log(f"[bold magenta]-> {attacker.name} switches focus to {target.name}![/bold magenta]")      
            elif chip.effect_type == "POISE_RUPTURE_SPECIAL_TYPE4":
                self.apply_status_logic(attacker, StatusEffect("Poise", "[light_cyan1]༄[/light_cyan1]", 4, STATUS_DESCS["Poise"], duration=6))
                self.apply_status_logic(target, StatusEffect("Rupture", "[medium_spring_green]✧[/medium_spring_green]", 4, STATUS_DESCS["Rupture"], duration=4))    
            elif chip.effect_type == "MIYU_SPECIAL_1":
                self.apply_status_logic(attacker, StatusEffect("Poise", "[light_cyan1]༄[/light_cyan1]", 7, STATUS_DESCS["Poise"], duration=2))
                self.apply_status_logic(target, StatusEffect("Paralysis", "[orange1]ϟ[/orange1]", 1, STATUS_DESCS["Paralysis"], duration=2, type="DEBUFF"))
                team = self.enemies if target in self.enemies else self.allies
                living = [u for u in team if u.hp > 0 and u != target]
                if living:
                    non_paralyzed = [u for u in living if not any(s.name == "Paralysis" for s in u.status_effects)]
                    target = __import__('random').choice(non_paralyzed) if non_paralyzed else __import__('random').choice(living)
                    self.log(f"[bold magenta]-> {attacker.name} switches focus to {target.name}![/bold magenta]")
            elif chip.effect_type == "MIYU_SPECIAL_2":
                self.apply_status_logic(attacker, StatusEffect("Poise", "[light_cyan1]༄[/light_cyan1]", 4, STATUS_DESCS["Poise"], duration=4))
                self.apply_status_logic(target, StatusEffect("Paralysis", "[orange1]ϟ[/orange1]", 1, STATUS_DESCS["Paralysis"], duration=3, type="DEBUFF"))
                team = self.enemies if target in self.enemies else self.allies
                living = [u for u in team if u.hp > 0 and u != target]
                if living:
                    non_paralyzed = [u for u in living if not any(s.name == "Paralysis" for s in u.status_effects)]
                    target = __import__('random').choice(non_paralyzed) if non_paralyzed else __import__('random').choice(living)
                    self.log(f"[bold magenta]-> {attacker.name} switches focus to {target.name}![/bold magenta]")

            # MEI TARGET SWITCHING LOGIC
            if chip.effect_type in ["MEI_SPECIAL_1", "MEI_SPECIAL_2"]:
                team = self.enemies if target in self.enemies else self.allies
                living = [u for u in team if u.hp > 0 and u != target]
                if living:
                    target = random.choice(living)
                    self.log(f"[bold magenta]-> {attacker.name} switches focus to {target.name}![/bold magenta]")
            elif chip.effect_type in ["MEI_SPECIAL_4", "MEI_SPECIAL_5"]:
                team = self.enemies if target in self.enemies else self.allies
                living = [u for u in team if u.hp > 0 and u != target]
                if living:
                    non_paralyzed = [u for u in living if not any(s.name == "Paralysis" for s in u.status_effects)]
                    target = random.choice(non_paralyzed) if non_paralyzed else random.choice(living)
                    self.log(f"[bold magenta]-> {attacker.name} switches focus to {target.name}![/bold magenta]")

            # --- BLOOD-BROKEN GUARD EFFECTS ---
            elif chip.effect_type == "POISE_BLEED_SPECIAL_TYPE1":
                self.apply_status_logic(target, StatusEffect("Bleed", "[red]💧︎[/red]", chip.effect_val, STATUS_DESCS["Bleed"], duration=1, type="DEBUFF"))
                self.apply_status_logic(attacker, StatusEffect("Poise", "[light_cyan1]༄[/light_cyan1]", chip.effect_val, STATUS_DESCS["Poise"], duration=chip.effect_val, type="BUFF"))
            elif chip.effect_type == "POISE_BLEED_SPECIAL_TYPE2":
                self.apply_status_logic(target, StatusEffect("Bleed", "[red]💧︎[/red]", 1, STATUS_DESCS["Bleed"], duration=chip.effect_val, type="DEBUFF"))
                self.apply_status_logic(attacker, StatusEffect("Poise", "[light_cyan1]༄[/light_cyan1]", chip.effect_val, STATUS_DESCS["Poise"], duration=chip.effect_val, type="BUFF"))

            # --- JADE RAIN MONASTERY EFFECTS ---
            elif chip.effect_type == "FOG_STEP_SPECIAL":
                # Check Rupture for Final Damage Reduction
                if any(s.name in RUPTURE_LIST for s in target.status_effects):
                    reduction_pct = chip.effect_val / 100.0
                    if not hasattr(attacker, "next_turn_modifiers"): attacker.next_turn_modifiers = {}
                    attacker.next_turn_modifiers["incoming_dmg_mult"] = attacker.next_turn_modifiers.get("incoming_dmg_mult", 1.0) * (1.0 - reduction_pct)
                # Switch Target prioritizing Rupture
                team = self.enemies if target in self.enemies else self.allies
                living = [u for u in team if u.hp > 0 and u != target]
                if living:
                    ruptured_targets = [u for u in living if any(s.name in RUPTURE_LIST for s in u.status_effects)]
                    target = __import__('random').choice(ruptured_targets) if ruptured_targets else __import__('random').choice(living)
                    self.log(f"[bold magenta]-> {attacker.name} switches focus to {target.name}![/bold magenta]")

            # --- IBARA NINJA EFFECTS ---
            elif chip.effect_type == "IBARA_ACT4_SPECIAL1":
                invis = next((s for s in attacker.status_effects if s.name == "Invisibility"), None)
                # Requires 3+ Invisibility
                if invis and invis.duration >= 3:
                    if any(s.name == "Bleed" for s in target.status_effects):
                        self.apply_status_logic(target, StatusEffect("Bleed", "[red]💧︎[/red]", 1, STATUS_DESCS["Bleed"], duration=2, type="DEBUFF"))
                    self.apply_status_logic(target, StatusEffect("Bleed", "[red]💧︎[/red]", 5, STATUS_DESCS["Bleed"], duration=0, type="DEBUFF"))
                self.apply_status_logic(target, StatusEffect("Bleed", "[red]💧︎[/red]", 1, STATUS_DESCS["Bleed"], duration=2, type="DEBUFF"))
                
                # The unconditional +2 Bleed Count still applies regardless of Invisibility!
                self.apply_status_logic(target, StatusEffect("Bleed", "[red]💧︎[/red]", 1, STATUS_DESCS["Bleed"], duration=2, type="DEBUFF"))

            # --- TEN THOUSAND BLOSSOM BROTHERHOOD EFFECTS ---
            elif chip.effect_type == "POISE_RUPTURE_SINKING_SPECIAL1":
                self.apply_status_logic(target, StatusEffect("Rupture", "[medium_spring_green]✧[/medium_spring_green]", chip.effect_val, STATUS_DESCS["Rupture"], duration=1))
                self.apply_status_logic(target, StatusEffect("Sinking", "[blue3]♆[/blue3]", chip.effect_val, STATUS_DESCS["Sinking"], duration=1, type="DEBUFF"))
            elif chip.effect_type == "BREAKTHEENEMY_SPECIAL":
                self.apply_status_logic(target, StatusEffect("Bind", "[gold1]⛓[/gold1]", 1, STATUS_DESCS["Bind"], duration=4))
                self.apply_status_logic(target, StatusEffect("Rupture", "[medium_spring_green]✧[/medium_spring_green]", 0, STATUS_DESCS["Rupture"], duration=4))
            elif chip.effect_type == "FORMALINE_SPECIAL":
                team = self.allies if attacker in self.allies else self.enemies
                x = len([u for u in team if u.hp > 0 and "Ten Thousand Blossom Brotherhood" in u.name])
                target.temp_modifiers["outgoing_dmg_flat"] = target.temp_modifiers.get("outgoing_dmg_flat", 0) - x
                if not hasattr(target, "next_turn_modifiers"): target.next_turn_modifiers = {}
                target.next_turn_modifiers["outgoing_dmg_flat"] = target.next_turn_modifiers.get("outgoing_dmg_flat", 0) - x
            elif chip.effect_type == "RUPTURE_SINKING_SPECIAL_TYPE1":
                self.apply_status_logic(target, StatusEffect("Rupture", "[medium_spring_green]✧[/medium_spring_green]", chip.effect_val, STATUS_DESCS["Rupture"], duration=1))
                self.apply_status_logic(target, StatusEffect("Sinking", "[blue3]♆[/blue3]", chip.effect_val, STATUS_DESCS["Sinking"], duration=1, type="DEBUFF"))
            elif chip.effect_type in ["ISOLATETHEENEMY_SPECIAL_TYPE1", "ISOLATETHEENEMY_SPECIAL_TYPE2"]:
                team = self.enemies if target in self.enemies else self.allies
                living = [u for u in team if u.hp > 0 and u != target]
                if living:
                    target = random.choice(living)
                    self.log(f"[bold magenta]-> {attacker.name} isolates and switches focus to {target.name}![/bold magenta]")
            elif chip.effect_type == "ISOLATETHEENEMY_SPECIAL_TYPE3":
                self.apply_status_logic(target, StatusEffect("Sinking", "[blue3]♆[/blue3]", 1, STATUS_DESCS["Sinking"], duration=5, type="DEBUFF"))
            elif chip.effect_type == "POISE_PARALYSIS_SPECIAL1":
                self.apply_status_logic(target, StatusEffect("Paralysis", "[orange1]ϟ[/orange1]", 1, STATUS_DESCS["Paralysis"], duration=chip.effect_val, type="DEBUFF"))
                team = self.enemies if target in self.enemies else self.allies
                living = [u for u in team if u.hp > 0 and u != target]
                if living:
                    target = random.choice(living)
                    self.log(f"[bold magenta]-> {attacker.name} switches focus to {target.name}![/bold magenta]")
            elif chip.effect_type == "BIND_HASTE_SPECIAL_TYPE1":
                self.apply_status_logic(target, StatusEffect("Bind", "[gold1]⛓[/gold1]", 1, STATUS_DESCS["Bind"], duration=chip.effect_val))
                self.apply_status_logic(attacker, StatusEffect("Haste", "[yellow1]🢙[/yellow1]", 0, STATUS_DESCS["Haste"], duration=chip.effect_val))

            # --- ZHAO FENG SKILL EFFECTS ---
            elif chip.effect_type == "ZHAOFENG_SPECIAL_1":
                self.apply_status_logic(target, StatusEffect("Rupture", "[medium_spring_green]✧[/medium_spring_green]", 2, STATUS_DESCS["Rupture"], duration=1))
                self.apply_status_logic(target, StatusEffect("Sinking", "[blue3]♆[/blue3]", 2, STATUS_DESCS["Sinking"], duration=1, type="DEBUFF"))
            elif chip.effect_type == "ZHAOFENG_SPECIAL_2":
                self.apply_status_logic(target, StatusEffect("Rupture", "[medium_spring_green]✧[/medium_spring_green]", 1, STATUS_DESCS["Rupture"], duration=2))
                self.apply_status_logic(target, StatusEffect("Sinking", "[blue3]♆[/blue3]", 1, STATUS_DESCS["Sinking"], duration=2, type="DEBUFF"))
            elif chip.effect_type in ["ZHAOFENG_SPECIAL_3", "ZHAOFENG_SPECIAL_4"]:
                self.apply_status_logic(target, StatusEffect("Rupture", "[medium_spring_green]✧[/medium_spring_green]", 4, STATUS_DESCS["Rupture"], duration=1))
            elif chip.effect_type in ["ZHAOFENG_SPECIAL_5", "ZHAOFENG_SPECIAL_6"]:
                mal = next((s for s in target.status_effects if s.name == "Malice"), None)
                if mal:
                    heal = min(20, mal.duration * 2)
                    attacker.hp = min(attacker.max_hp, attacker.hp + heal)
                    self.log(f"[hot_pink]{attacker.name} drains Malice to heal {heal} HP![/hot_pink]")
                if chip.effect_type == "ZHAOFENG_SPECIAL_6":
                    self.apply_status_logic(target, StatusEffect("Malice", "[hot_pink]♨[/hot_pink]", 0, STATUS_DESCS["Malice"], duration=3, type="DEBUFF"))
                else:
                    team = self.enemies if target in self.enemies else self.allies
                    living = [u for u in team if u.hp > 0 and u != target]
                    if living:
                        mal_t = [u for u in living if any(s.name == "Malice" for s in u.status_effects)]
                        target = random.choice(mal_t) if mal_t else random.choice(living)
                        self.log(f"[bold magenta]-> {attacker.name} switches focus to {target.name}![/bold magenta]")
            elif chip.effect_type in ["ZHAOFENG_SPECIAL_8", "ZHAOFENG_SPECIAL_9", "ZHAOFENG_SPECIAL_10"]:
                amt = 2 if chip.effect_type == "ZHAOFENG_SPECIAL_8" else (3 if chip.effect_type == "ZHAOFENG_SPECIAL_9" else 4)
                self.apply_status_logic(target, StatusEffect("Blossom", "[hot_pink]❀[/hot_pink]", 0, STATUS_DESCS["Blossom"], duration=amt, type="DEBUFF"))
                team = self.enemies if target in self.enemies else self.allies
                living = [u for u in team if u.hp > 0 and u != target]
                if living:
                    no_blo = [u for u in living if not any(s.name == "Blossom" for s in u.status_effects)]
                    target = random.choice(no_blo) if no_blo else random.choice(living)
                    self.log(f"[bold magenta]-> {attacker.name} switches focus to {target.name}![/bold magenta]")

            # --- KAGEROU SKILL EFFECTS ---
            elif chip.effect_type == "KAGEROU_SPECIAL_1":
                if any(s.name == "Bleed" for s in target.status_effects):
                    self.apply_status_logic(target, StatusEffect("Bleed", "[red]💧︎[/red]", 5, STATUS_DESCS["Bleed"], duration=0, type="DEBUFF"))
                team = self.enemies if target in self.enemies else self.allies
                living = [u for u in team if u.hp > 0 and u != target]
                if living:
                    target = random.choice(living)
                    self.log(f"[bold magenta]-> {attacker.name} switches focus to {target.name}![/bold magenta]")
            elif chip.effect_type == "KAGEROU_SPECIAL_2":
                self.apply_status_logic(target, StatusEffect("Bleed", "[red]💧︎[/red]", 1, STATUS_DESCS["Bleed"], duration=3, type="DEBUFF"))
            elif chip.effect_type == "KAGEROU_SPECIAL_3":
                self.apply_status_logic(attacker, StatusEffect("Poise", "[light_cyan1]༄[/light_cyan1]", 10, STATUS_DESCS["Poise"], duration=0))
            elif chip.effect_type in ["KAGEROU_SPECIAL_4", "KAGEROU_SPECIAL_5"]:
                team = self.enemies if target in self.enemies else self.allies
                living = [u for u in team if u.hp > 0 and u != target]
                if living:
                    target = random.choice(living)
                    self.log(f"[bold magenta]-> {attacker.name} switches focus to {target.name}![/bold magenta]")

            """
            End of STEP 3's elif blocks
            """

            # HP CLAMP FOR AKASUKE DURING 4-25
            self.clamp_akasuke1()
            # HP CLAMP FOR KAGEROU DURING 4-26
            active_tgt_passives = getattr(target, "passives", []) or (getattr(target.kata, "passives", []) if getattr(target, "kata", None) else [])
            if any(p.effect_type == "PASSIVE_KAGEROU_THORN" for p in active_tgt_passives):
                lb = next((s for s in target.status_effects if s.name == "Leaking Bloodlust"), None)
                if (not lb or lb.duration < 99) and target.hp < 1:
                    target.hp = 1

            if target.hp <= 0:
                target.hp = 0
                self.log(f"[bold red]{target.name} was defeated![/bold red]")

            # --- DELAY BETWEEN CHIP HITS ---
            # If this is a multi-hit skill and not the last chip, render the current state and pause
            if len(chips_to_execute) > 1 and chip_idx < len(chips_to_execute) - 1:
                self.render_battle_screen()
                time.sleep(0.75)

        # --- PARALYSIS DECAY ---
        para_eff_end = next((s for s in attacker.status_effects if s.name == "Paralysis"), None)
        if para_eff_end:
            para_eff_end.duration -= 1
            if para_eff_end.duration <= 0:
                attacker.status_effects.remove(para_eff_end)

        self.render_battle_screen()
        time.sleep(0.5)

    def apply_status_logic(self, target, new_status):
        """
        Handles stacking logic (Potency vs Count).
        Implements 'First Time' Application rules for Bleed.
        """
        
        # --- PRE-PROCESS: DELAYED APPLICATION (Bind & Haste only so far) ---
        if new_status.name == "Bind":
            if not hasattr(target, "pending_bind"): target.pending_bind = 0
            target.pending_bind = min(5, target.pending_bind + new_status.duration)
            return
        if new_status.name == "Haste":
            if not hasattr(target, "pending_haste"): target.pending_haste = 0
            target.pending_haste = min(5, target.pending_haste + new_status.duration)
            return
        # --- PRE-PROCESS: DUAL-STACK EFFECTS MINIMUM 1 RULE ---
        if new_status.name in DUAL_STACK_EFFECTS:
            if new_status.duration > 0 and new_status.potency <= 0:
                new_status.potency = 1
            elif new_status.potency > 0 and new_status.duration <= 0:
                new_status.duration = 1

        # --- FIND EXISTING ---
        existing = next((s for s in target.status_effects if s.name == new_status.name), None)
        
        if existing:
            # --- MERGE LOGIC FOR ALL STATUS EFFECTS ---
            if new_status.name in DUAL_STACK_EFFECTS:
                existing.duration = min(99, existing.duration + new_status.duration)
                existing.potency = min(99, existing.potency + new_status.potency)
            elif new_status.name in ["Bind", "Haste", "Pierce Fragility", "Invisibility", "Flickering Invisibility"]:
                existing.duration = min(5, existing.duration + new_status.duration)
            elif new_status.name == "Riposte":
                existing.duration = min(50, existing.duration + new_status.duration)
            elif new_status.name in ["Paralysis", "Leaking Bloodlust"]:
                existing.duration = min(99, existing.duration + new_status.duration)
            elif new_status.name == "Overheat":
                existing.duration = min(3, existing.duration + new_status.duration)
            elif new_status.name == "Cloud Sword [云]":
                existing.duration = min(1, existing.duration + new_status.duration)            
            else:
                # Generic Stacking
                existing.duration += new_status.duration
                existing.potency += new_status.potency
        else:
            # --- NEW APPLICATION (FIRST TIME LOGIC ONLY FOR DUAL STACK EFFECTS WHERE RULES FORCE BOTH STACK TYPES TO HAVE AT LEAST 1) ---
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

        active_passives = getattr(target, "passives", []) or (getattr(target.kata, "passives", []) if getattr(target, "kata", None) else [])
        # INGRAINED COMMAND PARALYSIS CAP (MEI BOSS)
        if new_status.name == "Paralysis" and any(p.effect_type == "PASSIVE_INGRAINED_COMMAND" for p in active_passives):
            new_status.duration = min(1, new_status.duration)
        # BREATHING TECHNIQUES POISE CAP (MEI BOSS)
        if new_status.name == "Poise" and any(p.effect_type == "PASSIVE_BREATHING_TECHNIQUES" for p in active_passives):
            new_status.potency = min(30, new_status.potency)
            new_status.duration = min(30, new_status.duration)
        existing = next((s for s in target.status_effects if s.name == new_status.name), None)
        if existing:
            # Re-cap Poise if merged
            if new_status.name == "Poise" and any(p.effect_type == "PASSIVE_BREATHING_TECHNIQUES" for p in active_passives):
                existing.potency = min(30, existing.potency)
                existing.duration = min(30, existing.duration)
            # Re-cap Paralysis if merged
            elif new_status.name == "Paralysis" and any(p.effect_type == "PASSIVE_INGRAINED_COMMAND" for p in active_passives):
                existing.duration = 1
        # --- ZHAO FENG BOSS PASSIVE (BIND + PARALYSIS IMMUNITY) ---
        active_passives = getattr(target, "passives", []) or (getattr(target.kata, "passives", []) if getattr(target, "kata", None) else [])
        if any(p.effect_type == "PASSIVE_CRUMBLING_FORM" for p in active_passives):
            if new_status.name in ["Paralysis", "Bind"]:
                return # Immune
                
        # --- PRE-PROCESS: DELAYED APPLICATION (Bind & Haste) ---
        # ... (Rest of the method continues as normal)

            """
            End of execute_skill()
            """

    def inspect_unit_menu(self):
        clear_screen()
        config.console.print(Panel("[bold]INSPECT MODE[/bold]", style="white on blue"))
        
        all_units = self.allies + self.enemies
        for idx, unit in enumerate(all_units):
            config.console.print(f"[{idx+1}] {unit.name}", highlight=False)
        
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

            # --- EXTERNAL SKILL POOL LOGIC ---
            external_pool_text = ""
            external_skills_list = []  # Store for input handling
            
            if hasattr(unit, "appendable_skills") and unit.appendable_skills:
                external_pool_text += "\n[bold]External Skill Pool:[/bold]\n"
                
                # Sort by order of found Skills (Meaning we can design the list order in stages.py ourselves!)
                sorted_external = sorted(unit.appendable_skills.items())
                for idx, (_, skill) in enumerate(sorted_external):
                    external_skills_list.append(skill)
                    c = get_element_color(skill.element)
                    t_r = get_tier_roman(skill.tier)
                    dmg_str = f"[bold]Dmg: {skill.base_damage}[/bold]"
                    
                    # Just print the summary line with the EX index
                    external_pool_text += f"[bold light_green]EX{idx+1}[/bold light_green]: [{c}]{skill.name}[/{c}] ({t_r}) {dmg_str}\n"

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
{pool_text}{external_pool_text}
            """
            layout = Layout()
            layout.split_row(Layout(Panel(content)), Layout(Panel(res_table)))
            config.console.print(layout, highlight=False)
            config.console.print("\nType [bold]SE#[/bold] to view status details, [bold]P#[/bold] to view passive details, [bold]EX#[/bold] for external skills, or [Enter] to return.")
            
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
                        disp_desc = STATUS_DESCS["Fairylight"]
                    elif disp_name == "Rupture":
                        disp_desc = STATUS_DESCS["Rupture"]
                    
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

            # --- EXTERNAL SKILL EXPANSION INPUT ---
            elif choice.startswith("EX") and choice[2:].isdigit():
                idx = int(choice[2:]) - 1
                
                if hasattr(unit, "appendable_skills") and unit.appendable_skills:
                    if 0 <= idx < len(external_skills_list):
                        skill = external_skills_list[idx]
                        c = get_element_color(skill.element)
                        t_r = get_tier_roman(skill.tier)
                        
                        if hasattr(skill, "inspect_description") and skill.inspect_description:
                            desc = skill.inspect_description
                        else:
                            desc = skill.description if skill.description else ""
                            
                        dmg_str = f"[bold]Dmg: {skill.base_damage}[/bold]"
                        formatted_desc = desc.replace("\n", "\n")
                        
                        # Preserve original element colors and description formatting
                        skill_content = f"[{c}]{skill.name}[/{c}][white] ({t_r}) {dmg_str}[/white]\n       [light_green]{formatted_desc}[/light_green]"
                        
                        config.console.print(Panel(skill_content, title="External Skill", style="light_green"))
                        get_player_input("Press Enter...")

    def check_win_condition(self):
        if all(e.hp <= 0 for e in self.enemies):
            self.is_battle_over = True; self.won = True; return True
        return False

    def check_loss_condition(self):
        if all(a.hp <= 0 for a in self.allies):
            self.is_battle_over = True; self.won = False; return True
        return False

    def clamp_akasuke1(self):
        zhao_alive = any(e.name == "Zhao Feng" and e.hp > 0 for e in self.enemies)
        if zhao_alive:
            for ally in self.allies:
                if ally.name == "Akasuke" and ally.hp < 1:
                    if any(a.name != "Akasuke" and a.hp > 0 for a in self.allies):
                        ally.hp = 1

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