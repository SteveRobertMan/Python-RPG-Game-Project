import sys
import time
import random
from rich.panel import Panel 
from rich.console import Console 
import config
import scd
from player_state import player

if not hasattr(config, "console"): config.console = Console()
if not hasattr(config, "current_state"):
    config.STATE_TITLE = "TITLE"
    config.STATE_PROLOGUE = "PROLOGUE"
    config.STATE_BATTLE = "BATTLE"
    config.STATE_MAIN_MENU = "MAIN_MENU"
    config.STATE_STAGE_SELECT = "STAGE_SELECT"
    config.STATE_COUNCIL_LOGS = "COUNCIL_LOGS"
    config.STATE_NODE_SELECT = "NODE_SELECT"
    config.STATE_PARTY_MANAGEMENT = "PARTY_MANAGEMENT"
    config.current_state = config.STATE_TITLE
    config.player_data = {}
    
console = config.console

import stages
import story_manager
from ui_components import draw_title_screen, get_player_input, clear_screen, draw_stage_select_menu, draw_council_logs_menu, draw_bestiary_menu, draw_material_logs, draw_node_select_menu, draw_party_management_menu
from save_system import save_manager
from battle_system import battle_manager
from gacha_system import gacha_system 
from player_state import player 
from entities import MATERIALS_DB

def sync_currencies():
    if "materials" in config.player_data:
        mats = config.player_data["materials"]
        player.currencies["microchips"] = mats.get("Microchip", 0)
        player.currencies["microprocessors"] = mats.get("Microprocessor", 0)

def handle_title_screen():
    draw_title_screen()
    choice = get_player_input("Enter Option Key: ")
    if choice == "1":
        config.player_data = save_manager.data.copy()
        config.player_data["latest_stage"] = -1 
        config.player_data["materials"] = {"Microchip": 50, "Microprocessor": 10}
        config.player_data["cleared_stages"] = [] 
        config.player_data["node_progress"] = None 
        sync_currencies() 
        config.current_state = config.STATE_PROLOGUE
    elif choice == "2":
        console_print_load_prompt()
    elif choice == "3":
        confirm_quit()
    else:
        console.print("[red]Invalid Option![/red]")
        get_player_input("Press Enter to try again...")

def console_print_load_prompt():
    clear_screen()
    console.print("[bold cyan]Paste your Save Strip below:[/bold cyan]")
    strip = get_player_input()
    
    # 1. Parse the strip into a dictionary
    loaded_data = save_manager.load_save_strip(strip)
    
    if loaded_data:
        # 2. Update Global Config (Stages, Node Progress)
        config.player_data = loaded_data
        
        if "node_progress" not in config.player_data: 
            config.player_data["node_progress"] = None
        
        # 3. CRITICAL FIX: Inject Inventory into Player Object
        # The save manager returns 'katas' as a list of dicts: [{'name':..., 'aptitude':...}]
        # We must put this where the Gacha/UI expects it: player.inventory
        player.inventory["katas"] = loaded_data.get("katas", [])
        
        # 4. Clean up Config (Optional but clean)
        # We remove it from the global dict so we don't have two sources of truth
        if "katas" in config.player_data:
            del config.player_data["katas"]
        
        # 5. Sync Currencies
        # This function (defined in main.py) usually maps config['materials'] -> player.currencies
        sync_currencies() 
        
        console.print("[green]Save Loaded Successfully![/green]")
        
        # 6. Determine State
        if config.player_data.get("latest_stage", -1) == -1: 
            config.current_state = config.STATE_PROLOGUE
        else: 
            config.current_state = config.STATE_MAIN_MENU
            
        get_player_input("Press Enter to continue...")
    else:
        console.print("[bold red]Invalid Save Strip![/bold red]")
        get_player_input("Press Enter to return to Title...")

def confirm_quit():
    clear_screen()
    console.print(Panel("Are you sure you want to quit?", style="bold red"))
    console.print("[1] Yes (Generate Save Strip)\n[0] No")
    
    choice = get_player_input()
    
    if choice == "1":
        # CRITICAL FIX: Pass the 'player' instance, NOT 'config.player_data'
        # The save manager needs to access player.inventory and player.currencies
        if player:
            # Sync any stage progress first just in case
            # (Assuming stage logic updates config.player_data, 
            # save_manager reads that from config global, but reads inventory from player object)
            strip = save_manager.generate_save_strip(player)
            
            console.print(f"\n[bold]Here is your Save Strip, copy it:[/bold]\n")
            console.print(Panel(f"{strip}", style="yellow"))
            console.print("\n[dim]Select text and Ctrl+C to copy.[/dim]")
            
        get_player_input("Press Enter to exit...")
        sys.exit()

def sync_player_roster():
    """
    Checks player's progress and permanently adds unlocked characters 
    to player.units if they are missing.
    """
    latest = config.player_data.get("latest_stage", 0)
    
    # Get list of names currently in our persistent roster
    current_roster_names = [u.name for u in player.units]

    # Definition of Unlocks: (Name, Required Stage Clear, Factory Function)
    # Note: stages.py has these create functions.
    unlock_milestones = [
        ("Akasuke", 0, stages.create_akasuke),
        ("Yuri", 0, stages.create_yuri),
        ("Benikawa", 4, stages.create_benikawa),
        ("Shigemura", 15, stages.create_shigemura),
        ("Naganohara", 24, stages.create_naganohara)
    ]

    for name, req_stage, factory_func in unlock_milestones:
        # If we passed the stage AND we don't have the unit yet:
        if latest >= req_stage and name not in current_roster_names:
            new_member = factory_func()
            
            # Ensure the unit knows it's a player unit (crucial for UI/Save)
            new_member.is_player = True 
            
            player.units.append(new_member)
            
            # Optional: Notify console purely for debug
            # config.console.print(f"[dim]Debug: Added {name} to persistent roster.[/dim]")

