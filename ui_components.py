from rich.panel import Panel
from rich.align import Align
from rich.text import Text
from rich.table import Table
from rich.layout import Layout
import config 
import time
import rich
import scd
from entities import ELEMENT_NAMES, Kata, get_element_color, get_tier_roman, MATERIALS_DB
import stages

def clear_screen():
    config.console.clear()

def print_header(text):
    config.console.print(Panel(Align.center(text, vertical="middle"), style="bold white on blue"))

def draw_title_screen():
    clear_screen()
    title_text = Text(config.GAME_TITLE, style="bold magenta", justify="center")
    title_text.stylize("blink", 0, len(config.GAME_TITLE))
    
    content = """
    [bold]Faction Slop / Timeline Merchant Story[/bold]
    
    Select an Option:
    
    [1] Start Game
    [2] Load Save
    [3] Quit Game
    """
    panel = Panel(
        Align.center(content, vertical="middle"),
        title=config.GAME_TITLE,
        subtitle="Python RPG Project",
        style="cyan",
        height=20 
    )
    config.console.print(panel)

def get_player_input(prompt_text=">> "):
    return config.console.input(f"[bold yellow]{prompt_text}[/bold yellow]")

def draw_stage_select_menu(unlocked_stage):
    # Initialize page: Default to 1, but if Act 1 is cleared (stage > 10), start on Page 2
    current_page = 1
    if unlocked_stage >= 11:
        current_page = 2

    while True:
        clear_screen()
        print_header("STAGE SELECT")

        if current_page == 1:
            # --- ACT 1: OVERTHROWN ---
            table = Table(title="Act 1: Overthrown", expand=True)
            table.add_column("Stage", justify="center")
            table.add_column("Title", justify="left")
            table.add_column("Status", justify="center")

            # Helper lambda for status text
            get_status = lambda req, current: "[green]CLEAR[/green]" if current > req else "[yellow]OPEN[/yellow]"

            # List of (Stage ID, Title, Unlock Index Requirement)
            act1_stages = [
                ("1-1", "Voluntold", 0),
                ("1-2", "Class-Skipper", 1),
                ("1-3", "Chromatic Divergence Phenomenon", 2),
                ("1-4", "Kidnapping Case", 3),
                ("1-5", "Weekday Errands", 4),
                ("1-6", "Sparring Match", 5),
                ("1-7", "A Job", 6),
                ("1-8", "Interrogation", 7),
                ("1-9", "Meeting", 8),
                ("1-10", "Raid", 9),
                ("1-11", "Overthrown", 10),
            ]

            for s_id, s_title, req_idx in act1_stages:
                if unlocked_stage >= req_idx:
                    status = get_status(req_idx, unlocked_stage)
                    table.add_row(s_id, s_title, status)
                else:
                    table.add_row(s_id, "???", "[dim]LOCKED[/dim]")
            
            config.console.print(table)
            config.console.print("\n[N] Next Page (Act 2) | [0] Return")

        elif current_page == 2:
            # --- ACT 2: RETAKE UNDER PROGRESS ---
            # Using Gold/Orange style for Act 2
            table = Table(title="Act 2: Retake Under Progress", expand=True, style="bold gold1", border_style="gold1")
            table.add_column("Stage", justify="center", style="cyan")
            table.add_column("Title", justify="left", style="white")
            table.add_column("Status", justify="center")

            get_status = lambda req, current: "[green]CLEAR[/green]" if current > req else "[yellow]OPEN[/yellow]"

            # Act 2 Stages (Indices 11 to 21)
            act2_stages = [
                ("2-1", "Pyrrhic Victory", 11),
                ("2-2", "Immediate Return", 12),
                ("2-3", "Stalemate At The Gates", 13),
                ("2-4", "Breakthrough Plan", 14),
                ("2-5", "Labyrinth Of Motives", 15),
                ("2-6", "Upperclassman", 16),
                ("2-7", "Kokoro’s Echo", 17),
                ("2-8", "Heart's Burden", 18),
                ("2-9", "Chains Of Fury", 19),
                ("2-10", "Iron & Fists", 20),
                ("2-11", "Parallaxis Scorer", 21),
            ]

            for s_id, s_title, req_idx in act2_stages:
                if unlocked_stage >= req_idx:
                    status = get_status(req_idx, unlocked_stage)
                    table.add_row(s_id, s_title, status)
                else:
                    # Logic: If Act 1 isn't fully cleared, Act 2 shouldn't be visible? 
                    # Assuming we show locked slots if on the page.
                    table.add_row(s_id, "???", "[dim]LOCKED[/dim]")

            config.console.print(table)
            config.console.print("\n[P] Previous Page (Act 1) | [0] Return")

        # --- INPUT HANDLING ---
        choice = get_player_input("Enter Stage ID (e.g. \"1-1\") or Option > ").lower()

        if choice == "0":
            return "0"
        
        elif choice == "n" and current_page == 1:
            current_page = 2
            continue
        
        elif choice == "p" and current_page == 2:
            current_page = 1
            continue

        # Check for valid stage ID pattern (e.g. "1-1", "2-10")
        if "-" in choice:
            # Validation Logic: Is this stage unlocked?
            try:
                act, sub = map(int, choice.split("-"))
                
                # Calculate required unlock index based on ID
                # Formula map: 1-1=0 ... 1-11=10 | 2-1=11 ... 2-11=21
                required_idx = -1
                if act == 1:
                    required_idx = sub - 1
                elif act == 2:
                    required_idx = 10 + sub 
                
                if required_idx != -1:
                    if unlocked_stage >= required_idx:
                        return choice.upper() # Return valid ID to main loop

            except ValueError:
                config.console.print("[bold red]Invalid Format.[/bold red]")

