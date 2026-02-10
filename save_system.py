import config
from entities import MATERIALS_DB
import entities
# Import the ID Maps from SCD
from scd import KATA_ID_MAP, KATA_NAME_TO_ID

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
        }

    def generate_save_strip(self, player_obj):
        """
        Generates a save string using IDs.
        Format: !stg{X}!mat{ID}:{QTY}!kta{ID}={APTITUDE}!
        
        Args:
            player_obj: The actual PlayerState instance.
        """
        # 1. Get Stage (From Global Config)
        stg_val = config.player_data.get("latest_stage", -1)
        strip = f"!stg{stg_val}!"
        
        # 2. Get Materials (From Player Currencies & Global Materials)
        # Combine player.currencies (Microchips) with generic materials
        
        # A. Map specific currencies to Material IDs (if defined in entities)
        # Microchip (ID 01), Microprocessor (ID 02)
        if hasattr(player_obj, "currencies"):
            mc = player_obj.currencies.get("microchips", 0)
            mp = player_obj.currencies.get("microprocessors", 0)
            strip += f"mat01:{mc}!mat02:{mp}!"

        # B. Generic Materials from config (if any)
        mats = config.player_data.get("materials", {})
        for name, qty in mats.items():
            if name in MATERIALS_DB and name not in ["Microchip", "Microprocessor"]:
                mid = MATERIALS_DB[name].save_id
                strip += f"mat{mid}:{qty}!"
        
        # 3. Get Katas (From Player Inventory)
        # FIX: Access attribute directly, do not use .get() on the object
        katas = []
        if hasattr(player_obj, "inventory"):
            katas = player_obj.inventory.get("katas", [])
        
        for k_entry in katas:
            # Handle Dictionary Format (Standard)
            if isinstance(k_entry, dict):
                name = k_entry.get("name")
                apt = k_entry.get("aptitude", "I")
                
                if name in KATA_NAME_TO_ID:
                    kid = KATA_NAME_TO_ID[name]
                    strip += f"kta{kid}={apt}!"
            
            # Handle Legacy String Format
            elif isinstance(k_entry, str):
                 if k_entry in KATA_NAME_TO_ID:
                    kid = KATA_NAME_TO_ID[k_entry]
                    strip += f"kta{kid}=I!"

        # 4. Get Equipped Loadouts
        # Iterate through player units and match them to the UNIT_ORDER_MAP
        if hasattr(player_obj, "units"):
                    for unit in player_obj.units:
                        if unit.name in UNIT_ORDER_MAP:
                            u_id = UNIT_ORDER_MAP.index(unit.name) + 1
                            
                            # Check for Kata and the new source_key field
                            if unit.kata and hasattr(unit.kata, 'source_key') and unit.kata.source_key:
                                
                                # Use the Unique SCD Key to find the ID
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
                        loaded_data["katas"].append({
                            "name": name,
                            "aptitude": apt
                        })
                except: pass

            # Load Loadouts
            elif part.startswith("u"):
                try:
                    # u1=kta5
                    if "=" in part:
                        u_part, k_part = part.split("=")
                        u_idx = int(u_part.replace("u", ""))
                        k_id = int(k_part.replace("kta", ""))
                        loaded_data["katas"][u_idx] = k_id
                except: pass
                
        return loaded_data

save_manager = SaveManager()