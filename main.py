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
        
        # 3. Inject Inventory into Player Object
        player.inventory["katas"] = loaded_data.get("katas", [])
        
        # 4. Clean up Config
        if "katas" in config.player_data:
            del config.player_data["katas"]
        
        # 5. Sync Currencies
        sync_currencies() 
        
        # --- [NEW] LOADOUT APPLICATION LOGIC ---
        
        # A. Sync Roster First (Ensures player.units exists in strict order)
        sync_player_roster()
        
        # B. Apply Equipped Katas
        equipped = loaded_data.get("equipped", {})
        
        for u_idx, k_id in equipped.items():
            # Safety Check: Unit index matches unlocked roster size
            if 1 <= u_idx <= len(player.units):
                # Map 1-based index (Save) to 0-based index (List)
                unit = player.units[u_idx - 1]
                
                # Fetch Kata Data
                if k_id in scd.KATA_ID_MAP:
                    k_name = scd.KATA_ID_MAP[k_id]
                    k_data = scd.get_kata_data_by_name(k_name)
                    
                    if k_data:
                        # 1. Equip the Kata Object (Resets deck/stats)
                        unit.equip_kata(k_data["kata_obj"])
                        
                        # 2. Restore HP to Max
                        unit.max_hp = k_data["max_hp"]
                        unit.hp = unit.max_hp 
                        
                        # 3. Restore Rift Aptitude (Check Inventory for Upgrades)
                        for inv_kata in player.inventory["katas"]:
                            if inv_kata["name"] == k_name:
                                unit.kata.rift_aptitude = inv_kata.get("aptitude", "I")
                                break

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
        # Pass the 'player' instance so inventory/units are accessible
        if player:
            strip = save_manager.generate_save_strip(player)
            
            console.print(f"\n[bold]Here is your Save Strip, copy it:[/bold]\n")
            console.print(f"[yellow]{strip}[/yellow]")
            console.print("\n[dim]Select text and Ctrl+C to copy.[/dim]")
            
        get_player_input("Press Enter to exit...")
        sys.exit()

def sync_player_roster():
    """
    Checks player's progress and permanently adds unlocked characters 
    to player.units if they are missing.
    """
    latest = config.player_data.get("latest_stage", 0)
    
    current_roster_names = [u.name for u in player.units]

    # Definition of Unlocks: (Name, Required Stage Clear, Factory Function)
    unlock_milestones = [
        ("Akasuke", 0, stages.create_akasuke),
        ("Yuri", 0, stages.create_yuri),
        ("Benikawa", 4, stages.create_benikawa),
        ("Shigemura", 15, stages.create_shigemura),
        ("Naganohara", 41, stages.create_naganohara),
        ("Hana", 56, stages.create_hana),
        ("Kagaku", 56, stages.create_kagaku),
        ("Natsume", 56, stages.create_natsume)
    ]
    
    for name, req_stage, factory_func in unlock_milestones:
        if latest >= req_stage and name not in current_roster_names:
            new_member = factory_func()
            new_member.is_player = True 
            player.units.append(new_member)