def draw_node_select_menu(stage_name, cleared_indices):
    clear_screen()
    print_header(f"{stage_name}: NODE SELECT")
    
    config.console.print("[italic]You must clear all nodes to complete this stage.[/italic]")
    config.console.print("[italic]Party HP is only partially restored between battles.[/italic]\n")

    # --- DEBUG: FORCE INT CONVERSION ---
    # This ensures that even if data loaded as strings ("0"), we treat them as ints (0)
    # safe_cleared is a Set of integers for perfect matching
    safe_cleared = {int(x) for x in cleared_indices}
    
    # UNCOMMENT THE LINE BELOW IF YOU NEED TO SEE WHAT THE GAME SEES:
    # config.console.print(f"[dim red]Debug - Cleared Indices: {safe_cleared}[/dim red]")

    nodes = []

    # Stage 1-5: Weekday Errands
    if stage_name == "1-5: Weekday Errands":
        nodes = [
            ("Node 1", "Class-Skipping Freshman(s)"),
            ("Node 2", "Kidnapper Hooligan(s)"),
            ("Node 3", "Kidnapper Hooligan Leader (Mixed Group)")
        ]
    
    # Stage 1-10: Raid
    elif stage_name == "1-10: Raid":
        nodes = [
            ("Node 1", "Slender Heiwa Seiritsu Delinquent(s)"),
            ("Node 2", "Bulky Heiwa Seiritsu Delinquent(s)"),
            ("Node 3", "Slender Heiwa Seiritsu Delinquent(s) (Mixed Group)"),
            ("Node 4", "Bulky Heiwa Seiritsu Delinquent(s) (Mixed Group)")
        ]
    
    # Stage 2-3: Stalemate At The Gates
    elif stage_name == "2-3: Stalemate At The Gates":
        nodes = [
            ("Node 1", "Slender Heiwa Seiritsu Delinquent(s) (Mixed Group)"),
            ("Node 2", "Bulky Heiwa Seiritsu Delinquent(s) (Mixed Group)"),
        ]

    # Stage 2-4: Breakthrough Plan
    elif stage_name == "2-4: Breakthrough Plan":
        nodes = [
            ("Node 1", "Spike Bat Heiwa Seiritsu Delinquent(s)"),
            ("Node 2", "Chain Fist Heiwa Seiritsu Delinquent(s)"),
            ("Node 3", "Spike Bat Heiwa Seiritsu Delinquent (Mixed Group)"),
        ]

    # Stage 2-5: Labyrinth Of Motives
    elif stage_name == "2-5: Labyrinth Of Motives":
        nodes = [
            ("Node 1", "Slender Heiwa Seiritsu Delinquent(s) (Mixed Group)"),
            ("Node 2", "Bulky Heiwa Seiritsu Delinquent(s) (Mixed Group)"),
            ("Node 3", "Spike Bat Heiwa Seiritsu Delinquent(s) (Mixed Group)"),
            ("Node 4", "Chain Fist Heiwa Seiritsu Delinquent(s) (Mixed Group)"),
            ("Node 5", "Slender Heiwa Seiritsu Delinquent(s) (Mixed Group)"),
        ]
    
    # Render the selected list
    for i, (name, desc) in enumerate(nodes):
        desc_text = f"[white]{desc}[/white]"
        desc_text = f"[not bold]{desc_text}[/not bold]"
        
        # Check against the safe integer set
        if i in safe_cleared:
            status = "[green]CLEARED[/green]"
        else:
            status = "[yellow]AVAILABLE[/yellow]"
            
        config.console.print(f"[{i+1}] {name} - {desc_text} ({status})")
        
    config.console.print("\n[0] Back (Warning: Giving up resets node progress!)")

