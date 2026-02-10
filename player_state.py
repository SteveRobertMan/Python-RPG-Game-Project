import os
import config
from entities import Entity
import scd # Needed to fetch Kata data by ID
# Import the save manager (and the Unit Map to resolve IDs)
from save_system import save_manager, UNIT_ORDER_MAP 

SAVE_FILE = "savegame.txt"

class PlayerState:
    # ... (Previous __init__ and add_unit remain unchanged) ...
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
        if unit_name not in [u.name for u in self.units]:
            new_unit = Entity(unit_name, is_player=True)
            self.units.append(new_unit)
            self.unlocked_units.append(unit_name)
            if len(self.party) < 4:
                self.party.append(new_unit)

    def save_game(self):
        # ... (Existing save_game logic remains the same) ...
        if "materials" not in config.player_data:
            config.player_data["materials"] = {}
        save_string = save_manager.generate_save_strip(self)
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
                    
                    # 4. Apply Currencies
                    mats = loaded_data.get("materials", {})
                    self.currencies["microchips"] = mats.get("Microchip", 0)
                    self.currencies["microprocessors"] = mats.get("Microprocessor", 0)
                    
                    # 5. Apply Inventory
                    self.inventory["katas"] = loaded_data["katas"]
                    
                    # 6. [NEW] Apply Equipped Loadouts
                    loadouts = loaded_data.get("loadouts", {})
                    
                    for unit in self.units:
                        # Find this unit's ID in the map
                        if unit.name in UNIT_ORDER_MAP:
                            u_id = UNIT_ORDER_MAP.index(unit.name) + 1
                            
                            # Check if we have a saved loadout for this ID
                            if u_id in loadouts:
                                k_id = loadouts[u_id]
                                
                                # Resolve ID -> Name -> Data
                                if k_id in scd.KATA_ID_MAP:
                                    k_name = scd.KATA_ID_MAP[k_id]
                                    k_data = scd.get_kata_data_by_name(k_name)
                                    
                                    if k_data:
                                        # Equip the base Kata
                                        unit.equip_kata(k_data["kata_obj"])
                                        unit.max_hp = k_data["max_hp"]
                                        unit.hp = unit.max_hp
                                        
                                        # [CRITICAL] Restore Rift Aptitude from Inventory
                                        # We look for the Kata in inventory to find its saved aptitude
                                        for inv_k in self.inventory["katas"]:
                                            if inv_k["name"] == k_name:
                                                unit.kata.rift_aptitude = inv_k.get("aptitude", "I")
                                                break

                    print("Save Loaded.")
                    return True
            except Exception as e:
                print(f"Load Failed: {e}")
        return False

# Initialize
player = PlayerState()