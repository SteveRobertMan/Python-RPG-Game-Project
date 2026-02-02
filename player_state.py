import os
from entities import Entity
# Import the save manager
from save_system import save_manager
import config

# We change this to .txt because we are saving a "Strip" string, not a JSON object
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

    # ... [add_unit method remains the same] ...

    def save_game(self):
        """
        Generates the Save Strip and writes it to the file.
        """
        # 1. Update global config data with local currency/unit data if needed
        # (Assuming config.player_data shares references, but let's be safe)
        if "materials" not in config.player_data:
            config.player_data["materials"] = {}
            
        # 2. Generate the String !stgX!ktaY!...
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
                    # 3. Apply to Config (Global State)
                    config.player_data["latest_stage"] = loaded_data["latest_stage"]
                    config.player_data["materials"] = loaded_data["materials"]
                    
                    # 4. Apply to Player (Inventory State)
                    # CRITICAL: This restores the "Owned Katas" list
                    self.inventory["katas"] = loaded_data["katas"]
                    
                    print("Save Loaded.")
                    return True
            except Exception as e:
                print(f"Load Failed: {e}")
        return False

# Create the instance
player = PlayerState()