def draw_council_logs_menu():
    clear_screen()
    print_header("STUDENT COUNCIL LOGS")
    
    content = """
    Select Database:
    
    [1] Enemies (Bestiary)
    [2] Materials
    [3] Status Effects (Coming Soon)
    [0] Return
    """
    config.console.print(Panel(Align.center(content), style="white on black"))

def draw_material_logs():
    clear_screen()
    config.console.print(Panel("[bold]MATERIAL LOGS[/bold]", style="white on blue"))
    
    player_mats = config.player_data.get("materials", {})
    
    for mat in MATERIALS_DB.values():
        count = player_mats.get(mat.name, 0)
        c_style = "green" if count > 0 else "dim red"
        config.console.print(f"[bold cyan]{mat.name}[/bold cyan] (Owned: [{c_style}]{count}[/{c_style}])")
        config.console.print(f"[italic]{mat.description}[/italic]")
        config.console.print("-" * 30)
        
    get_player_input("Press Enter to return...")

def draw_bestiary_menu():
    full_database = stages.get_enemy_database()
    latest_stage = config.player_data.get("latest_stage", -1)
    
    visible_enemies = [e for e in full_database if latest_stage >= getattr(e, 'unlock_stage_id', 999)]
    
    while True:
        clear_screen()
        config.console.print(Panel("[bold]ENEMY BESTIARY[/bold]", style="red on black"))
        
        if not visible_enemies:
            config.console.print("[dim italic]No enemy data available yet. Clear more stages to unlock.[/dim italic]")
        else:
            config.console.print("Select an enemy to view details:\n")
            for idx, enemy in enumerate(visible_enemies):
                config.console.print(f"[{idx+1}] {enemy.name}")
            
        config.console.print("[0] Return")
        
        choice = get_player_input("Select > ")
        if choice == "0":
            break
            
        if choice.isdigit():
            idx = int(choice) - 1
            if 0 <= idx < len(visible_enemies):
                draw_bestiary_details(visible_enemies[idx])

def draw_bestiary_details(unit):
    clear_screen()
    
    res_table = Table(title="Elemental Weaknesses", box=None)
    res_table.add_column("Element"); res_table.add_column("Mult")
    
    for i, name in enumerate(ELEMENT_NAMES):
        color = get_element_color(i)
        val = unit.resistances[i]
        style = "green" if val < 1.0 else ("red" if val > 1.0 else "white")
        res_table.add_row(f"[{color}]{name}[/{color}]", f"[{style}]{val}x[/{style}]")

    pool_text = ""
    if unit.kata and hasattr(unit.kata, 'skill_pool_def'):
        # Sort by Tier
        sorted_pool = sorted(unit.kata.skill_pool_def, key=lambda x: x[0].tier)
        for skill, count in sorted_pool:
            c = get_element_color(skill.element)
            t_r = get_tier_roman(skill.tier)
            desc = skill.description if skill.description else ""
            dmg_str = f"[bold]Dmg: {skill.base_damage}[/bold]"
            pool_text += f"x{count} [{c}]{skill.name}[/{c}] ({t_r}) {dmg_str} [light_green]{desc}[/light_green]\n"
    else:
        pool_text = "No Kata / Skill info available."

    desc_text = getattr(unit, 'description', 'No description available.')

    content = f"""
[bold]{unit.name}[/bold]
HP: {unit.max_hp}
Rift Aptitude: {unit.kata.rift_aptitude if unit.kata else "?"}

[bold italic]{desc_text}[/bold italic]

[bold]Skill Pool:[/bold]
{pool_text}
    """
    
    layout = Layout()
    layout.split_row(Layout(Panel(content, title="Details")), Layout(Panel(res_table)))
    config.console.print(layout)
    
    get_player_input("Press Enter to return...")

