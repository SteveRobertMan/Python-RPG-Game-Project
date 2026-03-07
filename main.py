import sys
import time
import random
import copy
import math
from rich.panel import Panel 
from rich.console import Console 
import config
import scd
from player_state import player
import ui_components

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
import lattice_encounters
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
        player.currencies["jade microchips"] = mats.get("Jade Microchip", 0)

def handle_title_screen():
    draw_title_screen()
    choice = get_player_input("Enter Option Key: ")
    if choice == "1":
        config.player_data = save_manager.data.copy()
        config.player_data["latest_stage"] = -1 
        #FOR TESTING: config.player_data["materials"] = {"Microchip": 50, "Microprocessor": 10}
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

def terminate_lattice_run(run_state, is_victory=False):
    """Calculates final rewards, updates player profile, and cleans up the run."""
    stats = run_state.get("cleared_stats", {"battles": 0, "elites": 0, "bosses": 0, "events": 0})
    highest_day = run_state.get("day", 1)
    lattice_name = run_state.get("lattice", "Stable Lattice")
    
    # Random Multipliers
    xp_mult = random.uniform(1.01, 1.50)
    man_mult = random.uniform(1.01, 1.50)
    
    # --- XP CALCULATION ---
    # Formula: [[(Battles*2)+(Elites*3)+(Events*1)+(Bosses*4)]*(Highest Day)]*Random Multiplier
    base_xp = (stats["battles"] * 2) + (stats["elites"] * 3) + (stats["events"] * 1) + (stats["bosses"] * 4)
    gained_xp = math.floor((base_xp * highest_day) * xp_mult)
    
    # --- MANUSCRIPT CALCULATION ---
    # Formula: [[(Battles/3)+(Elites/2)+(Events/2)+(Bosses/2)]+(Highest Day)+1]*Random Multiplier
    base_man = (stats["battles"] / 3.0) + (stats["elites"] / 2.0) + (stats["events"] / 2.0) + (stats["bosses"] / 2.0)
    gained_manuscripts = math.floor((base_man + highest_day + 1) * man_mult)

    # --- APPLY TO PLAYER PROFILE ---
    from player_state import player
    from save_system import save_manager
    import ui_components
    
    player.lattice_xp[lattice_name] = player.lattice_xp.get(lattice_name, 0) + gained_xp
    player.manuscripts_owned[lattice_name] = player.manuscripts_owned.get(lattice_name, 0) + gained_manuscripts
    
    # Handle Level Ups
    current_lvl = player.lattice_levels.get(lattice_name, 1)
    # XP Req Formula: 20 + (Current Required / 20) -> Approx: 20 + (Lvl * 1) for simplicity unless recursive is strictly needed
    while True:
        req_xp = int(20 + sum([(20 + (i * 1)) / 20 for i in range(1, current_lvl)]))
        if player.lattice_xp[lattice_name] >= req_xp:
            player.lattice_xp[lattice_name] -= req_xp
            current_lvl += 1
            player.lattice_levels[lattice_name] = current_lvl
        else:
            break

    # Clean up the run state
    save_manager.delete_lattice_run()
    config.run_state = None
    config.player_data["lattice_mode"] = False
    
    # Display Results UI
    ui_components.clear_screen()
    ui_components.print_header(f"LATTICE TRIAGE COMPLETE")
    ui_components.config.console.print(f"Status: {'[green]SURVIVED[/green]' if is_victory else '[red]VANGUARD DEFEATED[/red]'}")
    ui_components.config.console.print(f"Days Reached: {highest_day}")
    ui_components.config.console.print(f"Battles: {stats['battles']} | Elites: {stats['elites']} | Events: {stats['events']} | Bosses: {stats['bosses']}\n")
    ui_components.config.console.print(f"[bold cyan]+ {gained_xp} {lattice_name} XP[/bold cyan] (Current Level: {current_lvl})")
    ui_components.config.console.print(f"[bold yellow]+ {gained_manuscripts} {lattice_name} Manuscripts[/bold yellow]")
    
    ui_components.get_player_input("\nPress Enter to return to the Hub...")
    config.current_state = config.STATE_LATTICE_MENU

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

def is_map_fully_connected(grid, start_pos, total_nodes):
    """Flood-fill algorithm to verify all nodes are reachable."""
    size = len(grid)
    visited = set()
    queue = [start_pos]
    visited.add(start_pos)
    node_count = 0

    while queue:
        x, y = queue.pop(0)
        # Check adjacent (Up, Down, Left, Right)
        for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < size and 0 <= ny < size:
                if (nx, ny) not in visited and grid[ny][nx] != '☒':
                    visited.add((nx, ny))
                    queue.append((nx, ny))
                    if grid[ny][nx] != '☑': # If it's a real playable node
                        node_count += 1
                        
    return node_count >= total_nodes

