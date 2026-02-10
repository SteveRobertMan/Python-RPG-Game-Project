import os
import config
from entities import Entity
import scd 
from save_system import save_manager

SAVE_FILE = "savegame.txt"

class PlayerState:
    def __init__(self):
        self.currencies = {
            "microchips": 0, 
            "microprocessors": 0 
        }
        self.inventory = {
            "katas": [] 
        }
        self.units = [] 
        self.unlocked_units = [] 
        self.party = [] 

    def add_unit(self, unit_name):
        # Prevent duplicates
        if unit_name not in [u.name for u in self.units]:
            new_unit = Entity(unit_name, is_player=True)
            self.units.append(new_unit)
            self.unlocked_units.append(unit_name)
            if len(self.party) < 4:
                self.party.append(new_unit)

    def save_game(self):
        if "materials" not in config.player_data:
            config.player_data["materials"] = {}
        save_string = save_manager.generate_save_strip(self)
        try:
            with open(SAVE_FILE, 'w', encoding='utf-8') as f:
                f.write(save_string)
            config.console.print("[green]Game Saved Successfully.[/green]")
        except Exception as e:
            print(f"Save Failed: {e}")

    def load_game(self):
        """
        Reads the Save Strip and populates the player object.
        """
        if os.path.exists(SAVE_FILE):
            try:
                with open(SAVE_FILE, 'r', encoding='utf-8') as f:
                    save_string = f.read().strip()
                
                loaded_data = save_manager.load_save_strip(save_string)
                
                if loaded_data:
                    config.player_data["latest_stage"] = loaded_data["latest_stage"]
                    
                    mats = loaded_data.get("materials", {})
                    self.currencies["microchips"] = mats.get("Microchip", 0)
                    self.currencies["microprocessors"] = mats.get("Microprocessor", 0)
                    
                    self.inventory["katas"] = loaded_data["katas"]
                    
                    # --- LOADOUT APPLICATION ---
                    loadouts = loaded_data.get("loadouts", {})
                    
                    for u_name, k_key in loadouts.items():
                        # 1. Ensure Unit Exists (Load save -> Unit must be unlocked)
                        self.add_unit(u_name)
                        
                        # 2. Find the Unit Object
                        unit = next((u for u in self.units if u.name == u_name), None)
                        
                        if unit:
                            # 3. Retrieve Kata Data from SCD
                            k_data = scd.get_kata_data_by_name(k_key)
                            
                            if k_data:
                                # 4. Equip using Entity method
                                unit.equip_kata(k_data["kata_obj"])
                                
                                # 5. Restore Stats (Max HP comes from Kata Data)
                                unit.max_hp = k_data["max_hp"]
                                unit.hp = unit.max_hp
                                
                                # 6. Restore Aptitude (Check Inventory for matches)
                                # We scan inventory for the same Kata Key Name
                                for inv_item in self.inventory["katas"]:
                                    if inv_item["name"] == k_key:
                                        unit.kata.rift_aptitude = inv_item.get("aptitude", "I")
                                        break
                                        
                    print("Save Loaded.")
                    return True
            except Exception as e:
                print(f"Load Failed: {e}")
        return False

# Initialize
player = PlayerState()