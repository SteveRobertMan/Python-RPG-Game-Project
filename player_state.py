import os
import config
from entities import Entity
# Import the save manager
from save_system import save_manager

# We change this to .txt because we are saving a "Strip" string
SAVE_FILE = "savegame.txt"

class PlayerState:
    def __init__(self):
        self.currencies = {
            "microchips": 0, 
            "microprocessors": 0 
        }
        
        # This is where the game lives while running
        self.inventory = {
            "katas": [] 
        }

        self.units = [] 
        self.unlocked_units = [] 
        self.party = [] 

    def add_unit(self, unit_name):
        if unit_name not in [u.name for u in self.units]:
            new_unit = Entity(unit_name, is_player=True)
            self.units.append(new_unit)
            self.unlocked_units.append(unit_name)
            if len(self.party) < 4:
                self.party.append(new_unit)

    def save_game(self):
        """
        Generates the Save Strip and writes it to the file.
        """
        # 1. Update global config data if needed
        if "materials" not in config.player_data:
            config.player_data["materials"] = {}
            
        # 2. Generate the String using self (the Player Object)
        save_string = save_manager.generate_save_strip(self)
        
        # 3. Write String to File
        try:
            with open(SAVE_FILE, 'w', encoding='utf-8') as f:
                f.write(save_string)
            print("Game Saved Successfully.")
        except Exception as e:
            print(f"Save Failed: {e}")

    def load_game(self):
        """
        Reads the Save Strip and populates the player object.
        """
        if os.path.exists(SAVE_FILE):
            try:
                # 1. Read String
                with open(SAVE_FILE, 'r', encoding='utf-8') as f:
                    save_string = f.read().strip()
                
                # 2. Parse String into Data Dict
                loaded_data = save_manager.load_save_strip(save_string)
                
                if loaded_data:
                    # 3. Apply Stage
                    config.player_data["latest_stage"] = loaded_data["latest_stage"]
                    
                    # 4. Apply Currencies (Extract from loaded materials)
                    # We map the loaded materials back to currencies
                    mats = loaded_data.get("materials", {})
                    self.currencies["microchips"] = mats.get("Microchip", 0)
                    self.currencies["microprocessors"] = mats.get("Microprocessor", 0)
                    
                    # 5. Apply Inventory (The Fix!)
                    self.inventory["katas"] = loaded_data["katas"]
                    
                    print("Save Loaded.")
                    return True
            except Exception as e:
                print(f"Load Failed: {e}")
        return False

# Initialize
player = PlayerState()