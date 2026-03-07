import config
from entities import MATERIALS_DB
# Import the ID Maps from SCD
from scd import KATA_ID_MAP, KATA_NAME_TO_ID
import json
import os

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
            "equipped": {},
            "lattice": {}
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
            jm = player_obj.currencies.get("jade_microchips", 0)
            strip += f"mat01:{mc}!mat02:{mp}!mat03:{jm}!"

        mats = config.player_data.get("materials", {})
        for name, qty in mats.items():
            if name in MATERIALS_DB and name not in ["Microchip", "Microprocessor", "Jade Microchip"]:
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

        # 4. Get Equipped Loadouts
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
        
        # 5. Append Lattice Data
        if hasattr(player_obj, "lattice_xp"):
            strip += f"ltcX={player_obj.lattice_xp['Stable Lattice']},{player_obj.lattice_xp['Steadfast Lattice']}!"
            strip += f"ltcL={player_obj.lattice_levels['Stable Lattice']},{player_obj.lattice_levels['Steadfast Lattice']}!"
            strip += f"ltcM={player_obj.manuscripts_owned['Stable Lattice']},{player_obj.manuscripts_owned['Steadfast Lattice']}!"
            
            if player_obj.discovered_manifolds: strip += f"dMan={','.join(player_obj.discovered_manifolds)}!"
            if player_obj.discovered_events: strip += f"dEvt={','.join(map(str, player_obj.discovered_events))}!"
            if player_obj.discovered_endings: strip += f"dEnd={','.join(map(str, player_obj.discovered_endings))}!"
            if player_obj.discovered_fluxes: strip += f"dFlx={','.join(map(str, player_obj.discovered_fluxes))}!"

        return strip

    def load_save_strip(self, strip_string):
        """
        Parses the save string back into a Data Dictionary.
        """
        loaded_data = {
            "latest_stage": -1,
            "katas": [], 
            "materials": {},
            "equipped": {},
            "lattice": {
                "xp": {"Stable Lattice": 0, "Steadfast Lattice": 0},
                "levels": {"Stable Lattice": 1, "Steadfast Lattice": 1},
                "manuscripts": {"Stable Lattice": 0, "Steadfast Lattice": 0},
                "d_man": [], "d_evt": [], "d_end": [], "d_flx": []
            }
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

            # EQUIPPED LOADOUTS
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
            
            # LATTICE
            elif part.startswith("ltcX="):
                vals = part.replace("ltcX=", "").split(",")
                loaded_data["lattice"]["xp"] = {"Stable Lattice": int(vals[0]), "Steadfast Lattice": int(vals[1])}
            elif part.startswith("ltcL="):
                vals = part.replace("ltcL=", "").split(",")
                loaded_data["lattice"]["levels"] = {"Stable Lattice": int(vals[0]), "Steadfast Lattice": int(vals[1])}
            elif part.startswith("ltcM="):
                vals = part.replace("ltcM=", "").split(",")
                loaded_data["lattice"]["manuscripts"] = {"Stable Lattice": int(vals[0]), "Steadfast Lattice": int(vals[1])}
            elif part.startswith("dMan="): loaded_data["lattice"]["d_man"] = part.replace("dMan=", "").split(",")
            elif part.startswith("dEvt="): loaded_data["lattice"]["d_evt"] = [int(x) for x in part.replace("dEvt=", "").split(",")]
            elif part.startswith("dEnd="): loaded_data["lattice"]["d_end"] = [int(x) for x in part.replace("dEnd=", "").split(",")]
            elif part.startswith("dFlx="): loaded_data["lattice"]["d_flx"] = [int(x) for x in part.replace("dFlx=", "").split(",")]
                
        return loaded_data
    
    # Mid-Run Save Handlers (Dual-Save Architecture with the Lattice Triage gamemode)
    def save_lattice_run(self, run_state_dict):
        """Saves current mid-run status in JSON format."""
        try:
            with open("lattice_save.json", 'w', encoding='utf-8') as f:
                json.dump(run_state_dict, f)
        except Exception as e:
            print(f"Failed to save Lattice Run: {e}")
    def load_lattice_run(self):
        """Returns the run dict if it exists, otherwise None."""
        if os.path.exists("lattice_save.json"):
            try:
                with open("lattice_save.json", 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                return None
        return None
    def delete_lattice_run(self):
        """Cleans up the mid-run save after victory/defeat/abandonment."""
        if os.path.exists("lattice_save.json"):
            os.remove("lattice_save.json")

save_manager = SaveManager()