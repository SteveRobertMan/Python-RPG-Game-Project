import random
import time
from rich.panel import Panel
from rich import box

# Fixed Imports
import config
from ui_components import clear_screen, get_player_input
from player_state import player 

# Local Console Reference
console = config.console

# Constants
RARITY_1 = 1 
RARITY_2 = 2 
RARITY_3 = 3 
RARITY_4 = 4 

class GachaSystem:
    def __init__(self):
        self.pool = {
            RARITY_4: [
                "Heiwa Seiritsu’s Upperclassman | ‘Chain Reaper Of Heiwa’ Shigemura",
                "Kasakura High School Disciplinary Committee President Yuri",
                "Kiryoku Gakuen Student Council Fairy | ‘Forest Guardian’ Benikawa",
                "Riposte Gang Squad Leader Naganohara",
                "Riposte Gang Executive Hanefuji Akasuke",
                "Benikawa Ninja Clan – Ayame Benikawa",
                "Black Water Dock Master Natsume",
                "Yunhai Association Enforcer Captain Inami Yuri"
            ],
            RARITY_3: [
                "Heiwa Seiritsu’s Upperclassman | ‘Crusher’ Benikawa",
                "Kasakura High School Disciplinary Committee Vice President Shigemura",
                "Kiryoku Gakuen Student Council Fairy | ‘Lake Strider’ Hana",
                "Heiwa Seiritsu Student – Goodwill Infiltrator Shigemura",
                "Black Water Dock Gang Squad Leader Shigemura"
            ],
            RARITY_2: [
                "‘Iron Fist Of Heiwa’ Delinquent Leader Akasuke",
                "Kasakura High School Disciplinary Committee Member Benikawa",
                "Kiryoku Gakuen Self-Defense Club President Yuri",
                "Kiryoku Gakuen Student Council ‘Lesser Fairy’ Yuri",
                "Kasakura High School Disciplinary Committee Member Kagaku",
                "Yunhai Association Enforcer Akasuke",
                "Yunhai Association Enforcer Naganohara",
                "Luoxia Gardening School Student Kagaku",
                "Luoxia Gardening School Student Hana"
            ],
            RARITY_1: [
                "Kasakura High School Student Akasuke",
                "Kasakura High School Student Yuri",
                "Kasakura High School Student Benikawa",
                "Kasakura High School Student Shigemura",
                "Kasakura High School Student Naganohara",
                "Kasakura High School Student Natsume",
                "Kasakura High School Student Hana",
                "Kasakura High School Student Kagaku",
                "Heiwa Seiritsu High School Student Yuri",
                "Heiwa Seiritsu High School Student Naganohara"
            ]
        }
        
        # Standard Rates
        self.rates = {
            RARITY_4: 0.03,  # 3%
            RARITY_3: 0.12,  # 12%
            RARITY_2: 0.35,  # 35%
            RARITY_1: 0.50   # 50%
        }

    def get_pity_counters(self, banner_name):
        """Ensures pity dictionary exists and returns the specific banner's counters."""
        if not hasattr(player, "pity"):
            player.pity = {}
            
        if banner_name not in player.pity:
            player.pity[banner_name] = {"pity_3": 0, "pity_4": 0}
            
        return player.pity[banner_name]

    def display_new_unit_fanfare(self, unit_name):
        """Displays a flashy banner for 4-star pulls."""
        text = f"\n\n[bold center blink]★ NEW KATA OBTAINED ★[/bold center blink]\n\n[bold yellow center size=24]{unit_name}[/bold yellow center size=24]\n\n[italic center]Legendary Kata Acquired[/italic center]\n"
        
        console.print(Panel(
            text,
            style="gold1 on grey11",
            box=box.DOUBLE,
            padding=(2, 4),
            title="[bold red]!!! LEGENDARY SIGNAL !!![/bold red]",
            subtitle="[bold red]PARALLAXIS SYSTEM[/bold red]"
        ))
        time.sleep(1.5)

    def execute_pull_sequence(self, banner_name, currency_type_str, count):
        """Main logic for rolling the gacha."""
        currency_key = currency_type_str.lower() + "s"
        cost = 1 * count
        current_funds = player.currencies.get(currency_key, 0)
        
        if current_funds < cost:
            console.print(f"[red]Not enough {currency_type_str}! Need {cost}, have {current_funds}.[/red]")
            return

        # Deduct Cost
        player.currencies[currency_key] = current_funds - cost
        
        console.print(f"\n[bold white]Initiating {count}x Extraction...[/bold white]\n")
        time.sleep(0.5)

        first_new_4star = None

        for i in range(count):
            counters = self.get_pity_counters(banner_name)
            counters["pity_3"] += 1
            counters["pity_4"] += 1
            
            # Determine Rarity
            result_rarity = self.calculate_rarity(counters)
            
            # Reset Pity
            if result_rarity == RARITY_4:
                counters["pity_4"] = 0
            elif result_rarity == RARITY_3:
                counters["pity_3"] = 0
                
            # Pick Item
            item_name = random.choice(self.pool[result_rarity])
            is_new = self.check_if_new(item_name)
            
            # Track for Fanfare
            if result_rarity == RARITY_4 and is_new:
                if first_new_4star is None:
                    first_new_4star = item_name

            # Add to Inventory
            self.handle_item_acquisition(item_name, result_rarity, is_new)
            
            if count > 1:
                time.sleep(0.1)

        # Save State Immediately
        player.save_game()
        
        # Show Fanfare if applicable
        if first_new_4star:
            time.sleep(0.5)
            clear_screen()
            self.display_new_unit_fanfare(first_new_4star)

    def check_if_new(self, item_name):
        """
        Checks if the item exists in the player's inventory.
        Handles both Dictionary format (New) and String format (Legacy).
        """
        if "katas" not in player.inventory:
            player.inventory["katas"] = []
            return True
            
        for k in player.inventory["katas"]:
            # Robust check: Handles both Dicts and Strings
            if isinstance(k, dict) and k.get("name") == item_name:
                return False
            elif isinstance(k, str) and k == item_name:
                return False
        return True

    def handle_item_acquisition(self, item_name, rarity, is_new):
        """Adds item to inventory (as Dict) or refunds materials for duplicates."""
        rarity_colors = {4: "bold yellow", 3: "bold magenta", 2: "blue", 1: "white"}
        r_style = rarity_colors.get(rarity, "white")
        
        tier_symbols = "㊋" * rarity
        
        if is_new:
            # SAVE LOGIC: Append as Dictionary to preserve Aptitude
            new_kata_entry = {
                "name": item_name, 
                "aptitude": "I"
            }
            player.inventory["katas"].append(new_kata_entry)
            
            console.print(f"[{r_style}]>> SCORED: {item_name} {tier_symbols}[/{r_style}] [bold yellow]NEW![/bold yellow]")
        else:
            # DUPLICATE LOGIC: Refund Materials
            rewards = {
                RARITY_4: ("Microchip", 10), 
                RARITY_3: ("Microchip", 1),  
                RARITY_2: ("Microprocessor", 1),
                RARITY_1: (None, 0)
            }
            
            mat_name, qty = rewards[rarity]
            refund_str = ""
            if mat_name:
                key = mat_name.lower() + "s"
                player.currencies[key] += qty
                refund_str = f"-> [dim]Dupe! Converted to {qty} {mat_name}s[/dim]"
            
            console.print(f"[{r_style}]>> SCORED: {item_name} {tier_symbols}[/{r_style}] {refund_str}")

    def calculate_rarity(self, counters):
        # Hard Pity
        if counters["pity_4"] >= 67: return RARITY_4
        if counters["pity_3"] >= 35: return RARITY_3
        
        # RNG Roll
        roll = random.random()
        cumulative = 0.0
        
        cumulative += self.rates[RARITY_4]
        if roll < cumulative: return RARITY_4
        
        cumulative += self.rates[RARITY_3]
        if roll < cumulative: return RARITY_3
        
        cumulative += self.rates[RARITY_2]
        if roll < cumulative: return RARITY_2
        
        return RARITY_1

    def run_gacha_menu(self):
        """Main Loop for the Gacha UI."""
        while True:
            clear_screen()
            console.print(Panel("[bold magenta]PARALLAXIS SCORING[/bold magenta]", subtitle="G.C.H. System"))
            
            m_chips = player.currencies.get("microchips", 0)
            m_procs = player.currencies.get("microprocessors", 0)
            console.print(f"Funds: [cyan]{m_chips} Microchips[/cyan] | [green]{m_procs} Microprocessors[/green]")
            
            console.print("\nSelect Banner:")
            console.print(f"[sea_green1][1] RATE UP: Act 4: Steadfastness [勇往直前] || 『NeverTurnBack』 (Uses Microchips)[sea_green1]")
            console.print("[2] Shamiko Labs (Uses Microprocessors)")
            console.print("[3] View Pity Counters")
            console.print("[0] Back to Menu")
            
            choice = get_player_input()
            
            if choice == "0":
                break
            elif choice == "1":
                self.prompt_pull_options("RATE UP: Act 4: Steadfastness [勇往直前] || 『NeverTurnBack』", "Microchip")
            elif choice == "2":
                self.prompt_pull_options("Shamiko Labs", "Microprocessor")
            elif choice == "3":
                p = getattr(player, "pity", {})
                console.print(p)
                get_player_input("Press Enter...")

    def prompt_pull_options(self, banner_name, currency_name):
        console.print(f"\n[bold]{banner_name}[/bold]")
        
        console.print(f"[white][1] Pull 1x (Cost: 1 {currency_name})[/white]")
        console.print(f"[blue][2] Pull 10x (Cost: 10 {currency_name}s)[/blue]")
        
        console.print("[white][0] Cancel[/white]")
        
        sub_choice = get_player_input("Amount > ")
        
        if sub_choice == "1":
            self.execute_pull_sequence(banner_name, currency_name, 1)
            get_player_input("Press Enter...")
        elif sub_choice == "2":
            self.execute_pull_sequence(banner_name, currency_name, 10)
            get_player_input("Press Enter...")

gacha_system = GachaSystem()