def get_equipped_data(unit_name):
    """
    Searches the persistent player roster for a specific unit.
    If found, returns a dictionary packet formatted for stages.create_X().
    If not found (e.g., first time meeting), returns None.
    """
    # 1. Find the unit in persistent storage
    found_unit = next((u for u in player.units if u.name == unit_name), None)
    
    if found_unit:
        # 2. Package the data exactly how create_naganohara expects it
        return {
            "kata_obj": found_unit.kata,         # The equipped Kata object
            "max_hp": found_unit.max_hp,         # The modified HP
            "description": found_unit.description # The modified Lore
        }
    
    return None

def run_game():
    while True:
        if config.current_state == config.STATE_TITLE:
            handle_title_screen()
            
        elif config.current_state == config.STATE_PROLOGUE:
            story_manager.play_prologue()
            config.current_state = config.STATE_BATTLE
            
        elif config.current_state == config.STATE_BATTLE:
            # 1. Get Base Party
            party = stages.get_player_party()
            
            # 2. Identify Stage
            stage_id = config.player_data.get("selected_stage", 0) 
            if config.player_data.get("latest_stage", 0) == -1: stage_id = 0

            ### GUEST INJECTION LOGIC ###
            # --- BENIKAWA INJECTION LOGIC ---
            latest_cleared = config.player_data.get("latest_stage", -1)
            
            if (latest_cleared >= 4 or stage_id == 4) and stage_id != 7:
                has_beni = any(u.name == "Benikawa" for u in party)
                if not has_beni:
                    # UPDATED: Pass the persistent loadout data
                    loadout = get_equipped_data("Benikawa")
                    party.append(stages.create_benikawa(loadout))
            
            if stage_id == 7:
                party = [p for p in party if p.name != "Benikawa"]

            # --- SHIGEMURA INJECTION LOGIC ---
            if (latest_cleared >= 15 or stage_id in [151,152,153]):
                has_shige = any(u.name == "Shigemura" for u in party)
                if not has_shige:
                    # UPDATED: Pass the persistent loadout data
                    loadout = get_equipped_data("Shigemura")
                    party.append(stages.create_shigemura(loadout))
            
            # --- NAGANOHARA INJECTION LOGIC ---
            is_guest_appearance = (stage_id == 16 or stage_id in [161, 162, 163, 164, 165])
            is_officially_unlocked = (latest_cleared >= 24)
            if is_guest_appearance:
                has_naga = any(u.name == "Naganohara" for u in party)
                
                if not has_naga:
                    if is_guest_appearance:
                        guest_loadout = scd.get_kata_data_by_name("Heiwa Seiritsu High School Student (Naganohara)")
                        party.append(stages.create_naganohara(guest_loadout))
                    elif is_officially_unlocked:
                        loadout = get_equipped_data("Naganohara")
                        party.append(stages.create_naganohara(loadout))

            # --- AKASUKE SPECIAL INJECTION LOGIC ---
            if stage_id == 21:
                # 1. Fetch the forced Guest Data
                guest_loadout = scd.get_kata_data_by_name("‘Iron Fist Of Heiwa’ Delinquent Leader")
                guest_akasuke = stages.create_akasuke(guest_loadout)
                
                # 2. Check if Akasuke is already in the party
                aka_index = -1
                for i, unit in enumerate(party):
                    if unit.name == "Akasuke":
                        aka_index = i
                        break
                
                # 3. Inject Logic
                if aka_index != -1:
                    # FOUND: Replace the player's Akasuke with the Guest Version
                    # This ensures no clones, and forces the guest stats/loadout
                    party[aka_index] = guest_akasuke
                    #print("Existing Akasuke swapped for Guest Version.")
                else:
                    # NOT FOUND: Add the Guest Akasuke to the end
                    party.append(guest_akasuke)
                    #print("Guest Akasuke added to party.")

            # Stage 6 Special: Akasuke Solo
            if stage_id == 6:
                party = [member for member in party if member.name == "Akasuke"]

            # Stage 18-21 Special: Akasuke, Yuri, Benikawa only team
            if stage_id in [18,19,20,21]:
                party = [member for member in party if member.name in ["Akasuke","Yuri","Benikawa"]]
            
            enemies = stages.load_stage_enemies(stage_id)
            if not enemies:
                console.print("[red]Error: Enemies not found for this stage![/red]")
                time.sleep(2)
                config.current_state = config.STATE_MAIN_MENU
                continue

            # Story Pre-Battle Check
            should_play_story = True
            if stage_id > 0 and latest_cleared >= stage_id: should_play_story = False
            if stage_id == 0 and latest_cleared >= 0: should_play_story = False

            if should_play_story:
                if stage_id == 2: story_manager.play_stage_1_2_start()
                elif stage_id == 4: story_manager.play_stage_1_4_start()
                elif stage_id == 6: story_manager.play_stage_1_6_start()
                elif stage_id == 7: story_manager.play_stage_1_7_start()
                elif stage_id == 18: story_manager.play_stage_2_7_start()
                elif stage_id == 19: story_manager.play_stage_2_8_start()
                elif stage_id == 20: story_manager.play_stage_2_9_start()
                elif stage_id == 21: story_manager.play_stage_2_10_start()

            battle_manager.start_battle(party, enemies, stage_id)
            
            clear_screen()
            if battle_manager.won:
                console.print("[bold green]VICTORY![/bold green]")
                
                rewards_text = []
                mats = config.player_data["materials"]
                
                # --- NODE STAGE HANDLING (Unified Logic) ---
                # Check if this battle belongs to the currently active Node Stage
                np = config.player_data.get("node_progress")
                
                # SAFEGUARD & VALIDATION
                is_valid_node_battle = False
                
                # 1. We must have active node progress (np)
                # 2. The battle ID (e.g. 51) divided by 10 must match the active Stage ID (e.g. 5)
                if np is not None:
                    parent_of_current_stage = stage_id // 10
                    if parent_of_current_stage == np["stage"]:
                        is_valid_node_battle = True

                # ONLY execute if validation passed
                if is_valid_node_battle: 
                    is_first_node_clear = stage_id not in config.player_data.get("cleared_stages", [])

                            # --- 1. REWARD DISTRIBUTION ---
                            
                            # >> STAGE 1-5 (IDs 51, 52, 53)
                    if np["stage"] == 5:
                        if stage_id in [51, 52]:
                            if is_first_node_clear:
                                rewards_text.extend(["2x Microchip", "2x Microprocessor"])
                                mats["Microchip"] = mats.get("Microchip", 0) + 2
                                mats["Microprocessor"] = mats.get("Microprocessor", 0) + 2
                            else:
                                if random.random() < 0.25:
                                    rewards_text.append("1x Cafeteria Melon Bread")
                                    mats["Cafeteria Melon Bread"] = mats.get("Cafeteria Melon Bread", 0) + 1
                        elif stage_id == 53:
                            if is_first_node_clear:
                                rewards_text.extend(["2x Microchip", "2x Microprocessor", "2x Cafeteria Melon Bread"])
                                mats["Microchip"] = mats.get("Microchip", 0) + 2
                                mats["Microprocessor"] = mats.get("Microprocessor", 0) + 2
                                mats["Cafeteria Melon Bread"] = mats.get("Cafeteria Melon Bread", 0) + 2
                            else:
                                if random.random() < 0.50:
                                    rewards_text.append("1x Cafeteria Melon Bread")
                                    mats["Cafeteria Melon Bread"] = mats.get("Cafeteria Melon Bread", 0) + 1

                    # >> STAGE 1-10 (IDs 101, 102, 103, 104)
                    elif np["stage"] == 10:
                        if stage_id in [101, 102]:
                            if is_first_node_clear:
                                rewards_text.extend(["2x Microchip", "2x Microprocessor"])
                                mats["Microchip"] = mats.get("Microchip", 0) + 2
                                mats["Microprocessor"] = mats.get("Microprocessor", 0) + 2
                            else:
                                if random.random() < 0.30:
                                    rewards_text.append("1x Microchip")
                                    mats["Microchip"] = mats.get("Microchip", 0) + 1
                        elif stage_id in [103, 104]:
                            if is_first_node_clear:
                                rewards_text.extend(["3x Microchip", "3x Microprocessor"])
                                mats["Microchip"] = mats.get("Microchip", 0) + 3
                                mats["Microprocessor"] = mats.get("Microprocessor", 0) + 3
                            else:
                                if random.random() < 0.30:
                                    rewards_text.append("1x Microprocessor")
                                    mats["Microprocessor"] = mats.get("Microprocessor", 0) + 1

                    # >> STAGE 2-3 (IDs 141, 142)
                    elif np["stage"] == 14:
                        if stage_id in [141, 142]:
                            if is_first_node_clear:
                                rewards_text.extend(["1x Cafeteria Melon Bread", "1x Vending Machine Coffee"])
                                mats["Cafeteria Melon Bread"] = mats.get("Cafeteria Melon Bread", 0) + 1
                                mats["Vending Machine Coffee"] = mats.get("Vending Machine Coffee", 0) + 1
                            else:
                                if random.random() < 0.25:
                                    rewards_text.append("1x Cafeteria Melon Bread")
                                    mats["Cafeteria Melon Bread"] = mats.get("Cafeteria Melon Bread", 0) + 1
                                if random.random() < 0.25:
                                    rewards_text.append("1x Vending Machine Coffee")
                                    mats["Vending Machine Coffee"] = mats.get("Vending Machine Coffee", 0) + 1

                    # >> STAGE 2-4 (IDs 151, 152, 153)
                    elif np["stage"] == 15:
                        if stage_id in [151, 152, 153]:
                            if is_first_node_clear:
                                rewards_text.extend(["1x Microchip", "1x Microprocessor"])
                                mats["Microchip"] = mats.get("Microchip", 0) + 1
                                mats["Microprocessor"] = mats.get("Microprocessor", 0) + 1                            
                            else:
                                if random.random() < 0.25:
                                    rewards_text.append("1x Cafeteria Melon Bread")
                                    mats["Cafeteria Melon Bread"] = mats.get("Cafeteria Melon Bread", 0) + 1
                                if random.random() < 0.25:
                                    rewards_text.append("1x Vending Machine Coffee")
                                    mats["Vending Machine Coffee"] = mats.get("Vending Machine Coffee", 0) + 1

                    # >> STAGE 2-5 (IDs 161, 162, 163, 164, 165)
                    elif np["stage"] == 16:
                        if stage_id in [161, 162]: # Nodes 1 & 2
                            if is_first_node_clear:
                                rewards_text.append("2x Microchip")
                                mats["Microchip"] = mats.get("Microchip", 0) + 2
                            else:
                                if random.random() < 0.50:
                                    rewards_text.append("1x Vending Machine Coffee")
                                    mats["Vending Machine Coffee"] = mats.get("Vending Machine Coffee", 0) + 1
                        elif stage_id in [163, 164]: # Nodes 3 & 4
                            if is_first_node_clear:
                                rewards_text.append("2x Vending Machine Coffee")
                                mats["Vending Machine Coffee"] = mats.get("Vending Machine Coffee", 0) + 2
                            else:
                                if random.random() < 0.50:
                                    rewards_text.append("1x Vending Machine Coffee")
                                    mats["Vending Machine Coffee"] = mats.get("Vending Machine Coffee", 0) + 1
                        elif stage_id == 165: # Node 5
                            if is_first_node_clear:
                                rewards_text.append("3x Cafeteria Melon Bread")
                                mats["Cafeteria Melon Bread"] = mats.get("Cafeteria Melon Bread", 0) + 3
                            else:
                                if random.random() < 0.50:
                                    rewards_text.append("1x Vending Machine Coffee")
                                    mats["Vending Machine Coffee"] = mats.get("Vending Machine Coffee", 0) + 1

                            # --- 2. HP PERSISTENCE & HEALING (Unified) ---
                            for p in party:
                                if p.hp > 0:
                                    missing = p.max_hp - p.hp
                                    heal = missing // 2
                                    p.hp += heal
                                    if heal > 0: console.print(f"{p.name} recovers {heal} HP.")
                                np["party_hp"][p.name] = p.hp

                    # --- 3. PROGRESS TRACKING (The Fix) ---
                    # Calculate Index: 51 - 50 - 1 = 0
                    node_idx = stage_id - (np["stage"] * 10) - 1
                    
                    if node_idx not in np["cleared_indices"]:
                        np["cleared_indices"].append(node_idx)
                        # CRITICAL: Force save back to config to ensure persistence
                        config.player_data["node_progress"] = np

                    # --- 4. COMPLETION CHECK ---
                    nodes_required_map = {5: 3, 10: 4, 14: 2, 15: 3, 16: 5}
                    req_count = nodes_required_map.get(np["stage"], 99)

                    if len(np["cleared_indices"]) >= req_count:
                        # -- STAGE COMPLETE --
                        stage_name_map = {5: "1-5", 10: "1-10", 14: "2-3", 15: "2-4", 16: "2-5"}
                        s_name = stage_name_map.get(np["stage"], "??")
                        console.print(f"[bold green]STAGE {s_name} COMPLETE![/bold green]")

                        # Play Story / Update Latest Stage
                        if config.player_data["latest_stage"] < np["stage"]:
                            if np["stage"] == 10:
                                story_manager.play_stage_1_10_end()
                            elif np["stage"] == 14:
                                story_manager.play_stage_2_3_end()
                            elif np["stage"] == 15:
                                story_manager.play_stage_2_4_end()
                                rewards_text.append("[bold magenta]NEW MEMBER: Shigemura[/bold magenta]")
                            elif np["stage"] == 16:
                                story_manager.play_stage_2_5_end()
                            
                            config.player_data["latest_stage"] = np["stage"]

                        # Cleanup & Save to Permanent Cleared List
                        cl = config.player_data.get("cleared_stages", [])
                        
                        # Add individual nodes to cleared list so they don't drop First Clear rewards again
                        start_id = (np["stage"] * 10) + 1
                        for i in range(req_count):
                            nid = start_id + i
                            if nid not in cl: cl.append(nid)
                        
                        config.player_data["cleared_stages"] = cl
                        config.player_data["node_progress"] = None # Reset progress

                        config.current_state = config.STATE_MAIN_MENU
                    else:
                        # -- STAGE ONGOING --
                        config.current_state = config.STATE_NODE_SELECT

                # --- STANDARD STAGES ---
                else:
                    if stage_id == 0: 
                        console.print("Tutorial Cleared.")
                        if config.player_data["latest_stage"] < 0: config.player_data["latest_stage"] = 0
                    
                    elif stage_id == 2:
                        if should_play_story:
                            story_manager.play_stage_1_2_end()
                            rewards_text.extend(["3x Microchip", "3x Microprocessor"])
                            mats["Microchip"] = mats.get("Microchip", 0) + 3
                            mats["Microprocessor"] = mats.get("Microprocessor", 0) + 3
                            if config.player_data["latest_stage"] < 2: config.player_data["latest_stage"] = 2
                            cl = config.player_data.get("cleared_stages", [])
                            if 2 not in cl: cl.append(2); config.player_data["cleared_stages"] = cl
                        else:
                            if random.random() < 0.25: rewards_text.append("1x Microchip"); mats["Microchip"] = mats.get("Microchip", 0) + 1
                            if random.random() < 0.25: rewards_text.append("1x Cafeteria Melon Bread"); mats["Cafeteria Melon Bread"] = mats.get("Cafeteria Melon Bread", 0) + 1

                    elif stage_id == 4:
                        if should_play_story:
                            story_manager.play_stage_1_4_end()
                            rewards_text.extend(["3x Microchip", "3x Microprocessor", "[bold magenta]NEW MEMBER: Benikawa[/bold magenta]"])
                            mats["Microchip"] = mats.get("Microchip", 0) + 3
                            mats["Microprocessor"] = mats.get("Microprocessor", 0) + 3
                            if config.player_data["latest_stage"] < 4: config.player_data["latest_stage"] = 4
                            cl = config.player_data.get("cleared_stages", [])
                            if 4 not in cl: cl.append(4); config.player_data["cleared_stages"] = cl
                        else:
                            if random.random() < 0.50: rewards_text.append("1x Cafeteria Melon Bread"); mats["Cafeteria Melon Bread"] = mats.get("Cafeteria Melon Bread", 0) + 1
                    
                    elif stage_id == 6:
                        if should_play_story:
                            story_manager.play_stage_1_6_end()
                            rewards_text.extend(["3x Microchip", "3x Microprocessor"])
                            mats["Microchip"] = mats.get("Microchip", 0) + 3
                            mats["Microprocessor"] = mats.get("Microprocessor", 0) + 3
                            if config.player_data["latest_stage"] < 6: config.player_data["latest_stage"] = 6
                            cl = config.player_data.get("cleared_stages", [])
                            if 6 not in cl: cl.append(6); config.player_data["cleared_stages"] = cl
                        else:
                            if random.random() < 0.50: rewards_text.append("1x Cafeteria Melon Bread"); mats["Cafeteria Melon Bread"] = mats.get("Cafeteria Melon Bread", 0) + 1

                    elif stage_id == 7:
                        if should_play_story:
                            story_manager.play_stage_1_7_end()
                            rewards_text.extend(["5x Microchip", "5x Microprocessor"])
                            mats["Microchip"] = mats.get("Microchip", 0) + 5
                            mats["Microprocessor"] = mats.get("Microprocessor", 0) + 5
                            if config.player_data["latest_stage"] < 7: config.player_data["latest_stage"] = 7
                            cl = config.player_data.get("cleared_stages", [])
                            if 7 not in cl: cl.append(7); config.player_data["cleared_stages"] = cl
                        else:
                            if random.random() < 0.50: rewards_text.append("1x Cafeteria Melon Bread"); mats["Cafeteria Melon Bread"] = mats.get("Cafeteria Melon Bread", 0) + 1

                    elif stage_id == 8: # Rewards for 1-8 replay
                        if random.random() < 0.50: rewards_text.append("1x Microchip"); mats["Microchip"] = mats.get("Microchip", 0) + 1

                    elif stage_id == 9: # Rewards for 1-9 replay
                        if random.random() < 0.50: rewards_text.append("1x Microprocessor"); mats["Microprocessor"] = mats.get("Microprocessor", 0) + 1

                    elif stage_id == 18:
                        if should_play_story:
                            story_manager.play_stage_2_7_end()
                            rewards_text.extend(["3x Microchip", "3x Microprocessor"])
                            mats["Microchip"] = mats.get("Microchip", 0) + 3
                            mats["Microprocessor"] = mats.get("Microprocessor", 0) + 3
                            if config.player_data["latest_stage"] < 18: config.player_data["latest_stage"] = 18
                            cl = config.player_data.get("cleared_stages", [])
                            if 18 not in cl: cl.append(18); config.player_data["cleared_stages"] = cl
                        else:
                            if random.random() < 0.65: rewards_text.append("1x Microchip"); mats["Microchip"] = mats.get("Microchip", 0) + 1
                            if random.random() < 0.65: rewards_text.append("1x Microprocessor"); mats["Microprocessor"] = mats.get("Microprocessor", 0) + 1

                    elif stage_id == 19:
                        if should_play_story:
                            story_manager.play_stage_2_8_end()
                            rewards_text.extend(["3x Microchip", "3x Microprocessor"])
                            mats["Microchip"] = mats.get("Microchip", 0) + 3
                            mats["Microprocessor"] = mats.get("Microprocessor", 0) + 3
                            if config.player_data["latest_stage"] < 19: config.player_data["latest_stage"] = 19
                            cl = config.player_data.get("cleared_stages", [])
                            if 19 not in cl: cl.append(19); config.player_data["cleared_stages"] = cl
                        else:
                            if random.random() < 0.65: rewards_text.append("1x Microchip"); mats["Microchip"] = mats.get("Microchip", 0) + 1
                            if random.random() < 0.65: rewards_text.append("1x Microprocessor"); mats["Microprocessor"] = mats.get("Microprocessor", 0) + 1

                    elif stage_id == 20:
                        if should_play_story:
                            story_manager.play_stage_2_9_end()
                            rewards_text.extend(["3x Microchip", "3x Microprocessor"])
                            mats["Microchip"] = mats.get("Microchip", 0) + 3
                            mats["Microprocessor"] = mats.get("Microprocessor", 0) + 3
                            if config.player_data["latest_stage"] < 20: config.player_data["latest_stage"] = 20
                            cl = config.player_data.get("cleared_stages", [])
                            if 20 not in cl: cl.append(20); config.player_data["cleared_stages"] = cl
                        else:
                            if random.random() < 0.65: rewards_text.append("1x Microchip"); mats["Microchip"] = mats.get("Microchip", 0) + 1
                            if random.random() < 0.65: rewards_text.append("1x Microprocessor"); mats["Microprocessor"] = mats.get("Microprocessor", 0) + 1

                    elif stage_id == 21:
                        if should_play_story:
                            story_manager.play_stage_2_10_end()
                            rewards_text.extend(["3x Microchip", "3x Microprocessor"])
                            mats["Microchip"] = mats.get("Microchip", 0) + 3
                            mats["Microprocessor"] = mats.get("Microprocessor", 0) + 3
                            if config.player_data["latest_stage"] < 21: config.player_data["latest_stage"] = 21
                            cl = config.player_data.get("cleared_stages", [])
                            if 21 not in cl: cl.append(21); config.player_data["cleared_stages"] = cl
                        else:
                            if random.random() < 0.65: rewards_text.append("1x Microchip"); mats["Microchip"] = mats.get("Microchip", 0) + 1
                            if random.random() < 0.65: rewards_text.append("1x Microprocessor"); mats["Microprocessor"] = mats.get("Microprocessor", 0) + 1

                    config.current_state = config.STATE_MAIN_MENU

                if rewards_text:
                    console.print("[bold yellow]REWARDS:[/bold yellow]")
                    for r in rewards_text: console.print(f"- {r}")
                else:
                    if stage_id != 0 and stage_id < 50: console.print("[dim]No drops this time.[/dim]")

                sync_currencies()
            else:
                # DEFEAT / RETREAT
                console.print("[bold red]DEFEAT...[/bold red]")
                if config.player_data.get("node_progress"):
                    config.player_data["node_progress"] = None
                    console.print("[red]Node Stage Progress Lost![/red]")
                
                config.current_state = config.STATE_MAIN_MENU 
            
            get_player_input("Press Enter to continue...")

        elif config.current_state == config.STATE_MAIN_MENU:
            sync_player_roster()
            if config.player_data.get("node_progress"):
                config.current_state = config.STATE_NODE_SELECT
                continue

            clear_screen()
            console.print(Panel("[bold]MAIN MENU[/bold]", style="blue"))
            console.print(f"Current Stage: {config.player_data.get('latest_stage', 0)}")
            sync_currencies()
            console.print("\n[1] Stage Select")
            console.print("[2] Gacha (Parallaxis)")
            console.print("[3] Council Logs")
            console.print("[4] Party Management") # <--- NEW OPTION
            console.print("[5] Save & Quit")
            choice = get_player_input("Select Option: ")
            if choice == "1":
                config.current_state = config.STATE_STAGE_SELECT
            elif choice == "2": 
                gacha_system.run_gacha_menu()
                config.player_data["materials"]["Microchip"] = player.currencies["microchips"]
                config.player_data["materials"]["Microprocessor"] = player.currencies["microprocessors"]
            elif choice == "3": config.current_state = config.STATE_COUNCIL_LOGS
            elif choice == "4": 
                config.current_state = config.STATE_PARTY_MANAGEMENT
            elif choice == "5": confirm_quit()

        elif config.current_state == config.STATE_STAGE_SELECT:
            unlocked = config.player_data.get("latest_stage", 0)
            choice = draw_stage_select_menu(unlocked)
            if choice == "0": config.current_state = config.STATE_MAIN_MENU
            
            elif choice == "1-1":
                if unlocked >= 0:
                    if unlocked >= 1:
                        console.print("[dim]Stage Cleared.[/dim]")
                        time.sleep(0.5)
                    else:
                        story_manager.play_stage_1_1_story()
                        console.print("[bold yellow]First Clear Rewards:[/bold yellow]")
                        console.print("3x Microchip")
                        console.print("3x Microprocessor")
                        mats = config.player_data["materials"]
                        mats["Microchip"] = mats.get("Microchip", 0) + 3
                        mats["Microprocessor"] = mats.get("Microprocessor", 0) + 3
                        if config.player_data["latest_stage"] < 1: config.player_data["latest_stage"] = 1
                        sync_currencies()
                        get_player_input("Press Enter...")
                else:
                    console.print("[red]Locked![/red]")
                    time.sleep(1)
            
            elif choice == "1-2":
                if unlocked >= 1:
                    config.player_data["selected_stage"] = 2
                    config.current_state = config.STATE_BATTLE
                else:
                    console.print("[red]Locked![/red]")
                    time.sleep(1)

            elif choice == "1-3":
                if unlocked >= 2:
                    if unlocked >= 3:
                        console.print("[dim]Stage Cleared.[/dim]")
                        time.sleep(0.5)
                    else:
                        story_manager.play_stage_1_3_story()
                        console.print("[bold yellow]First Clear Rewards:[/bold yellow]")
                        console.print("3x Microchip")
                        console.print("3x Microprocessor")
                        mats = config.player_data["materials"]
                        mats["Microchip"] = mats.get("Microchip", 0) + 3
                        mats["Microprocessor"] = mats.get("Microprocessor", 0) + 3
                        if config.player_data["latest_stage"] < 3: config.player_data["latest_stage"] = 3
                        sync_currencies()
                        get_player_input("Press Enter...")
                else:
                    console.print("[red]Locked![/red]")
                    time.sleep(1)

            elif choice == "1-4":
                if unlocked >= 3:
                    config.player_data["selected_stage"] = 4
                    config.current_state = config.STATE_BATTLE
                else:
                    console.print("[red]Locked![/red]")
                    time.sleep(1)

            elif choice == "1-5":
                if unlocked >= 4:
                    latest = config.player_data.get("latest_stage", 0)
                    if latest < 5:
                        story_manager.play_stage_1_5_start()
                    
                    config.player_data["node_progress"] = {
                        "stage": 5,
                        "cleared_indices": [],
                        "party_hp": {}
                    }
                    config.current_state = config.STATE_NODE_SELECT
                else:
                    console.print("[red]Locked![/red]")
                    time.sleep(1)

            elif choice == "1-6":
                if unlocked >= 5:
                    config.player_data["selected_stage"] = 6
                    config.current_state = config.STATE_BATTLE
                else:
                    console.print("[red]Locked![/red]")
                    time.sleep(1)

            elif choice == "1-7":
                if unlocked >= 6:
                    config.player_data["selected_stage"] = 7
                    config.current_state = config.STATE_BATTLE
                else:
                    console.print("[red]Locked![/red]")
                    time.sleep(1)

            elif choice == "1-8":
                if unlocked >= 7:
                    if unlocked >= 8:
                        console.print("[dim]Stage Cleared.[/dim]")
                        time.sleep(0.5)
                    else:
                        story_manager.play_stage_1_8_story()
                        console.print("[bold yellow]First Clear Rewards:[/bold yellow]")
                        console.print("2x Microchip")
                        console.print("2x Microprocessor")
                        
                        mats = config.player_data["materials"]
                        mats["Microchip"] = mats.get("Microchip", 0) + 2
                        mats["Microprocessor"] = mats.get("Microprocessor", 0) + 2
                        
                        if config.player_data["latest_stage"] < 8: 
                            config.player_data["latest_stage"] = 8
                        
                        cl = config.player_data.get("cleared_stages", [])
                        if 8 not in cl: 
                            cl.append(8)
                            config.player_data["cleared_stages"] = cl

                        sync_currencies()
                        get_player_input("Press Enter...")
                else:
                    console.print("[red]Locked![/red]")
                    time.sleep(1)
            
            elif choice == "1-9":
                if unlocked >= 8:
                    if unlocked >= 9:
                        console.print("[dim]Stage Cleared.[/dim]")
                        time.sleep(0.5)
                    else:
                        story_manager.play_stage_1_9_story()
                        console.print("[bold yellow]First Clear Rewards:[/bold yellow]")
                        console.print("2x Microchip")
                        console.print("2x Microprocessor")
                        
                        mats = config.player_data["materials"]
                        mats["Microchip"] = mats.get("Microchip", 0) + 2
                        mats["Microprocessor"] = mats.get("Microprocessor", 0) + 2
                        
                        if config.player_data["latest_stage"] < 9: 
                            config.player_data["latest_stage"] = 9
                        
                        cl = config.player_data.get("cleared_stages", [])
                        if 9 not in cl: 
                            cl.append(9)
                            config.player_data["cleared_stages"] = cl

                        sync_currencies()
                        get_player_input("Press Enter...")
                else:
                    console.print("[red]Locked![/red]")
                    time.sleep(1)

            elif choice == "1-10":
                if unlocked >= 9:
                    latest = config.player_data.get("latest_stage", 0)
                    if latest < 10:
                        story_manager.play_stage_1_10_start()
                    
                    config.player_data["node_progress"] = {
                        "stage": 10,
                        "cleared_indices": [],
                        "party_hp": {}
                    }
                    config.current_state = config.STATE_NODE_SELECT
                else:
                    console.print("[red]Locked![/red]")
                    time.sleep(1)

            elif choice == "1-11":
                if unlocked >= 10:
                    if unlocked >= 11:
                        console.print("[dim]Stage Cleared.[/dim]")
                        time.sleep(0.5)
                    else:
                        story_manager.play_stage_1_11_story()
                        console.print("[bold yellow]First Clear Rewards:[/bold yellow]")
                        console.print("5x Microchip")
                        
                        mats = config.player_data["materials"]
                        mats["Microchip"] = mats.get("Microchip", 0) + 5
                        
                        if config.player_data["latest_stage"] < 11: 
                            config.player_data["latest_stage"] = 11
                        
                        cl = config.player_data.get("cleared_stages", [])
                        if 11 not in cl: 
                            cl.append(11)
                            config.player_data["cleared_stages"] = cl

                        sync_currencies()
                        get_player_input("Press Enter...")
                else:
                    console.print("[red]Locked![/red]")
                    time.sleep(1)

            elif choice == "2-1":
                if unlocked >= 11:
                    if unlocked >= 12:
                        console.print("[dim]Stage Cleared.[/dim]")
                        time.sleep(0.5)
                    else:
                        story_manager.play_stage_2_1_story()
                        console.print("[bold yellow]First Clear Rewards:[/bold yellow]")
                        console.print("2x Microchip")
                        console.print("2x Microprocessor")
                        
                        mats = config.player_data["materials"]
                        mats["Microchip"] = mats.get("Microchip", 0) + 2
                        mats["Microprocessor"] = mats.get("Microprocessor", 0) + 2
                        
                        if config.player_data["latest_stage"] < 12: 
                            config.player_data["latest_stage"] = 12
                        
                        cl = config.player_data.get("cleared_stages", [])
                        if 12 not in cl: 
                            cl.append(12)
                            config.player_data["cleared_stages"] = cl

                        sync_currencies()
                        get_player_input("Press Enter...")
                else:
                    console.print("[red]Locked![/red]")
                    time.sleep(1)

            elif choice == "2-2":
                if unlocked >= 12:
                    if unlocked >= 13:
                        console.print("[dim]Stage Cleared.[/dim]")
                        time.sleep(0.5)
                    else:
                        story_manager.play_stage_2_2_story()
                        console.print("[bold yellow]First Clear Rewards:[/bold yellow]")
                        console.print("2x Microchip")
                        console.print("2x Microprocessor")
                        mats = config.player_data["materials"]
                        mats["Microchip"] = mats.get("Microchip", 0) + 2
                        mats["Microprocessor"] = mats.get("Microprocessor", 0) + 2
                        if config.player_data["latest_stage"] < 13: config.player_data["latest_stage"] = 13
                        sync_currencies()
                        get_player_input("Press Enter...")
                else:
                    console.print("[red]Locked![/red]")
                    time.sleep(1)

            elif choice == "2-3":
                if unlocked >= 13:
                    latest = config.player_data.get("latest_stage", 0)
                    if latest < 14:
                        story_manager.play_stage_2_3_start()
                    
                    config.player_data["node_progress"] = {
                        "stage": 14,
                        "cleared_indices": [],
                        "party_hp": {}
                    }
                    config.current_state = config.STATE_NODE_SELECT
                else:
                    console.print("[red]Locked![/red]")
                    time.sleep(1)

            elif choice == "2-4":
                if unlocked >= 14:
                    latest = config.player_data.get("latest_stage", 0)
                    if latest < 15:
                        story_manager.play_stage_2_4_start()
                    
                    config.player_data["node_progress"] = {
                        "stage": 15,
                        "cleared_indices": [],
                        "party_hp": {}
                    }
                    config.current_state = config.STATE_NODE_SELECT
                else:
                    console.print("[red]Locked![/red]")
                    time.sleep(1)

            elif choice == "2-5":
                if unlocked >= 15:
                    latest = config.player_data.get("latest_stage", 0)
                    if latest < 16:
                        story_manager.play_stage_2_5_start()
                    
                    config.player_data["node_progress"] = {
                        "stage": 16,
                        "cleared_indices": [],
                        "party_hp": {}
                    }
                    config.current_state = config.STATE_NODE_SELECT
                else:
                    console.print("[red]Locked![/red]")
                    time.sleep(1)

            elif choice == "2-6":
                if unlocked >= 16:
                    if unlocked >= 17:
                        console.print("[dim]Stage Cleared.[/dim]")
                        time.sleep(0.5)
                    else:
                        story_manager.play_stage_2_6_story()
                        console.print("[bold yellow]First Clear Rewards:[/bold yellow]")
                        console.print("2x Microchip")
                        console.print("2x Microprocessor")
                        mats = config.player_data["materials"]
                        mats["Microchip"] = mats.get("Microchip", 0) + 2
                        mats["Microprocessor"] = mats.get("Microprocessor", 0) + 2
                        if config.player_data["latest_stage"] < 17: config.player_data["latest_stage"] = 17
                        sync_currencies()
                        get_player_input("Press Enter...")
                else:
                    console.print("[red]Locked![/red]")
                    time.sleep(1)

            elif choice == "2-7":
                if unlocked >= 17:
                    config.player_data["selected_stage"] = 18
                    config.current_state = config.STATE_BATTLE
                else:
                    console.print("[red]Locked![/red]")
                    time.sleep(1)

            elif choice == "2-8":
                if unlocked >= 18:
                    config.player_data["selected_stage"] = 19
                    config.current_state = config.STATE_BATTLE
                else:
                    console.print("[red]Locked![/red]")
                    time.sleep(1)

            elif choice == "2-9":
                if unlocked >= 19:
                    config.player_data["selected_stage"] = 20
                    config.current_state = config.STATE_BATTLE
                else:
                    console.print("[red]Locked![/red]")
                    time.sleep(1)

            elif choice == "2-10":
                if unlocked >= 20:
                    config.player_data["selected_stage"] = 21
                    config.current_state = config.STATE_BATTLE
                else:
                    console.print("[red]Locked![/red]")
                    time.sleep(1)

            elif choice == "2-11":
                if unlocked >= 21:
                    if unlocked >= 22:
                        console.print("[dim]Stage Cleared.[/dim]")
                        time.sleep(0.5)
                    else:
                        story_manager.play_stage_2_11_story()
                        console.print("[bold yellow]First Clear Rewards:[/bold yellow]")
                        console.print("3x Microchip")
                        console.print("3x Microprocessor")
                        mats = config.player_data["materials"]
                        mats["Microchip"] = mats.get("Microchip", 0) + 3
                        mats["Microprocessor"] = mats.get("Microprocessor", 0) + 3
                        if config.player_data["latest_stage"] < 22: config.player_data["latest_stage"] = 22
                        sync_currencies()
                        get_player_input("Press Enter...")
                else:
                    console.print("[red]Locked![/red]")
                    time.sleep(1)

        elif config.current_state == config.STATE_NODE_SELECT:
            np = config.player_data.get("node_progress")
            if not np:
                config.current_state = config.STATE_MAIN_MENU
                continue
            
            # --- NODE SELECT LOGIC (DON'T DELETE) ---#
            stage_num = np["stage"]
            
            if stage_num == 5:
                draw_node_select_menu("1-5: Weekday Errands", np["cleared_indices"])
                valid_indices = ["1", "2", "3"]
                start_id = 51
            elif stage_num == 10:
                draw_node_select_menu("1-10: Raid", np["cleared_indices"])
                valid_indices = ["1", "2", "3", "4"]
                start_id = 101
            elif stage_num == 14:
                draw_node_select_menu("2-3: Stalemate At The Gates", np["cleared_indices"])
                valid_indices = ["1", "2"]
                start_id = 141
            elif stage_num == 15:
                draw_node_select_menu("2-4: Breakthrough Plan", np["cleared_indices"])
                valid_indices = ["1", "2", "3"]
                start_id = 151
            elif stage_num == 16:
                draw_node_select_menu("2-5: Labyrinth Of Motives", np["cleared_indices"])
                valid_indices = ["1", "2", "3", "4", "5"]
                start_id = 161
            else:
                # Fallback / Error
                config.current_state = config.STATE_MAIN_MENU
                continue

            choice = get_player_input("Select Node > ")
            
            if choice == "0":
                console.print("[bold red]Warning:[/bold red] Giving up now will reset all progress in this stage.")
                c2 = get_player_input("Type 'Y' to confirm > ").upper()
                if c2 == "Y":
                    config.player_data["node_progress"] = None
                    config.current_state = config.STATE_MAIN_MENU
            
            elif choice in valid_indices:
                idx = int(choice) - 1
                if idx in np["cleared_indices"]:
                    console.print("[dim]Node already cleared.[/dim]")
                    time.sleep(1)
                else:
                    stage_id = start_id + idx
                    config.player_data["selected_stage"] = stage_id
                    config.current_state = config.STATE_BATTLE

        elif config.current_state == config.STATE_COUNCIL_LOGS:
            draw_council_logs_menu()
            choice = get_player_input()
            if choice == "0": config.current_state = config.STATE_MAIN_MENU
            elif choice == "1": draw_bestiary_menu()
            elif choice == "2": draw_material_logs()

        elif config.current_state == config.STATE_PARTY_MANAGEMENT:
            # We pass the 'player' object so the UI can read units and inventory
            # We expect the function to return a 'next_state' string or Handle the loop internally
            # For consistency with your code, we'll assume a loop pattern similar to Council Logs:
            draw_party_management_menu(player)
            
            # Note: We assume draw_party_management_menu contains its own internal loop 
            # for selecting characters/equipment to avoid cluttering main.py. 
            # When it breaks that loop, we return here.  
            config.current_state = config.STATE_MAIN_MENU

if __name__ == "__main__":
    run_game()