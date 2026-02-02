import config
from entities import MATERIALS_DB
# Import the ID Maps from SCD
from scd import KATA_ID_MAP, KATA_NAME_TO_ID

class SaveManager:
    def __init__(self):
        # The structure used when a save is loaded
        self.data = {
            "latest_stage": -1,  
            "katas": [],   
            "materials": {},     
        }

    def generate_save_strip(self, player_obj):
        """
        Generates a save string using IDs.
        Format: !stg{X}!mat{ID}:{QTY}!kta{ID}={APTITUDE}!
        
        Arguments:
            player_obj: The PlayerState instance (containing the .inventory attribute)
        """
        # 1. Get Stage (From Global Config Dictionary)
        # We use config.player_data because that is where the main game loop updates stage progress
        stg_val = config.player_data.get("latest_stage", -1)
        strip = f"!stg{stg_val}!"
        
        # 2. Get Materials (From Global Config Dictionary)
        mats = config.player_data.get("materials", {})
        for name, qty in mats.items():
            if name in MATERIALS_DB:
                mid = MATERIALS_DB[name].save_id
                strip += f"mat{mid}:{qty}!"
        
        # 3. Get Katas (From Player Object Inventory)
        # player_obj is the Class Instance, so we access .inventory directly
        if hasattr(player_obj, "inventory"):
            katas = player_obj.inventory.get("katas", [])
        else:
            katas = []
        
        for k_entry in katas:
            # Check for Dictionary format (Standard New Format)
            if isinstance(k_entry, dict):
                name = k_entry.get("name")
                apt = k_entry.get("aptitude", "I")
                
                # Convert Name -> ID
                if name in KATA_NAME_TO_ID:
                    kid = KATA_NAME_TO_ID[name]
                    strip += f"kta{kid}={apt}!"
                else:
                    print(f"Warning: Cannot save unknown Kata '{name}'")
            
            # Check for String format (Legacy/Fallback)
            elif isinstance(k_entry, str):
                 if k_entry in KATA_NAME_TO_ID:
                    kid = KATA_NAME_TO_ID[k_entry]
                    strip += f"kta{kid}=I!"

        return strip

    def load_save_strip(self, strip_string):
        """
        Parses the save string back into a Data Dictionary.
        Output: {'katas': [{'name': '...', 'aptitude': '...'}], ...}
        """
        loaded_data = {
            "latest_stage": -1,
            "katas": [], 
            "materials": {}
        }
        
        # Map Material IDs back to Names
        id_to_name_mat = {m.save_id: name for name, m in MATERIALS_DB.items()}

        segments = strip_string.split("!")
        
        for part in segments:
            if not part: continue
            
            # STAGE
            if part.startswith("stg"):
                try: loaded_data["latest_stage"] = int(part.replace("stg", ""))
                except: pass

            # MATERIALS
            elif part.startswith("mat"):
                try:
                    content = part.replace("mat", "")
                    mid, qty = content.split(":")
                    if mid in id_to_name_mat:
                        loaded_data["materials"][id_to_name_mat[mid]] = int(qty)
                except: pass

            # KATAS (Convert ID -> Dictionary)
            elif part.startswith("kta"):
                try:
                    # Format: kta10=I
                    content = part.replace("kta", "", 1)
                    
                    kid_str = content
                    apt = "I"
                    
                    if "=" in content:
                        kid_str, apt = content.split("=", 1)
                    
                    kid = int(kid_str)
                    
                    # Convert ID -> Name
                    if kid in KATA_ID_MAP:
                        name = KATA_ID_MAP[kid]
                        
                        # Reconstruct the Dictionary
                        # This matches exactly what Gacha System creates
                        loaded_data["katas"].append({
                            "name": name,
                            "aptitude": apt
                        })
                except: pass
                
        return loaded_data

save_manager = SaveManager()