def get_equipped_data(unit_name):
    """
    Searches the persistent player roster for a specific unit.
    Returns dictionary for Guest injection logic.
    """
    found_unit = next((u for u in player.units if u.name == unit_name), None)
    
    if found_unit:
        return {
            "kata_obj": found_unit.kata,         
            "max_hp": found_unit.max_hp,         
            "description": found_unit.description 
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

            ### INJECTION LOGIC ###
            latest_cleared = config.player_data.get("latest_stage", -1)

            party = [p for p in party if p.name != "Akasuke"]
            loadout = get_equipped_data("Akasuke")
            party.append(stages.create_akasuke(loadout))
            party = [p for p in party if p.name != "Yuri"]
            loadout = get_equipped_data("Yuri")
            party.append(stages.create_yuri(loadout))
            
            if (latest_cleared >= 4 or stage_id == 4) and stage_id != 7:
                has_beni = any(u.name == "Benikawa" for u in party)
                if not has_beni:
                    loadout = get_equipped_data("Benikawa")
                    party.append(stages.create_benikawa(loadout))
            
            if stage_id == 7:
                party = [p for p in party if p.name != "Benikawa"]

            if (latest_cleared >= 15 or stage_id in [15001,15002,15003]):
                has_shige = any(u.name == "Shigemura" for u in party)
                if not has_shige:
                    loadout = get_equipped_data("Shigemura")
                    party.append(stages.create_shigemura(loadout))
            
            is_guest_appearance1 = (stage_id in [16, 16001, 16002, 16003, 16004, 16005, 41, 41001, 41002, 41003, 41004])
            is_officially_unlocked = (latest_cleared >= 41 and not stage_id == 42)
            if is_guest_appearance1:
                has_naga = any(u.name == "Naganohara" for u in party)
                if not has_naga:
                    if is_guest_appearance1:
                        guest_loadout = scd.get_kata_data_by_name("Heiwa Seiritsu High School Student Naganohara")
                        party.append(stages.create_naganohara(guest_loadout))
                    elif is_officially_unlocked:
                        loadout = get_equipped_data("Naganohara")
                        party.append(stages.create_naganohara(loadout))

            if stage_id == 21:
                party = [p for p in party if p.name != "Akasuke"]
                guest_loadout = scd.get_kata_data_by_name("‘Iron Fist Of Heiwa’ Delinquent Leader Akasuke")
                guest_akasuke = stages.create_akasuke(guest_loadout)
                party.insert(0, guest_akasuke)

            if stage_id in [6]:
                party = [member for member in party if member.name == "Akasuke"]

            if stage_id in [18,19,20,21]:
                party = [member for member in party if member.name in ["Akasuke","Yuri","Benikawa"]]

            if stage_id in [25, 26, 28, 29]:
                has_hana = any(u.name == "Hana" for u in party)
                if not has_hana:
                    loadout = get_equipped_data("Hana")
                    party.append(stages.create_hana(loadout))
                party = [member for member in party if member.name in ["Akasuke","Yuri","Benikawa","Hana"]]

            if stage_id == 31:
                party = [member for member in party if member.name == "Benikawa"]

            if stage_id in [32, 33, 34, 35, 36]:
                party = [member for member in party if member.name in ["Akasuke","Yuri","Benikawa","Shigemura"]]

            if stage_id == 38:
                party = [p for p in party if p.name != "Kagaku"]
                guest_loadout = scd.get_kata_data_by_name("Kasakura High School Disciplinary Committee Member Kagaku")
                guest_kagaku = stages.create_kagaku(guest_loadout)
                party.insert(0, guest_kagaku)
                party = [member for member in party if member.name == "Kagaku"]
    
            if stage_id == 39:
                party = [p for p in party if p.name != "Akasuke"]
                guest_loadout = scd.get_kata_data_by_name("Kasakura High School Student Akasuke")
                guest_akasuke = stages.create_akasuke(guest_loadout)
                party.insert(0, guest_akasuke)
                party = [member for member in party if member.name == "Akasuke"]
    
            if stage_id == 41:
                party = [member for member in party if member.name in ["Akasuke","Yuri","Benikawa","Shigemura","Naganohara"]]
    
            if stage_id == 42:
                party = [member for member in party if member.name in ["Akasuke","Yuri","Benikawa","Shigemura","Naganohara","Kagaku"]]
                party = [p for p in party if p.name != "Naganohara"]
                guest_loadout = scd.get_kata_data_by_name("Riposte Gang Squad Leader Naganohara")
                guest_naganohara = stages.create_naganohara(guest_loadout)
                party.insert(4, guest_naganohara)
                party = [p for p in party if p.name != "Kagaku"]
                guest_loadout = scd.get_kata_data_by_name("Kasakura High School Disciplinary Committee Member Kagaku")
                guest_kagaku = stages.create_kagaku(guest_loadout)
                party.insert(5, guest_kagaku)

            if stage_id in [49, 50, 51, 52, 53]:
                required_members = ["Akasuke", "Yuri", "Benikawa", "Shigemura", "Naganohara", "Hana", "Kagaku"]
                for req_name in required_members:
                    if not any(u.name == req_name for u in party):
                        loadout = get_equipped_data(req_name)
                        factory_func = getattr(stages, f"create_{req_name.lower()}")
                        party.append(factory_func(loadout))
                party = [p for p in party if p.name != "Hana"]
                guest_loadout = scd.get_kata_data_by_name("Kiryoku Gakuen Student Council Fairy | ‘Lake Strider’ Hana")
                guest_hana = stages.create_hana(guest_loadout)
                party.insert(5, guest_hana)
                party = [p for p in party if p.name != "Kagaku"]
                guest_loadout = scd.get_kata_data_by_name("Kasakura High School Disciplinary Committee Member Kagaku")
                guest_kagaku = stages.create_kagaku(guest_loadout)
                party.insert(6, guest_kagaku)

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
                elif stage_id == 25: story_manager.play_stage_3_3_start()
                elif stage_id == 26: story_manager.play_stage_3_4_start()
                elif stage_id == 28: story_manager.play_stage_3_6_start()
                elif stage_id == 31: story_manager.play_stage_3_9_start()
                elif stage_id == 33: story_manager.play_stage_3_11_start()
                elif stage_id == 35: story_manager.play_stage_3_13_start()
                elif stage_id == 36: story_manager.play_stage_3_14_start()
                elif stage_id == 37: story_manager.play_stage_3_15_start()
                elif stage_id == 38: story_manager.play_stage_3_16_start()
                elif stage_id == 39: story_manager.play_stage_3_17_start()
                elif stage_id == 42: story_manager.play_stage_3_20_start()
                elif stage_id == 49: pass # story_manager.play_stage_4_4_start()

            battle_manager.start_battle(party, enemies, stage_id)
            
            clear_screen()
            if battle_manager.won:
                console.print("[bold green]VICTORY![/bold green]")
                
                rewards_text = []
                mats = config.player_data["materials"]
                
                # --- NODE STAGE HANDLING ---
                np = config.player_data.get("node_progress")
                is_valid_node_battle = False
                
                if np is not None:
                    parent_of_current_stage = stage_id // 1000
                    if parent_of_current_stage == np["stage"]:
                        is_valid_node_battle = True

                if is_valid_node_battle: 
                    is_first_node_clear = stage_id not in config.player_data.get("cleared_stages", [])

                    # >> STAGE 1-5 (IDs 5001, 5002, 5003)
                    if np["stage"] == 5:
                        if stage_id in [5001, 5002]:
                            if is_first_node_clear:
                                rewards_text.extend(["2x Microchip", "2x Microprocessor"])
                                mats["Microchip"] = mats.get("Microchip", 0) + 2
                                mats["Microprocessor"] = mats.get("Microprocessor", 0) + 2
                            else:
                                if random.random() < 0.25:
                                    rewards_text.append("1x Cafeteria Melon Bread")
                                    mats["Cafeteria Melon Bread"] = mats.get("Cafeteria Melon Bread", 0) + 1
                        elif stage_id == 5003:
                            if is_first_node_clear:
                                rewards_text.extend(["2x Microchip", "2x Microprocessor", "2x Cafeteria Melon Bread"])
                                mats["Microchip"] = mats.get("Microchip", 0) + 2
                                mats["Microprocessor"] = mats.get("Microprocessor", 0) + 2
                                mats["Cafeteria Melon Bread"] = mats.get("Cafeteria Melon Bread", 0) + 2
                            else:
                                if random.random() < 0.50:
                                    rewards_text.append("1x Cafeteria Melon Bread")
                                    mats["Cafeteria Melon Bread"] = mats.get("Cafeteria Melon Bread", 0) + 1

                    # >> STAGE 1-10 (IDs 10001, 10002, 10003, 10004)
                    elif np["stage"] == 10:
                        if stage_id in [10001, 10002]:
                            if is_first_node_clear:
                                rewards_text.extend(["2x Microchip", "2x Microprocessor"])
                                mats["Microchip"] = mats.get("Microchip", 0) + 2
                                mats["Microprocessor"] = mats.get("Microprocessor", 0) + 2
                            else:
                                if random.random() < 0.30:
                                    rewards_text.append("1x Microchip")
                                    mats["Microchip"] = mats.get("Microchip", 0) + 1
                        elif stage_id in [10003, 10004]:
                            if is_first_node_clear:
                                rewards_text.extend(["3x Microchip", "3x Microprocessor"])
                                mats["Microchip"] = mats.get("Microchip", 0) + 3
                                mats["Microprocessor"] = mats.get("Microprocessor", 0) + 3
                            else:
                                if random.random() < 0.30:
                                    rewards_text.append("1x Microprocessor")
                                    mats["Microprocessor"] = mats.get("Microprocessor", 0) + 1

                    # >> STAGE 2-3 (IDs 14001, 14002)
                    elif np["stage"] == 14:
                        if stage_id in [14001, 14002]:
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

                    # >> STAGE 2-4 (IDs 15001, 15002, 15003)
                    elif np["stage"] == 15:
                        if stage_id in [15001, 15002, 15003]:
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

                    # >> STAGE 2-5 (IDs 16001, 16002, 16003, 16004, 16005)
                    elif np["stage"] == 16:
                        if stage_id in [16001, 16002]: # Nodes 1 & 2
                            if is_first_node_clear:
                                rewards_text.append("2x Microchip")
                                mats["Microchip"] = mats.get("Microchip", 0) + 2
                            else:
                                if random.random() < 0.50:
                                    rewards_text.append("1x Vending Machine Coffee")
                                    mats["Vending Machine Coffee"] = mats.get("Vending Machine Coffee", 0) + 1
                        elif stage_id in [16003, 16004]: # Nodes 3 & 4
                            if is_first_node_clear:
                                rewards_text.append("2x Vending Machine Coffee")
                                mats["Vending Machine Coffee"] = mats.get("Vending Machine Coffee", 0) + 2
                            else:
                                if random.random() < 0.50:
                                    rewards_text.append("1x Vending Machine Coffee")
                                    mats["Vending Machine Coffee"] = mats.get("Vending Machine Coffee", 0) + 1
                        elif stage_id == 16005: # Node 5
                            if is_first_node_clear:
                                rewards_text.append("3x Cafeteria Melon Bread")
                                mats["Cafeteria Melon Bread"] = mats.get("Cafeteria Melon Bread", 0) + 3
                            else:
                                if random.random() < 0.50:
                                    rewards_text.append("1x Vending Machine Coffee")
                                    mats["Vending Machine Coffee"] = mats.get("Vending Machine Coffee", 0) + 1

                    # >> STAGE 3-10 (IDs 32001, 32002, 32003)
                    elif np["stage"] == 32:
                        if stage_id in [32001, 32002]:
                            if is_first_node_clear:
                                rewards_text.append("2x Microchip")
                                mats["Microchip"] = mats.get("Microchip", 0) + 2
                            else:
                                if random.random() < 0.25:
                                    rewards_text.append("1x Sports Water Bottle")
                                    mats["Sports Water Bottle"] = mats.get("Sports Water Bottle", 0) + 1
                        elif stage_id == 32003:
                            if is_first_node_clear:
                                rewards_text.append("1x Sports Water Bottle")
                                mats["Sports Water Bottle"] = mats.get("Sports Water Bottle", 0) + 3
                            else:
                                if random.random() < 0.25:
                                    rewards_text.append("1x Sports Water Bottle")
                                    mats["Sports Water Bottle"] = mats.get("Sports Water Bottle", 0) + 1

                    # >> STAGE 3-12 (IDs 34001, 34002, 34003)
                    elif np["stage"] == 34:
                        if stage_id in [34001, 34002, 34003]:
                            if is_first_node_clear:
                                rewards_text.append("1x Sports Water Bottle")
                                rewards_text.append("2x Microprocessor")
                                mats["Sports Water Bottle"] = mats.get("Sports Water Bottle", 0) + 1
                                mats["Microprocessor"] = mats.get("Microprocessor", 0) + 2
                            else:
                                if random.random() < 0.65:
                                    rewards_text.append("1x Microchip")
                                    mats["Microchip"] = mats.get("Microchip", 0) + 1

                    # >> STAGE 3-19 (IDs 41001, 41002, 41003, 41004)
                    elif np["stage"] == 41:
                        if stage_id in [41001, 41002, 41003, 41004]:
                            if is_first_node_clear:
                                rewards_text.append("1x Microchip")
                                mats["Microchip"] = mats.get("Microchip", 0) + 1
                            else:
                                if random.random() < 0.375:
                                    rewards_text.append("1x Cafeteria Melon Bread")
                                    rewards_text.append("1x Vending Machine Coffee")
                                    rewards_text.append("1x Sports Water Bottle")
                                    mats["Cafeteria Melon Bread"] = mats.get("Cafeteria Melon Bread", 0) + 1
                                    mats["Vending Machine Coffee"] = mats.get("Vending Machine Coffee", 0) + 1
                                    mats["Sports Water Bottle"] = mats.get("Sports Water Bottle", 0) + 1

                    # HP HEALING MESSAGE
                    console.print(f"Party HP Fully Recovered.")

                    # PROGRESS TRACKING
                    node_idx = stage_id - (np["stage"] * 1000) - 1
                    
                    if node_idx not in np["cleared_indices"]:
                        np["cleared_indices"].append(node_idx)
                        config.player_data["node_progress"] = np

                    # COMPLETION CHECK
                    nodes_required_map = {5: 3, 10: 4, 14: 2, 15: 3, 16: 5, 32: 3, 34: 3, 41: 4}
                    req_count = nodes_required_map.get(np["stage"], 99)

                    if len(np["cleared_indices"]) >= req_count:
                        # -- STAGE COMPLETE --
                        stage_name_map = {5: "1-5", 10: "1-10", 14: "2-3", 15: "2-4", 16: "2-5", 32: "3-10", 34: "3-12", 41: "3-19"}
                        s_name = stage_name_map.get(np["stage"], "??")
                        console.print(f"[bold green]STAGE {s_name} COMPLETE![/bold green]")

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
                            # Stage 3-10 has no story end sequence
                            # Stage 3-12 has no story end sequence
                            elif np["stage"] == 38:
                                story_manager.play_stage_3_15_end()
                            elif np["stage"] == 41:
                                story_manager.play_stage_3_19_end()
                                rewards_text.append("[bold magenta]NEW MEMBER: Naganohara[/bold magenta]")
                            
                            config.player_data["latest_stage"] = np["stage"]

                        cl = config.player_data.get("cleared_stages", [])
                        
                        start_id = (np["stage"] * 1000) + 1
                        for i in range(req_count):
                            nid = start_id + i
                            if nid not in cl: cl.append(nid)
                        
                        config.player_data["cleared_stages"] = cl
                        config.player_data["node_progress"] = None # Reset progress

                        config.current_state = config.STATE_MAIN_MENU
                    else:
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

                    elif stage_id == 8: 
                        if random.random() < 0.50: rewards_text.append("1x Microchip"); mats["Microchip"] = mats.get("Microchip", 0) + 1

                    elif stage_id == 9: 
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

                    elif stage_id in [25, 26, 28, 29, 31]:
                        checklatest = stage_id
                        if should_play_story:
                            if stage_id == 29:
                                story_manager.play_stage_3_7_end()
                            elif stage_id == 31:
                                story_manager.play_stage_3_9_end()
                            rewards_text.extend(["3x Microchip", "3x Microprocessor"])
                            mats["Microchip"] = mats.get("Microchip", 0) + 3
                            mats["Microprocessor"] = mats.get("Microprocessor", 0) + 3
                            if config.player_data["latest_stage"] < checklatest: config.player_data["latest_stage"] = checklatest
                            cl = config.player_data.get("cleared_stages", [])
                            if checklatest not in cl: cl.append(checklatest); config.player_data["cleared_stages"] = cl
                        else:
                            if random.random() < 0.75: rewards_text.append("1x Microchip"); mats["Microchip"] = mats.get("Microchip", 0) + 1
                            if random.random() < 0.75: rewards_text.append("1x Microprocessor"); mats["Microprocessor"] = mats.get("Microprocessor", 0) + 1

                    elif stage_id in [33, 35, 36, 37, 38, 39, 40]:
                        checklatest = stage_id
                        if should_play_story:
                            if stage_id == 33:
                                story_manager.play_stage_3_11_end()
                            if stage_id == 37:
                                story_manager.play_stage_3_15_end()
                            if stage_id == 38:
                                story_manager.play_stage_3_16_end()
                            if stage_id == 39:
                                story_manager.play_stage_3_17_end()
                            rewards_text.extend(["2x Microprocessor", "1x Sports Water Bottle"])
                            mats["Microprocessor"] = mats.get("Microprocessor", 0) + 2
                            mats["Sports Water Bottle"] = mats.get("Sports Water Bottle", 0) + 1
                            if config.player_data["latest_stage"] < checklatest: config.player_data["latest_stage"] = checklatest
                            cl = config.player_data.get("cleared_stages", [])
                            if checklatest not in cl: cl.append(checklatest); config.player_data["cleared_stages"] = cl
                        else:
                            if random.random() < 0.25: rewards_text.append("1x Sports Water Bottle"); mats["Sports Water Bottle"] = mats.get("Sports Water Bottle", 0) + 1
                            if random.random() < 0.8: rewards_text.append("1x Microprocessor"); mats["Microprocessor"] = mats.get("Microprocessor", 0) + 1

                    elif stage_id == 42:
                        checklatest = stage_id
                        if should_play_story:
                            rewards_text.extend(["5x Microchip"])
                            mats["Microchip"] = mats.get("Microchip", 0) + 5
                            if config.player_data["latest_stage"] < checklatest: config.player_data["latest_stage"] = checklatest
                            cl = config.player_data.get("cleared_stages", [])
                            if checklatest not in cl: cl.append(checklatest); config.player_data["cleared_stages"] = cl
                        else:
                            if random.random() < 0.8: rewards_text.append("1x Microchip"); mats["Microchip"] = mats.get("Microchip", 0) + 1

                    elif stage_id == 49: # Stage 4-4
                        checklatest = stage_id
                        if should_play_story:
                            # story_manager.play_stage_4_4_end()
                            rewards_text.extend([
                                "2x Microchip", 
                                "2x Microprocessor",
                            ])
                            mats["Microchip"] = mats.get("Microchip", 0) + 2
                            mats["Microprocessor"] = mats.get("Microprocessor", 0) + 2
                            if config.player_data["latest_stage"] < checklatest: config.player_data["latest_stage"] = checklatest
                            cl = config.player_data.get("cleared_stages", [])
                            if checklatest not in cl: cl.append(checklatest); config.player_data["cleared_stages"] = cl
                        else:
                            if random.random() < 0.7: rewards_text.append("1x Microchip"); mats["Microchip"] = mats.get("Microchip", 0) + 1
                            if random.random() < 0.7: rewards_text.append("1x Microprocessor"); mats["Microprocessor"] = mats.get("Microprocessor", 0) + 1

                    config.current_state = config.STATE_MAIN_MENU

                if rewards_text:
                    console.print("[bold yellow]REWARDS:[/bold yellow]")
                    for r in rewards_text: console.print(f"- {r}")
                else:
                    if stage_id != 0 and stage_id < 50: console.print("[dim]No drops this time.[/dim]")

                sync_currencies()
            else:
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
            console.print("[4] Party Management") 
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
                        if config.player_data["latest_stage"] < 8: config.player_data["latest_stage"] = 8
                        cl = config.player_data.get("cleared_stages", [])
                        if 8 not in cl: cl.append(8); config.player_data["cleared_stages"] = cl
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
                        if config.player_data["latest_stage"] < 9: config.player_data["latest_stage"] = 9
                        cl = config.player_data.get("cleared_stages", [])
                        if 9 not in cl: cl.append(9); config.player_data["cleared_stages"] = cl
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
                        if config.player_data["latest_stage"] < 11: config.player_data["latest_stage"] = 11
                        cl = config.player_data.get("cleared_stages", [])
                        if 11 not in cl: cl.append(11); config.player_data["cleared_stages"] = cl
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
                        if config.player_data["latest_stage"] < 12: config.player_data["latest_stage"] = 12
                        cl = config.player_data.get("cleared_stages", [])
                        if 12 not in cl: cl.append(12); config.player_data["cleared_stages"] = cl
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

            elif choice == "3-1":
                if unlocked >= 22:
                    if unlocked >= 23:
                        console.print("[dim]Stage Cleared.[/dim]")
                        time.sleep(0.5)
                    else:
                        story_manager.play_stage_3_1_story()
                        console.print("[bold yellow]First Clear Rewards:[/bold yellow]")
                        console.print("2x Microchip")
                        console.print("2x Microprocessor")
                        mats = config.player_data["materials"]
                        mats["Microchip"] = mats.get("Microchip", 0) + 2
                        mats["Microprocessor"] = mats.get("Microprocessor", 0) + 2
                        if config.player_data["latest_stage"] < 23: config.player_data["latest_stage"] = 23
                        sync_currencies()
                        get_player_input("Press Enter...")
                else:
                    console.print("[red]Locked![/red]")
                    time.sleep(1)

            elif choice == "3-2":
                if unlocked >= 23:
                    if unlocked >= 24:
                        console.print("[dim]Stage Cleared.[/dim]")
                        time.sleep(0.5)
                    else:
                        story_manager.play_stage_3_2_story()
                        console.print("[bold yellow]First Clear Rewards:[/bold yellow]")
                        console.print("2x Microchip")
                        console.print("2x Microprocessor")
                        mats = config.player_data["materials"]
                        mats["Microchip"] = mats.get("Microchip", 0) + 2
                        mats["Microprocessor"] = mats.get("Microprocessor", 0) + 2
                        if config.player_data["latest_stage"] < 24: config.player_data["latest_stage"] = 24
                        sync_currencies()
                        get_player_input("Press Enter...")
                else:
                    console.print("[red]Locked![/red]")
                    time.sleep(1)

            elif choice == "3-3":
                if unlocked >= 24:
                    config.player_data["selected_stage"] = 25
                    config.current_state = config.STATE_BATTLE
                else:
                    console.print("[red]Locked![/red]")
                    time.sleep(1)

            elif choice == "3-4":
                if unlocked >= 25:
                    config.player_data["selected_stage"] = 26
                    config.current_state = config.STATE_BATTLE
                else:
                    console.print("[red]Locked![/red]")
                    time.sleep(1)

            elif choice == "3-5":
                if unlocked >= 26:
                    if unlocked >= 27:
                        console.print("[dim]Stage Cleared.[/dim]")
                        time.sleep(0.5)
                    else:
                        story_manager.play_stage_3_5_story()
                        console.print("[bold yellow]First Clear Rewards:[/bold yellow]")
                        console.print("2x Microchip")
                        console.print("2x Microprocessor")
                        mats = config.player_data["materials"]
                        mats["Microchip"] = mats.get("Microchip", 0) + 2
                        mats["Microprocessor"] = mats.get("Microprocessor", 0) + 2
                        if config.player_data["latest_stage"] < 27: config.player_data["latest_stage"] = 27
                        sync_currencies()
                        get_player_input("Press Enter...")
                else:
                    console.print("[red]Locked![/red]")
                    time.sleep(1)

            elif choice == "3-6":
                if unlocked >= 27:
                    config.player_data["selected_stage"] = 28
                    config.current_state = config.STATE_BATTLE
                else:
                    console.print("[red]Locked![/red]")
                    time.sleep(1)

            elif choice == "3-7":
                if unlocked >= 28:
                    config.player_data["selected_stage"] = 29
                    config.current_state = config.STATE_BATTLE
                else:
                    console.print("[red]Locked![/red]")
                    time.sleep(1)

            elif choice == "3-8":
                if unlocked >= 29:
                    if unlocked >= 30:
                        console.print("[dim]Stage Cleared.[/dim]")
                        time.sleep(0.5)
                    else:
                        story_manager.play_stage_3_8_story()
                        console.print("[bold yellow]First Clear Rewards:[/bold yellow]")
                        console.print("2x Microchip")
                        console.print("2x Microprocessor")
                        mats = config.player_data["materials"]
                        mats["Microchip"] = mats.get("Microchip", 0) + 2
                        mats["Microprocessor"] = mats.get("Microprocessor", 0) + 2
                        if config.player_data["latest_stage"] < 30: config.player_data["latest_stage"] = 30
                        sync_currencies()
                        get_player_input("Press Enter...")
                else:
                    console.print("[red]Locked![/red]")
                    time.sleep(1)

            elif choice == "3-9":
                if unlocked >= 30:
                    config.player_data["selected_stage"] = 31
                    config.current_state = config.STATE_BATTLE
                else:
                    console.print("[red]Locked![/red]")
                    time.sleep(1)

            elif choice == "3-10":
                if unlocked >= 31:
                    latest = config.player_data.get("latest_stage", 0)
                    if latest < 32:
                        story_manager.play_stage_3_10_start()
                    config.player_data["node_progress"] = {
                        "stage": 32,
                        "cleared_indices": [],
                        "party_hp": {}
                    }
                    config.current_state = config.STATE_NODE_SELECT
                else:
                    console.print("[red]Locked![/red]")
                    time.sleep(1)

            elif choice == "3-11":
                if unlocked >= 32:
                    config.player_data["selected_stage"] = 33
                    config.current_state = config.STATE_BATTLE
                else:
                    console.print("[red]Locked![/red]")
                    time.sleep(1)

            elif choice == "3-12":
                if unlocked >= 33:
                    latest = config.player_data.get("latest_stage", 0)
                    if latest < 34:
                        story_manager.play_stage_3_12_start()
                    config.player_data["node_progress"] = {
                        "stage": 34,
                        "cleared_indices": [],
                        "party_hp": {}
                    }
                    config.current_state = config.STATE_NODE_SELECT
                else:
                    console.print("[red]Locked![/red]")
                    time.sleep(1)

            elif choice == "3-13":
                if unlocked >= 34:
                    config.player_data["selected_stage"] = 35
                    config.current_state = config.STATE_BATTLE
                else:
                    console.print("[red]Locked![/red]")
                    time.sleep(1)

            elif choice == "3-14":
                if unlocked >= 35:
                    config.player_data["selected_stage"] = 36
                    config.current_state = config.STATE_BATTLE
                else:
                    console.print("[red]Locked![/red]")
                    time.sleep(1)

            elif choice == "3-15":
                if unlocked >= 36:
                    config.player_data["selected_stage"] = 37
                    config.current_state = config.STATE_BATTLE
                else:
                    console.print("[red]Locked![/red]")
                    time.sleep(1)

            elif choice == "3-16":
                if unlocked >= 37:
                    config.player_data["selected_stage"] = 38
                    config.current_state = config.STATE_BATTLE
                else:
                    console.print("[red]Locked![/red]")
                    time.sleep(1)

            elif choice == "3-17":
                if unlocked >= 38:
                    config.player_data["selected_stage"] = 39
                    config.current_state = config.STATE_BATTLE
                else:
                    console.print("[red]Locked![/red]")
                    time.sleep(1)

            elif choice == "3-18":
                if unlocked >= 39:
                    if unlocked >= 40:
                        console.print("[dim]Stage Cleared.[/dim]")
                        time.sleep(0.5)
                    else:
                        story_manager.play_stage_3_18_story()
                        console.print("[bold yellow]First Clear Rewards:[/bold yellow]")
                        console.print("2x Microchip")
                        console.print("2x Microprocessor")
                        mats = config.player_data["materials"]
                        mats["Microchip"] = mats.get("Microchip", 0) + 2
                        mats["Microprocessor"] = mats.get("Microprocessor", 0) + 2
                        if config.player_data["latest_stage"] < 40: config.player_data["latest_stage"] = 40
                        sync_currencies()
                        get_player_input("Press Enter...")
                else:
                    console.print("[red]Locked![/red]")
                    time.sleep(1)

            elif choice == "3-19":
                if unlocked >= 40:
                    latest = config.player_data.get("latest_stage", 0)
                    if latest < 41:
                        story_manager.play_stage_3_19_start()
                    config.player_data["node_progress"] = {
                        "stage": 41,
                        "cleared_indices": [],
                        "party_hp": {}
                    }
                    config.current_state = config.STATE_NODE_SELECT
                else:
                    console.print("[red]Locked![/red]")
                    time.sleep(1)

            elif choice == "3-20":
                if unlocked >= 41:
                    config.player_data["selected_stage"] = 42
                    config.current_state = config.STATE_BATTLE
                else:
                    console.print("[red]Locked![/red]")
                    time.sleep(1)

            elif choice == "3-21":
                if unlocked >= 42:
                    if unlocked >= 43:
                        console.print("[dim]Stage Cleared.[/dim]")
                        time.sleep(0.5)
                    else:
                        story_manager.play_stage_3_21_story()
                        console.print("[bold yellow]First Clear Rewards:[/bold yellow]")
                        console.print("1x Microchip")
                        console.print("1x Microprocessor")
                        mats = config.player_data["materials"]
                        mats["Microchip"] = mats.get("Microchip", 0) + 1
                        mats["Microprocessor"] = mats.get("Microprocessor", 0) + 1
                        if config.player_data["latest_stage"] < 43: config.player_data["latest_stage"] = 43
                        sync_currencies()
                        get_player_input("Press Enter...")
                else:
                    console.print("[red]Locked![/red]")
                    time.sleep(1)

            elif choice == "3-22":
                if unlocked >= 43:
                    if unlocked >= 44:
                        console.print("[dim]Stage Cleared.[/dim]")
                        time.sleep(0.5)
                    else:
                        story_manager.play_stage_3_22_story()
                        console.print("[bold yellow]First Clear Rewards:[/bold yellow]")
                        console.print("1x Microchip")
                        console.print("1x Microprocessor")
                        mats = config.player_data["materials"]
                        mats["Microchip"] = mats.get("Microchip", 0) + 1
                        mats["Microprocessor"] = mats.get("Microprocessor", 0) + 1
                        if config.player_data["latest_stage"] < 44: config.player_data["latest_stage"] = 44
                        sync_currencies()
                        get_player_input("Press Enter...")
                else:
                    console.print("[red]Locked![/red]")
                    time.sleep(1)

            elif choice == "3-23":
                if unlocked >= 44:
                    if unlocked >= 45:
                        console.print("[dim]Stage Cleared.[/dim]")
                        time.sleep(0.5)
                    else:
                        story_manager.play_stage_3_23_story()
                        console.print("[bold yellow]First Clear Rewards:[/bold yellow]")
                        console.print("5x Microchip")
                        mats = config.player_data["materials"]
                        mats["Microchip"] = mats.get("Microchip", 0) + 5
                        if config.player_data["latest_stage"] < 45: config.player_data["latest_stage"] = 45
                        sync_currencies()
                        get_player_input("Press Enter...")
                else:
                    console.print("[red]Locked![/red]")
                    time.sleep(1)

            elif choice == "4-1":
                if unlocked >= 45:
                    if unlocked >= 46:
                        console.print("[dim]Stage Cleared.[/dim]")
                        time.sleep(0.5)
                    else:
                        # story_manager.play_stage_4_1_story()
                        console.print("[bold yellow]First Clear Rewards:[/bold yellow]")
                        console.print("2x Microchip")
                        console.print("2x Microprocessor")
                        mats = config.player_data["materials"]
                        mats["Microchip"] = mats.get("Microchip", 0) + 2
                        mats["Microprocessor"] = mats.get("Microprocessor", 0) + 2
                        if config.player_data["latest_stage"] < 46: config.player_data["latest_stage"] = 46
                        sync_currencies()
                        get_player_input("Press Enter...")
                else:
                    console.print("[red]Locked![/red]")
                    time.sleep(1)

            elif choice == "4-2":
                if unlocked >= 46:
                    if unlocked >= 47:
                        console.print("[dim]Stage Cleared.[/dim]")
                        time.sleep(0.5)
                    else:
                        # story_manager.play_stage_4_2_story()
                        console.print("[bold yellow]First Clear Rewards:[/bold yellow]")
                        console.print("3x Sports Water Bottle")
                        mats = config.player_data["materials"]
                        mats["Sports Water Bottle"] = mats.get("Sports Water Bottle", 0) + 3
                        if config.player_data["latest_stage"] < 47: config.player_data["latest_stage"] = 47
                        sync_currencies()
                        get_player_input("Press Enter...")
                else:
                    console.print("[red]Locked![/red]")
                    time.sleep(1)

            elif choice == "4-3":
                if unlocked >= 47:
                    if unlocked >= 48:
                        console.print("[dim]Stage Cleared.[/dim]")
                        time.sleep(0.5)
                    else:
                        # story_manager.play_stage_4_3_story()
                        console.print("[bold yellow]First Clear Rewards:[/bold yellow]")
                        console.print("3x Microchip")
                        mats = config.player_data["materials"]
                        mats["Microchip"] = mats.get("Microchip", 0) + 3
                        if config.player_data["latest_stage"] < 48: config.player_data["latest_stage"] = 48
                        sync_currencies()
                        get_player_input("Press Enter...")
                else:
                    console.print("[red]Locked![/red]")
                    time.sleep(1)

            elif choice == "4-4":
                if unlocked >= 48:
                    config.player_data["selected_stage"] = 49
                    config.current_state = config.STATE_BATTLE
                else:
                    console.print("[red]Locked![/red]")
                    time.sleep(1)
                    
        elif config.current_state == config.STATE_NODE_SELECT:
            np = config.player_data.get("node_progress")
            if not np:
                config.current_state = config.STATE_MAIN_MENU
                continue
            
            stage_num = np["stage"]
            if stage_num == 5:
                draw_node_select_menu("1-5: Weekday Errands", np["cleared_indices"])
                valid_indices = ["1", "2", "3"]
                start_id = 5001
            elif stage_num == 10:
                draw_node_select_menu("1-10: Raid", np["cleared_indices"])
                valid_indices = ["1", "2", "3", "4"]
                start_id = 10001
            elif stage_num == 14:
                draw_node_select_menu("2-3: Stalemate At The Gates", np["cleared_indices"])
                valid_indices = ["1", "2"]
                start_id = 14001
            elif stage_num == 15:
                draw_node_select_menu("2-4: Breakthrough Plan", np["cleared_indices"])
                valid_indices = ["1", "2", "3"]
                start_id = 15001
            elif stage_num == 16:
                draw_node_select_menu("2-5: Labyrinth Of Motives", np["cleared_indices"])
                valid_indices = ["1", "2", "3", "4", "5"]
                start_id = 16001
            elif stage_num == 32:
                draw_node_select_menu("3-10: Silent Passenger", np["cleared_indices"])
                valid_indices = ["1", "2", "3"]
                start_id = 32001
            elif stage_num == 34:
                draw_node_select_menu("3-12: Weapons", np["cleared_indices"])
                valid_indices = ["1", "2", "3"]
                start_id = 34001
            elif stage_num == 41:
                draw_node_select_menu("3-19: Riposte", np["cleared_indices"])
                valid_indices = ["1", "2", "3", "4"]
                start_id = 41001
            else:
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
            draw_party_management_menu(player)
            config.current_state = config.STATE_MAIN_MENU

if __name__ == "__main__":
    run_game()