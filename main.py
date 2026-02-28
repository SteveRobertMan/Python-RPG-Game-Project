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
        ("Natsume", 56, stages.create_natsume),
        ("Hana", 56, stages.create_hana),
        ("Kagaku", 56, stages.create_kagaku)
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

            # --- DYNAMIC ROSTER INJECTION ---
            # Automatically apply loadouts and inject ALL permanently unlocked characters 
            # (Akasuke, Yuri, Benikawa, Shigemura, Naganohara, Hana, Kagaku, Natsume, etc.)
            for unlocked_unit in player.units:
                # Remove the base/default version of the unit if stages.get_player_party() added it
                party = [p for p in party if p.name != unlocked_unit.name]
                
                # Get their currently equipped kata and add the fully configured unit to the party
                loadout = get_equipped_data(unlocked_unit.name)
                
                # Dynamically call stages.create_akasuke, create_benikawa, etc.
                factory_func = getattr(stages, f"create_{unlocked_unit.name.lower()}")
                party.append(factory_func(loadout))
            
            if stage_id == 4:
                has_beni = any(u.name == "Benikawa" for u in party)
                if not has_beni:
                    loadout = get_equipped_data("Benikawa")
                    party.append(stages.create_benikawa(loadout))
            
            if stage_id == 7:
                party = [member for member in party if member.name in ["Akasuke","Yuri"]]

            if (stage_id in [15001,15002,15003]):
                has_shige = any(u.name == "Shigemura" for u in party)
                if not has_shige:
                    loadout = get_equipped_data("Shigemura")
                    party.append(stages.create_shigemura(loadout))
            
            is_guest_appearance1 = (stage_id in [16, 16001, 16002, 16003, 16004, 16005, 41, 41001, 41002, 41003, 41004])
            is_officially_unlocked = (latest_cleared >= 41)
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
                party.append(guest_naganohara)
                party = [p for p in party if p.name != "Kagaku"]
                guest_loadout = scd.get_kata_data_by_name("Kasakura High School Disciplinary Committee Member Kagaku")
                guest_kagaku = stages.create_kagaku(guest_loadout)
                party.append(guest_kagaku)

            if stage_id in [49, 50, 51, 52, 53, 54, 56001, 56002, 56003, 56004, 56005]:
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

            if stage_id in [56001, 56002, 56003, 56004, 56005]:
                party = [p for p in party if p.name != "Natsume"]
                guest_loadout = scd.get_kata_data_by_name("Kasakura High School Student Natsume")
                guest_natsume = stages.create_natsume(guest_loadout)
                party.insert(5, guest_natsume)

            enemies = stages.load_stage_enemies(stage_id)
            if not enemies:
                console.print("[red]Error: Enemies not found for this stage![/red]")
                time.sleep(2)
                config.current_state = config.STATE_MAIN_MENU
                continue
    
            if stage_id in [63,65]:
                party = [member for member in party if member.name in ["Yuri","Benikawa","Shigemura","Hana"]]   
            if stage_id == 64:
                party = [member for member in party if member.name in ["Akasuke","Naganohara","Natsume","Kagaku"]]

            # Story Pre-Battle Check
            should_play_story = True
            if stage_id > 0 and latest_cleared >= stage_id: should_play_story = False
            if stage_id == 0 and latest_cleared >= 0: should_play_story = False

            # Dictionary routing for PRE-battle stories
            STORY_STARTS = {
                2: story_manager.play_stage_1_2_start, 
                4: story_manager.play_stage_1_4_start,
                6: story_manager.play_stage_1_6_start, 
                7: story_manager.play_stage_1_7_start,
                18: story_manager.play_stage_2_7_start, 
                19: story_manager.play_stage_2_8_start,
                20: story_manager.play_stage_2_9_start, 
                21: story_manager.play_stage_2_10_start,
                25: story_manager.play_stage_3_3_start, 
                26: story_manager.play_stage_3_4_start,
                28: story_manager.play_stage_3_6_start, 
                31: story_manager.play_stage_3_9_start,
                33: story_manager.play_stage_3_11_start, 
                35: story_manager.play_stage_3_13_start,
                36: story_manager.play_stage_3_14_start, 
                37: story_manager.play_stage_3_15_start,
                38: story_manager.play_stage_3_16_start, 
                39: story_manager.play_stage_3_17_start,
                42: story_manager.play_stage_3_20_start, 
                49: story_manager.play_stage_4_4_start,
                50: story_manager.play_stage_4_5_start, 
                51: story_manager.play_stage_4_6_start,
                52: story_manager.play_stage_4_7_start, 
                53: story_manager.play_stage_4_8_start,
                62: story_manager.play_stage_4_17_start, 
                63: story_manager.play_stage_4_18_start,
                64: story_manager.play_stage_4_19_start, 
                65: story_manager.play_stage_4_20_start,
                66: story_manager.play_stage_4_21_start, 
                70: story_manager.play_stage_4_25_start,
                71: story_manager.play_stage_4_26_start,
            }

            if should_play_story and stage_id in STORY_STARTS:
                STORY_STARTS[stage_id]()

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

                    # --- 1. NODE REWARDS MAP ---
                    # stage_id : ( {First Clear Drops}, [(Drop Chance, "Item Name", Qty)] )
                    NODE_REWARDS_MAP = {
                        5001: ({"Microchip": 2, "Microprocessor": 2}, [(0.25, "Cafeteria Melon Bread", 1)]),
                        5002: ({"Microchip": 2, "Microprocessor": 2}, [(0.25, "Cafeteria Melon Bread", 1)]),
                        5003: ({"Microchip": 2, "Microprocessor": 2, "Cafeteria Melon Bread": 2}, [(0.50, "Cafeteria Melon Bread", 1)]),
                        
                        10001: ({"Microchip": 2, "Microprocessor": 2}, [(0.30, "Microchip", 1)]),
                        10002: ({"Microchip": 2, "Microprocessor": 2}, [(0.30, "Microchip", 1)]),
                        10003: ({"Microchip": 3, "Microprocessor": 3}, [(0.30, "Microprocessor", 1)]),
                        10004: ({"Microchip": 3, "Microprocessor": 3}, [(0.30, "Microprocessor", 1)]),
                        
                        14001: ({"Cafeteria Melon Bread": 1, "Vending Machine Coffee": 1}, [(0.25, "Cafeteria Melon Bread", 1), (0.25, "Vending Machine Coffee", 1)]),
                        14002: ({"Cafeteria Melon Bread": 1, "Vending Machine Coffee": 1}, [(0.25, "Cafeteria Melon Bread", 1), (0.25, "Vending Machine Coffee", 1)]),
                        
                        15001: ({"Microchip": 1, "Microprocessor": 1}, [(0.25, "Cafeteria Melon Bread", 1), (0.25, "Vending Machine Coffee", 1)]),
                        15002: ({"Microchip": 1, "Microprocessor": 1}, [(0.25, "Cafeteria Melon Bread", 1), (0.25, "Vending Machine Coffee", 1)]),
                        15003: ({"Microchip": 1, "Microprocessor": 1}, [(0.25, "Cafeteria Melon Bread", 1), (0.25, "Vending Machine Coffee", 1)]),
                        
                        16001: ({"Microchip": 2}, [(0.50, "Vending Machine Coffee", 1)]),
                        16002: ({"Microchip": 2}, [(0.50, "Vending Machine Coffee", 1)]),
                        16003: ({"Vending Machine Coffee": 2}, [(0.50, "Vending Machine Coffee", 1)]),
                        16004: ({"Vending Machine Coffee": 2}, [(0.50, "Vending Machine Coffee", 1)]),
                        16005: ({"Cafeteria Melon Bread": 3}, [(0.50, "Vending Machine Coffee", 1)]),
                        
                        32001: ({"Microchip": 2}, [(0.25, "Sports Water Bottle", 1)]),
                        32002: ({"Microchip": 2}, [(0.25, "Sports Water Bottle", 1)]),
                        32003: ({"Sports Water Bottle": 3}, [(0.25, "Sports Water Bottle", 1)]),
                        
                        34001: ({"Sports Water Bottle": 1, "Microprocessor": 2}, [(0.65, "Microchip", 1)]),
                        34002: ({"Sports Water Bottle": 1, "Microprocessor": 2}, [(0.65, "Microchip", 1)]),
                        34003: ({"Sports Water Bottle": 1, "Microprocessor": 2}, [(0.65, "Microchip", 1)]),
                        
                        41001: ({"Microchip": 1}, [(0.375, "Cafeteria Melon Bread", 1), (0.375, "Vending Machine Coffee", 1), (0.375, "Sports Water Bottle", 1)]),
                        41002: ({"Microchip": 1}, [(0.375, "Cafeteria Melon Bread", 1), (0.375, "Vending Machine Coffee", 1), (0.375, "Sports Water Bottle", 1)]),
                        41003: ({"Microchip": 1}, [(0.375, "Cafeteria Melon Bread", 1), (0.375, "Vending Machine Coffee", 1), (0.375, "Sports Water Bottle", 1)]),
                        41004: ({"Microchip": 1}, [(0.375, "Cafeteria Melon Bread", 1), (0.375, "Vending Machine Coffee", 1), (0.375, "Sports Water Bottle", 1)]),

                        56001: ({"Yunhai Herbal Powder": 1}, [(0.15, "Yunhai Herbal Powder", 1)]),
                        56002: ({"Microchip": 1}, [(0.15, "Yunhai Herbal Powder", 1)]),
                        56003: ({"Microchip": 1}, [(0.15, "Yunhai Herbal Powder", 1)]),
                        56004: ({"Microchip": 1}, [(0.15, "Yunhai Herbal Powder", 1)]),
                        56005: ({"Yunhai Herbal Powder": 1}, [(0.15, "Yunhai Herbal Powder", 1)]),

                        57001: ({"Yunhai Herbal Powder": 1}, [(0.15, "Yunhai Herbal Powder", 1)]),
                        57002: ({"Microchip": 1}, [(0.15, "Yunhai Herbal Powder", 1)]),
                        57003: ({"Microchip": 1}, [(0.15, "Yunhai Herbal Powder", 1)]),
                        57004: ({"Microchip": 1}, [(0.15, "Yunhai Herbal Powder", 1)]),
                        57005: ({"Yunhai Herbal Powder": 1}, [(0.15, "Yunhai Herbal Powder", 1)]),

                        58001: ({"Yunhai Herbal Powder": 1}, [(0.15, "Yunhai Herbal Powder", 1)]),
                        58002: ({"Microchip": 1}, [(0.15, "Yunhai Herbal Powder", 1)]),
                        58003: ({"Microchip": 1}, [(0.15, "Yunhai Herbal Powder", 1)]),
                        58004: ({"Microchip": 1}, [(0.15, "Yunhai Herbal Powder", 1)]),
                        58005: ({"Yunhai Herbal Powder": 1}, [(0.15, "Yunhai Herbal Powder", 1)]),

                        60001: ({"Yunhai Herbal Powder": 1}, [(0.15, "Yunhai Herbal Powder", 1)]),
                        60002: ({"Microchip": 1}, [(0.15, "Yunhai Herbal Powder", 1)]),
                        60003: ({"Yunhai Herbal Powder": 1}, [(0.15, "Yunhai Herbal Powder", 1)]),

                        68001: ({"Microprocessor": 2}, [(0.15, "Jade Microchip", 1)]),
                        68002: ({"Microprocessor": 2}, [(0.15, "Jade Microchip", 1)]),
                        68003: ({"Microprocessor": 2}, [(0.15, "Jade Microchip", 1)]),
                        68004: ({"Microprocessor": 2}, [(0.15, "Jade Microchip", 1)]),

                        69001: ({"Microchip": 2}, [(0.15, "Jade Microchip", 1)]),
                        69002: ({"Microchip": 2}, [(0.15, "Jade Microchip", 1)]),
                        69003: ({"Microchip": 2}, [(0.15, "Jade Microchip", 1)]),
                    }

                    # Apply Dynamic Rewards
                    if stage_id in NODE_REWARDS_MAP:
                        first_drops, repeat_drops = NODE_REWARDS_MAP[stage_id]
                        if is_first_node_clear:
                            for item, qty in first_drops.items():
                                rewards_text.append(f"{qty}x {item}")
                                mats[item] = mats.get(item, 0) + qty
                        else:
                            for chance, item, qty in repeat_drops:
                                if random.random() < chance:
                                    rewards_text.append(f"{qty}x {item}")
                                    mats[item] = mats.get(item, 0) + qty

                    # HP HEALING MESSAGE
                    console.print(f"Party HP Fully Recovered.")

                    # PROGRESS TRACKING
                    node_idx = stage_id - (np["stage"] * 1000) - 1
                    if node_idx not in np["cleared_indices"]:
                        np["cleared_indices"].append(node_idx)
                        config.player_data["node_progress"] = np

                    # --- 2. NODE COMPLETION METADATA ---
                    # np_stage : (required_nodes, Stage Name)
                    NODE_META_MAP = {
                        5: (3, "1-5"), 10: (4, "1-10"), 14: (2, "2-3"),
                        15: (3, "2-4"), 16: (5, "2-5"), 32: (3, "3-10"),
                        34: (3, "3-12"), 41: (4, "3-19"), 56: (5, "4-11"), 57: (5, "4-12"), 58: (5, "4-13"), 60: (3, "4-15"), 68: (4, "4-23"), 69: (3, "4-24")
                    }
                    req_count, s_name = NODE_META_MAP.get(np["stage"], (99, "??"))

                    # COMPLETION CHECK
                    if len(np["cleared_indices"]) >= req_count:
                        console.print(f"[bold green]STAGE {s_name} COMPLETE![/bold green]")

                        if config.player_data["latest_stage"] < np["stage"]:
                            
                            # --- 3. NODE STORY ENDS MAP ---
                            # np_stage : (Story Function, Optional Special Reward String)
                            NODE_STORY_ENDS = {
                                10: (story_manager.play_stage_1_10_end, None),
                                14: (story_manager.play_stage_2_3_end, None),
                                15: (story_manager.play_stage_2_4_end, "[bold magenta]NEW MEMBER: Shigemura[/bold magenta]"),
                                16: (story_manager.play_stage_2_5_end, None),
                                38: (story_manager.play_stage_3_15_end, None),
                                41: (story_manager.play_stage_3_19_end, "[bold magenta]NEW MEMBER: Naganohara[/bold magenta]"),
                                56: (story_manager.play_stage_4_11_end, "[bold magenta]NEW MEMBER: Natsume[/bold magenta]\n[bold magenta]NEW MEMBER: Hana[/bold magenta]\n[bold magenta]NEW MEMBER: Kagaku[/bold magenta]"),
                                57: (story_manager.play_stage_4_12_end, None),
                                58: (story_manager.play_stage_4_13_end, None),
                                60: (story_manager.play_stage_4_15_end, None),
                            }
                            
                            if np["stage"] in NODE_STORY_ENDS:
                                end_func, extra_reward = NODE_STORY_ENDS[np["stage"]]
                                end_func()
                                if extra_reward:
                                    rewards_text.append(extra_reward)
                            
                            config.player_data["latest_stage"] = np["stage"]

                        # Apply Clear Flags
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

                # --- STANDARD STAGES REWARDS ---
                else:
                    # Grouping Stages by Reward Types
                    group_3chip_3proc = [2, 4, 6, 7, 18, 19, 20, 21, 25, 26, 28, 29, 31]
                    group_2proc_1water = [33, 35, 36, 37, 38, 39, 40]
                    group_2chip_2proc = [49, 50, 51]
                    group_yunhai = [52, 53, 56, 57, 58, 60]
                    group_5jade = [62, 63, 70]
                    group_1jade = [64, 65, 66, 68, 69, 71]
                    
                    # Dictionary routing for POST-battle stories (Standard Stages)
                    STORY_ENDS = {
                        # --- ACT 1 ---
                        2: story_manager.play_stage_1_2_end,
                        4: story_manager.play_stage_1_4_end,
                        6: story_manager.play_stage_1_6_end,
                        7: story_manager.play_stage_1_7_end,
                        # --- ACT 2 ---
                        18: story_manager.play_stage_2_7_end,
                        19: story_manager.play_stage_2_8_end,
                        20: story_manager.play_stage_2_9_end,
                        21: story_manager.play_stage_2_10_end,
                        # --- ACT 3 ---
                        29: story_manager.play_stage_3_7_end,
                        31: story_manager.play_stage_3_9_end,
                        33: story_manager.play_stage_3_11_end,
                        37: story_manager.play_stage_3_15_end,
                        38: story_manager.play_stage_3_16_end,
                        39: story_manager.play_stage_3_17_end,
                        # --- ACT 4 ---
                        49: story_manager.play_stage_4_4_end,   
                        50: story_manager.play_stage_4_5_end,
                        51: story_manager.play_stage_4_6_end,
                        52: story_manager.play_stage_4_7_end,
                        53: story_manager.play_stage_4_8_end,
                        56: story_manager.play_stage_4_11_end,
                        57: story_manager.play_stage_4_12_end,
                        58: story_manager.play_stage_4_13_end,
                        60: story_manager.play_stage_4_15_end,
                        62: story_manager.play_stage_4_17_end,
                        63: story_manager.play_stage_4_18_end,
                        66: story_manager.play_stage_4_21_end,
                    }

                    if should_play_story:
                        if stage_id in STORY_ENDS:
                            STORY_ENDS[stage_id]()
                            
                        # Apply First Clear Rewards Based on Groups
                        if stage_id in group_3chip_3proc:
                            amt = 5 if stage_id == 7 else 3
                            rewards_text.extend([f"{amt}x Microchip", f"{amt}x Microprocessor"])
                            mats["Microchip"] = mats.get("Microchip", 0) + amt
                            mats["Microprocessor"] = mats.get("Microprocessor", 0) + amt
                        
                        elif stage_id in group_2proc_1water:
                            rewards_text.extend(["2x Microprocessor", "1x Sports Water Bottle"])
                            mats["Microprocessor"] = mats.get("Microprocessor", 0) + 2
                            mats["Sports Water Bottle"] = mats.get("Sports Water Bottle", 0) + 1
                            
                        elif stage_id in group_2chip_2proc:
                            rewards_text.extend(["2x Microchip", "2x Microprocessor"])
                            mats["Microchip"] = mats.get("Microchip", 0) + 2
                            mats["Microprocessor"] = mats.get("Microprocessor", 0) + 2
                            
                        elif stage_id in group_yunhai:
                            rewards_text.extend(["1x Yunhai Herbal Powder", "1x Microprocessor"])
                            mats["Yunhai Herbal Powder"] = mats.get("Yunhai Herbal Powder", 0) + 1
                            mats["Microprocessor"] = mats.get("Microprocessor", 0) + 1
                            
                        elif stage_id in group_5jade:
                            rewards_text.extend(["5x Jade Microchip"])
                            mats["Jade Microchip"] = mats.get("Jade Microchip", 0) + 5
                            
                        elif stage_id in group_1jade:
                            rewards_text.extend(["1x Jade Microchip"])
                            mats["Jade Microchip"] = mats.get("Jade Microchip", 0) + 1

                        # Update Progress
                        if config.player_data["latest_stage"] < stage_id: 
                            config.player_data["latest_stage"] = stage_id
                        cl = config.player_data.get("cleared_stages", [])
                        if stage_id not in cl: cl.append(stage_id)
                        config.player_data["cleared_stages"] = cl

                    else:
                        # Apply Repeat Clear Rewards
                        if stage_id in group_3chip_3proc:
                            if random.random() < 0.65: rewards_text.append("1x Microchip"); mats["Microchip"] = mats.get("Microchip", 0) + 1
                            if random.random() < 0.65: rewards_text.append("1x Microprocessor"); mats["Microprocessor"] = mats.get("Microprocessor", 0) + 1
                        
                        elif stage_id in group_2chip_2proc:
                            if random.random() < 0.7: rewards_text.append("1x Microchip"); mats["Microchip"] = mats.get("Microchip", 0) + 1
                            if random.random() < 0.7: rewards_text.append("1x Microprocessor"); mats["Microprocessor"] = mats.get("Microprocessor", 0) + 1
                            
                        elif stage_id in group_yunhai:
                            if random.random() < 0.45: rewards_text.append("1x Yunhai Herbal Powder"); mats["Yunhai Herbal Powder"] = mats.get("Yunhai Herbal Powder", 0) + 1
                            
                        elif stage_id in group_5jade + group_1jade:
                            if random.random() < 0.3: rewards_text.append("1x Jade Microchip"); mats["Jade Microchip"] = mats.get("Jade Microchip", 0) + 1

                    config.current_state = config.STATE_MAIN_MENU

                if rewards_text:
                    console.print("[bold yellow]REWARDS:[/bold yellow]")
                    for r in rewards_text: console.print(f"- {r}")
                else:
                    if stage_id != 0: console.print("[dim]No drops this time.[/dim]")

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
            # --- STAGE DEFINITION MAPS ---
            # req_idx : (Story_Function, [Reward String List], {Material Update Dict})
            STORY_STAGES = {
                # --- ACT 1 ---
                0:  (story_manager.play_stage_1_1_story, ["3x Microchip", "3x Microprocessor"], {"Microchip": 3, "Microprocessor": 3}),
                2:  (story_manager.play_stage_1_3_story, ["3x Microchip", "3x Microprocessor"], {"Microchip": 3, "Microprocessor": 3}),
                7:  (story_manager.play_stage_1_8_story, ["2x Microchip", "2x Microprocessor"], {"Microchip": 2, "Microprocessor": 2}),
                8:  (story_manager.play_stage_1_9_story, ["2x Microchip", "2x Microprocessor"], {"Microchip": 2, "Microprocessor": 2}),
                10: (story_manager.play_stage_1_11_story, ["5x Microchip"], {"Microchip": 5}),
                # --- ACT 2 ---
                11: (story_manager.play_stage_2_1_story, ["2x Microchip", "2x Microprocessor"], {"Microchip": 2, "Microprocessor": 2}),
                12: (story_manager.play_stage_2_2_story, ["2x Microchip", "2x Microprocessor"], {"Microchip": 2, "Microprocessor": 2}),
                16: (story_manager.play_stage_2_6_story, ["2x Microchip", "2x Microprocessor"], {"Microchip": 2, "Microprocessor": 2}),
                21: (story_manager.play_stage_2_11_story, ["3x Microchip", "3x Microprocessor"], {"Microchip": 3, "Microprocessor": 3}),
                # --- ACT 3 ---
                22: (story_manager.play_stage_3_1_story, ["2x Microchip", "2x Microprocessor"], {"Microchip": 2, "Microprocessor": 2}),
                23: (story_manager.play_stage_3_2_story, ["2x Microchip", "2x Microprocessor"], {"Microchip": 2, "Microprocessor": 2}),
                26: (story_manager.play_stage_3_5_story, ["2x Microchip", "2x Microprocessor"], {"Microchip": 2, "Microprocessor": 2}),
                29: (story_manager.play_stage_3_8_story, ["2x Microchip", "2x Microprocessor"], {"Microchip": 2, "Microprocessor": 2}),
                39: (story_manager.play_stage_3_18_story, ["2x Microchip", "2x Microprocessor"], {"Microchip": 2, "Microprocessor": 2}),
                42: (story_manager.play_stage_3_21_story, ["1x Microchip", "1x Microprocessor"], {"Microchip": 1, "Microprocessor": 1}),
                43: (story_manager.play_stage_3_22_story, ["1x Microchip", "1x Microprocessor"], {"Microchip": 1, "Microprocessor": 1}),
                44: (story_manager.play_stage_3_23_story, ["5x Microchip"], {"Microchip": 5}),
                # --- ACT 4 ---
                45: (story_manager.play_stage_4_1_story, ["2x Microchip", "2x Microprocessor"], {"Microchip": 2, "Microprocessor": 2}),
                46: (story_manager.play_stage_4_2_story, ["3x Sports Water Bottle"], {"Sports Water Bottle": 3}),
                47: (story_manager.play_stage_4_3_story, ["3x Microchip"], {"Microchip": 3}),
                53: (story_manager.play_stage_4_9_story, ["1x Yunhai Herbal Powder"], {"Yunhai Herbal Powder": 1}),
                54: (story_manager.play_stage_4_10_story, ["1x Yunhai Herbal Powder"], {"Yunhai Herbal Powder": 1}),
                58: (story_manager.play_stage_4_14_story, ["1x Yunhai Herbal Powder"], {"Yunhai Herbal Powder": 1}),
                60: (story_manager.play_stage_4_16_story, ["3x Yunhai Herbal Powder"], {"Yunhai Herbal Powder": 3}),
                66: (story_manager.play_stage_4_22_story, ["2x Jade Microchip"], {"Jade Microchip": 2}),
                71: (story_manager.play_stage_4_27_story, ["2x Jade Microchip"], {"Jade Microchip": 2}),
                72: (story_manager.play_stage_4_28_story, ["10x Microprocessor"], {"Microprocessor": 10}),
            }

            # req_idx : stage_id
            BATTLE_STAGES = {
                # Act 1
                1: 2, 3: 4, 5: 6, 6: 7, 
                # Act 2
                17: 18, 18: 19, 19: 20, 20: 21,
                # Act 3
                24: 25, 25: 26, 27: 28, 28: 29, 30: 31, 32: 33, 34: 35, 35: 36, 36: 37, 37: 38, 38: 39, 41: 42,
                # Act 4
                48: 49, 49: 50, 50: 51, 51: 52, 52: 53, 61: 62, 62: 63, 63: 64, 64: 65, 65: 66, 69: 70, 70: 71
            }

            # req_idx : (Node Start Function, node_stage_number)
            NODE_STAGES = {
                4:  (story_manager.play_stage_1_5_start, 5),
                9:  (story_manager.play_stage_1_10_start, 10),
                13: (story_manager.play_stage_2_3_start, 14),
                14: (story_manager.play_stage_2_4_start, 15),
                15: (story_manager.play_stage_2_5_start, 16),
                31: (story_manager.play_stage_3_10_start, 32),
                33: (story_manager.play_stage_3_12_start, 34),
                40: (story_manager.play_stage_3_19_start, 41),
                55: (story_manager.play_stage_4_11_start, 56),
                56: (story_manager.play_stage_4_12_start, 57),
                57: (story_manager.play_stage_4_13_start, 58),
                59: (story_manager.play_stage_4_15_start, 60),
                67: (story_manager.play_stage_4_23_start, 68),
                68: (story_manager.play_stage_4_24_start, 69),
            }
            
            unlocked = config.player_data.get("latest_stage", 0)
            choice = draw_stage_select_menu(unlocked)
            
            if choice == "0": 
                config.current_state = config.STATE_MAIN_MENU
                continue
            
            # Use string parsing for modular logic!
            if "-" in choice:
                act, sub = map(int, choice.split("-"))
                
                # Calculate required unlock index (req_idx)
                req_idx = -1
                if act == 1: req_idx = sub - 1
                elif act == 2: req_idx = 10 + sub
                elif act == 3: req_idx = 21 + sub
                elif act == 4: req_idx = 44 + sub

                if unlocked >= req_idx:
                    # 1. Is it a Story Stage?
                    if req_idx in STORY_STAGES:
                        if unlocked > req_idx:
                            console.print("[dim]Stage Cleared.[/dim]")
                            time.sleep(0.5)
                        else:
                            story_func, rew_text, mat_dict = STORY_STAGES[req_idx]
                            story_func()
                            console.print("[bold yellow]First Clear Rewards:[/bold yellow]")
                            for text in rew_text: console.print(text)
                            
                            mats = config.player_data["materials"]
                            for mat_name, amt in mat_dict.items():
                                mats[mat_name] = mats.get(mat_name, 0) + amt
                            
                            if config.player_data["latest_stage"] < (req_idx + 1): 
                                config.player_data["latest_stage"] = req_idx + 1
                            
                            cl = config.player_data.get("cleared_stages", [])
                            if (req_idx + 1) not in cl: cl.append(req_idx + 1)
                            config.player_data["cleared_stages"] = cl
                            
                            sync_currencies()
                            get_player_input("Press Enter...")
                            
                    # 2. Is it a standard Battle Stage?
                    elif req_idx in BATTLE_STAGES:
                        config.player_data["selected_stage"] = BATTLE_STAGES[req_idx]
                        config.current_state = config.STATE_BATTLE
                        
                    # 3. Is it a Node Stage?
                    elif req_idx in NODE_STAGES:
                        start_func, node_id = NODE_STAGES[req_idx]
                        if unlocked <= req_idx: 
                            start_func()
                        
                        config.player_data["node_progress"] = {
                            "stage": node_id,
                            "cleared_indices": [],
                            "party_hp": {}
                        }
                        config.current_state = config.STATE_NODE_SELECT
                else:
                    console.print("[red]Locked![/red]")
                    time.sleep(1)
            
            if choice == "0": 
                config.current_state = config.STATE_MAIN_MENU
                continue
                    
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
            elif stage_num == 56:
                draw_node_select_menu("4-11: Endless Wave I", np["cleared_indices"])
                valid_indices = ["1", "2", "3", "4", "5"]
                start_id = 56001
            elif stage_num == 57:
                draw_node_select_menu("4-12: Endless Wave II", np["cleared_indices"])
                valid_indices = ["1", "2", "3", "4", "5"]
                start_id = 57001
            elif stage_num == 58:
                draw_node_select_menu("4-13: Endless Wave III", np["cleared_indices"])
                valid_indices = ["1", "2", "3", "4", "5"]
                start_id = 58001
            elif stage_num == 60:
                draw_node_select_menu("4-15: Classical Performance", np["cleared_indices"])
                valid_indices = ["1", "2", "3"]
                start_id = 60001
            elif stage_num == 68:
                draw_node_select_menu("4-23: A Senior's Morale", np["cleared_indices"])
                valid_indices = ["1", "2", "3", "4"]
                start_id = 68001
            elif stage_num == 69:
                draw_node_select_menu("4-24: The Ten Thousand Blossom Brotherhood", np["cleared_indices"])
                valid_indices = ["1", "2", "3"]
                start_id = 69001
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