# --- PARTY MANAGEMENT & INVENTORY UI --

def draw_party_management_menu(player_obj):
    while True:
        clear_screen()
        print_header("PARTY MANAGEMENT")

        if not player_obj.units:
            config.console.print("[dim]No characters unlocked yet.[/dim]")
            get_player_input("Press Enter to return...")
            return

        # List Characters
        table = Table(title="Select Character", expand=True, box=rich.box.SIMPLE)
        table.add_column("#", justify="center", style="cyan", width=4)
        table.add_column("Name", style="bold white")
        table.add_column("Current Kata", style="yellow")
        table.add_column("HP", justify="right")

        for idx, unit in enumerate(player_obj.units):
            kata_name = unit.kata.name if unit.kata else "None"
            table.add_row(str(idx + 1), unit.name, kata_name, f"{unit.hp}/{unit.max_hp}")

        config.console.print(table)
        config.console.print("\n[0] Return to Main Menu")

        choice = get_player_input("Select Unit # > ")
        if choice == "0": break
        
        if choice.isdigit():
            idx = int(choice) - 1
            if 0 <= idx < len(player_obj.units):
                manage_unit_loadout(player_obj.units[idx], player_obj)

def manage_unit_loadout(unit, player_obj):
    """
    Displays the specific character's stats, deck, and equipment slot.
    """
    while True:
        clear_screen()
        config.console.print(Panel(f"[bold]{unit.name}[/bold]", style="blue on white"))

        # 1. Stats Display
        res_text = ""
        for i, val in enumerate(unit.resistances):
            color = get_element_color(i)
            # logic: Green if resistant (<1.0), Red if weak (>1.0), White if neutral
            style = "green" if val < 1.0 else ("red" if val > 1.0 else "white")
            res_text += f"[{color}]{ELEMENT_NAMES[i][:3]}[/{color}]: [{style}]{val}x[/{style}]  "
        
        # 2. Kata Info
        k_name = unit.kata.name if unit.kata else "None"
        # RARITY LOGIC: Repeat symbol N times
        k_rare = ("㊋" * unit.kata.rarity) if unit.kata else "-"
        k_apt = unit.kata.rift_aptitude if unit.kata else "-"

        info_panel = Panel(
            f"Equipped Kata: [bold yellow]{k_name}[/bold yellow]\n"
            f"Rarity: {k_rare}\n"
            f"Rift Aptitude: [gold1]{k_apt}[/gold1]\n"
            f"Max HP: {unit.max_hp}\n\n"
            f"[italic]{unit.kata.description}[/italic]\n\n"
            f"Resistances:\n{res_text}",
            title="Current Loadout"
        )
        config.console.print(info_panel)

        # 3. Detailed Deck Display
        deck_text = ""
        if unit.kata and hasattr(unit.kata, 'skill_pool_def'):
            # Sort by Tier (Low -> High)
            sorted_pool = sorted(unit.kata.skill_pool_def, key=lambda x: x[0].tier)
            
            for skill, count in sorted_pool:
                # Formatting Data
                c = get_element_color(skill.element)
                # Roman Numeral conversion
                tiers = ["", "I", "II", "III", "IV", "V"]
                t_r = tiers[skill.tier] if 0 < skill.tier <= 5 else str(skill.tier)
                
                # Header Line
                header = f"x{count} [{c}]{skill.name}[/{c}] ({t_r}) [bold]Dmg: {skill.base_damage}[/bold]"
                
                # Condition: Only add description line if description exists
                if skill.description:
                    deck_text += f"{header}\n    [light_green]{skill.description}[/light_green]\n"
                else:
                    # No description: Just the header, then move to next line
                    deck_text += f"{header}\n"
        else:
            deck_text = "[dim]No Kata or Skills available.[/dim]"

        # Print the detailed deck in a panel
        config.console.print(Panel(deck_text, title="Deck Preview", style="white", expand=True))

        # 4. Input Loop
        config.console.print("\n[E] Equip from Inventory")
        config.console.print("[0] Back")

        choice = get_player_input("> ").upper()
        if choice == "0": break
        elif choice == "E": open_equip_menu(unit, player_obj)