def generate_lattice_map(day):
    """Generates the procedural map and guarantees playability."""
    size = min(5 + (day * 2), 11) # Caps at 11 for sane rendering, though can grow
    raw_node_amount = int(((size ** 2) / 2) * random.uniform(0.60, 1.30))
    moves = int((raw_node_amount * 2) * random.uniform(0.40, 1.20))
    
    while True:
        # Create empty grid filled with walls
        grid = [['☒' for _ in range(size)] for _ in range(size)]
        center = size // 2
        player_pos = (center, center)
        grid[center][center] = '☑' # Mark starting space as a cleared space
        
        # Calculate Node Distribution
        battles = int(raw_node_amount * 0.50)
        elites = int(raw_node_amount * 0.10)
        events = int(raw_node_amount * 0.30)
        empties = max(1, raw_node_amount - battles - elites - events)
        
        total_real_nodes = battles + elites + events
        nodes_to_place = ['☑'] * empties + ['⛞'] * battles + ['▣'] * events + ['𖣯'] * elites
        random.shuffle(nodes_to_place)
        
        # Phase 1: Place adjacent empties (Safe Nodes)
        adjacents = [(center, center-1), (center, center+1), (center-1, center), (center+1, center)]
        placed_empties = 0
        for ax, ay in adjacents:
            if placed_empties < empties and 0 <= ax < size and 0 <= ay < size:
                grid[ay][ax] = '☑'
                nodes_to_place.remove('☑')
                placed_empties += 1
                
        # Phase 2: Random walk generation
        current_options = []
        for ax, ay in adjacents:
             if grid[ay][ax] != '☒' and grid[ay][ax] != '✾':
                 current_options.append((ax, ay))
                 
        if not current_options:
            continue # Failed generation, retry

        placed = 0
        while nodes_to_place and placed < 1000: # Timeout prevention
            placed += 1
            node_type = nodes_to_place.pop(0)
            
            # Find an existing non-wall tile to branch from
            branch_points = []
            for y in range(size):
                for x in range(size):
                    if grid[y][x] != '☒' and grid[y][x] != '✾':
                        # Check if it has at least one adjacent wall
                        has_wall = False
                        for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < size and 0 <= ny < size and grid[ny][nx] == '☒':
                                has_wall = True
                                break
                        if has_wall:
                            branch_points.append((x, y))
            
            if not branch_points: break
            base_x, base_y = random.choice(branch_points)
            
            # Find an empty wall adjacent to this base
            valid_targets = []
            for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                nx, ny = base_x + dx, base_y + dy
                if 0 <= nx < size and 0 <= ny < size and grid[ny][nx] == '☒':
                    valid_targets.append((nx, ny))
            
            if valid_targets:
                tx, ty = random.choice(valid_targets)
                grid[ty][tx] = node_type
            else:
                nodes_to_place.append(node_type) # Put back if failed
                random.shuffle(nodes_to_place)

        # Validate Pathfinding
        if is_map_fully_connected(grid, player_pos, total_real_nodes):
            return grid, player_pos, moves

# --- REPLACE open_manuscript_shop IN main.py ---
def open_manuscript_shop(lattice_name, run_state):
    """The pre-run buff shop where players spend Manuscripts."""
    from player_state import player
    import ui_components
    # Initialize run_state buff trackers if not present
    if "manuscript_buffs" not in run_state:
        run_state["manuscript_buffs"] = {
            "strength": 0, "vitality": 0, "pathfinding": 0, "enfeeble": 0,
            "riches": 0, "bargaining": 0, "treasure_hunter": 0, "boost": 0
        }
    buff_costs = [1, 2, 4, 6] # Example tier costs for Strength/Vitality (adjust per raw content for others if needed)
    while True:
        ui_components.clear_screen()
        ui_components.print_header(f"MANUSCRIPT SHOP: {lattice_name}")
        owned = player.manuscripts_owned.get(lattice_name, 0)
        config.console.print(f"[bold yellow]Owned Manuscripts:[/bold yellow] {owned}\n")
        # Display current levels
        b = run_state["manuscript_buffs"]
        config.console.print(f"Current Buffs:")
        config.console.print(f"Strength Lvl {b['strength']} | Vitality Lvl {b['vitality']} | Pathfinding Lvl {b['pathfinding']} | Enfeeble Lvl {b['enfeeble']}")
        config.console.print(f"Riches Lvl {b['riches']} | Bargain Lvl {b['bargaining']} | Treasure Lvl {b['treasure_hunter']} | Boost Lvl {b['boost']}\n")
        config.console.print("[honeydew2][1] Upgrade Strength[/honeydew2]")
        config.console.print("[honeydew2][2] Upgrade Vitality[/honeydew2]")
        config.console.print("[honeydew2][3] Upgrade Pathfinding[/honeydew2]")
        config.console.print("[honeydew2][4] Upgrade Enfeeble[/honeydew2]")
        config.console.print("[honeydew2][5] Upgrade Riches[/honeydew2]")
        config.console.print("[honeydew2][6] Upgrade Bargaining[/honeydew2]")
        config.console.print("[honeydew2][7] Upgrade Treasure Hunter[/honeydew2]")
        config.console.print("[honeydew2][8] Upgrade Boost[/honeydew2]")
        config.console.print("[honeydew2][0] Done / Start Run[/honeydew2]")
        choice = ui_components.get_player_input("Select Upgrade (or 0 to exit) > ")
        if choice == "0": break
        mapping = {"1": "strength", "2": "vitality", "3": "pathfinding", "4": "enfeeble", 
                   "5": "riches", "6": "bargaining", "7": "treasure_hunter", "8": "boost"}
        if choice in mapping:
            stat = mapping[choice]
            current_lvl = b[stat]
            if current_lvl >= 4:
                config.console.print("[red]Already at MAX level![/red]")
            else:
                cost = buff_costs[current_lvl] # Using uniform cost array for example
                if owned >= cost:
                    player.manuscripts_owned[lattice_name] -= cost
                    run_state["manuscript_buffs"][stat] += 1
                    config.console.print(f"[green]Upgraded {stat} to Lvl {current_lvl + 1}![/green]")
                else:
                    config.console.print(f"[red]Not enough Manuscripts! Need {cost}.[/red]")
            ui_components.time.sleep(1)

