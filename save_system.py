import config
from entities import MATERIALS_DB
# Import the ID Maps from SCD
from scd import KATA_ID_MAP, KATA_NAME_TO_ID

# Fixed Unit Order for Save/Load indexing
UNIT_ORDER_MAP = [
    "Akasuke", 
    "Yuri", 
    "Benikawa", 
    "Shigemura", 
    "Naganohara", 
    "Natsume", 
    "Hana", 
    "Kagaku"
]

class SaveManager:
    def __init__(self):
        # The structure used when a save is loaded
        self.data = {
            "latest_stage": -1,  
            "katas": [],   
            "materials": {},
            "equipped": {} # [NEW] Stores {Unit_Index: Kata_ID}
        }

    def generate_save_strip(self, player_obj):
        """
        Generates a save string using IDs.
        Format: !stg{X}!mat{ID}:{QTY}!kta{ID}={APTITUDE}!u{UID}=kta{KID}!
        """
        # 1. Get Stage
        stg_val = config.player_data.get("latest_stage", -1)
        strip = f"!stg{stg_val}!"
        
        # 2. Get Materials
        if hasattr(player_obj, "currencies"):
            mc = player_obj.currencies.get("microchips", 0)
            mp = player_obj.currencies.get("microprocessors", 0)
            strip += f"mat01:{mc}!mat02:{mp}!"

        mats = config.player_data.get("materials", {})
        for name, qty in mats.items():
            if name in MATERIALS_DB and name not in ["Microchip", "Microprocessor"]:
                mid = MATERIALS_DB[name].save_id
                strip += f"mat{mid}:{qty}!"
        
        # 3. Get Katas (Inventory)
        katas = []
        if hasattr(player_obj, "inventory"):
            katas = player_obj.inventory.get("katas", [])
        
        for k_entry in katas:
            if isinstance(k_entry, dict):
                name = k_entry.get("name")
                apt = k_entry.get("aptitude", "I")
                if name in KATA_NAME_TO_ID:
                    kid = KATA_NAME_TO_ID[name]
                    strip += f"kta{kid}={apt}!"
            elif isinstance(k_entry, str):
                 if k_entry in KATA_NAME_TO_ID:
                    kid = KATA_NAME_TO_ID[k_entry]
                    strip += f"kta{kid}=I!"

        # 4. [NEW] Get Equipped Loadouts
        if hasattr(player_obj, "units"):
            for unit in player_obj.units:
                # Use the Source Key (set in SCD) to identify the specific Kata version
                # Checks if unit is in our supported list and has a kata with a source key
                if unit.name in UNIT_ORDER_MAP and unit.kata and hasattr(unit.kata, 'source_key'):
                    
                    # 1. Calculate Unit ID (1-based index based on MAP)
                    u_id = UNIT_ORDER_MAP.index(unit.name) + 1
                    
                    # 2. Get Kata ID from Source Key
                    if unit.kata.source_key in KATA_NAME_TO_ID:
                        k_id = KATA_NAME_TO_ID[unit.kata.source_key]
                        strip += f"u{u_id}=kta{k_id}!"

        return strip

    def load_save_strip(self, strip_string):
        """
        Parses the save string back into a Data Dictionary.
        """
        loaded_data = {
            "latest_stage": -1,
            "katas": [], 
            "materials": {},
            "equipped": {} # [NEW]
        }
        
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

            # KATAS (Inventory)
            elif part.startswith("kta"):
                try:
                    content = part.replace("kta", "", 1)
                    kid_str = content
                    apt = "I"
                    if "=" in content:
                        kid_str, apt = content.split("=", 1)
                    kid = int(kid_str)
                    
                    if kid in KATA_ID_MAP:
                        name = KATA_ID_MAP[kid]
                        loaded_data["katas"].append({
                            "name": name,
                            "aptitude": apt
                        })
                except: pass

            # [NEW] EQUIPPED LOADOUTS
            elif part.startswith("u"):
                try:
                    # Format: u1=kta5
                    if "=" in part:
                        u_part, k_part = part.split("=")
                        
                        # Extract IDs
                        u_idx = int(u_part.replace("u", ""))
                        k_id = int(k_part.replace("kta", ""))
                        
                        # Store in separate 'equipped' dict
                        loaded_data["equipped"][u_idx] = k_id
                except: pass
                
        return loaded_data

save_manager = SaveManager()