def open_equip_menu(unit, player_obj):
    while True:
        clear_screen()
        # Header Helper
        config.console.print(Panel(f"[bold]EQUIP KATA: {unit.name}[/bold]", style="blue on white"))

        # 1. Filter Inventory
        available_options = []
        
        # Iterating through the list of dictionaries from Gacha
        for inv_entry in player_obj.inventory.get("katas", []):
            
            # EXTRACT THE NAME FROM THE DICT
            # Structure is: {"name": "Gacha String", "aptitude": "I"}
            unique_name = inv_entry.get("name")
            
            # Pass the unique identifier to SCD
            data = scd.get_kata_data_by_name(unique_name)
            
            if data:
                k_obj = data["kata_obj"]
                
                # CHECK COMPATIBILITY
                # k_obj.owner_name was set in SCD based on the unique_name
                if k_obj.owner_name == unit.name or k_obj.owner_name == "Any":
                    # Store tuple: (Unique ID, Data Dict, Aptitude from Inventory)
                    available_options.append( (unique_name, data, inv_entry.get("aptitude", "I")) )

        if not available_options:
            config.console.print("[red]No compatible Katas found in inventory.[/red]")
            get_player_input("Press Enter...")
            return

        # 2. Display Options
        table = Table(title=f"Available Katas for {unit.name}", box=rich.box.SIMPLE)
        table.add_column("#", style="cyan", width=4)
        table.add_column("Kata Name", style="bold white")
        table.add_column("Rarity", justify="center")
        table.add_column("HP", justify="right")
        
        for i, (u_name, data, aptitude) in enumerate(available_options):
            k_obj = data["kata_obj"]
            rarity_str = "㊋" * k_obj.rarity
            table.add_row(str(i+1), k_obj.name, rarity_str, str(data['max_hp']))

        config.console.print(table)
        config.console.print("\n[0] Cancel")
        
        choice = get_player_input("Select Kata > ")
        
        if choice == "0": break

        # --- HANDLE DEFAULT EQUIP ---
        elif choice == "D":
            # Construct the default key based on stages.py conventions
            # Convention: "Name (Default)"
            default_key = f"{unit.name} (Default)"
            
            # Retrieve Default Data from SCD
            default_data = scd.get_kata_data_by_name(default_key)
            
            if default_data:
                # Apply Default Logic
                unit.equip_kata(default_data["kata_obj"])
                unit.max_hp = default_data["max_hp"]
                unit.hp = unit.max_hp # Full heal
                
                # We can optionally reset description to default, though unit object might have persistent bio
                if "description" in default_data:
                    unit.description = default_data["description"]

                config.console.print(f"\n[green]Reverted to Default: {default_data['kata_obj'].name}![/green]")
                time.sleep(1)
                return
            else:
                config.console.print(f"\n[red]Error: Default data for {unit.name} not found in SCD.[/red]")
                time.sleep(1.5)
        
        if choice.isdigit():
            idx = int(choice) - 1
            if 0 <= idx < len(available_options):
                selected_uname, selected_data, selected_apt = available_options[idx]
                
                # --- APPLY THE EQUIPMENT ---
                
                # 1. Update Unit's internal Kata Object
                unit.equip_kata(selected_data["kata_obj"])
                
                # 2. Inject the Aptitude (Stored in Inventory, not SCD)
                if unit.kata:
                    unit.kata.rift_aptitude = selected_apt
                
                # 3. Update Unit Stats
                unit.max_hp = selected_data["max_hp"]
                unit.hp = unit.max_hp # Full heal on switch
                
                config.console.print(f"\n[green]Successfully equipped {selected_data['kata_obj'].name}![/green]")
                time.sleep(1)
                return