def generate_static_shop_items(lattice_name, owned_manifolds):
    """Generates 6-8 shop items prioritizing unowned items and using correct rates."""
    import random
    
    # Example placeholder pools (You will fill these with the raw content lists)
    pool = {
        "I": ["Cafeteria Melon Bread (I)", "Station Melon Bread (I)"], 
        "II": ["Standard Kasakura Tracksuit (II)"],
        "III": ["Kevlar Undersuit (III)"],
        "IV": ["Chipped Broadsword (IV)"]
    }
    
    num_items = random.randint(6, 8)
    shop_inventory = []
    
    # Rule: 40% chance to guarantee Tier III, else 80% Tier II
    first_tier = None
    if random.random() < 0.40: first_tier = "III"
    elif random.random() < 0.80: first_tier = "II"
    
    for i in range(num_items):
        target_tier = "I"
        if i == 0 and first_tier:
            target_tier = first_tier
        else:
            roll = random.random()
            if roll < 0.03: target_tier = "IV"
            elif roll < 0.18: target_tier = "III"
            elif roll < 0.50: target_tier = "II"
            else: target_tier = "I"
            
        # Try to find unowned item of target tier
        available = [m for m in pool[target_tier] if m not in owned_manifolds and m not in [x["name"] for x in shop_inventory]]
        if not available:
            # Fallback to lower tiers if empty
            available = [m for t in ["I", "II", "III", "IV"] for m in pool[t] if m not in owned_manifolds and m not in [x["name"] for x in shop_inventory]]
            
        if available:
            chosen = random.choice(available)
            tier_val = {"I":1, "II":2, "III":3, "IV":4}.get(target_tier, 1)
            price = int(80 * tier_val * random.uniform(0.80, 1.60))
            shop_inventory.append({"name": chosen, "price": price, "locked": False, "tier": tier_val})
            
    return shop_inventory

def open_static_shop(run_state):
    """Interactive loop for the end-of-floor Static Shop."""
    import ui_components
    import random
    
    heals_left = 2
    team_changes_left = 1
    refresh_cost = int(50 * random.uniform(0.60, 1.20))
    inventory = generate_static_shop_items(run_state["lattice"], run_state["owned_manifolds"])
    
    while True:
        ui_components.clear_screen()
        ui_components.print_header(f"STATIC SHOP - DAY {run_state['day']}")
        config.console.print(f"[bold]Static Owned:[/bold] {config.STATIC_SYMBOL} {run_state['static']}\n")
        
        # Draw Inventory
        for idx, item in enumerate(inventory):
            if item["locked"]:
                config.console.print(f"[{idx+1}] [dim]SOLD OUT[/dim]")
            else:
                config.console.print(f"[{idx+1}] {item['name']} - {config.STATIC_SYMBOL} {item['price']}")
                
        config.console.print("\n[H] Heal 30% HP (Cost: 100) " + f"[{heals_left} left]")
        config.console.print(f"[T] Change Team (Cost: 100) [{team_changes_left} left]")
        config.console.print(f"[R] Refresh Shop (Cost: {refresh_cost})")
        config.console.print(f"[S] Sell Owned Manifolds")
        config.console.print("\n[0] Exit Shop & Proceed to Boss / Next Day")
        
        choice = ui_components.get_player_input("Select > ").upper()
        
        if choice == "0":
            break
        elif choice.isdigit() and 1 <= int(choice) <= len(inventory):
            idx = int(choice) - 1
            item = inventory[idx]
            if not item["locked"] and run_state["static"] >= item["price"]:
                run_state["static"] -= item["price"]
                item["locked"] = True
                run_state["owned_manifolds"].append(item["name"])
                config.console.print(f"[green]Bought {item['name']}![/green]")
                ui_components.time.sleep(1)
            elif not item["locked"]:
                config.console.print("[red]Not enough Static![/red]")
                ui_components.time.sleep(1)
        elif choice == "H" and heals_left > 0 and run_state["static"] >= 100:
            run_state["static"] -= 100
            heals_left -= 1
            for u_name, (hp, max_hp) in run_state["hp_data"].items():
                run_state["hp_data"][u_name] = (min(max_hp, hp + int(max_hp * 0.30)), max_hp)
            config.console.print("[green]Party Healed![/green]")
            ui_components.time.sleep(1)
        elif choice == "R" and run_state["static"] >= refresh_cost:
            run_state["static"] -= refresh_cost
            refresh_cost = int(refresh_cost * random.uniform(1.20, 1.40))
            inventory = generate_static_shop_items(run_state["lattice"], run_state["owned_manifolds"])
            config.console.print("[yellow]Shop Refreshed![/yellow]")
            ui_components.time.sleep(1)

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

            if stage_id in [58001, 58002, 58003, 58004, 58005, 60001, 60002, 60003, 60004, 60005]:
                party = [p for p in party if p.name != "Akasuke"]

            if config.player_data.get("lattice_mode", False):
                enemies = config.player_data.get("current_enemies", [])
            else:
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
            
            # Safely inject Lattice data into the battle system to prevent crashes
            if config.player_data.get("lattice_mode", False):
                battle_manager.is_lattice_mode = True
                battle_manager.run_state = config.run_state
                battle_manager.lattice_node_type = config.player_data.get("lattice_node_type", "battles")
            else:
                battle_manager.is_lattice_mode = False

            battle_manager.start_battle(party, enemies, stage_id)
            
            if config.player_data.get("lattice_mode", False):
                config.player_data["lattice_mode"] = False # Safety reset
                continue # CRITICAL: We need this to skip all the campaign rewards below and loop!
            
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
                    parent_stage = stage_id // 1000
                    already_cleared_by_progression = config.player_data.get("latest_stage", -1) >= parent_stage
                    is_first_node_clear = (stage_id not in config.player_data.get("cleared_stages", [])) and not already_cleared_by_progression

                    # --- 1. NODE REWARDS MAP ---
                    # stage_id : ( {First Clear Drops}, [(Drop Chance, "Item Name", Qty)] )
                    NODE_REWARDS_MAP = {
                        5001: ({"Microchip": 2, "Microprocessor": 3}, [(0.25, "Cafeteria Melon Bread", 1)]),
                        5002: ({"Microchip": 2, "Microprocessor": 3}, [(0.25, "Cafeteria Melon Bread", 1)]),
                        5003: ({"Microchip": 2, "Microprocessor": 3}, [(0.25, "Cafeteria Melon Bread", 1)]),
                        
                        10001: ({"Microchip": 2, "Microprocessor": 2}, [(0.40, "Cafeteria Melon Bread", 1)]),
                        10002: ({"Microchip": 2, "Microprocessor": 2}, [(0.40, "Cafeteria Melon Bread", 1)]),
                        10003: ({"Microchip": 2, "Microprocessor": 2}, [(0.40, "Cafeteria Melon Bread", 1)]),
                        10004: ({"Microchip": 2, "Microprocessor": 2}, [(0.40, "Cafeteria Melon Bread", 1)]),
                        
                        14001: ({"Microchip": 2, "Microprocessor": 2}, [(0.65, "Cafeteria Melon Bread", 1), (0.25, "Vending Machine Coffee", 1)]),
                        14001: ({"Microchip": 2, "Microprocessor": 2}, [(0.65, "Cafeteria Melon Bread", 1), (0.25, "Vending Machine Coffee", 1)]),
                        
                        15001: ({"Microchip": 2, "Microprocessor": 3}, [(0.65, "Cafeteria Melon Bread", 1), (0.25, "Vending Machine Coffee", 1)]),
                        15002: ({"Microchip": 2, "Microprocessor": 3}, [(0.65, "Cafeteria Melon Bread", 1), (0.25, "Vending Machine Coffee", 1)]),
                        15003: ({"Microchip": 2, "Microprocessor": 3}, [(0.65, "Cafeteria Melon Bread", 1), (0.25, "Vending Machine Coffee", 1)]),
                        
                        16001: ({"Microchip": 2, "Microprocessor": 3}, [(0.50, "Vending Machine Coffee", 1)]),
                        16002: ({"Microchip": 2, "Microprocessor": 3}, [(0.50, "Vending Machine Coffee", 1)]),
                        16003: ({"Microchip": 2, "Microprocessor": 3}, [(0.50, "Vending Machine Coffee", 1)]),
                        16004: ({"Microchip": 2, "Microprocessor": 3}, [(0.50, "Vending Machine Coffee", 1)]),
                        16005: ({"Microchip": 2, "Microprocessor": 3}, [(0.50, "Vending Machine Coffee", 1)]),
                        
                        32001: ({"Microchip": 3}, [(0.25, "Sports Water Bottle", 1)]),
                        32002: ({"Microchip": 3}, [(0.25, "Sports Water Bottle", 1)]),
                        32003: ({"Microchip": 3}, [(0.25, "Sports Water Bottle", 1)]),
                        
                        34001: ({"Microchip": 2, "Microprocessor": 2}, [(0.50, "Sports Water Bottle", 1)]),
                        34002: ({"Microchip": 2, "Microprocessor": 2}, [(0.50, "Sports Water Bottle", 1)]),
                        34003: ({"Microchip": 2, "Microprocessor": 2}, [(0.50, "Sports Water Bottle", 1)]),
                        
                        41001: ({"Microchip": 3}, [(0.375, "Cafeteria Melon Bread", 1), (0.375, "Vending Machine Coffee", 1), (0.375, "Sports Water Bottle", 1)]),
                        41002: ({"Microchip": 3}, [(0.375, "Cafeteria Melon Bread", 1), (0.375, "Vending Machine Coffee", 1), (0.375, "Sports Water Bottle", 1)]),
                        41003: ({"Microchip": 3}, [(0.375, "Cafeteria Melon Bread", 1), (0.375, "Vending Machine Coffee", 1), (0.375, "Sports Water Bottle", 1)]),
                        41004: ({"Microchip": 3}, [(0.375, "Cafeteria Melon Bread", 1), (0.375, "Vending Machine Coffee", 1), (0.375, "Sports Water Bottle", 1)]),

                        56001: ({"Microchip": 3}, [(0.25, "Yunhai Herbal Powder", 1)]),
                        56002: ({"Microprocessor": 3}, [(0.25, "Yunhai Herbal Powder", 1)]),
                        56003: ({"Microchip": 3}, [(0.25, "Yunhai Herbal Powder", 1)]),
                        56004: ({"Microprocessor": 3}, [(0.25, "Yunhai Herbal Powder", 1)]),
                        56005: ({"Microchip": 3}, [(0.25, "Yunhai Herbal Powder", 1)]),

                        57001: ({"Microchip": 3}, [(0.25, "Yunhai Herbal Powder", 1)]),
                        57002: ({"Microprocessor": 3}, [(0.25, "Yunhai Herbal Powder", 1)]),
                        57003: ({"Microchip": 3}, [(0.25, "Yunhai Herbal Powder", 1)]),
                        57004: ({"Microprocessor": 3}, [(0.25, "Yunhai Herbal Powder", 1)]),
                        57005: ({"Microchip": 3}, [(0.25, "Yunhai Herbal Powder", 1)]),

                        58001: ({"Microchip": 3}, [(0.25, "Yunhai Herbal Powder", 1)]),
                        58002: ({"Microprocessor": 3}, [(0.25, "Yunhai Herbal Powder", 1)]),
                        58003: ({"Microchip": 3}, [(0.25, "Yunhai Herbal Powder", 1)]),
                        58004: ({"Microprocessor": 3}, [(0.25, "Yunhai Herbal Powder", 1)]),
                        58005: ({"Microchip": 3}, [(0.25, "Yunhai Herbal Powder", 1)]),

                        60001: ({"Microchip": 3}, [(0.50, "Yunhai Herbal Powder", 1)]),
                        60002: ({"Microchip": 3}, [(0.50, "Yunhai Herbal Powder", 1)]),
                        60003: ({"Microchip": 3}, [(0.50, "Yunhai Herbal Powder", 1)]),

                        68001: ({"Jade Microchip": 3}, [(0.50, "Yunhai Herbal Powder", 1)]),
                        68002: ({"Jade Microchip": 3}, [(0.50, "Yunhai Herbal Powder", 1)]),
                        68003: ({"Jade Microchip": 3}, [(0.50, "Yunhai Herbal Powder", 1)]),
                        68004: ({"Jade Microchip": 3}, [(0.50, "Yunhai Herbal Powder", 1)]),

                        69001: ({"Jade Microchip": 3}, [(0.50, "Yunhai Herbal Powder", 1)]),
                        69002: ({"Jade Microchip": 3}, [(0.50, "Yunhai Herbal Powder", 1)]),
                        69003: ({"Jade Microchip": 3}, [(0.50, "Yunhai Herbal Powder", 1)]),
                    }

                    # Apply Dynamic Rewards
                    if stage_id in NODE_REWARDS_MAP:
                        first_drops, repeat_drops = NODE_REWARDS_MAP[stage_id]
                        if is_first_node_clear:
                            for item, qty in first_drops.items():
                                rewards_text.append(f"{qty}x {item}")
                                mats[item] = mats.get(item, 0) + qty
                            # IMPORTANT: Immediately mark this specific node as cleared so it can't be farmed
                            config.player_data.setdefault("cleared_stages", []).append(stage_id)
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
                                16: (story_manager.play_stage_2_5_end, "[bold green]NEW FEATURE: PARALLAXIS SCORER (GACHA) UNLOCKED![/bold green]"),
                                38: (story_manager.play_stage_3_15_end, None),
                                41: (story_manager.play_stage_3_19_end, "[bold magenta]NEW MEMBER: Naganohara[/bold magenta]"),
                                56: (story_manager.play_stage_4_11_end, "[bold magenta]NEW MEMBERS: Natsume, Hana, Kagaku"),
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
                    group_chipproc_bread = [2, 4, 6, 7]
                    group_chipproc_coffee = [2, 4, 6, 7, 18, 19, 20, 21]
                    group_chipproc_bottle = [25, 26, 28, 29, 31, 33, 35, 36, 37, 38, 39, 40]
                    group_chipproc_herb = [49, 50, 51, 52, 53, 56, 57, 58, 60, 62, 63, 64, 65, 66]
                    group_jadechip_herb = [68, 69, 70, 71]
                    
                    # Dictionary routing for POST-battle stories (Standard Stages)
                    # stage_id : (Story Function, Optional Special Reward String)
                    STORY_ENDS = {
                        # --- ACT 1 ---
                        2: (story_manager.play_stage_1_2_end, None),
                        4: (story_manager.play_stage_1_4_end, "[bold magenta]NEW MEMBER: Benikawa[/bold magenta]"),
                        6: (story_manager.play_stage_1_6_end, None),
                        7: (story_manager.play_stage_1_7_end, None),
                        # --- ACT 2 ---
                        18: (story_manager.play_stage_2_7_end, None),
                        19: (story_manager.play_stage_2_8_end, None),
                        20: (story_manager.play_stage_2_9_end, None),
                        21: (story_manager.play_stage_2_10_end, None),
                        # --- ACT 3 ---
                        29: (story_manager.play_stage_3_7_end, None),
                        31: (story_manager.play_stage_3_9_end, None),
                        33: (story_manager.play_stage_3_11_end, None),
                        37: (story_manager.play_stage_3_15_end, None),
                        38: (story_manager.play_stage_3_16_end, None),
                        39: (story_manager.play_stage_3_17_end, None),
                        # --- ACT 4 ---
                        49: (story_manager.play_stage_4_4_end, None),   
                        50: (story_manager.play_stage_4_5_end, None),
                        51: (story_manager.play_stage_4_6_end, None),
                        52: (story_manager.play_stage_4_7_end, None),
                        53: (story_manager.play_stage_4_8_end, None),
                        56: (story_manager.play_stage_4_11_end, None),
                        57: (story_manager.play_stage_4_12_end, None),
                        58: (story_manager.play_stage_4_13_end, None),
                        60: (story_manager.play_stage_4_15_end, None),
                        62: (story_manager.play_stage_4_17_end, None),
                        63: (story_manager.play_stage_4_18_end, None),
                        66: (story_manager.play_stage_4_21_end, None),
                        70: (story_manager.play_stage_4_25_end, None),
                        71: (story_manager.play_stage_4_26_end, None)
                    }

                    if should_play_story:
                        if stage_id in STORY_ENDS:
                            end_func, extra_reward = STORY_ENDS[stage_id]
                            end_func()
                            if extra_reward:
                                rewards_text.append(extra_reward)
                            
                        # Apply First Clear Rewards Based on Groups
                        if stage_id in group_chipproc_bread:
                            rewards_text.extend([f"2x Microchip", f"2x Microprocessor"])
                            mats["Microchip"] = mats.get("Microchip", 0) + 2
                            mats["Microprocessor"] = mats.get("Microprocessor", 0) + 2
                        elif stage_id in group_chipproc_coffee:
                            rewards_text.extend(["2x Microchip", "2x Microprocessor"])
                            mats["Microchip"] = mats.get("Microchip", 0) + 2
                            mats["Microprocessor"] = mats.get("Microprocessor", 0) + 2
                        elif stage_id in group_chipproc_bottle:
                            rewards_text.extend(["2x Microchip", "2x Microprocessor"])
                            mats["Microchip"] = mats.get("Microchip", 0) + 2
                            mats["Microprocessor"] = mats.get("Microprocessor", 0) + 2
                        elif stage_id in group_chipproc_herb:
                            rewards_text.extend(["2x Microchip", "2x Microprocessor"])
                            mats["Microchip"] = mats.get("Microchip", 0) + 2
                            mats["Microprocessor"] = mats.get("Microprocessor", 0) + 2
                        elif stage_id in group_jadechip_herb:
                            rewards_text.extend(["3x Jade Microchip"])
                            mats["Jade Microchip"] = mats.get("Jade Microchip", 0) + 3

                        # Update Progress
                        if config.player_data["latest_stage"] < stage_id: 
                            config.player_data["latest_stage"] = stage_id
                        cl = config.player_data.get("cleared_stages", [])
                        if stage_id not in cl: cl.append(stage_id)
                        config.player_data["cleared_stages"] = cl

                    else:
                        # Apply Repeat Clear Rewards
                        if stage_id in group_chipproc_bread:
                            if random.random() < 0.25: rewards_text.append("1x Cafeteria Melon Bread"); mats["Cafeteria Melon Bread"] = mats.get("Cafeteria Melon Bread", 0) + 1
                        elif stage_id in group_chipproc_coffee:
                            if random.random() < 0.25: rewards_text.append("1x Vending Machine Coffee"); mats["Vending Machine Coffee"] = mats.get("Vending Machine Coffee", 0) + 1
                        elif stage_id in group_chipproc_bottle:
                            if random.random() < 0.25: rewards_text.append("1x Sports Water Bottle"); mats["Sports Water Bottle"] = mats.get("Sports Water Bottle", 0) + 1
                        elif stage_id in group_chipproc_herb:
                            if random.random() < 0.25: rewards_text.append("1x Yunhai Herbal Powder"); mats["Yunhai Herbal Powder"] = mats.get("Yunhai Herbal Powder", 0) + 1
                        elif stage_id in group_jadechip_herb:
                            if random.random() < 0.25: rewards_text.append("1x Yunhai Herbal Powder"); mats["Yunhai Herbal Powder"] = mats.get("Yunhai Herbal Powder", 0) + 1
                    
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
            console.print("[2] Lattice Triage")
            console.print("[3] Gacha (Parallaxis)")
            console.print("[4] Council Logs")
            console.print("[5] Party Management") 
            console.print("[6] Save & Quit")
            choice = get_player_input("Select Option: ")
            if choice == "1":
                config.current_state = config.STATE_STAGE_SELECT
            elif choice == "2":
                if config.player_data.get("latest_stage", 0) >= 73:
                    config.current_state = config.STATE_LATTICE_MENU
                else:
                    console.print("[bold red]Undiscovered: Clear Stage 4-28 to unlock Lattice Triage.[/bold red]")
                    time.sleep(1.0)
            elif choice == "3":
                # Check if Stage 2-5 (ID 16) is cleared
                if config.player_data.get("latest_stage", 0) >= 16:
                    gacha_system.run_gacha_menu()
                    config.player_data["materials"]["Microchip"] = player.currencies["microchips"]
                    config.player_data["materials"]["Microprocessor"] = player.currencies["microprocessors"]
                    config.player_data["materials"]["Jade Microchip"] = player.currencies["jade microchips"]
                else:
                    console.print("[bold red]Undiscovered: Clear Stage 2-5 to unlock the Parallaxis Scorer.[/bold red]")
                    time.sleep(1.0)
            elif choice == "4": 
                config.current_state = config.STATE_COUNCIL_LOGS
            elif choice == "5": 
                config.current_state = config.STATE_PARTY_MANAGEMENT
            elif choice == "6": 
                confirm_quit()
            
        elif config.current_state == config.STATE_STAGE_SELECT:
            # --- STAGE DEFINITION MAPS ---
            # req_idx : (Story_Function, [Reward String List], {Material Update Dict})
            STORY_STAGES = {
                # --- ACT 1 ---
                0:(story_manager.play_stage_1_1_story, ["1x Microchip", "1x Microprocessor"], {"Microchip": 1, "Microprocessor": 1}, None),
                2:(story_manager.play_stage_1_3_story, ["1x Microchip", "1x Microprocessor"], {"Microchip": 1, "Microprocessor": 1}, None),
                7:(story_manager.play_stage_1_8_story, ["1x Microchip", "1x Microprocessor"], {"Microchip": 1, "Microprocessor": 1}, None),
                8:(story_manager.play_stage_1_9_story, ["1x Microchip", "1x Microprocessor"], {"Microchip": 1, "Microprocessor": 1}, None),
                10:(story_manager.play_stage_1_11_story, ["5x Microchip"], {"Microchip": 5}, None),
                # --- ACT 2 ---
                11:(story_manager.play_stage_2_1_story, ["1x Microchip", "1x Microprocessor"], {"Microchip": 1, "Microprocessor": 1}, None),
                12:(story_manager.play_stage_2_2_story, ["1x Microchip", "1x Microprocessor"], {"Microchip": 1, "Microprocessor": 1}, None),
                16:(story_manager.play_stage_2_6_story, ["1x Microchip", "1x Microprocessor"], {"Microchip": 1, "Microprocessor": 1}, None),
                21:(story_manager.play_stage_2_11_story, ["5x Microchip"], {"Microchip": 5}),
                # --- ACT 3 ---
                22:(story_manager.play_stage_3_1_story, ["1x Microchip", "1x Microprocessor"], {"Microchip": 1, "Microprocessor": 1}, None),
                23:(story_manager.play_stage_3_2_story, ["1x Microchip", "1x Microprocessor"], {"Microchip": 1, "Microprocessor": 1}, None),
                26:(story_manager.play_stage_3_5_story, ["1x Microchip", "1x Microprocessor"], {"Microchip": 1, "Microprocessor": 1}, None),
                29:(story_manager.play_stage_3_8_story, ["1x Microchip", "1x Microprocessor"], {"Microchip": 1, "Microprocessor": 1}, None),
                39:(story_manager.play_stage_3_18_story, ["1x Microchip", "1x Microprocessor"], {"Microchip": 1, "Microprocessor": 1}, None),
                42:(story_manager.play_stage_3_21_story, ["1x Microchip", "1x Microprocessor"], {"Microchip": 1, "Microprocessor": 1}, None),
                43:(story_manager.play_stage_3_22_story, ["1x Microchip", "1x Microprocessor"], {"Microchip": 1, "Microprocessor": 1}, None),
                44:(story_manager.play_stage_3_23_story, ["5x Microchip"], {"Microchip": 5}),
                # --- ACT 4 ---
                45:(story_manager.play_stage_4_1_story, ["1x Microchip", "1x Microprocessor"], {"Microchip": 1, "Microprocessor": 1}, None),
                46:(story_manager.play_stage_4_2_story, ["1x Microchip", "1x Microprocessor"], {"Microchip": 1, "Microprocessor": 1}, None),
                47:(story_manager.play_stage_4_3_story, ["1x Microchip", "1x Microprocessor"], {"Microchip": 1, "Microprocessor": 1}, None),
                53:(story_manager.play_stage_4_9_story, ["1x Microchip", "1x Microprocessor"], {"Microchip": 1, "Microprocessor": 1}, None),
                54:(story_manager.play_stage_4_10_story, ["1x Microchip", "1x Microprocessor"], {"Microchip": 1, "Microprocessor": 1}, None),
                58:(story_manager.play_stage_4_14_story, ["1x Microchip", "1x Microprocessor"], {"Microchip": 1, "Microprocessor": 1}, None),
                60:(story_manager.play_stage_4_16_story, ["1x Microchip", "1x Microprocessor"], {"Microchip": 1, "Microprocessor": 1}, None),
                66:(story_manager.play_stage_4_22_story, ["1x Jade Microchip"], {"Jade Microchip": 1}, None),
                71:(story_manager.play_stage_4_27_story, ["1x Jade Microchip"], {"Jade Microchip": 1}, None),
                72:(story_manager.play_stage_4_28_story, ["5x Jade Microchip"], {"Jade Microchip": 5}, "[bold green]NEW GAMEMODE: LATTICE TRIAGE UNLOCKED![/bold green]"),
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
                            story_func, rew_text, mat_dict, extra_reward = STORY_STAGES[req_idx]
                            story_func()
                            console.print("[bold yellow]First Clear Rewards:[/bold yellow]")
                            if extra_reward:
                                rew_text.append(extra_reward)
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

        # LATTICE TRIAGE MAP MENU
        elif config.current_state == config.STATE_LATTICE_MENU:
            lattice_choice = ui_components.draw_lattice_main_menu(config.player_data.get("latest_stage", 0))
            
            if lattice_choice == "0":
                config.current_state = config.STATE_MAIN_MENU
            elif lattice_choice in ["1", "2"]:
                l_name = "Stable Lattice" if lattice_choice == "1" else "Steadfast Lattice"
                action = ui_components.draw_lattice_hub_menu(l_name, player)
                
                if action == "0":
                    continue
                elif action == "1":
                    # Start Run Setup
                    run_state = save_manager.load_lattice_run()
                    if not run_state:
                        # New Run Init
                        grid, pos, moves = generate_lattice_map(day=1)
                        run_state = {
                            "lattice": l_name,
                            "day": 1,
                            "static": 0,
                            "moves": moves,
                            "grid": grid,
                            "pos": pos,
                            "flux_color": "cyan" if lattice_choice == "1" else "sea_green1",
                            "hp_data": {u.name: (u.hp, u.max_hp) for u in player.party}
                        }
                        # CALL THE SHOP AFTER run_state IS CREATED
                        open_manuscript_shop(l_name, run_state)
                        # Save the fully initialized run (with manuscript buffs)
                        save_manager.save_lattice_run(run_state)
                        
                    config.run_state = run_state
                    config.current_state = config.STATE_LATTICE_TRIAGE

        # LATTICE TRIAGE MAP EXPLORATION
        elif config.current_state == config.STATE_LATTICE_TRIAGE:
            rs = config.run_state
            rs["pos"] = tuple(rs["pos"])
            ui_components.draw_lattice_map(
                rs["grid"], len(rs["grid"]), rs["pos"], 
                rs["day"], rs["flux_color"], rs["moves"], rs["static"]
            )
            
            move = ui_components.get_player_input("").upper()
            x, y = rs["pos"]
            nx, ny = x, y
            
            if move == "W": ny -= 1
            elif move == "S": ny += 1
            elif move == "A": nx -= 1
            elif move == "D": nx += 1
            elif move == "0": # Exit to Menu and Save
                save_manager.save_lattice_run(rs)
                config.current_state = config.STATE_MAIN_MENU
                continue
                
            # Bounds and Wall Check
            if 0 <= nx < len(rs["grid"]) and 0 <= ny < len(rs["grid"]) and rs["grid"][ny][nx] != '☒':
                target_node = rs["grid"][ny][nx]
                move_cost = 1 if target_node == '☑' else 2
                
                if rs["moves"] >= move_cost:
                    rs["moves"] -= move_cost
                    rs["pos"] = (nx, ny)
                    
                    if target_node == '⛞' or target_node == '𖣯': # Normal or Elite Battle
                        rs["grid"][ny][nx] = '☑' # Mark cleared
                        save_manager.save_lattice_run(rs)
                        
                        # 1. Distinguish between Elites and Normal Battles
                        is_elite = (target_node == '𖣯')
                        if is_elite:
                            possible_battles = [1000006, 1000009, 1000025, 1000034, 1000041, 1000049, 1000053, 1000063, 1000067, 1000070, 1000072, 1000083, 1000084, 1000090, 1000094]
                        else:
                            # Expand this list as needed from your Raw Content
                            possible_battles = [1000001, 1000002, 1000003, 1000004, 1000005, 1000007, 1000008, 1000010, 1000011, 1000012, 1000013, 1000014]
                        
                        chosen_battle_id = random.choice(possible_battles)
                        # Generate the enemies
                        enemy_party = stages.get_lattice_battle_group(chosen_battle_id, rs["day"])
                        
                        # Set up battle state
                        config.player_data["lattice_mode"] = True
                        config.player_data["lattice_node_type"] = "elites" if is_elite else "battles" # Track for XP Calc
                        config.player_data["current_enemies"] = enemy_party
                        config.current_state = config.STATE_BATTLE
                        
                    elif target_node == '▣': # Event
                        rs["grid"][ny][nx] = '☑'
                        if "cleared_stats" not in rs: rs["cleared_stats"] = {}
                        save_manager.save_lattice_run(rs)
                        # --- CHECK FOR DELAYED / QUEUED EVENTS ---
                        flags = rs.get("event_flags", {})
                        chosen_event_id = None
                        if rs["day"] == flags.get("jade_synthesis_day", -1): chosen_event_id = 13
                        elif rs["day"] == flags.get("fairy_auction_day", -1): chosen_event_id = 16
                        elif rs["day"] == flags.get("fairy_bidding_day", -1): chosen_event_id = 17
                        elif rs["day"] == flags.get("underworld_crucible_day", -1): chosen_event_id = 19
                        if not chosen_event_id:
                            # Normal random pool (Now testing up to Event 20)
                            valid_pool = [i for i in range(1, 21) if i not in [13, 16, 17, 19]]
                            chosen_event_id = random.choice(valid_pool)
                        survived = lattice_encounters.execute_lattice_event(chosen_event_id, rs, player)
                        if survived == False:
                            config.console.print("[bold red]The Vanguard has fallen to the anomalies of the Lattice...[/bold red]")
                            ui_components.time.sleep(2)
                            config.current_state = "LATTICE_CALCULATE_END"
                        elif survived == "BATTLE":
                            pass # Loops back into STATE_BATTLE
                        else:
                            rs["cleared_stats"]["events"] = rs["cleared_stats"].get("events", 0) + 1
                            save_manager.save_lattice_run(rs)
                else:
                    config.console.print("[yellow]Floor ending...[/yellow]")
                    ui_components.time.sleep(1)
                    # 1. Run the Shop
                    open_static_shop(rs)
                    # 2. Boss Battle (If Day >= 3)
                    if rs["day"] >= 3:
                        # Fetch boss based on Flux, run battle state logic here just like Elite/Normal
                        pass 
                    # 3. Post-Boss / End of Day Reward
                    ui_components.clear_screen()
                    ui_components.print_header("DAY COMPLETE - REWARD")
                    # (Generate 3 unowned manifolds here based on formula: Tier = (Day-1) + Chance)
                    # For brevity, let's assume `reward_choices` is generated.
                    reward_choices = ["Vending Machine Iced Tea (I)", "Hardcover Novel (II)", "Sandy Coat (II)"] 
                    config.console.print("Choose 1 Manifold:")
                    for i, r in enumerate(reward_choices):
                        config.console.print(f"[{i+1}] {r}")
                    while True:
                        sel = ui_components.get_player_input("Select > ")
                        if sel in ["1", "2", "3"]:
                            chosen_reward = reward_choices[int(sel)-1]
                            rs["owned_manifolds"].append(chosen_reward)
                            break
                    # 4. Progress to Next Day or End Gamemode
                    if rs["day"] >= 5:
                        config.current_state = "LATTICE_CALCULATE_END" # Win condition (Pass victory flag elsewhere)
                    else:
                        rs["day"] += 1
                        # Restore HP
                        for u_name, (hp, max_hp) in rs["hp_data"].items():
                            rs["hp_data"][u_name] = (max_hp, max_hp)
                        # Generate new map
                        rs["grid"], rs["pos"], rs["moves"] = generate_lattice_map(rs["day"])
                        save_manager.save_lattice_run(rs)
        
        elif config.current_state == "LATTICE_CALCULATE_END":
            terminate_lattice_run(config.run_state, is_victory=False)

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