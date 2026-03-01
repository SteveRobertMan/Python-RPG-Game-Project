import copy
from entities import Entity, Kata, Skill, StatusEffect
from entities import EL_EROS, EL_PHILIA, EL_STORGE, EL_AGAPE, EL_LUDUS, EL_PRAGMA, EL_PHILAUTIA
import config
import scd
from player_state import player
from scd import bleed_1, bleed_2, bleed_3, bleed_8, bind_1, rupture_1, rupture_2, rupture_3, rupture_6, rupturecount_2, bleedcount_2, bind_4, pierce_fragility_1, paralysis_2, blossom_1, malice_1
from entities import Chip, ChipSkill, Passive

# --- PARTY MEMBER CREATION ---

def create_akasuke(equipped_kata_data=None):
    unit = Entity("Akasuke", is_player=True)

    # 1. Resolve Loadout
    if not equipped_kata_data:
        equipped_kata_data = scd.get_kata_data_by_name("Kasakura High School Student Akasuke")

    # 2. Apply Stats & Kata
    if equipped_kata_data:
        custom_kata = equipped_kata_data["kata_obj"]
        
        # Default HP fallback is 72 (from original code)
        unit.max_hp = equipped_kata_data.get("max_hp", 72)
        unit.hp = unit.max_hp
        
        unit.description = equipped_kata_data.get("description", "Akasuke Hanefuji is a student of Kasakura High School, one of the most renowned educational institutes of the east. He wears a red coat with a white shirt underneath, black trousers, black tie and an eye patch over one of his red eyes, he has a strong sense of duty and protection for his peers. Akasuke’s hobbies include cooking and training as a karateka at his school’s club dojo, where he is also the club captain.")
        unit.equip_kata(custom_kata)
        
    return unit

def create_yuri(equipped_kata_data=None):
    unit = Entity("Yuri", is_player=True)

    if not equipped_kata_data:
        equipped_kata_data = scd.get_kata_data_by_name("Kasakura High School Student Yuri")

    if equipped_kata_data:
        custom_kata = equipped_kata_data["kata_obj"]
        
        # Default HP fallback is 63
        unit.max_hp = equipped_kata_data.get("max_hp", 63)
        unit.hp = unit.max_hp
        
        unit.description = equipped_kata_data.get("description", "Inami Yuri is a student of Kasakura High School, one of the most renowned educational institutes of the east. She has silver hair tied into a ponytail, wears a white windbreaker jacket over a black tracksuit, and has clear sapphire blue eyes that are always beaming with confidence. Yuri’s hobbies include running and training as a judoka at her school’s club dojo, where she is also the club captain.")
        unit.equip_kata(custom_kata)
        
    return unit

def create_benikawa(equipped_kata_data=None):
    unit = Entity("Benikawa", is_player=True)

    if not equipped_kata_data:
        equipped_kata_data = scd.get_kata_data_by_name("Kasakura High School Student Benikawa")

    if equipped_kata_data:
        custom_kata = equipped_kata_data["kata_obj"]
        
        # Default HP fallback is 70
        unit.max_hp = equipped_kata_data.get("max_hp", 70)
        unit.hp = unit.max_hp
        
        unit.description = equipped_kata_data.get("description", "Benikawa Ayame is a student of Kasakura High School, known among her peers as a cheerful and highly talented member of the karate club. She wears a standard white karate dougi with a black belt tied firmly at the waist, caramel-colored hair pulled into a high ponytail, and bright purple eyes that sparkle with playful energy. Benikawa’s hobbies include practicing karate at the school dojo, where she often seeks out strong opponents for sparring, and exploring the city’s food stalls.")
        unit.equip_kata(custom_kata)
        
    return unit

def create_shigemura(equipped_kata_data=None):
    unit = Entity("Shigemura", is_player=True)

    if not equipped_kata_data:
        equipped_kata_data = scd.get_kata_data_by_name("Kasakura High School Student Shigemura")

    if equipped_kata_data:
        custom_kata = equipped_kata_data["kata_obj"]
        
        # Default HP fallback is 81
        unit.max_hp = equipped_kata_data.get("max_hp", 81)
        unit.hp = unit.max_hp
        
        unit.description = equipped_kata_data.get("description", "Fuyuyama Shigemura is a student of Kasakura High School, one of the most renowned educational institutes of the east. He has short, neatly trimmed purple hair that falls slightly over his sharp violet eyes, giving him a perpetually calm and detached appearance. Shigemura possesses a sharp mind and keen observational skills, often noticing details others miss, and carries himself with an air of quiet confidence that rarely breaks into overt emotion.")
        unit.equip_kata(custom_kata)
        
    return unit

def create_naganohara(equipped_kata_data=None):
    unit = Entity("Naganohara", is_player=True)

    if not equipped_kata_data:
        equipped_kata_data = scd.get_kata_data_by_name("Kasakura High School Student Naganohara")

    if equipped_kata_data:
        custom_kata = equipped_kata_data["kata_obj"]

        unit.max_hp = equipped_kata_data.get("max_hp", 58)
        unit.hp = unit.max_hp

        unit.description = equipped_kata_data.get("description", "Naganohara Tsukimiyama is a student of Kasakura High School, one of the most renowned educational institutes of the east. She has bright pink twintails that bounce energetically with every movement and large, sparkling golden eyes full of life and mischief. Naganohara’s hobbies include dragging her friends into fun (and sometimes chaotic) group activities, collecting cute accessories, and being the loudest cheerleader in any situation. Despite her bubbly exterior, she is fiercely loyal and surprisingly perceptive when it comes to her friends’ feelings.")
        unit.equip_kata(custom_kata)
        
    return unit

def create_natsume(equipped_kata_data=None):
    unit = Entity("Natsume", is_player=True)

    if not equipped_kata_data:
        equipped_kata_data = scd.get_kata_data_by_name("Kasakura High School Student Natsume")

    if equipped_kata_data:
        custom_kata = equipped_kata_data["kata_obj"]

        unit.max_hp = equipped_kata_data.get("max_hp", 58)
        unit.hp = unit.max_hp

        unit.description = equipped_kata_data.get("description", "Yokubukai Natsume is a student of Kasakura High School, one of the most renowned educational institutes of the east. She has messy dark hair, perpetually tired eyes from staring at glowing monitors, and prefers to wear oversized hoodies or cozy pajamas wrapped in blankets rather than her school uniform. Natsume’s hobbies include gathering intelligence, operating as the school's brilliant 'Queen of Information' from behind a screen, and avoiding any form of outdoor physical activity at all costs.")
        unit.equip_kata(custom_kata)
        
    return unit

def create_hana(equipped_kata_data=None):
    unit = Entity("Hana", is_player=True)

    if not equipped_kata_data:
        equipped_kata_data = scd.get_kata_data_by_name("Kasakura High School Student Hana")

    if equipped_kata_data:
        custom_kata = equipped_kata_data["kata_obj"]

        unit.max_hp = equipped_kata_data.get("max_hp", 77)
        unit.hp = unit.max_hp

        unit.description = equipped_kata_data.get("description", "Hana Kaoru is a student of Kasakura High School, one of the most renowned educational institutes of the east. She has soft, flowing hair and gentle, highly observant eyes that radiate warmth, compassion, and an unwavering calmness. Hana’s hobbies include practicing self-defense and aikido at the school dojo—where her elegant, momentum-shifting throws earn high praise from her juniors—and offering empathetic, grounded support to her peers without ever losing her composure.")
        unit.equip_kata(custom_kata)
        
    return unit

def create_kagaku(equipped_kata_data=None):
    unit = Entity("Kagaku", is_player=True)

    if not equipped_kata_data:
        equipped_kata_data = scd.get_kata_data_by_name("Kasakura High School Student Kagaku")

    if equipped_kata_data:
        custom_kata = equipped_kata_data["kata_obj"]

        unit.max_hp = equipped_kata_data.get("max_hp", 60)
        unit.hp = unit.max_hp

        unit.description = equipped_kata_data.get("description", "Kagaku Shamiko is a student of Kasakura High School, one of the most renowned educational institutes of the east. She wears a slightly wrinkled white lab coat over her standard uniform, has unkempt hair from pulling frequent all-nighters, and sharp eyes that are constantly analyzing the mechanics of the world around her. Kagaku’s hobbies include drinking excessive amounts of coffee, inventing groundbreaking technology like the Parallaxis Scorer, and passionately theorizing about the scientific mysteries of the multiverse.")
        unit.equip_kata(custom_kata)
        
    return unit

def get_player_party():
    """
    Creates the battle party based on the unlocked roster.
    CRITICAL FIX: Checks player_state to apply equipped Katas 
    instead of generating fresh default units every time.
    """
    party = []
    
    # Define the core roster order
    # (You can adjust this list based on who is unlocked in your save data)
    # For now, we assume Akasuke and Yuri are the base party.
    roster_names = ["Akasuke", "Yuri"]
    
    for name in roster_names:
        # 1. Find the Persistent Unit from the Party Menu (player_state)
        # This unit holds the 'Kata' object we equipped in the UI
        persistent_unit = next((u for u in player.units if u.name == name), None)
        
        loadout_data = None
        
        if persistent_unit and persistent_unit.kata:
            # 2. Reconstruct the SCD Key
            # The Kata Object stored in the unit has a .name (e.g. "Kasakura High School Student")
            # But SCD expects the Unique Key (e.g. "Kasakura High School Student (Akasuke)")
            
            k_name = persistent_unit.kata.name
            k_owner = persistent_unit.kata.owner_name
            
            search_key = k_name
            
            # --- HANDLE GENERIC NAME CONFLICTS ---
            # If the Kata name is generic, append the owner name to match SCD keys
            if k_name == "Kasakura High School Student":
                search_key = f"{k_name} ({k_owner})"
            elif k_name == "Heiwa Seiritsu High School Student":
                search_key = f"{k_name} ({k_owner})"
            
            # 3. Retrieve the full data dictionary from SCD
            loadout_data = scd.get_kata_data_by_name(search_key)
        
        # 4. Create the Fresh Battle Instance with the Correct Loadout
        if name == "Akasuke":
            # If loadout_data is None, create_akasuke defaults to base automatically
            party.append(create_akasuke(loadout_data))
            
        elif name == "Yuri":
            party.append(create_yuri(loadout_data))
            
    return party

# --- ENEMY LOADING ---
def load_stage_enemies(stage_id):
    enemies = []
    
    # Cache the enemy database into a dictionary keyed by the enemy's name for easy lookup
    db_enemies = {e.name: e for e in get_enemy_database()}
    
    def spawn(base_name, label=""):
        """
        Deepcopies an enemy from the template database and attaches an identifying label.
        Deepcopying is essential so status effects, hp, and skill instances aren't 
        shared globally among identically named enemies.
        """
        if base_name not in db_enemies:
            return None
        new_enemy = copy.deepcopy(db_enemies[base_name])
        if label:
            new_enemy.name = f"{new_enemy.name} {label}"
        new_enemy.hp = new_enemy.max_hp
        return new_enemy

    if stage_id == 0: 
        enemies.append(spawn("Underwear Thief"))

    elif stage_id == 2:
        for label in ["A", "B", "C"]:
            enemies.append(spawn("Class-Skipping Freshman", label))
            
    elif stage_id == 4: 
        for label in ["A", "B", "C", "D", "E"]:
            enemies.append(spawn("Kidnapper Hooligan", label))
        enemies.append(spawn("Kidnapper Hooligan Leader"))

    elif stage_id == 5001:
        for label in ["A", "B", "C"]:
            enemies.append(spawn("Class-Skipping Freshman", label))

    elif stage_id == 5002:
        for label in ["A", "B", "C", "D"]:
            enemies.append(spawn("Kidnapper Hooligan", label))

    elif stage_id == 5003:
        for label in ["A", "B"]:
            enemies.append(spawn("Class-Skipping Freshman", label))
        for label in ["A", "B"]:
            enemies.append(spawn("Kidnapper Hooligan", label))
        enemies.append(spawn("Kidnapper Hooligan Leader"))

    elif stage_id == 6:
        enemies.append(spawn("Ayame Benikawa (Sparring)"))

    elif stage_id == 7:
        enemies.append(spawn("Ayame Benikawa (Ninja)"))
        for label in ["A", "B"]:
            enemies.append(spawn("Benikawa Body Double", label))

    # --- ACT 1 DELINQUENT NODES ---
    elif stage_id == 10001:
        for label in ["A", "B", "C"]:
            enemies.append(spawn("Slender Heiwa Seiritsu Delinquent", label))

    elif stage_id == 10002:
        for label in ["A", "B", "C"]:
            enemies.append(spawn("Bulky Heiwa Seiritsu Delinquent", label))

    elif stage_id == 10003:
        for label in ["A", "B"]:
            enemies.append(spawn("Slender Heiwa Seiritsu Delinquent", label))
        enemies.append(spawn("Bulky Heiwa Seiritsu Delinquent"))

    elif stage_id == 10004:
        for label in ["A", "B"]:
            enemies.append(spawn("Bulky Heiwa Seiritsu Delinquent", label))
        enemies.append(spawn("Slender Heiwa Seiritsu Delinquent"))

    # --- ACT 2 ENEMY LOGIC ---
    elif stage_id == 14001:
        enemies.append(spawn("Slender Heiwa Seiritsu Delinquent", "A"))
        enemies.append(spawn("Slender Heiwa Seiritsu Delinquent", "B"))
        enemies.append(spawn("Bulky Heiwa Seiritsu Delinquent"))

    elif stage_id == 14002:
        enemies.append(spawn("Slender Heiwa Seiritsu Delinquent"))
        enemies.append(spawn("Bulky Heiwa Seiritsu Delinquent", "A"))
        enemies.append(spawn("Bulky Heiwa Seiritsu Delinquent", "B"))

    elif stage_id == 15001:
        enemies.append(spawn("Spike Bat Heiwa Seiritsu Delinquent", "A"))
        enemies.append(spawn("Spike Bat Heiwa Seiritsu Delinquent", "B"))

    elif stage_id == 15002:
        enemies.append(spawn("Chain Fist Heiwa Seiritsu Delinquent", "A"))
        enemies.append(spawn("Chain Fist Heiwa Seiritsu Delinquent", "B"))

    elif stage_id == 15003:
        enemies.append(spawn("Spike Bat Heiwa Seiritsu Delinquent"))
        enemies.append(spawn("Chain Fist Heiwa Seiritsu Delinquent"))

    elif stage_id == 16001:
        enemies.append(spawn("Slender Heiwa Seiritsu Delinquent", "A"))
        enemies.append(spawn("Slender Heiwa Seiritsu Delinquent", "B"))
        enemies.append(spawn("Spike Bat Heiwa Seiritsu Delinquent", "A"))
        enemies.append(spawn("Spike Bat Heiwa Seiritsu Delinquent", "B"))

    elif stage_id == 16002:
        enemies.append(spawn("Bulky Heiwa Seiritsu Delinquent", "A"))
        enemies.append(spawn("Bulky Heiwa Seiritsu Delinquent", "B"))
        enemies.append(spawn("Chain Fist Heiwa Seiritsu Delinquent", "A"))
        enemies.append(spawn("Chain Fist Heiwa Seiritsu Delinquent", "B"))

    elif stage_id == 16003:
        enemies.append(spawn("Spike Bat Heiwa Seiritsu Delinquent", "A"))
        enemies.append(spawn("Spike Bat Heiwa Seiritsu Delinquent", "B"))
        enemies.append(spawn("Chain Fist Heiwa Seiritsu Delinquent"))

    elif stage_id == 16004:
        enemies.append(spawn("Spike Bat Heiwa Seiritsu Delinquent"))
        enemies.append(spawn("Chain Fist Heiwa Seiritsu Delinquent", "A"))
        enemies.append(spawn("Chain Fist Heiwa Seiritsu Delinquent", "B"))

    elif stage_id == 16005:
        enemies.append(spawn("Slender Heiwa Seiritsu Delinquent"))
        enemies.append(spawn("Bulky Heiwa Seiritsu Delinquent"))
        enemies.append(spawn("Spike Bat Heiwa Seiritsu Delinquent"))
        enemies.append(spawn("Chain Fist Heiwa Seiritsu Delinquent"))

    elif stage_id == 18:
        enemies.append(spawn("Spike Bat Heiwa Seiritsu Delinquent"))
        enemies.append(spawn("Chain Fist Heiwa Seiritsu Delinquent"))
        enemies.append(spawn("Heiwa Seiritsu Delinquent Leader Fighter"))

    elif stage_id == 19:
        enemies.append(spawn("Slender Heiwa Seiritsu Delinquent"))
        enemies.append(spawn("Bulky Heiwa Seiritsu Delinquent"))
        enemies.append(spawn("Heiwa Seiritsu Delinquent Leader Fighter", "A"))
        enemies.append(spawn("Heiwa Seiritsu Delinquent Leader Fighter", "B"))

    elif stage_id == 20:
        injured_boss = spawn("Heiwa Seiritsu Upperclassman Fighter")
        injured_boss.hp = 441
        enemies.append(injured_boss)

    elif stage_id == 21:
        enemies.append(spawn("‘Chain Reaper Of Heiwa’ Kurogane"))

    # --- ACT 3 ENEMY LOGIC ---
    elif stage_id == 25:
        enemies.append(spawn("Sparring Kiryoku Gakuen Student", "A"))
        enemies.append(spawn("Sparring Kiryoku Gakuen Student", "B"))
        enemies.append(spawn("Sparring Kiryoku Gakuen Student", "C"))
    
    elif stage_id == 26:
        enemies.append(spawn("Sparring Kiryoku Gakuen Student", "A"))
        enemies.append(spawn("Sparring Kiryoku Gakuen Student", "B"))
        enemies.append(spawn("Sparring Kiryoku Gakuen Student", "C"))
        enemies.append(spawn("Sparring Kiryoku Gakuen Student", "D"))

    elif stage_id == 28:
        enemies.append(spawn("‘Forest Guardian’ Fairy Ayako"))
        enemies.append(spawn("Kiryoku Gakuen Student Council Combatant", "A"))
        enemies.append(spawn("Kiryoku Gakuen Student Council Combatant", "B"))

    elif stage_id == 29:
        enemies.append(spawn("‘Lake Strider’ Fairy Sumiko"))
        enemies.append(spawn("Kiryoku Gakuen Student Council Combatant", "A"))
        enemies.append(spawn("Kiryoku Gakuen Student Council Combatant", "B"))
        enemies.append(spawn("Kiryoku Gakuen Student Council Combatant", "C"))

    elif stage_id == 31:
        weaker_heiwa_a = spawn("Infiltrating Heiwa Seiritsu High School Student", "A")
        weaker_heiwa_a.max_hp = 7
        weaker_heiwa_a.hp = 7
        weaker_heiwa_b = spawn("Infiltrating Heiwa Seiritsu High School Student", "B")
        weaker_heiwa_b.max_hp = 7
        weaker_heiwa_b.hp = 7
        weaker_heiwa_c = spawn("Infiltrating Heiwa Seiritsu High School Student", "C")
        weaker_heiwa_c.max_hp = 7
        weaker_heiwa_c.hp = 7
        enemies.append(weaker_heiwa_a)
        enemies.append(weaker_heiwa_b)
        enemies.append(weaker_heiwa_c)

    elif stage_id == 32001:
        enemies.append(spawn("Infiltrating Heiwa Seiritsu High School Student", "A"))
        enemies.append(spawn("Infiltrating Heiwa Seiritsu High School Student", "B"))
        enemies.append(spawn("Infiltrating Kiryoku Gakuen Student"))

    elif stage_id == 32002:
        enemies.append(spawn("Infiltrating Kiryoku Gakuen Student", "A"))
        enemies.append(spawn("Infiltrating Kiryoku Gakuen Student", "B"))
        enemies.append(spawn("Infiltrating Heiwa Seiritsu High School Student"))

    elif stage_id == 32003:
        enemies.append(spawn("Infiltrating Heiwa Seiritsu High School Student"))
        enemies.append(spawn("Infiltrating Kiryoku Gakuen Student"))
        enemies.append(spawn("Infiltrating Kasakura High School Student", "A"))
        enemies.append(spawn("Infiltrating Kasakura High School Student", "B"))

    elif stage_id == 33:
        enemies.append(spawn("Hisayuki Tadamasa"))

    elif stage_id == 34001:
        enemies.append(spawn("Infiltrating Heiwa Seiritsu Delinquent Leader", "A"))
        enemies.append(spawn("Infiltrating Heiwa Seiritsu Delinquent Leader", "B"))
        enemies.append(spawn("Infiltrating Kiryoku Gakuen Student Council Combatant"))

    elif stage_id == 34002:
        enemies.append(spawn("Infiltrating Kiryoku Gakuen Student Council Combatant", "A"))
        enemies.append(spawn("Infiltrating Kiryoku Gakuen Student Council Combatant", "B"))
        enemies.append(spawn("Infiltrating Kasakura High School Disciplinary Committee Combatant"))

    elif stage_id == 34003:
        enemies.append(spawn("Infiltrating Heiwa Seiritsu Delinquent Leader"))
        enemies.append(spawn("Infiltrating Kiryoku Gakuen Student Council Combatant"))
        enemies.append(spawn("Infiltrating Kasakura High School Disciplinary Committee Combatant", "A"))
        enemies.append(spawn("Infiltrating Kasakura High School Disciplinary Committee Combatant", "B"))

    elif stage_id == 35:
        enemies.append(spawn("Raven"))
        enemies.append(spawn("Infiltrating Heiwa Seiritsu High School Student", "A"))
        enemies.append(spawn("Infiltrating Heiwa Seiritsu High School Student", "B"))
        enemies.append(spawn("Infiltrating Heiwa Seiritsu Delinquent Leader"))

    elif stage_id == 36:
        enemies.append(spawn("Falcon"))
        enemies.append(spawn("Infiltrating Kiryoku Gakuen Student", "A"))
        enemies.append(spawn("Infiltrating Kiryoku Gakuen Student", "B"))
        enemies.append(spawn("Infiltrating Kiryoku Gakuen Student Council Combatant"))

    elif stage_id == 37:
        enemies.append(spawn("Eagle"))
        enemies.append(spawn("Raven (Injured)"))
        enemies.append(spawn("Falcon (Injured)"))

    elif stage_id == 38:
        weaker_heiwa_a = spawn("Unknown Faction Henchman", "A")
        weaker_heiwa_a.max_hp = 12
        weaker_heiwa_a.hp = 12
        weaker_heiwa_b = spawn("Unknown Faction Henchman", "B")
        weaker_heiwa_b.max_hp = 12
        weaker_heiwa_b.hp = 12
        enemies.append(weaker_heiwa_a)
        enemies.append(weaker_heiwa_b)
    
    elif stage_id == 39:
        enemies.append(spawn("Deadly Laser Beam World-Threatening Monster"))

    elif stage_id == 41001:
        enemies.append(spawn("Riposte Gang Henchman", "A"))
        enemies.append(spawn("Riposte Gang Henchman", "B"))
        enemies.append(spawn("Riposte Gang Henchman", "C"))

    elif stage_id == 41002:
        enemies.append(spawn("Riposte Gang Squad Leader"))
        enemies.append(spawn("Riposte Gang Henchman"))

    elif stage_id == 41003:
        enemies.append(spawn("Riposte Gang Henchman", "A"))
        enemies.append(spawn("Riposte Gang Henchman", "B"))
        enemies.append(spawn("Riposte Gang Squad Leader"))

    elif stage_id == 41004:
        enemies.append(spawn("Riposte Gang Squad Leader", "A"))
        enemies.append(spawn("Riposte Gang Squad Leader", "B"))

    elif stage_id == 42:
        enemies.append(spawn("Adam"))
        enemies.append(spawn("Riposte Gang Henchman"))
        enemies.append(spawn("Riposte Gang Squad Leader"))

    elif stage_id == 49:
        enemies.append(spawn("Infiltrating Yunhai Border Guard", "A"))
        enemies.append(spawn("Infiltrating Yunhai Border Guard", "B"))
        enemies.append(spawn("Infiltrating Yunhai Border Guard", "C"))

    elif stage_id == 50:
        enemies.append(spawn("Infiltrating Yunhai Border Guard", "A"))
        enemies.append(spawn("Infiltrating Yunhai Border Guard", "B"))
        enemies.append(spawn("Infiltrating Yunhai Border Guard Leader"))

    elif stage_id == 51:
        inf_yunhai_civ_a = spawn("Infiltrating Kiryoku Gakuen Student Council Combatant")
        inf_yunhai_civ_a.max_hp = 51
        inf_yunhai_civ_a.hp = 51
        inf_yunhai_civ_a.name = "Infiltrating Westward Megastructure Civilian A"
        enemies.append(inf_yunhai_civ_a)
        inf_yunhai_civ_b = spawn("Infiltrating Yunhai Border Guard Leader")
        inf_yunhai_civ_b.max_hp = 33
        inf_yunhai_civ_b.hp = 33
        inf_yunhai_civ_b.name = "Infiltrating Westward Megastructure Civilian B"
        enemies.append(inf_yunhai_civ_b)
        inf_yunhai_civ_c = spawn("Infiltrating Kasakura High School Disciplinary Committee Combatant")
        inf_yunhai_civ_c.max_hp = 54
        inf_yunhai_civ_c.hp = 54
        inf_yunhai_civ_c.name = "Infiltrating Westward Megastructure Civilian C"
        enemies.append(inf_yunhai_civ_c)
        inf_yunhai_civ_d = spawn("Infiltrating Yunhai Border Guard Leader")
        inf_yunhai_civ_d.max_hp = 30
        inf_yunhai_civ_d.hp = 30
        inf_yunhai_civ_d.name = "Infiltrating Westward Megastructure Civilian D"
        enemies.append(inf_yunhai_civ_d)

    elif stage_id == 52:
        enemies.append(spawn("Luoxia Martial Arts Practitioner Student", "A"))
        enemies.append(spawn("Luoxia Martial Arts Practitioner Student", "B"))
        enemies.append(spawn("Luoxia Martial Arts Practitioner Student", "C"))
    
    elif stage_id == 53:
        enemies.append(spawn("Natsume(?)"))

    elif stage_id == 56001:
        enemies.append(spawn("Golden Fist Union Gangster", "A"))
        enemies.append(spawn("Golden Fist Union Gangster", "B"))
        enemies.append(spawn("Golden Fist Union Gangster", "C"))
        enemies.append(spawn("Golden Fist Union Gangster", "D"))
    elif stage_id == 56002:
        enemies.append(spawn("Golden Fist Union Gangster", "A"))
        enemies.append(spawn("Golden Fist Union Gangster", "B"))
        enemies.append(spawn("Golden Fist Union Gangster", "C"))
        enemies.append(spawn("Golden Fist Union Gangster Leader"))
    elif stage_id == 56003:
        enemies.append(spawn("Golden Fist Union Gangster Leader", "A"))
        enemies.append(spawn("Golden Fist Union Gangster Leader", "B"))
        enemies.append(spawn("Golden Fist Union Gangster Leader", "C"))
    elif stage_id == 56004:
        enemies.append(spawn("Golden Fist Union Gangster", "A"))
        enemies.append(spawn("Golden Fist Union Gangster", "B"))
        enemies.append(spawn("Golden Fist Union Gangster Leader", "A"))
        enemies.append(spawn("Golden Fist Union Gangster Leader", "B"))
    elif stage_id == 56005:
        enemies.append(spawn("Golden Fist Union Gangster", "A"))
        enemies.append(spawn("Golden Fist Union Gangster", "B"))
        enemies.append(spawn("Golden Fist Union Gangster", "C"))
        enemies.append(spawn("Golden Fist Union Gangster", "D"))
        enemies.append(spawn("Golden Fist Union Gangster", "E"))

    elif stage_id == 57001:
        enemies.append(spawn("Black Water Dock Gangster", "A"))
        enemies.append(spawn("Black Water Dock Gangster", "B"))
        enemies.append(spawn("Black Water Dock Gangster", "C"))
        enemies.append(spawn("Black Water Dock Gangster", "D"))
    elif stage_id == 57002:
        enemies.append(spawn("Black Water Dock Gangster", "A"))
        enemies.append(spawn("Black Water Dock Gangster", "B"))
        enemies.append(spawn("Black Water Dock Gangster", "C"))
        enemies.append(spawn("Black Water Dock Gangster Leader"))
    elif stage_id == 57003:
        enemies.append(spawn("Black Water Dock Gangster Leader", "A"))
        enemies.append(spawn("Black Water Dock Gangster Leader", "B"))
        enemies.append(spawn("Black Water Dock Gangster Leader", "C"))
    elif stage_id == 57004:
        enemies.append(spawn("Black Water Dock Gangster", "A"))
        enemies.append(spawn("Black Water Dock Gangster", "B"))
        enemies.append(spawn("Black Water Dock Gangster Leader", "A"))
        enemies.append(spawn("Black Water Dock Gangster Leader", "B"))
    elif stage_id == 57005:
        enemies.append(spawn("Black Water Dock Gangster", "A"))
        enemies.append(spawn("Black Water Dock Gangster", "B"))
        enemies.append(spawn("Black Water Dock Gangster", "C"))
        enemies.append(spawn("Black Water Dock Gangster", "D"))
        enemies.append(spawn("Black Water Dock Gangster", "E"))

    elif stage_id == 58001:
        enemies.append(spawn("Twin Mountain Gate Gangster", "A"))
        enemies.append(spawn("Twin Mountain Gate Gangster", "B"))
        enemies.append(spawn("Twin Mountain Gate Gangster", "C"))
    elif stage_id == 58002:
        enemies.append(spawn("Twin Mountain Gate Gangster", "A"))
        enemies.append(spawn("Twin Mountain Gate Gangster", "B"))
        enemies.append(spawn("Twin Mountain Gate Gangster Leader"))
    elif stage_id == 58003:
        enemies.append(spawn("Twin Mountain Gate Gangster Leader", "A"))
        enemies.append(spawn("Twin Mountain Gate Gangster Leader", "B"))
    elif stage_id == 58004:
        enemies.append(spawn("Twin Mountain Gate Gangster"))
        enemies.append(spawn("Twin Mountain Gate Gangster Leader", "A"))
        enemies.append(spawn("Twin Mountain Gate Gangster Leader", "B"))
    elif stage_id == 58005:
        enemies.append(spawn("Twin Mountain Gate Gangster", "A"))
        enemies.append(spawn("Twin Mountain Gate Gangster", "B"))
        enemies.append(spawn("Twin Mountain Gate Gangster", "C"))
    elif stage_id == 60001:
        enemies.append(spawn("Golden Fist Union Gangster", "A"))
        enemies.append(spawn("Golden Fist Union Gangster", "B"))
        enemies.append(spawn("Golden Fist Union Gangster Leader"))
        enemies.append(spawn("Black Water Dock Gangster"))
        enemies.append(spawn("Black Water Dock Gangster Leader"))
    elif stage_id == 60002:
        enemies.append(spawn("Golden Fist Union Gangster Leader"))
        enemies.append(spawn("Black Water Dock Gangster", "A"))
        enemies.append(spawn("Black Water Dock Gangster", "B"))
        enemies.append(spawn("Twin Mountain Gate Gangster"))
        enemies.append(spawn("Twin Mountain Gate Gangster Leader"))
    elif stage_id == 60003:
        enemies.append(spawn("Golden Fist Union Gangster"))
        enemies.append(spawn("Golden Fist Union Gangster Leader"))
        enemies.append(spawn("Black Water Dock Gangster"))
        enemies.append(spawn("Black Water Dock Gangster Leader"))
        enemies.append(spawn("Twin Mountain Gate Gangster"))
        enemies.append(spawn("Twin Mountain Gate Gangster Leader"))
    elif stage_id == 62:
        enemies.append(spawn("Miyu"))
    elif stage_id == 63:
        enemies.append(spawn("Mei"))
    elif stage_id == 64:
        bbguard_a = spawn("Blood-Broken Guard Footsoldier", "A")
        bbguard_a.hp = 33
        enemies.append(bbguard_a)
        bbguard_b = spawn("Blood-Broken Guard Footsoldier", "B")
        bbguard_b.hp = 29
        enemies.append(bbguard_b)
        bbguard_c = spawn("Blood-Broken Guard Footsoldier", "C")
        bbguard_c.hp = 31
        enemies.append(bbguard_c)
    elif stage_id == 65:
        jrmons_a = spawn("Jade Rain Monastery Footsoldier", "A")
        jrmons_a.hp = 30
        enemies.append(jrmons_a)
        jrmons_b = spawn("Jade Rain Monastery Footsoldier", "B")
        jrmons_b.hp = 28
        enemies.append(jrmons_b)
        jrmons_c = spawn("Jade Rain Monastery Footsoldier", "C")
        jrmons_c.hp = 24
        enemies.append(jrmons_c)
    elif stage_id == 66:
        enemies.append(spawn("Ibara Ninja"))
    elif stage_id == 68001:
        enemies.append(spawn("Blood-Broken Guard Footsoldier", "A"))
        enemies.append(spawn("Blood-Broken Guard Footsoldier", "B"))
        enemies.append(spawn("Blood-Broken Guard Footsoldier", "C"))
    elif stage_id == 68002:
        enemies.append(spawn("Jade Rain Monastery Footsoldier", "A"))
        enemies.append(spawn("Jade Rain Monastery Footsoldier", "B"))
        enemies.append(spawn("Jade Rain Monastery Footsoldier", "C"))
    elif stage_id == 68003:
        enemies.append(spawn("Blood-Broken Guard Footsoldier", "A"))
        enemies.append(spawn("Blood-Broken Guard Footsoldier", "B"))
        enemies.append(spawn("Jade Rain Monastery Footsoldier"))
    elif stage_id == 68004:
        enemies.append(spawn("Blood-Broken Guard Footsoldier"))
        enemies.append(spawn("Jade Rain Monastery Footsoldier", "A"))
        enemies.append(spawn("Jade Rain Monastery Footsoldier", "B"))
    elif stage_id == 69001:
        enemies.append(spawn("Ten Thousand Blossom Brotherhood Linebreaker", "A"))
        enemies.append(spawn("Ten Thousand Blossom Brotherhood Linebreaker", "B"))
        enemies.append(spawn("Ten Thousand Blossom Brotherhood Linebreaker", "C"))
    elif stage_id == 69002:
        enemies.append(spawn("Ten Thousand Blossom Brotherhood Defender", "A"))
        enemies.append(spawn("Ten Thousand Blossom Brotherhood Defender", "B"))
        enemies.append(spawn("Ten Thousand Blossom Brotherhood Defender", "C"))
    elif stage_id == 69003:
        enemies.append(spawn("Ten Thousand Blossom Brotherhood Linebreaker", "A"))
        enemies.append(spawn("Ten Thousand Blossom Brotherhood Linebreaker", "B"))
        enemies.append(spawn("Ten Thousand Blossom Brotherhood Defender", "A"))
        enemies.append(spawn("Ten Thousand Blossom Brotherhood Defender", "B"))
    elif stage_id == 70:
        enemies.append(spawn("Zhao Feng"))
    elif stage_id == 71:
        enemies.append(spawn("Ibara Ninja - 'Kagerou The Untouchable'"))

    # Return ignoring any potential NoneType errors from typos in db
    return [e for e in enemies if e is not None]

def get_enemy_database():
    ########################################
    # --- EARLY KASAKURA / DELINQUENTS --- #
    ########################################
    
    thief = Entity("Underwear Thief", is_player=False)
    thief.max_hp = 30
    k_thief = Kata("Thief Intent", "Thief", 1, "0", [0.5, 1.2, 1.2, 1.2, 1.2, 0.5, 1.2])
    ts1 = Skill("Stumble Around", 1, EL_EROS, 0, "Does nothing")
    ts2 = Skill("Weak Bag Swing", 2, EL_AGAPE, 3, "")
    k_thief.skill_pool_def = [(ts1, 3), (ts2, 6)]
    k_thief.rift_aptitude = 0
    thief.equip_kata(k_thief)
    thief.description = "The infamous underwear thief terrorizing Kasakura High School’s female locker rooms.\nScum of the earth."
    thief.unlock_stage_id = 0 
    
    fresh = Entity("Class-Skipping Freshman", is_player=False)
    fresh.max_hp = 10
    k_fresh = Kata("Delinquent Attitude", "Freshman", 1, "0", [1.3, 1.3, 1.4, 1.4, 1.4, 1.4, 1.3])
    fs1 = Skill("Flimsy Punch", 1, EL_AGAPE, 3, "")
    fs2 = Skill("Kick", 2, EL_STORGE, 5, "")
    k_fresh.skill_pool_def = [(fs1, 4), (fs2, 5)]
    k_fresh.rift_aptitude = 0
    fresh.equip_kata(k_fresh)
    fresh.description = "A freshman reported to be skipping class and loitering behind campus, messing around and intimidating those that pass them."
    fresh.unlock_stage_id = 2 

    ###############################
    # --- KIDNAPPER HOOLIGANS --- #
    ###############################

    hool = Entity("Kidnapper Hooligan", is_player=False)
    hool.max_hp = 5
    k_hool = Kata("Hooligan", "Hooligan", 1, "0", [1.5]*7)
    s1 = Skill("Bash", 1, EL_PRAGMA, 5, "")
    k_hool.skill_pool_def = [(s1, 9)]
    k_hool.rift_aptitude = 0
    hool.equip_kata(k_hool)
    hool.description = "A musclebrained hooligan worker who kidnaps people for quick and dirty money. Often works in groups."
    hool.unlock_stage_id = 4

    lead = Entity("Kidnapper Hooligan Leader", is_player=False)
    lead.max_hp = 20
    k_lead = Kata("Leader", "Leader", 1, "0", [1.15, 1.15, 1.05, 1.05, 1.05, 1.05, 1.15])
    ls1 = Skill("Heavy Bash", 1, EL_PRAGMA, 6, "")
    ls2 = Skill("Block", 2, EL_LUDUS, 0, "[Combat Start] This unit takes -4 Final Damage this turn.", effect_type="BUFF_DEF_FLAT", effect_val=4)
    k_lead.skill_pool_def = [(ls1, 7), (ls2, 2)]
    k_lead.rift_aptitude = 0
    lead.equip_kata(k_lead)
    lead.description = "The leader of the hooligan workers. Stronger than their minions, spends most of their time barking orders."
    lead.unlock_stage_id = 4
    
    ###########################################
    # --- AYAME BENIKAWA (BOSS ENCOUNTER) --- #
    ###########################################

    benikawa = Entity("Ayame Benikawa (Sparring)", is_player=False)
    benikawa.max_hp = 29 
    res_b = [1.3, 1.3, 0.7, 0.7, 0.9, 0.9, 1.0]
    k_spar = Kata("Sparring Style", "Benikawa", 1, 2, res_b)
    s1 = Skill("Palm Strike", 1, EL_PHILIA, 2, "If the target has 70%- HP, deal -1 Final Damage", effect_type="COND_LOW_HP_MERCY", effect_val=1)
    s2 = Skill("Roundhouse Kick", 2, EL_STORGE, 3, "If the target has 70%- HP, deal -1 Final Damage", effect_type="COND_LOW_HP_MERCY", effect_val=1)
    s3 = Skill("Vital Strike", 3, EL_PHILAUTIA, 5, "[On Hit] Target will take +4 Final Damage from the next attack.", effect_type="ON_HIT_NEXT_TAKEN_FLAT", effect_val=4)
    k_spar.skill_pool_def = [(s1, 3), (s2, 3), (s3, 3)]
    k_spar.rift_aptitude = 2
    benikawa.equip_kata(k_spar)
    benikawa.description = "Akasuke’s fellow member and black belt of the Kasakura High School Karate Club, and sparring partner for today’s long awaited friendly match."
    benikawa.unlock_stage_id = 6

    ninja = Entity("Ayame Benikawa (Ninja)", is_player=False)
    ninja.max_hp = 60
    res_n = [1.5, 0.6, 0.6, 0.9, 1.5, 0.9, 0.6]
    k_ninja = Kata("Benikawa Ninja Arts", "Benikawa", 1, 4, res_n)
    s1 = Skill("Aim Vitals", 1, EL_EROS, 4, "[On Hit] Target will take +4 Final Damage from the next attack", effect_type="ON_HIT_NEXT_TAKEN_FLAT", effect_val=4)
    s2 = Skill("Crescent Kick", 2, EL_LUDUS, 5, "If the target has 80%- HP, deal +2 Final Damage", effect_type="COND_HP_BELOW_80_FLAT", effect_val=2)
    s3 = Skill("Reroute Nerves", 3, EL_PHILAUTIA, 8, "[On Hit] Target deals -80% damage next turn", effect_type="DEBUFF_ATK_MULT", effect_val=0.2)
    k_ninja.skill_pool_def = [(s1, 4), (s2, 3), (s3, 2)]
    k_ninja.rift_aptitude = 4
    ninja.equip_kata(k_ninja)
    ninja.description = (
        "Benikawa Ayame sheds her cheerful high-school karateka disguise to reveal her true identity as a trained assassin of the Benikawa ninja clan. "
        "Her ginger hair flows freely now, purple eyes sharp and predatory, movements silent and precise as she strikes with nerve-disrupting pressure-point techniques."
    )
    ninja.unlock_stage_id = 7

    double = Entity("Benikawa Body Double", is_player=False)
    double.max_hp = 20
    res_d = [1.4, 1.4, 1.5, 1.5, 1.4, 1.5, 1.4]
    k_double = Kata("Paper Clone", "Body Double", 1, 4, res_d)
    ds1 = Skill("Chop Strike", 1, EL_PRAGMA, 3, "")
    ds2 = Skill("Flying Kick", 2, EL_LUDUS, 5, "")
    k_double.skill_pool_def = [(ds1, 5), (ds2, 4)]
    k_double.rift_aptitude = 4
    double.equip_kata(k_double)
    double.description = (
        "A perfect paper talisman clone that mimics Ayame Benikawa’s exact appearance, voice, and mannerisms down to the playful grin and casual stance. "
        "Crafted with ninja origami techniques, the double can move fluidly and take light hits before disintegrating into a swirl of glowing paper slips. "
        "It serves as both a decoy to confuse opponents and a temporary extension of her will."
    )
    double.unlock_stage_id = 7

    ############################################
    # --- HEIWA SEIRITSU DELINQUENT GRUNTS --- #
    ############################################

    slender = Entity("Slender Heiwa Seiritsu Delinquent", is_player=False)
    slender.max_hp = 40
    res_s = [1.6, 1.6, 1.6, 1.4, 1.4, 1.4, 1.2]
    k_slender = Kata("Heiwa Slender", "Delinquent", 1, "0", res_s)
    ss1 = Skill("Pipe Smack", 1, EL_AGAPE, 4, "[On Hit] Target takes +1 Final Damage from next attack", effect_type="ON_HIT_NEXT_TAKEN_FLAT", effect_val=1)
    ss2 = Skill("Stubborn Rush", 2, EL_EROS, 4, "[Combat Start] Take +8 Final Damage for the turn", effect_type="BUFF_DEF_FLAT", effect_val=-8)
    k_slender.skill_pool_def = [(ss1, 5), (ss2, 4)]
    k_slender.rift_aptitude = 0
    slender.equip_kata(k_slender)
    slender.description = "An underperforming student who always acts before thinking. Has surprisingly many like minded buddies in the form of small gangs scattered throughout Heiwa Seiritsu campus."
    slender.unlock_stage_id = 10

    bulky = Entity("Bulky Heiwa Seiritsu Delinquent", is_player=False)
    bulky.max_hp = 45
    res_b = [1.2, 1.4, 1.6, 1.4, 1.6, 1.4, 1.6]
    k_bulky = Kata("Heiwa Bulky", "Delinquent", 1, "0", res_b)
    bs1 = Skill("Bat Bash", 1, EL_PHILAUTIA, 4, "[On Hit] Deal +1 Final Damage with next attack", effect_type="ON_HIT_NEXT_DEAL_FLAT", effect_val=1)
    bs2 = Skill("Stubborn Rush", 2, EL_EROS, 4, "[Combat Start] Take +8 Final Damage for the turn", effect_type="BUFF_DEF_FLAT", effect_val=-8)
    k_bulky.skill_pool_def = [(bs1, 5), (bs2, 4)]
    k_bulky.rift_aptitude = 0
    bulky.equip_kata(k_bulky)
    bulky.description = "An underperforming student who always acts before thinking. Eats a whole lot at all times, but under all the fat exists brawn that is not to be underestimated."
    bulky.unlock_stage_id = 10

    spike = Entity("Spike Bat Heiwa Seiritsu Delinquent", is_player=False)
    spike.max_hp = 30
    res_sp = [1.1, 1.6, 1.1, 1.2, 1.6, 1.6, 1.1]
    k_spike = Kata("Spike Bat Style", "Delinquent", 1, "0", res_sp)
    spi1 = Skill("Knock", 1, EL_STORGE, 5, "")
    spi2 = Skill("Sharp Swing", 2, EL_EROS, 5, "[On Hit] Inflict 1 Bleed Potency", effect_type="APPLY_STATUS")
    spi2.status_effect = bleed_1
    k_spike.skill_pool_def = [(spi1, 5), (spi2, 4)]
    k_spike.rift_aptitude = 0
    spike.equip_kata(k_spike)
    spike.description = "An older Heiwa Seiritsu thug student wielding a bat studded with cheap metal spikes, a common and effective makeshift weapon for school delinquents."
    spike.unlock_stage_id = 15

    chain = Entity("Chain Fist Heiwa Seiritsu Delinquent", is_player=False)
    chain.max_hp = 30
    res_ch = [1.6, 1.1, 1.6, 1.2, 1.2, 1.1, 1.6]
    k_chain = Kata("Chain Fist Style", "Delinquent", 1, "0", res_ch)
    ch1 = Skill("Shove", 1, EL_PHILIA, 6, "")
    ch2 = Skill("Cutting Fist", 2, EL_PRAGMA, 3, "[On Hit] Inflict 2 Bleed Potency", effect_type="APPLY_STATUS")
    ch2.status_effect = bleed_2
    k_chain.skill_pool_def = [(ch1, 5), (ch2, 4)]
    k_chain.rift_aptitude = 0
    chain.equip_kata(k_chain)
    chain.description = "An older Heiwa Seiritsu thug student that wraps old metal chains around their fists which prove effective in leaving cuts when swung roughly enough at an opponent."
    chain.unlock_stage_id = 15

    h_lead = Entity("Heiwa Seiritsu Delinquent Leader Fighter", is_player=False)
    h_lead.max_hp = 40
    res_hl = [1.7, 1.7, 1.3, 1.3, 1.3, 1.3, 1.3]
    k_hlead = Kata("Leader Style", "Leader", 1, "0", res_hl)
    hl1 = Skill("Headbutting", 1, EL_PHILIA, 5, "[On Hit] Inflict 1 Bleed Potency", effect_type="APPLY_STATUS")
    hl1.status_effect = bleed_1
    hl2 = Skill("Chained Bat Combo", 2, EL_PRAGMA, 5, "[On Hit] Inflict 2 Bleed Potency", effect_type="APPLY_STATUS")
    hl2.status_effect = bleed_2
    hl3 = Skill("Rally", 3, EL_PRAGMA, 0, "[On Use] All allied units of this unit take -1 Final Damage this turn", effect_type="AOE_BUFF_DEF_FLAT", effect_val=1)
    k_hlead.skill_pool_def = [(hl1, 4), (hl2, 3), (hl3, 2)]
    k_hlead.rift_aptitude = 1
    h_lead.equip_kata(k_hlead)
    h_lead.description = "A more experienced Heiwa Seiritsu thug student who has enough respect and proficiency with makeshift weapons to lead a small unit of thugs."
    h_lead.unlock_stage_id = 18

    ########################################
    # --- HEIWA SEIRITSU ELITES & BOSS --- #
    ########################################

    upper = Entity("Heiwa Seiritsu Upperclassman Fighter", is_player=False)
    upper.max_hp = 1523
    res_up = [1.0, 1.2, 1.0, 1.1, 1.1, 1.2, 0.7]
    k_up = Kata("Upperclassman Style", "Upperclassman", 1, "0", res_up)
    u1 = Skill("Chained Limb Combo", 1, EL_LUDUS, 14, "[On Hit] Inflict 2 Bleed Potency", effect_type="APPLY_STATUS")
    u1.status_effect = bleed_2
    u2 = Skill("Chain Whip", 2, EL_AGAPE, 15, "[On Hit] Inflict 3 Bleed Potency", effect_type="APPLY_STATUS")
    u2.status_effect = bleed_3
    u3 = Skill("Pull In And Thrash", 3, EL_AGAPE, 17, "[On Hit] Inflict 1 Bind next turn", effect_type="APPLY_STATUS")
    u3.status_effect = bind_1
    k_up.skill_pool_def = [(u1, 3), (u2, 3), (u3, 3)]
    k_up.rift_aptitude = 5
    upper.equip_kata(k_up)
    upper.description = "One of Heiwa Seiritsu’s “Upperclassman” elite fighters from the legends told throughout campus. They are highly experienced veterans who follow the most brutal combat mindsets and calculatingly fight with their specialty weapons."
    upper.unlock_stage_id = 20

    kuro = Entity("‘Chain Reaper Of Heiwa’ Kurogane", is_player=False)
    kuro.max_hp = 150
    res_ku = [1.3, 1.3, 1.1, 1.6, 1.6, 1.1, 1.6]
    k_ku = Kata("Reaper Style", "Kurogane", 1, "0", res_ku)
    ku1 = Skill("Chained Limb Flurry", 1, EL_PRAGMA, 5, "[On Hit] Inflict 2 Bleed Potency\n       [On Hit] Inflict 2 Bleed Count", effect_type="APPLY_BLEED_HEAVY_STACKS")
    ku2 = Skill("Heavy Chain Whip", 2, EL_AGAPE, 6, "[On Hit] Inflict 3 Bleed Potency\n       [On Hit] Inflict 1 Bind next turn", effect_type="APPLY_BLEED_AND_BIND")
    ku3 = Skill("Pull In For A Beatdown", 3, EL_AGAPE, 8, "[On Hit] Inflict 3 Bleed Potency\n       [On Hit] Inflict 2 Bind next turn", effect_type="APPLY_BLEED_AND_BIND_HEAVY")
    k_ku.skill_pool_def = [(ku1, 3), (ku2, 4), (ku3, 2)]
    k_ku.rift_aptitude = 6
    kuro.equip_kata(k_ku)
    kuro.description = "The true identity of the Heiwa Seiritsu Upperclassman: 'Chain Reaper Of Heiwa' Kurogane, has been revealed. A veteran hotblooded gangster on the run who tortures his opponents with masterful chain movements paired with his reckless fighting style. His motives are taking down Kasakura’s key figures and extracting information about the existence of “Katas”."
    kuro.unlock_stage_id = 21

    #############################################
    # --- KIRYOKU GAKUEN STUDENTS & FAIRIES --- #
    #############################################

    sp_kiryoku = Entity("Sparring Kiryoku Gakuen Student", is_player=False)
    sp_kiryoku.max_hp = 40
    k_sp_kiryoku = Kata("Kiryoku Sparring", "Kiryoku Student", 1, 1, [1.3, 1.3, 1.3, 1.5, 1.4, 1.3, 1.2])
    sk1 = Skill("Low Kick", 1, EL_LUDUS, 4, "[On Hit] Inflict 1 Rupture Potency", effect_type="APPLY_STATUS")
    sk1.status_effect = rupture_1
    sk2 = Skill("Cross Fist", 2, EL_AGAPE, 6, "[On Hit] Inflict 2 Rupture Count", effect_type="APPLY_STATUS")
    sk2.status_effect = rupturecount_2
    k_sp_kiryoku.skill_pool_def = [(sk1, 5), (sk2, 4)]
    sp_kiryoku.equip_kata(k_sp_kiryoku)
    sp_kiryoku.description = "Athletic girl members of the Self-Defense Club who possess a strangely highly optimistic mindset which completely lacks hesitation, fear, or frustration even in the face of absolute defeat. They fight with boundless energy and solid martial arts foundations, eagerly absorbing heavy blows just to learn from their opponents."
    sp_kiryoku.unlock_stage_id = 25

    c_kiryoku = Entity("Kiryoku Gakuen Student Council Combatant", is_player=False)
    c_kiryoku.max_hp = 50
    k_c_kiryoku = Kata("Council Combat", "Council Combatant", 1, 2, [1.3, 1.1, 1.1, 1.1, 1.3, 1.4, 1.4])
    ck1 = Skill("Suppression", 1, EL_AGAPE, 7, "[On Hit] Inflict 3 Rupture Potency", effect_type="APPLY_STATUS")
    ck1.status_effect = rupture_3
    ck2 = Skill("Focusing On Protection", 2, EL_PHILAUTIA, 5, "[On Use] All ally units deal -2 Base Damage this turn", effect_type="BASE_DAMAGE_DEBUFF_ALL", effect_val=2)
    ck3 = Skill("Rush In", 3, EL_PHILIA, 9, "[On Hit] Inflict 2 Rupture Count\n       [On Hit] Inflict 2 Fairylight Potency", effect_type="KIRYOKU_COUNCIL_SPECIAL")
    k_c_kiryoku.skill_pool_def = [(ck1, 4), (ck2, 2), (ck3, 3)]
    c_kiryoku.equip_kata(k_c_kiryoku)
    c_kiryoku.description = "These trusted enforcers serve directly beneath the Fairies of Kiryoku Gakuen’s student council, utilizing the precise, highly disciplined martial arts cultivated within the school’s top athletic clubs. They fight with unshakeable focus and coordinated teamwork, partially abandoning the usual friendly Kiryoku demeanor to efficiently suppress their targets. Those who work under the Fairies are often called “Lesser Fairies” for easier distinction, although they are all considered a part of the student council’s theme."
    c_kiryoku.unlock_stage_id = 28

    ayako = Entity("‘Forest Guardian’ Fairy Ayako", is_player=False)
    ayako.max_hp = 132
    k_ayako = Kata("Forest Guardian", "Ayako", 1, 7, [1.3, 1.0, 1.0, 0.9, 1.2, 1.0, 1.3])
    ay1 = Skill("Cross Distance", 1, EL_AGAPE, 5, "[On Hit] Inflict 3 Rupture Potency", effect_type="APPLY_STATUS")
    ay1.status_effect = rupture_3
    ay2 = Skill("Quickdraw Bokken", 2, EL_LUDUS, 7, "[On Hit] If target has Rupture, Inflict 2 Fairylight Potency", effect_type="FAIRYLIGHT_APPLY", effect_val=2)
    ay3 = Skill("Shukuchi (Incomplete)", 3, EL_PRAGMA, 10, "[On Hit] Inflict 3 Rupture Count\n       [On Hit] Inflict 4 Fairylight Potency", effect_type="AYAKO_SPECIAL")
    k_ayako.skill_pool_def = [(ay1, 3), (ay2, 3), (ay3, 3)]
    ayako.equip_kata(k_ayako)
    ayako.description = "Serving as the Security Head of the Kiryoku Student Council, Ayako is a feral, battle-hungry warrior who wields a solid oak bokken with devastating power. She fights using chaotic, bouncing trajectories and explosive acceleration that makes meeting her head-on incredibly dangerous. Fiercely protective of her empathic 'Queen', she relies on her overwhelming speed and predatory instincts to effortlessly overwhelm seasoned fighters."
    ayako.unlock_stage_id = 28

    sumiko = Entity("‘Lake Strider’ Fairy Sumiko", is_player=False)
    sumiko.max_hp = 143
    k_sumiko = Kata("Lake Strider", "Sumiko", 1, 6, [1.0, 1.2, 1.3, 0.7, 0.7, 1.1, 1.0])
    su1 = Skill("Distancing", 1, EL_PRAGMA, 5, "[On Hit] If target has Fairylight, inflict 5 Rupture Potency.", effect_type="FAIRYLIGHT_SPECIAL1", effect_val=5)
    su2 = Skill("Protection By The Fairies", 2, EL_LUDUS, 5, "[On Use] All ally units deal -8 Final Damage this turn\n       [On Hit] Gain 2 Haste next turn", effect_type="SUMIKO_SPECIAL_1")
    su3 = Skill("Shukuchi (Incomplete)", 3, EL_PRAGMA, 9, "[On Hit] Inflict 4 Rupture Count\n       [On Hit] Inflict 5 Rupture Potency\n       [On Hit] Gain 2 Haste next turn", effect_type="SUMIKO_SPECIAL_2")
    k_sumiko.skill_pool_def = [(su1, 3), (su2, 3), (su3, 3)]
    sumiko.equip_kata(k_sumiko)
    sumiko.description = "The calculating Treasurer of the Kiryoku Student Council, Sumiko controls the battlefield with an eerie, sisterly calmness. She utilizes a terrifying footwork technique called Shukuchi to seamlessly glide across the floor, instantly closing the distance between herself and her target without any visible inertia. Despite her ferocity in close-quarters combat, she prioritizes defense and spatial control, meticulously keeping threats pushed far away from her President, who is currently sleeping."
    sumiko.unlock_stage_id = 29

    ####################################
    # --- CRUISE SHIP INFILTRATORS --- #
    ####################################

    inf_heiwa = Entity("Infiltrating Heiwa Seiritsu High School Student", is_player=False)
    inf_heiwa.max_hp = 37
    k_inf_heiwa = Kata("Fake Delinquent", "Heiwa Infiltrator", 1, 0, [1.4, 1.3, 1.4, 1.7, 1.4, 1.4, 1.3])
    ih1 = Skill("Panicked Kick", 1, EL_PRAGMA, 7, "[On Hit] Inflict 2 Bleed Count", effect_type="APPLY_STATUS")
    ih1.status_effect = bleedcount_2
    ih2 = Skill("Metal Bat Swing", 2, EL_EROS, 8, "[On Hit] Inflict 2 Bleed Potency\n       [On Hit] Inflict 2 Rupture Potency", effect_type="BLEED_RUPTURE_SPECIAL_TYPE1", effect_val=2)
    k_inf_heiwa.skill_pool_def = [(ih1, 4), (ih2, 4)]
    inf_heiwa.equip_kata(k_inf_heiwa)
    inf_heiwa.description = "Hired thugs who disguised themselves as Heiwa Seiritsu's rowdy delinquents to quietly infiltrate the cruise ship's lower decks. They rely on crude street brawling and concealed weapons to overwhelm their targets with sheer numbers while securing the stolen cargo. However, they completely lack the genuine, unbreakable spirit of true Heiwa students, making their sloppy attacks easy to counter for seasoned martial artists."
    inf_heiwa.unlock_stage_id = 31

    inf_kiryoku = Entity("Infiltrating Kiryoku Gakuen Student", is_player=False)
    inf_kiryoku.max_hp = 35
    k_inf_kiryoku = Kata("Fake Athlete", "Kiryoku Infiltrator", 1, 0, [1.3, 1.4, 1.4, 1.2, 1.6, 1.6, 1.2])
    ik1 = Skill("Gut Punch", 1, EL_LUDUS, 6, "[On Hit] Inflict 2 Rupture Potency", effect_type="APPLY_STATUS")
    ik1.status_effect = rupture_2
    ik2 = Skill("Smackdown", 2, EL_AGAPE, 10, "[On Hit] Inflict 3 Rupture Potency", effect_type="APPLY_STATUS")
    ik2.status_effect = rupture_3
    k_inf_kiryoku.skill_pool_def = [(ik1, 4), (ik2, 4)]
    inf_kiryoku.equip_kata(k_inf_kiryoku)
    inf_kiryoku.description = "Wearing stolen Kiryoku athletic uniforms, these low-level pawns attempt to mimic the school's dynamic martial arts to blend in during the Goodwill Trip. While physically fit enough to carry out the heavy lifting for the weapon heist, their strikes lack the terrifying, adrenaline-fueled joy of actual Kiryoku combatants. They quickly crumble and break formation when faced with the overwhelming power and technique of Kasakura's vanguard."
    inf_kiryoku.unlock_stage_id = 32

    inf_kasa = Entity("Infiltrating Kasakura High School Student", is_player=False)
    inf_kasa.max_hp = 44
    k_inf_kasa = Kata("Fake Karateka", "Kasakura Infiltrator", 1, 0, [1.5, 1.4, 1.3, 1.2, 1.4, 1.4, 1.1])
    ika1 = Skill("Unsteady Hand Chop", 1, EL_EROS, 6, "[On Hit] Target will take +3 Final Damage from the next attack.", effect_type="ON_HIT_NEXT_TAKEN_FLAT", effect_val=3)
    ika2 = Skill("Grapple", 2, EL_STORGE, 7, "[On Hit] Target deals -20% damage next turn", effect_type="DEBUFF_ATK_MULT", effect_val=0.8)
    ika3 = Skill("Gotta Rest", 3, EL_AGAPE, 7, "[On Use] Deal 0 damage, then heal by supposed final damage", effect_type="SELF_HEAL_TYPE1")
    k_inf_kasa.skill_pool_def = [(ika1, 5), (ika2, 2), (ika3, 2)]
    inf_kasa.equip_kata(k_inf_kasa)
    inf_kasa.description = "These disguised criminals attempt to pass off as disciplined Kasakura students, utilizing standard karate or judo stances to maintain their cover in the ship's corridors. Beneath the pristine uniforms, they are nothing more than greedy mercenaries hired by a shadow mastermind to secure the massive weapons supply. Their rigid, unpolished forms are easily dismantled by prodigies like Akasuke and Yuri, instantly exposing their lack of true martial dedication."
    inf_kasa.unlock_stage_id = 32

    inf_lead = Entity("Infiltrating Heiwa Seiritsu Delinquent Leader", is_player=False)
    inf_lead.max_hp = 55
    k_inf_lead = Kata("Fake Leader", "Infiltrator Leader", 1, 1, [1.2, 1.2, 1.3, 1.6, 1.4, 1.3, 1.0])
    il1 = Skill("Wrapping Chains", 1, EL_EROS, 6, "[On Hit] Inflict 2 Bleed Potency\n       [On Hit] Inflict 2 Bleed Count", effect_type="APPLY_BLEED_HEAVY_STACKS")
    il2 = Skill("Metal Bat Desperation", 2, EL_PHILAUTIA, 9, "[On Hit] Inflict 3 Bleed Potency\n       [On Hit] Inflict 3 Rupture Potency", effect_type="BLEED_RUPTURE_SPECIAL_TYPE1", effect_val=3)
    il3 = Skill("Rally", 3, EL_EROS, 0, "[On Use] All allied units of this unit take -3 Final Damage this turn", effect_type="AOE_BUFF_DEF_FLAT", effect_val=3)
    k_inf_lead.skill_pool_def = [(il1, 3), (il2, 3), (il3, 3)]
    inf_lead.equip_kata(k_inf_lead)
    inf_lead.description = "Acting as squad commanders for the ship's infiltration forces, these washed-up gang leaders don the customized, untidy uniforms of Heiwa's notorious Upperclassmen. They bark aggressive orders and wield heavier, lethal blunt weapons to coordinate the theft of the ship's armory and suppress any interference. Despite their intimidating posturing, they possess none of the mythic, monstrous strength of the real Heiwa legends and rely entirely on intimidation."
    inf_lead.unlock_stage_id = 34

    inf_council = Entity("Infiltrating Kiryoku Gakuen Student Council Combatant", is_player=False)
    inf_council.max_hp = 53
    k_inf_council = Kata("Fake Council", "Fake Council", 1, 1, [1.1, 1.5, 1.5, 1.0, 1.2, 1.5, 1.3])
    ic1 = Skill("Baton Smack", 1, EL_AGAPE, 7, "[On Hit] Inflict 2 Rupture Potency\n       [On Hit] Inflict 2 Rupture Count", effect_type="APPLY_RUPTURE_HEAVY_STACKS")
    ic2 = Skill("Fairy Blessing (Fake)", 2, EL_PRAGMA, 7, "[On Hit] If target has Rupture, Inflict 2 Fairylight Potency", effect_type="FAIRYLIGHT_APPLY", effect_val=2)
    ic3 = Skill("Shukuchi (Fake)", 3, EL_EROS, 14, "[On Use] Gain 4 Bind next turn", effect_type="GAIN_STATUS")
    ic3.status_effect = bind_4
    k_inf_council.skill_pool_def = [(ic1, 3), (ic2, 4), (ic3, 2)]
    inf_council.equip_kata(k_inf_council)
    inf_council.description = "Disguised with the elite armbands of the Kiryoku Student Council, these specialized thugs are tasked with guarding the stolen weapon caches deep in the ship's hull. They use batons and coordinated tactical formations to mimic the Council's security enforcers, attempting to lock down chokepoints. However, their heavy-handed reliance on brute force completely betrays their lack of the intricate, acrobatic techniques mastered by the true 'Lesser Fairies.'"
    inf_council.unlock_stage_id = 34

    inf_disc = Entity("Infiltrating Kasakura High School Disciplinary Committee Combatant", is_player=False)
    inf_disc.max_hp = 56
    k_inf_disc = Kata("Fake Discipline", "Fake Disciplinary", 1, 1, [1.5, 1.2, 1.0, 1.3, 1.0, 1.4, 1.6])
    id1 = Skill("Bokken Violence", 1, EL_LUDUS, 6, "[On Use] Gain 2 Poise Potency\n       [On Use] Gain 2 Poise Count", effect_type="GAIN_POISE_SPECIAL", effect_val=2)
    id2 = Skill("Stun Baton", 2, EL_PHILAUTIA, 8, "[On Hit] Inflict 2 Bind\n       [On Hit] Inflict 2 Rupture Potency", effect_type="BIND_RUPTURE_SPECIAL_TYPE1", effect_val=2)
    id3 = Skill("Discipline", 3, EL_EROS, 10, "[On Use] Gain 4 Poise Potency\n       [On Use] Gain 4 Poise Count", effect_type="GAIN_POISE_SPECIAL", effect_val=4)
    k_inf_disc.skill_pool_def = [(id1, 3), (id2, 3), (id3, 3)]
    inf_disc.equip_kata(k_inf_disc)
    inf_disc.description = "Wearing the iconic white kimono uniforms of Kasakura’s Disciplinary Committee, these impostors use the guise of authority to restrict access to the ship's lower levels. They wield standard-issue bokkens and stun batons with practiced cruelty, completely lacking the honorable resolve of Yuri's true subordinates. Their mimicry shatters the moment they clash with genuine fighters, easily falling to Benikawa and Shigemura's superior battle IQ and speed."
    inf_disc.unlock_stage_id = 34

    ####################################
    # --- HISAYUKI TADAMASA (BOSS) --- #
    ####################################

    hisayuki = Entity("Hisayuki Tadamasa", is_player=False)
    hisayuki.max_hp = 255
    k_hisayuki = Kata("Battering Ram", "Hisayuki", 1, 5, [1.2, 0.5, 0.5, 1.5, 1.0, 1.0, 1.0])
    hi1 = Skill("Following Orders", 1, EL_STORGE, 7, "[On Use] This unit takes -40% damage next turn\n       [On Hit] If this unit has Haste, gain 1 Bind next turn. Otherwise, gain 1 Haste next turn", effect_type="HISAYUKI_SPECIAL_1")
    hi2 = Skill("Pick Up Speed", 2, EL_LUDUS, 11, "[Combat Start] If this unit has Bind, take +50% damage for the turn\n       [On Hit] If this unit has no Haste, gain 3 Haste next turn, otherwise, gain 1 Haste next turn", effect_type="HISAYUKI_SPECIAL_2")
    hi3 = Skill("Human Battering Ram", 3, EL_EROS, 14, "[On Hit] If this unit has Haste, deal +10% damage for every stack of Haste on self (Max +50%), then remove all Haste on self", effect_type="HISAYUKI_SPECIAL_3")
    k_hisayuki.skill_pool_def = [(hi1, 4), (hi2, 2), (hi3, 2)]
    hisayuki.equip_kata(k_hisayuki)
    hisayuki.description = "Encountered in the bowels of the cruise ship, this terrifying combatant acts as an unstoppable, linear human battering ram to protect the weapon thieves. Despite possessing monstrous durability and the ability to accelerate into bone-crushing tackles, he speaks in robotic, military-style commands while humbly claiming to be just an 'ordinary student'. It took Shigemura absorbing his full-speed tackle to create a brief, desperate opening for the rest of the team to finally take him down."
    hisayuki.unlock_stage_id = 33

    ############################
    # --- MERCENARY NINJAS --- #
    ############################

    raven = Entity("Raven", is_player=False)
    raven.max_hp = 115
    k_raven = Kata("Shadow Assassin", "Raven", 1, 6, [1.0, 1.1, 1.1, 1.0, 1.2, 1.2, 1.5])
    rv1 = Skill("Silent Step", 1, EL_PHILAUTIA, 3, "[Combat Start] This unit takes -6 Final Damage this turn", effect_type="BUFF_DEF_FLAT", effect_val=6)
    rv2 = Skill("Blind Spot Strike", 2, EL_PRAGMA, 7, "[On Hit] Target will take +6 Final Damage from the next attack\n       [On Hit] Gain 4 Poise Potency\n       [On Hit] Gain 4 Poise Count", effect_type="RAVEN_SPECIAL_1")
    rv3 = Skill("Disorient", 3, EL_PHILAUTIA, 10, "[On Hit] Target deals -70% damage next turn\n       [On Hit] Gain 6 Poise Potency", effect_type="RAVEN_SPECIAL_2")
    k_raven.skill_pool_def = [(rv1, 4), (rv2, 2), (rv3, 3)]
    raven.equip_kata(k_raven)
    raven.description = "One of the three rogue ninja mercenaries hired to secure the cruise ship's massive weapons supply in the lower decks. Operating outside many iron rules of the honorable ninja code, Raven utilizes blistering speed, stealth, and lethal trickery to disorient the Kasakura team. His fluid, shadow-like movements make him a highly dangerous adversary in the narrow, dimly lit corridors of the ship."
    raven.unlock_stage_id = 35

    falcon = Entity("Falcon", is_player=False)
    falcon.max_hp = 113
    k_falcon = Kata("Aerial Assassin", "Falcon", 1, 6, [1.3, 1.0, 1.0, 1.0, 1.4, 1.0, 1.5])
    fa1 = Skill("Assault Flow", 1, EL_EROS, 5, "[On Hit] Target will take +4 Final Damage from the next attack", effect_type="ON_HIT_NEXT_TAKEN_FLAT", effect_val=4)
    fa2 = Skill("Aerial Strike", 2, EL_LUDUS, 9, "[On Use] If this unit does not have Haste, gain 3 Haste next turn\n       [On Hit] Inflict 4 Rupture Potency", effect_type="FALCON_SPECIAL_1")
    fa3 = Skill("Incapacitate", 3, EL_PHILAUTIA, 10, "[On Hit] Target deals -70% damage next turn\n       [On Hit] Gain 2 Haste next turn\n       [On Hit] Inflict 2 Bind next turn", effect_type="FALCON_SPECIAL_2")
    k_falcon.skill_pool_def = [(fa1, 3), (fa2, 3), (fa3, 3)]
    falcon.equip_kata(k_falcon)
    falcon.description = "Operating alongside Raven, Falcon is a highly skilled mercenary ninja who infiltrated the Goodwill Trip to oversee the underground weapon heist. He specializes in relentless, coordinated aerial assaults and precision strikes, attempting to overwhelm the Kasakura students before they can react. Unbound by traditional clan loyalties, he fights with a ruthless pragmatism that forces Benikawa and Shigemura to rely on their own deeply ingrained ninja training."
    falcon.unlock_stage_id = 36

    eagle = Entity("Eagle", is_player=False)
    eagle.max_hp = 60
    k_eagle = Kata("Veteran Assassin", "Eagle", 1, 6, [0.9, 1.1, 1.1, 0.9, 1.0, 1.8, 1.8])
    ea1 = Skill("Pressuring", 1, EL_PHILAUTIA, 7, "[On Hit] Target will take +5 Final Damage from the next attack\n       [On Hit] Target deals -50% damage next turn", effect_type="EAGLE_SPECIAL_1")
    ea2 = Skill("Under Control", 2, EL_PHILAUTIA, 6, "[On Use] Gain 3 Poise Potency\n       [On Use] Gain 3 Poise Count\n       [On Hit] Inflict 2 Rupture Potency\n       [On Hit] Inflict 5 Rupture Count", effect_type="EAGLE_SPECIAL_2")
    ea3 = Skill("Tactical Retreat", 3, EL_STORGE, 10, "[On Use] Deal 0 damage, heal this unit’s ally with the lowest HP by supposed final damage amount, then heal the rest of this unit’s allies by half the healed amount (can include self)\n       [On Use] All of this unit’s allies gain 3 Haste next turn", effect_type="EAGLE_SPECIAL_3")
    k_eagle.skill_pool_def = [(ea1, 2), (ea2, 4), (ea3, 3)]
    eagle.equip_kata(k_eagle)
    eagle.description = "The third and arguably most elusive member of the rogue ninja trio guarding the ship's Hazard Vault. Despite being leader and the most experienced of all three ninjas, neither Raven or Falcon respect him, and they often find themselves arguing constantly on the smallest of things. After participating in the desperate final clash against the Kasakura vanguard, he attempts a frantic escape through the ship's lower levels."
    eagle.unlock_stage_id = 37

    raven_inj = Entity("Raven (Injured)", is_player=False)
    raven_inj.max_hp = 49
    k_raven_inj = Kata("Cornered Shadow", "Raven", 1, 5, [1.1, 1.2, 1.2, 1.1, 1.3, 1.3, 1.6])
    rvi1 = Skill("Retreating Step", 1, EL_PHILAUTIA, 3, "[Combat Start] This unit takes -9 Final Damage this turn", effect_type="BUFF_DEF_FLAT", effect_val=9)
    rvi2 = Skill("Covering Squad", 2, EL_PHILIA, 8, "[On Use] All allied units of this unit take -4 Final Damage this turn", effect_type="AOE_BUFF_DEF_FLAT", effect_val=4)
    k_raven_inj.skill_pool_def = [(rvi1, 5), (rvi2, 4)]
    raven_inj.equip_kata(k_raven_inj)
    raven_inj.description = "Pushed to his limits by the Kasakura vanguard, this battered mercenary ninja makes a final, desperate stand inside the ship's Hazard Vault alongside Eagle. Despite suffering from severe exhaustion and blunt-force trauma from Yuri and Akasuke's heavy strikes, he fiercely pushes through the pain to forward his goals. His movements, though compromised and bleeding, are driven by the sheer, terrifying survival instincts of a cornered assassin."
    raven_inj.unlock_stage_id = 37

    falcon_inj = Entity("Falcon (Injured)", is_player=False)
    falcon_inj.max_hp = 53
    k_falcon_inj = Kata("Cornered Aerial", "Falcon", 1, 5, [1.4, 1.1, 1.1, 1.1, 1.5, 1.1, 1.6])
    fai1 = Skill("Opportunistic Flow", 1, EL_AGAPE, 4, "[On Hit] Target will take +3 Final Damage from the next attack", effect_type="ON_HIT_NEXT_TAKEN_FLAT", effect_val=3)
    fai2 = Skill("Point Out Weakness", 2, EL_EROS, 8, "[On Use] All of this unit’s allies deal +3 Final Damage for the turn", effect_type="AOE_BUFF_ATK_FLAT", effect_val=3)
    k_falcon_inj.skill_pool_def = [(fai1, 5), (fai2, 4)]
    falcon_inj.equip_kata(k_falcon_inj)
    falcon_inj.description = "Forced back into the Hazard Vault, this heavily wounded ninja refuses to surrender despite being systematically dismantled by Kasakura's fighters. Bleeding and relying on fractured weapons, his once-flawless aerial maneuvers are reduced to desperate, erratic lunges aimed at taking down at least one opponent with him. His ragged final stand ultimately serves as a grim testament to the lethal tenacity of the underworld's rogue mercenaries."
    falcon_inj.unlock_stage_id = 37

    #########################################
    # --- MISCELLANEOUS / EARLY RIPOSTE --- #
    #########################################

    hench = Entity("Unknown Faction Henchman", is_player=False)
    hench.max_hp = 75
    k_hench = Kata("Rapier Guard", "Henchman", 1, 3, [1.3, 1.1, 1.1, 1.1, 0.8, 0.8, 1.0])
    he1 = Skill("Pierce", 1, EL_LUDUS, 5, "[On Hit] Inflict 1 Pierce Fragility", effect_type="APPLY_STATUS")
    he1.status_effect = pierce_fragility_1
    he2 = Skill("Counter", 2, EL_EROS, 7, "[Combat Start] If this unit takes damage this turn, deal +20% damage next turn", effect_type="COUNTER_SKILL_TYPE1", effect_val=20)
    he3 = Skill("Brutal Counter", 3, EL_EROS, 8, "[Combat Start] If this unit takes damage this turn, deal +40% damage next turn\n       [On Hit] Inflict 2 Pierce Fragility", effect_type="COUNTER_SKILL_SPECIAL_TYPE1")
    k_hench.skill_pool_def = [(he1, 4), (he2, 3), (he3, 2)]
    hench.equip_kata(k_hench)
    hench.description = "These well-dressed captors guard Kagaku Shamiko’s hotel room, armed with thin rapiers and clad in identical sandy-colored long coats. Operating under strict orders not to harm their VIP prisoner, they become complacent and easily panicked when she fakes a choking emergency. This fatal hesitation allows a Kata-empowered Kagaku to swiftly dismantle them using nothing but a heavy silver breakfast tray and a broken broomstick."
    hench.unlock_stage_id = 38

    mascot = Entity("Deadly Laser Beam World-Threatening Monster", is_player=False)
    mascot.max_hp = 30
    k_mascot = Kata("Mascot Suit", "Monster", 1, 600, [1.0]*7)
    ma1 = Skill("“Thermal Laser Of Destruction”", 1, EL_AGAPE, 15520, "[Combat Start] Reduce this unit’s Kata Rift Aptitude to 0\n       [On Hit] Reduce Damage to 0", effect_type="JOKE_SKILL")
    ma2 = Skill("“Imprenetrable Armor Of The Abyssal Scale”", 2, EL_PRAGMA, 0, "[Combat Start] Reduce this unit’s Kata Rift Aptitude to 0\n       [Combat Start] This unit takes -12000 Final Damage from “Divine” element attacks\n       [Combat Start] This unit deals back %300 damage when taking “Darkness” element damage attacks")
    ma3 = Skill("“Roar Which Tears The Heavens”", 3, EL_EROS, 51000, "[Combat Start] Reduce this unit’s Kata Rift Aptitude to 0\n       [On Use] Targets all “Disbehaving Junior” units", effect_type="JOKE_SKILL")
    k_mascot.skill_pool_def = [(ma1, 3), (ma2, 3), (ma3, 3)]
    mascot.equip_kata(k_mascot)
    mascot.description = "Despite the terrifying title, this 'beast' is actually just an embarrassingly highly motivated Kasakura High senior sweating inside a cheap, goofy Godzilla mascot costume. Stationed in the tropical jungle during the island's Scavenger Hunt, he acts as the highly dramatic guardian of a marked coconut to test the students' teamwork. He possesses zero actual combat prowess, enthusiastically throwing himself to the ground in defeat after taking a single, slow-motion mock punch from Akasuke."
    mascot.unlock_stage_id = 39

    ####################################
    # --- THE RIPOSTE GANG (ACT 3) --- #
    ####################################

    rip_hench = Entity("Riposte Gang Henchman", is_player=False)
    rip_hench.max_hp = 55
    k_rip_hench = Kata("Gang Henchman Rapier", "Riposte Henchman", 1, 4, [1.2, 1.1, 1.1, 1.1, 0.9, 0.9, 1.1])
    rh1 = Skill("Graceful Pierce", 1, EL_LUDUS, 7, "[On Hit] Inflict 1 Pierce Fragility", effect_type="APPLY_STATUS")
    rh1.status_effect = pierce_fragility_1
    rh2 = Skill("Elegant Counter", 2, EL_AGAPE, 6, "[Combat Start] If this unit takes damage this turn, deal +30% damage next turn\n       [On Hit] Inflict 3 Pierce Fragility", effect_type="COUNTER_SKILL_SPECIAL_TYPE3")
    rh3 = Skill("Riposte", 3, EL_STORGE, 10, "[On Use] Gain 10 Riposte\n       [On Hit] If target has Pierce Fragility, gain 10 Riposte", effect_type="RIPOSTE_GAIN_SPECIAL_1")
    k_rip_hench.skill_pool_def = [(rh1, 4), (rh2, 3), (rh3, 2)]
    rip_hench.equip_kata(k_rip_hench)
    rip_hench.description = "The standard foot soldiers of the notorious Absconder syndicate, these ruthless thugs flood the hotel corridors in their signature sandy coats. They fight using a highly dangerous, sacrificial counter-attacking style, willingly absorbing heavy blunt force trauma just to create a split-second opening for a lethal rapier thrust. Their unnatural toughness and sheer numbers make them incredibly dangerous to fight recklessly, forcing the Kasakura vanguard to rely on flawless, one-hit knockouts."
    rip_hench.unlock_stage_id = 41

    rip_lead = Entity("Riposte Gang Squad Leader", is_player=False)
    rip_lead.max_hp = 75
    k_rip_lead = Kata("Veteran Henchman Rapier", "Riposte Leader", 1, 6, [1.1, 1.0, 1.0, 1.2, 0.9, 0.9, 1.0])
    rl1 = Skill("Stylish Vital Pierce", 1, EL_EROS, 9, "[On Hit] If target has Pierce Fragility, inflict 2 Pierce Fragility. Otherwise, inflict 1 Pierce Fragility", effect_type="PIERCE_FRAGILITY_INFLICT_SPECIAL_1")
    rl2 = Skill("Breakthrough", 2, EL_AGAPE, 9, "[Combat Start] All of this unit’s allies deal +4 Final Damage this turn\n       [On Use] Gain 10 Riposte\n       [On Hit] Inflict 2 Pierce Fragility", effect_type="RIPOSTE_SQUAD_LEADER_SPECIAL_1")
    rl3 = Skill("Balestra Riposte", 3, EL_LUDUS, 12, "[On Use] Fix this unit’s Riposte stack to 30\n       [On Hit] Inflict 3 Pierce Fragility", effect_type="RIPOSTE_SQUAD_LEADER_SPECIAL_2")
    k_rip_lead.skill_pool_def = [(rl1, 3), (rl2, 3), (rl3, 3)]
    rip_lead.equip_kata(k_rip_lead)
    rip_lead.description = "Seasoned veteran criminals of the underworld, these dark-coated enforcers lead the syndicate's defensive lines during the grueling hotel siege. Their rapier stances are significantly lower and more refined than the standard henchmen, allowing them to effortlessly parry and deliver devastating counter-strikes to vital points. Their overwhelming proficiency stalled the Kasakura strike team completely, forcing Akasuke to temporarily borrow their exact Kata just to beat them at their own ruthless game."
    rip_lead.unlock_stage_id = 41

    adam = Entity("Adam", is_player=False)
    adam.max_hp = 295
    k_adam = Kata("Executive Rapier", "Adam", 1, 9, [1.0, 1.0, 1.0, 1.15, 1.15, 1.0, 1.15])
    ad1 = Skill("En Garde", 1, EL_PRAGMA, 6, "[On Use] If this unit does not have Haste, gain 2 Haste next turn\n       [On Hit] Inflict 2 Pierce Fragility\n       [On Hit] Gain 10 Riposte", effect_type="ADAM_SPECIAL_1")
    ad2 = Skill("Advance-Lunge", 2, EL_LUDUS, 10, "[Combat Start] All of this unit’s allies deal +3 Final Damage this turn\n       [Combat Start] All of this unit’s allies take -2 Final Damage this turn\n       [On Hit] Gain 5 Riposte for every stack of Pierce Fragility the target has\n       [On Hit] Inflict 3 Pierce Fragility", effect_type="ADAM_SPECIAL_2")
    ad3 = Skill("Fleche Riposte (Incomplete)", 3, EL_LUDUS, 35, "[Combat Start] This unit takes +3 Final Damage this turn\n       [Combat Start] This unit deals -20 Base Damage this turn\n       [On Hit] Inflict 5 Pierce Fragility\n       [On Hit] Fix this unit’s Riposte stack to 50", effect_type="ADAM_SPECIAL_3")
    k_adam.skill_pool_def = [(ad1, 4), (ad2, 3), (ad3, 2)]
    adam.equip_kata(k_adam)
    adam.description = "A remarkably young and immensely talented Executive of the Riposte Gang, Adam flawlessly blends the grace of a high-class chef with the lethal precision of a master swordsman. He wields his rapier with terrifying perfection, capable of holding off six Kata-enhanced fighters simultaneously through sheer battle IQ and unnatural physical toughness before finally reaching his limit. Despite his criminal allegiance and composed demeanor, he possesses a surprisingly naive loyalty to his terrifying Boss and showed genuine, polite hospitality toward his captive."
    adam.unlock_stage_id = 42

    ########################################
    # --- YUNHAI BORDER GUARDS (ACT 4) --- #
    ########################################

    guard = Entity("Infiltrating Yunhai Border Guard", is_player=False)
    guard.max_hp = 62
    k_guard = Kata("Yunhai Guard", "Yunhai", 1, 1, [1.1, 0.8, 0.9, 1.2, 1.0, 1.0, 1.3])
    # Skill I: Metal Baton ◈◈
    s1_c1 = Chip(base_damage=2, effect_type="APPLY_STATUS")
    s1_c1.status_effect = scd.rupturecount_2
    s1_c2 = Chip(base_damage=3, effect_type="APPLY_STATUS")
    s1_c2.status_effect = scd.rupture_1
    s1_desc_brief = "[On Hit] Inflict Rupture Count\n       [On Hit] Inflict Rupture Potency"
    s1_desc_inspect = "◈ Base Damage: 2\n       [On Hit] Inflict 2 Rupture Count\n       ◈ Base Damage: 3\n       [On Hit] Inflict 1 Rupture Potency"
    g_s1 = ChipSkill("Metal Baton ◈◈", 1, EL_AGAPE, [s1_c1, s1_c2], description=s1_desc_brief, inspect_description=s1_desc_inspect)
    # Skill II: Pinning ◈◈
    s2_c1 = Chip(base_damage=5, effect_type="RUPTURE_DAMAGE_BUFF_TYPE2", effect_val=2)
    s2_c2 = Chip(base_damage=1, effect_type="APPLY_STATUS")
    s2_c2.status_effect = scd.rupture_2
    s2_desc_brief = "[On Hit] Inflict Rupture Potency\n       [On Hit] If target has Rupture, deal +Final Damage"
    s2_desc_inspect = "◈ Base Damage: 5\n       [On Hit] If target has Rupture, deal +2 Final Damage\n       ◈ Base Damage: 1\n       [On Hit] Inflict 2 Rupture Potency"
    g_s2 = ChipSkill("Pinning ◈◈", 2, EL_STORGE, [s2_c1, s2_c2], description=s2_desc_brief, inspect_description=s2_desc_inspect)
    k_guard.skill_pool_def = [(g_s1, 4), (g_s2, 4)]
    guard.equip_kata(k_guard)
    guard.description = "infiltratingyunhaiborderguarddesc"
    guard.unlock_stage_id = 49

    guard_leader = Entity("Infiltrating Yunhai Border Guard Leader", is_player=False)
    guard_leader.max_hp = 90
    k_guard_leader = Kata("Yunhai Guard Leader", "Yunhai", 2, 2, [1.2, 0.6, 0.6, 1.3, 1.3, 1.3, 1.2])
    # Skill I: Heavy Metal Baton ◈◈
    s1_c1 = Chip(base_damage=4, effect_type="APPLY_STATUS")
    s1_c1.status_effect = scd.rupturecount_2
    s1_c2 = Chip(base_damage=5, effect_type="APPLY_STATUS")
    s1_c2.status_effect = scd.rupturecount_2
    s1_desc_brief = "[On Hit] Inflict Rupture Count"
    s1_desc_inspect = "◈ Base Damage: 4\n       [On Hit] Inflict 2 Rupture Count\n       ◈ Base Damage: 5\n       [On Hit] Inflict 2 Rupture Count"
    gl_s1 = ChipSkill("Heavy Metal Baton ◈◈", 1, EL_AGAPE, [s1_c1, s1_c2], description=s1_desc_brief, inspect_description=s1_desc_inspect)
    # Skill II: Takedown ◈◈◈
    s2_c1 = Chip(base_damage=7, effect_type="RUPTURE_DAMAGE_BUFF_TYPE2", effect_val=3)
    s2_c2 = Chip(base_damage=2, effect_type="BLEED_RUPTURE_SPECIAL_TYPE1", effect_val=1)
    s2_c3 = Chip(base_damage=2, effect_type="BLEED_RUPTURE_SPECIAL_TYPE1", effect_val=1)
    s2_desc_brief = "[On Hit] Inflict Rupture Potency\n       [On Hit] Inflict Bleed Potency\n       [On Hit] If target has Rupture, deal +Final Damage"
    s2_desc_inspect = "◈ Base Damage: 7\n       [On Hit] If target has Rupture, deal +3 Final Damage\n       ◈ Base Damage: 2\n       [On Hit] Inflict 1 Bleed Potency\n       [On Hit] Inflict 1 Rupture Potency\n       ◈ Base Damage: 2\n       [On Hit] Inflict 1 Bleed Potency\n       [On Hit] Inflict 1 Rupture Potency"
    gl_s2 = ChipSkill("Takedown ◈◈◈", 2, EL_EROS, [s2_c1, s2_c2, s2_c3], description=s2_desc_brief, inspect_description=s2_desc_inspect)
    # Skill III: Lightweight Armor
    gl_s3 = Skill("Lightweight Armor", 3, EL_LUDUS, 0, "[Combat Start] This unit takes -3 Final Damage this turn\n       [Combat Start] Gain 3 Haste next turn", effect_type="LIGHTWEIGHT_SPECIAL", effect_val=3)
    k_guard_leader.skill_pool_def = [(gl_s1, 3), (gl_s2, 3), (gl_s3, 2)]
    guard_leader.equip_kata(k_guard_leader)
    guard_leader.description = "infiltratingyunhaiborderguardleaderdesc"
    guard_leader.unlock_stage_id = 50

    #######################################
    # --- LUOXIA MARTIAL ARTS (ACT 4) --- #
    #######################################

    luoxia_student = Entity("Luoxia Martial Arts Practitioner Student", is_player=False)
    luoxia_student.max_hp = 51
    luoxia_student.pace = 2
    k_luoxia = Kata("Luoxia Arts", "Luoxia", 1, 1, [1.3, 1.4, 1.5, 0.9, 1.3, 1.4, 1.4])
    # Skill I ◈◈
    ls_s1_c1 = Chip(base_damage=3)
    ls_s1_c2 = Chip(base_damage=3)
    ls_s1_desc_inspect = "◈ Base Damage: 3\n       ◈ Base Damage: 3"
    ls_s1 = ChipSkill("Palm Heel Strike ◈◈", 1, EL_PHILIA, [ls_s1_c1, ls_s1_c2], inspect_description=ls_s1_desc_inspect)
    # Skill II ◈◈
    ls_s2_c1 = Chip(base_damage=3, effect_type="RUPTURE_BUFF_DEF_SPECIAL_1")
    ls_s2_c2 = Chip(base_damage=3, effect_type="RUPTURE_BUFF_DEF_SPECIAL_2")
    ls_s2_desc_brief = "[Combat Start] Take -2 Final Damage this turn\n       [On Hit] Take -Final Damage next turn\n       [On Hit] Inflict Rupture Potency\n       [On Hit] Inflict Rupture Count"
    ls_s2_desc_inspect = "[Combat Start] Take -2 Final Damage this turn\n       ◈ Base Damage: 3\n       [On Hit] Take -1 Final Damage next turn\n       [On Hit] Inflict 2 Rupture Potency\n       ◈ Base Damage: 3\n       [On Hit] Take -1 Final Damage next turn\n       [On Hit] Inflict 2 Rupture Count"
    ls_s2 = ChipSkill("Outward Block ◈◈", 2, EL_STORGE, [ls_s2_c1, ls_s2_c2], description=ls_s2_desc_brief, inspect_description=ls_s2_desc_inspect, effect_type="BUFF_DEF_FLAT", effect_val=2)
    # Skill III
    ls_s3_desc = "[On Use] Gain 3 Poise Count\n       [On Hit] Gain 3 Poise Potency\n       [On Hit] Inflict 3 Rupture Potency"
    ls_s3 = Skill("Centerline Punch", 3, EL_STORGE, 10, ls_s3_desc, effect_type="POISE_RUPTURE_SPECIAL_TYPE1", effect_val=3)
    k_luoxia.skill_pool_def = [(ls_s1, 5), (ls_s2, 2), (ls_s3, 2)]
    luoxia_student.equip_kata(k_luoxia)
    luoxia_student.description = "luoxiamartialartspractitionerstudent"
    luoxia_student.unlock_stage_id = 52

    #################################
    # --- NATSUME? (ACT 4 BOSS) --- #
    #################################
    natsume = Entity("Natsume(?)", is_player=False)
    natsume.max_hp = 333
    natsume.pace = 4
    k_natsume = Kata("Strange Kata", "Natsume?", 1, 16, [1.3, 1.1, 1.1, 1.1, 1.1, 1.1, 1.3])
    # Skill I: Chop / Split [劈] ◈◈◈
    n_s1_c1 = Chip(base_damage=10, effect_type="NATSUME_STRANGE_SPECIAL_1")
    n_s1_c2 = Chip(base_damage=20, effect_type="NATSUME_STRANGE_SPECIAL_2")
    n_s1_c3 = Chip(base_damage=20, effect_type="NATSUME_STRANGE_SPECIAL_2")
    n_s1_desc = "[On Use] Gain Poise Count\n       [On Hit] Inflict Rupture Potency\n       [On Hit] Inflict Rupture Count"
    n_s1_insp = "◈ Base Damage: 10\n       [On Use] Base Damage -80%\n       [On Use] Gain 2 Poise Count\n       [On Hit] Inflict 3 Rupture Count\n       ◈ Base Damage: 20\n       [On Use] Base Damage -80%\n       [On Use] Gain 1 Poise Count\n       [On Hit] Inflict 1 Rupture Potency\n       ◈ Base Damage: 20\n       [On Use] Base Damage -80%\n       [On Use] Gain 1 Poise Count\n       [On Hit] Inflict 1 Rupture Potency"
    n_s1 = ChipSkill("Chop / Split [劈] ◈◈◈", 1, EL_PHILAUTIA, [n_s1_c1, n_s1_c2, n_s1_c3], description=n_s1_desc, inspect_description=n_s1_insp)
    # Skill II: Frost Moon Slice [霜月斬] ◈◈◈◈
    n_s2_c1 = Chip(base_damage=16, effect_type="NATSUME_STRANGE_SPECIAL_3")
    n_s2_c2 = Chip(base_damage=16, effect_type="NATSUME_STRANGE_SPECIAL_4")
    n_s2_c3 = Chip(base_damage=16, effect_type="NATSUME_STRANGE_SPECIAL_4")
    n_s2_c4 = Chip(base_damage=16, effect_type="NATSUME_STRANGE_SPECIAL_4")
    n_s2_desc = "[On Use] Gain Bind next turn\n       [On Hit] Inflict Sinking Potency\n       [On Hit] Inflict Sinking Count"
    n_s2_insp = "◈ Base Damage: 16\n       [On Use] Base Damage -80%\n       [On Use] Gain 1 Bind next turn\n       [On Hit] Inflict 5 Sinking Count\n       ◈ Base Damage: 16\n       [On Use] Base Damage -80%\n       [On Hit] Inflict 1 Sinking Potency\n       ◈ Base Damage: 16\n       [On Use] Base Damage -80%\n       [On Hit] Inflict 1 Sinking Potency\n       ◈ Base Damage: 16\n       [On Use] Base Damage -80%\n       [On Hit] Inflict 1 Sinking Potency"
    n_s2 = ChipSkill("Frost Moon Slice [霜月斬] ◈◈◈◈", 2, EL_LUDUS, [n_s2_c1, n_s2_c2, n_s2_c3, n_s2_c4], description=n_s2_desc, inspect_description=n_s2_insp)
    # Skill III: Star Fall Thrust [墜星刺] ◈◈◈◈
    n_s3_c1 = Chip(base_damage=100, effect_type="NATSUME_STRANGE_SPECIAL_5")
    n_s3_c2 = Chip(base_damage=34, effect_type="NATSUME_STRANGE_SPECIAL_6")
    n_s3_c3 = Chip(base_damage=34, effect_type="NATSUME_STRANGE_SPECIAL_5")
    n_s3_c4 = Chip(base_damage=34, effect_type="NATSUME_STRANGE_SPECIAL_6")
    n_s3_desc = "[On Use] Gain Bind next turn\n       [On Use] Gain Poise Count\n       [On Use] Gain Poise Potency\n       [On Hit] Inflict Rupture Potency\n       [On Hit] Inflict Sinking Potency"
    n_s3_insp = "◈ Base Damage: 100\n       [On Use] Base Damage -85%\n       [On Use] Gain 1 Bind next turn\n       [On Use] Gain 2 Poise Potency\n       [On Use] Gain 2 Poise Count\n       [On Hit] Inflict 2 Sinking Potency\n       ◈ Base Damage: 34\n       [On Use] Base Damage -85%\n       [On Use] Gain 2 Poise Potency\n       [On Use] Gain 2 Poise Count\n       [On Hit] Inflict 2 Rupture Potency\n       ◈ Base Damage: 34\n       [On Use] Base Damage -85%\n       [On Use] Gain 1 Bind next turn\n       [On Use] Gain 2 Poise Potency\n       [On Use] Gain 2 Poise Count\n       [On Hit] Inflict 2 Sinking Potency\n       ◈ Base Damage: 34\n       [On Use] Base Damage -85%\n       [On Use] Gain 2 Poise Potency\n       [On Use] Gain 2 Poise Count\n       [On Hit] Inflict 2 Rupture Potency"
    n_s3 = ChipSkill("Star Fall Thrust [墜星刺] ◈◈◈◈", 3, EL_PRAGMA, [n_s3_c1, n_s3_c2, n_s3_c3, n_s3_c4], description=n_s3_desc, inspect_description=n_s3_insp)
    k_natsume.skill_pool_def = [(n_s1, 3), (n_s2, 2), (n_s3, 2)]
    natsume.equip_kata(k_natsume)
    natsume.description = "natsumestrangekatadescription"
    natsume.unlock_stage_id = 53

    ######################################
    # --- GOLDEN FIST UNION (ACT 4) --- #
    ######################################
    gf_gangster = Entity("Golden Fist Union Gangster", is_player=False)
    gf_gangster.max_hp = 30
    gf_gangster.pace = 1
    k_gfg = Kata("Golden Fist Thug", "Golden Fist", 1, 2, [1.6, 1.0, 1.0, 1.5, 1.5, 1.5, 1.6])
    gfg_s1 = Skill("Gilded Hands", 1, EL_STORGE, 6, "[On Hit] Inflict 2 Bleed Potency\n       [On Hit] Inflict 2 Bleed Count", effect_type="APPLY_BLEED_HEAVY_STACKS")
    gfg_s2 = Skill("Beatdown", 2, EL_STORGE, 8, "[On Hit] If target has Rupture, deal +3 Final Damage", effect_type="RUPTURE_DAMAGE_BUFF_TYPE2", effect_val=3)
    k_gfg.skill_pool_def = [(gfg_s1, 4), (gfg_s2, 4)]
    gfg_p1 = Passive("For The Golden Fist", "When attacking, if target has Bleed, deal +2 Final Damage", "PASSIVE_GOLDEN_FIST", 2, color="yellow")
    k_gfg.passives.append(gfg_p1)
    gf_gangster.equip_kata(k_gfg)
    gf_gangster.description = "goldenfistuniongangsterdescription"
    gf_gangster.unlock_stage_id = 56
    
    gf_leader = Entity("Golden Fist Union Gangster Leader", is_player=False)
    gf_leader.max_hp = 50
    gf_leader.pace = 1
    k_gfl = Kata("Golden Fist Leader", "Golden Fist Leader", 1, 2, [1.7, 1.0, 0.9, 1.4, 1.4, 1.4, 1.7])
    gfl_s1 = Skill("Gilded Grapple", 1, EL_STORGE, 8, "[On Hit] Inflict 2 Bleed Potency\n       [On Hit] Inflict 2 Bleed Count\n       [On Hit] Inflict 2 Rupture Potency\n       [On Hit] Inflict 2 Rupture Count", effect_type="APPLY_BLEED_RUPTURE_HEAVY_STACKS")
    gfl_s2 = Skill("Heavy Beatdown", 2, EL_EROS, 10, "[On Hit] If target has Rupture, deal +3 Final Damage\n       [On Hit] Inflict 3 Rupture Count", effect_type="RUPTURE_BUFF_AND_COUNT_SPECIAL", effect_val=3)
    gfl_s3 = Skill("Flashy Gear", 3, EL_STORGE, 0, "[Combat Start] This unit takes -8 Final Damage this turn\n       [Combat Start] All of this unit’s allies from “Golden Fist Union” deal +4 Final Damage this turn (this effect cannot stack)\n       [On Use] Gain 5 Bind next turn", effect_type="GOLDEN_FIST_SPECIAL")
    k_gfl.skill_pool_def = [(gfl_s1, 3), (gfl_s2, 3), (gfl_s3, 2)]
    # Assign Passives
    gfl_p1 = Passive("For The Golden Fist", "When attacking, if target has Bleed, deal +2 Final Damage", "PASSIVE_GOLDEN_FIST", 2, color="yellow")
    gfl_p2 = Passive("Crude Command", "When this unit is present, all of this unit’s allies from “Golden Fist Union” take -2 Final Damage from attacks (does not stack)", "PASSIVE_CRUDE_COMMAND", 2, color="yellow")
    k_gfl.passives.extend([gfl_p1, gfl_p2])
    gf_leader.equip_kata(k_gfl)
    gf_leader.description = "goldenfistuniongangsterleaderdescription"
    gf_leader.unlock_stage_id = 56

    ####################################
    # --- BLACK WATER DOCK (ACT 4) --- #
    ####################################
    bw_gangster = Entity("Black Water Dock Gangster", is_player=False)
    bw_gangster.max_hp = 45
    bw_gangster.pace = 1
    k_bw = Kata("Dock Gangster Arts", "Black Water Dock", 1, 2, [1.1, 1.5, 1.5, 1.0, 1.6, 1.0, 1.3])
    # Skill I
    bw_s1_desc = "[On Use] If this unit has Poise, gain 3 Poise Potency\n       [On Hit] Gain 3 Poise Count\n       [On Hit] Inflict 3 Rupture Potency"
    bw_s1 = Skill("Close Quarters Combat", 1, EL_PRAGMA, 5, bw_s1_desc, effect_type="POISE_RUPTURE_SPECIAL_TYPE2", effect_val=3)
    # Skill II
    bw_s2_desc = "[On Hit] Inflict 1 Rupture Potency\n       [On Hit] If this unit has Poise, inflict 1 Paralysis\n       [On Hit] Inflict 1 Paralysis"
    bw_s2 = Skill("Shocking Spearplay", 2, EL_LUDUS, 10, bw_s2_desc, effect_type="RUPTURE_PARALYSIS_SPECIAL_TYPE1", effect_val=1)
    k_bw.skill_pool_def = [(bw_s1, 4), (bw_s2, 4)]
    # Passive
    bw_p1 = Passive("The Dock’s Spearplay", "When attacking, if target has Paralysis, inflict 1 Rupture Potency", "PASSIVE_DOCK_SPEARPLAY", 1, color="blue")
    k_bw.passives.append(bw_p1)
    bw_gangster.equip_kata(k_bw)
    bw_gangster.description = "blackwaterdockgangster"
    bw_gangster.unlock_stage_id = 57

    bw_leader = Entity("Black Water Dock Gangster Leader", is_player=False)
    bw_leader.max_hp = 63
    bw_leader.pace = 1
    k_bw_leader = Kata("Dock Leader Arts", "Black Water Dock Leader", 1, 2, [1.0, 1.3, 1.3, 1.0, 1.7, 1.0, 1.2])
    # Skill I
    bw_l_s1_desc = "[On Hit] Gain 2 Poise Count\n       [On Hit] Gain 2 Poise Potency\n       [On Hit] Gain 2 Haste next turn"
    bw_l_s1 = Skill("Unreachable Footwork", 1, EL_LUDUS, 5, bw_l_s1_desc, effect_type="POISE_HASTE_SPECIAL_TYPE1", effect_val=2)
    # Skill II
    bw_l_s2_desc = "[On Hit] Inflict 2 Rupture Count\n       [On Hit] Inflict 2 Rupture Potency\n       [On Hit] Inflict 2 Paralysis"
    bw_l_s2 = Skill("Paralyzing Spearplay", 2, EL_PHILAUTIA, 11, bw_l_s2_desc, effect_type="RUPTURE_PARALYSIS_SPECIAL_TYPE2", effect_val=2)
    # Skill III
    bw_l_s3_desc = "[On Hit] Deal +3 Base Damage for every stack of Paralysis the target has (Max +15 Base Damage)\n       [On Hit] Inflict 3 Paralysis"
    bw_l_s3 = Skill("Heart Point", 3, EL_AGAPE, 4, bw_l_s3_desc, effect_type="PARALYSIS_SPECIAL_TYPE1", effect_val=3)
    k_bw_leader.skill_pool_def = [(bw_l_s1, 3), (bw_l_s2, 3), (bw_l_s3, 3)]
    # Passives
    bw_l_p1 = Passive("The Dock’s Spearplay", "When attacking, if target has Paralysis, inflict 1 Rupture Potency", "PASSIVE_DOCK_SPEARPLAY", 1, color="blue")
    bw_l_p2 = Passive("Returning Current", "When this unit gets hit, if attacker has Paralysis, inflict 2 Rupture Count", "PASSIVE_RETURNING_CURRENT", 2, color="blue")
    k_bw_leader.passives.extend([bw_l_p1, bw_l_p2])
    bw_leader.equip_kata(k_bw_leader)
    bw_leader.description = "blackwaterdockgangsterleader"
    bw_leader.unlock_stage_id = 57

    #######################################
    # --- TWIN MOUNTAIN GATE (ACT 4) --- #
    #######################################

    tmg_gangster = Entity("Twin Mountain Gate Gangster", is_player=False)
    tmg_gangster.max_hp = 43
    tmg_gangster.pace = 1
    k_tmg = Kata("Twin Axe Arts", "Twin Mountain Gate", 1, 2, [1.4, 1.5, 1.5, 1.5, 1.3, 1.4, 1.4])
    # Skill I ◈◈
    tmg_s1_c1 = Chip(base_damage=3, effect_type="APPLY_STATUS")
    tmg_s1_c1.status_effect = scd.bleed_3
    tmg_s1_c2 = Chip(base_damage=4, effect_type="APPLY_STATUS")
    tmg_s1_c2.status_effect = scd.rupture_3
    tmg_s1_desc_brief = "[On Hit] Inflict Bleed Potency\n       [On Hit] Inflict Rupture Potency"
    tmg_s1_desc_inspect = "◈ Base Damage: 3\n       [On Hit] Inflict 3 Bleed Potency\n       ◈ Base Damage: 4\n       [On Hit] Inflict 3 Rupture Potency"
    tmg_s1 = ChipSkill("Twin Axe ◈◈", 1, EL_EROS, [tmg_s1_c1, tmg_s1_c2], description=tmg_s1_desc_brief, inspect_description=tmg_s1_desc_inspect)
    # Skill II ◈◈◈◈
    tmg_s2_c1 = Chip(base_damage=2, effect_type="BLEED_RUPTURE_SPECIAL_TYPE2")
    tmg_s2_c2 = Chip(base_damage=2, effect_type="BLEED_RUPTURE_SPECIAL_TYPE2")
    tmg_s2_c3 = Chip(base_damage=2, effect_type="BLEED_RUPTURE_SPECIAL_TYPE2")
    tmg_s2_c4 = Chip(base_damage=2, effect_type="RUMBLE_SPECIAL")
    tmg_s2_desc_brief = "[On Use] This unit takes +Final Damage next turn\n       [On Hit] Inflict Bleed Count\n       [On Hit] Inflict Rupture Count\n       [On Hit] Inflict Paralysis"
    tmg_s2_desc_inspect = "◈ Base Damage: 2\n       [On Hit] Inflict 1 Bleed Count\n       [On Hit] Inflict 2 Rupture Count\n       ◈ Base Damage: 2\n       [On Hit] Inflict 1 Bleed Count\n       [On Hit] Inflict 2 Rupture Count\n       ◈ Base Damage: 2\n       [On Hit] Inflict 1 Bleed Count\n       [On Hit] Inflict 2 Rupture Count\n       ◈ Base Damage: 2\n       [On Use] This unit takes +5 Final Damage next turn\n       [On Hit] Inflict 2 Paralysis"
    tmg_s2 = ChipSkill("Rumble ◈◈◈◈", 2, EL_EROS, [tmg_s2_c1, tmg_s2_c2, tmg_s2_c3, tmg_s2_c4], description=tmg_s2_desc_brief, inspect_description=tmg_s2_desc_inspect)
    k_tmg.skill_pool_def = [(tmg_s1, 4), (tmg_s2, 4)]
    tmg_p1 = Passive("Ruthlessness", "When attacking, deal +1 Base Damage for every chip used within this turn", "PASSIVE_RUTHLESSNESS", 1, color="red")
    k_tmg.passives.append(tmg_p1)
    tmg_gangster.equip_kata(k_tmg)
    tmg_gangster.description = "twinmountaingategangster"
    tmg_gangster.unlock_stage_id = 58

    tmg_leader = Entity("Twin Mountain Gate Gangster Leader", is_player=False)
    tmg_leader.max_hp = 55
    tmg_leader.pace = 1
    k_tmg_leader = Kata("Leader Axe Arts", "Twin Mountain Gate Leader", 1, 2, [1.4, 1.5, 1.5, 1.5, 1.6, 1.4, 1.4])
    # Skill I
    tmg_l_s1_desc = "[On Hit] Inflict 4 Bleed Potency"
    tmg_l_s1 = Skill("Double Axe", 1, EL_PHILIA, 8, tmg_l_s1_desc, effect_type="APPLY_STATUS")
    tmg_l_s1.status_effect = scd.bleed_4
    # Skill II ◈◈◈
    tmg_l_s2_c1 = Chip(base_damage=3, effect_type="BLEED_PARALYSIS_SPECIAL_TYPE1")
    tmg_l_s2_c2 = Chip(base_damage=3, effect_type="BLEED_PARALYSIS_SPECIAL_TYPE1")
    tmg_l_s2_c3 = Chip(base_damage=4, effect_type="BLEED_PARALYSIS_SPECIAL_TYPE2")
    tmg_l_s2_desc_brief = "[On Use] This unit takes +Final Damage next turn\n       [On Hit] Inflict Bleed Count\n       [On Hit] Inflict Paralysis"
    tmg_l_s2_desc_inspect = "◈ Base Damage: 3\n       [On Hit] Inflict 2 Bleed Count\n       [On Hit] Inflict 1 Paralysis\n       ◈ Base Damage: 3\n       [On Hit] Inflict 2 Bleed Count\n       [On Hit] Inflict 1 Paralysis\n       ◈ Base Damage: 4\n       [On Use] This unit takes +6 Final Damage next turn\n       [On Hit] Inflict 2 Bleed Count\n       [On Hit] Inflict 1 Paralysis"
    tmg_l_s2 = ChipSkill("Disable ◈◈◈", 2, EL_EROS, [tmg_l_s2_c1, tmg_l_s2_c2, tmg_l_s2_c3], description=tmg_l_s2_desc_brief, inspect_description=tmg_l_s2_desc_inspect)
    # Skill III ◈◈◈◈◈
    tmg_l_s3_c1 = Chip(base_damage=3, effect_type="APPLY_BLEED_HEAVY_STACKS")
    tmg_l_s3_c2 = Chip(base_damage=3, effect_type="BLEED_PARALYSIS_SPECIAL_TYPE1")
    tmg_l_s3_c3 = Chip(base_damage=3, effect_type="SWITCH_RANDOM_TYPE1")
    tmg_l_s3_c4 = Chip(base_damage=3, effect_type="APPLY_BLEED_HEAVY_STACKS")
    tmg_l_s3_c5 = Chip(base_damage=3, effect_type="BLEED_PARALYSIS_SPECIAL_TYPE1")
    tmg_l_s3_desc_brief = "[On Hit] Inflict Bleed Potency\n       [On Hit] Inflict Bleed Count\n       [On Hit] Inflict Paralysis\n       [On Hit] Switches to a new random target"
    tmg_l_s3_desc_inspect = "◈ Base Damage: 3\n       [On Hit] Inflict 2 Bleed Potency\n       [On Hit] Inflict 2 Bleed Count\n       ◈ Base Damage: 3\n       [On Hit] Inflict 2 Bleed Count\n       [On Hit] Inflict 1 Paralysis\n       ◈ Base Damage: 3\n       [On Hit] Switches to a new random target\n       ◈ Base Damage: 3\n       [On Hit] Inflict 2 Bleed Potency\n       [On Hit] Inflict 2 Bleed Count\n       ◈ Base Damage: 3\n       [On Hit] Inflict 2 Bleed Count\n       [On Hit] Inflict 1 Paralysis"
    tmg_l_s3 = ChipSkill("Frenzy ◈◈◈◈◈", 3, EL_EROS, [tmg_l_s3_c1, tmg_l_s3_c2, tmg_l_s3_c3, tmg_l_s3_c4, tmg_l_s3_c5], description=tmg_l_s3_desc_brief, inspect_description=tmg_l_s3_desc_inspect)
    k_tmg_leader.skill_pool_def = [(tmg_l_s1, 5), (tmg_l_s2, 2), (tmg_l_s3, 1)]
    tmg_l_p1 = Passive("Ruthlessness", "When attacking, deal +1 Base Damage for every chip used within this turn", "PASSIVE_RUTHLESSNESS", 1, color="red")
    tmg_l_p2 = Passive("Unpredictable", "Take -1 Final Damage for every chip used within this turn on the next turn", "PASSIVE_UNPREDICTABLE", 2, color="red")
    k_tmg_leader.passives.extend([tmg_l_p1, tmg_l_p2])
    tmg_leader.equip_kata(k_tmg_leader)
    tmg_leader.description = "twinmountaingategangsterleader"
    tmg_leader.unlock_stage_id = 58

    #############################
    # --- MIYU (ACT 4 BOSS) --- #
    #############################
    miyu = Entity("Miyu", is_player=False)
    miyu.max_hp = 1020
    miyu.pace = 3
    k_miyu = Kata("Wing Chun Arts", "Miyu", 1, 20, [0.9, 1.0, 1.0, 1.1, 0.9, 0.9, 1.0])
    # === ORIGINAL SKILL POOL ===
    # S1: Pak Sau [拍手]
    m_s1_desc_brief = "[On Use] Gain 3 Poise Count\n       [On Hit] Inflict 3 Rupture Potency"
    m_s1 = Skill("Pak Sau [拍手]", 1, EL_PRAGMA, 14, m_s1_desc_brief, effect_type="POISE_RUPTURE_SPECIAL_TYPE3", effect_val=3)
    # S2: Circling Hand [圈手] ◈◈
    m_s2_c1 = Chip(base_damage=8, effect_type="GAIN_POISE_SPECIAL_2")
    m_s2_c2 = Chip(base_damage=10, effect_type="APPLY_RUPTURE_SPECIAL_1")
    m_s2_desc = "[On Use] Gain Poise Potency\n       [On Use] Gain Poise Count\n       [On Hit] Inflict Rupture Potency\n       [On Hit] Inflict Rupture Count"
    m_s2_insp = "◈ Base Damage: 8\n       [On Use] Gain 3 Poise Potency\n       [On Use] Gain 2 Poise Count\n       ◈ Base Damage: 10\n       [On Hit] Inflict 3 Rupture Potency\n       [On Hit] Inflict 2 Rupture Count"
    m_s2 = ChipSkill("Circling Hand [圈手] ◈◈", 2, EL_LUDUS, [m_s2_c1, m_s2_c2], description=m_s2_desc, inspect_description=m_s2_insp)
    k_miyu.skill_pool_def = [(m_s1, 4), (m_s2, 3)]
    # === APPENDABLE TEMPORARY SKILLS ===
    # S3: Tan Sau [攤手]
    m_s3_desc = "[On Use] Gain 4 Poise Potency\n       [On Use] Gain 4 Poise Count\n       [On Hit] Inflict 4 Rupture Potency"
    m_s3 = Skill("Tan Sau [攤手]", 1, EL_EROS, 22, m_s3_desc, effect_type="POISE_RUPTURE_SPECIAL_TYPE1", effect_val=4)
    m_s3.is_temporary = True
    # S4: Lifting Hand [問手] ◈◈◈
    m_s4_c1 = Chip(base_damage=8, effect_type="GAIN_POISE_SPECIAL_3")
    m_s4_c2 = Chip(base_damage=8, effect_type="APPLY_RUPTURE_SPECIAL_2")
    m_s4_c3 = Chip(base_damage=10, effect_type="POISE_RUPTURE_SPECIAL_TYPE4")
    m_s4_desc = "[On Use] Gain Poise Potency\n       [On Use] Gain Poise Count\n       [On Hit] Inflict Rupture Potency\n       [On Hit] Inflict Rupture Count\n       [On Hit] Switches to a new random target"
    m_s4_insp = "◈ Base Damage: 8\n       [On Use] Gain 4 Poise Potency\n       [On Use] Gain 3 Poise Count\n       [On Hit] Switches to a new random target\n       ◈ Base Damage: 8\n       [On Hit] Inflict 4 Rupture Potency\n       [On Hit] Inflict 2 Rupture Count\n       [On Hit] Switches to a new random target\n       ◈ Base Damage: 10\n       [On Use] Gain 4 Poise Potency\n       [On Use] Gain 6 Poise Count\n       [On Hit] Inflict 4 Rupture Potency\n       [On Hit] Inflict 4 Rupture Count"
    m_s4 = ChipSkill("Lifting Hand [問手] ◈◈◈", 2, EL_EROS, [m_s4_c1, m_s4_c2, m_s4_c3], description=m_s4_desc, inspect_description=m_s4_insp)
    m_s4.is_temporary = True
    for c in m_s4.chips: c.is_temporary = True
    # S5: Question Mark Kick [問號踢] ◈◈◈
    m_s5_c1 = Chip(base_damage=15, effect_type="MIYU_SPECIAL_1")
    m_s5_c2 = Chip(base_damage=15, effect_type="MIYU_SPECIAL_2")
    m_s5_c3 = Chip(base_damage=20, effect_type="APPLY_STATUS")
    m_s5_c3.status_effect = scd.paralysis_5
    m_s5_desc = "[Combat Start] Deal +[(Pace-2)*10]% Base Damage with all skills this turn\n       [Combat Start] Take +[8+(Pace-3)] Final Damage for this turn\n       [On Use] Gain Poise Potency\n       [On Use] Gain Poise Count\n       [On Hit] Inflict Paralysis\n       [On Hit] Switches to a new random target (Prioritizes units without Paralysis)"
    m_s5_insp = "◈ Base Damage: 15\n       [On Use] Gain 7 Poise Potency\n       [On Use] Gain 2 Poise Count\n       [On Hit] Inflict 2 Paralysis\n       [On Hit] Switches to a new random target (Prioritizes units without Paralysis)\n       ◈ Base Damage: 15\n       [On Use] Gain 4 Poise Potency\n       [On Use] Gain 4 Poise Count\n       [On Hit] Inflict 3 Paralysis\n       [On Hit] Switches to a new random target (Prioritizes units without Paralysis)\n       ◈ Base Damage: 20\n       [On Hit] Inflict 5 Paralysis"
    m_s5 = ChipSkill("Question Mark Kick [問號踢] ◈◈◈", 3, EL_EROS, [m_s5_c1, m_s5_c2, m_s5_c3], description=m_s5_desc, inspect_description=m_s5_insp, effect_type="MIYU_S5_COMBAT_START")
    m_s5.is_temporary = True
    for c in m_s5.chips: c.is_temporary = True
    # === PASSIVES ===
    m_p1 = Passive("Wing Chun [詠春]", "Tally amount of Critical Hits this unit performs throughout battle. Append these skills randomly into Skill Pool when the Tally reaches the following numbers:\n2 Critical Hits – ‘Tan Sau [攤手]’\n4 Critical Hits – ‘Lifting Hand [問手]’\n7 Critical Hits – ‘Question Mark Kick [問號踢]’\nAfter reaching 7 Critical Hits, immediately reset the Tally.", "PASSIVE_WING_CHUN", 1, color="pale_turquoise1")
    m_p2 = Passive("Acceleration [加速度]", "At start of turn, convert all Poise Potency and Poise Count and add to Acceleration Potency and Acceleration Count, respectively. Then, if this unit has 30 [Acceleration Potency+Count], remove all Acceleration, Pick Up 1 Pace, and gain 1 Overheat. This effect can occur 3 times\nIf this unit already has 6+ Pace, instead, remove 70% of Acceleration Potency and Acceleration Count each, then gain 2 Overheat.", "PASSIVE_ACCELERATION", 2, color="pale_turquoise1")
    m_p3 = Passive("Impediment - Severed Arm [障礙－斷臂]", "Deal -50% Final Damage with attacks\nTake 200% Final Damage from attacks", "PASSIVE_SEVERED_ARM", 3, color="grey74")
    k_miyu.passives.extend([m_p1, m_p2, m_p3])
    miyu.equip_kata(k_miyu)
    miyu.description = "miyudescription"
    miyu.unlock_stage_id = 62
    miyu.appendable_skills = {2: m_s3, 4: m_s4, 7: m_s5}

    ############################
    # --- MEI (ACT 4 BOSS) --- #
    ############################
    mei = Entity("Mei", is_player=False)
    mei.max_hp = 114
    mei.pace = 2
    k_mei = Kata("Mei Arts", "Mei", 1, 14, [1.0, 1.1, 1.0, 1.0, 1.2, 1.0, 1.2])
    # Skill I: Stab / Thrust [刺] (Ludus)
    mei_s1_desc = "[On Use] Gain 8 Poise Potency\n       [On Use] Gain 8 Poise Count"
    mei_s1 = Skill("Stab / Thrust [刺]", 1, EL_LUDUS, 6, mei_s1_desc, effect_type="GAIN_POISE_SPECIAL", effect_val=8)
    # Skill II: White Crane [白鹤] ◈◈◈ (Storge)
    mei_s2_c1 = Chip(base_damage=4, effect_type="MEI_SPECIAL_1")
    mei_s2_c2 = Chip(base_damage=4, effect_type="MEI_SPECIAL_2")
    mei_s2_c3 = Chip(base_damage=7, effect_type="MEI_SPECIAL_3")
    mei_s2_desc = "[On Critical Hit] Inflict Rupture Potency\n       [On Critical Hit] Inflict Rupture Count\n       [On Critical Hit] Inflict Paralysis\n       [On Critical Hit] Gain Haste\n       [On Hit] Switches to a new random target"
    mei_s2_insp = "◈ Base Damage: 4\n       [On Critical Hit] Gain 1 Haste next turn\n       [On Critical Hit] Inflict 2 Rupture Potency\n       [On Critical Hit] Inflict 2 Rupture Count\n       [On Hit] Switches to a new random target\n       ◈ Base Damage: 4\n       [On Critical Hit] Gain 1 Haste next turn\n       [On Critical Hit] Inflict 3 Paralysis\n       [On Hit] Switches to a new random target\n       ◈ Base Damage: 7\n       [On Critical Hit] Inflict 2 Rupture Potency\n       [On Critical Hit] Inflict 2 Rupture Count\n       [On Critical Hit] Inflict 3 Paralysis"
    mei_s2 = ChipSkill("White Crane [白鹤] ◈◈◈", 2, EL_STORGE, [mei_s2_c1, mei_s2_c2, mei_s2_c3], description=mei_s2_desc, inspect_description=mei_s2_insp)
    # Skill III: Sparrow Skims Over Water [燕子抄水] ◈◈◈◈ (Pragma)
    mei_s3_c1 = Chip(base_damage=5, effect_type="MEI_SPECIAL_4")
    mei_s3_c2 = Chip(base_damage=5, effect_type="MEI_SPECIAL_4")
    mei_s3_c3 = Chip(base_damage=1, effect_type="MEI_SPECIAL_5")
    mei_s3_c4 = Chip(base_damage=7, effect_type="APPLY_STATUS_CRITICAL")
    mei_s3_c4.status_effect = scd.paralysis_7
    mei_s3_desc = "[On Critical Hit] Gain Poise Potency\n       [On Critical Hit] Gain Poise Count\n       [On Critical Hit] Inflict Paralysis\n       [On Hit] Switches to a new random target (Prioritizes units without Paralysis)"
    mei_s3_insp = "◈ Base Damage: 5\n       [On Critical Hit] Gain 4 Poise Potency\n       [On Critical Hit] Gain 4 Poise Count\n       [On Critical Hit] Inflict 2 Paralysis\n       [On Hit] Switches to a new random target (Prioritizes units without Paralysis)\n       ◈ Base Damage: 5\n       [On Critical Hit] Gain 4 Poise Potency\n       [On Critical Hit] Gain 4 Poise Count\n       [On Critical Hit] Inflict 2 Paralysis\n       [On Hit] Switches to a new random target (Prioritizes units without Paralysis)\n       ◈ Base Damage: 1\n       [On Critical Hit] Gain 8 Poise Potency\n       [On Critical Hit] Inflict 3 Paralysis\n       [On Hit] Switches to a new random target (Prioritizes units without Paralysis)\n       ◈ Base Damage: 7\n       [On Critical Hit] Inflict 7 Paralysis"
    mei_s3 = ChipSkill("Sparrow Skims Over Water [燕子抄水] ◈◈◈◈", 3, EL_PRAGMA, [mei_s3_c1, mei_s3_c2, mei_s3_c3, mei_s3_c4], description=mei_s3_desc, inspect_description=mei_s3_insp)
    # Skill IV: Parting The Grass To Seek The Snake [拨草寻蛇] (Agape)
    mei_s4 = Skill("Parting The Grass To Seek The Snake [拨草寻蛇]", 4, EL_AGAPE, 5, "[On Critical Hit] Gain 1 Cloud Sword [云]", effect_type="APPLY_STATUS_CRITICAL")
    mei_s4.status_effect = scd.cloud_sword_1
    k_mei.skill_pool_def = [(mei_s1, 8), (mei_s2, 2), (mei_s3, 2), (mei_s4, 4)]
    # Passives
    mei_p1 = Passive("Breathing Techniques", "This unit’s max Poise Potency and Count stack count are fixed at 30/30. At the start of turn, convert any Poise Potency and Count over 20 into healing each", "PASSIVE_BREATHING_TECHNIQUES", color="pale_turquoise1")
    mei_p2 = Passive("Enforcement", "Tally amount of Critical Hits this unit performs throughout battle (Max 3). At the start of turn, reset the Tally\nEvery Critical Hit this unit lands grants one of the following buffs at random:\nDeal +(Current Tally) Final Damage next turn\nTake -(Current Tally) Final Damage from attacks next turn\nThis effect can occur 4 times per turn. Gained buffs can stack", "PASSIVE_ENFORCEMENT", color="light_salmon1")
    mei_p3 = Passive("Ingrained Command", "This unit’s max Paralysis stack count is fixed at 1. At the start of every second turn, gain 1 Paralysis. If this unit has Paralysis, take -50% Final Damage from attacks", "PASSIVE_INGRAINED_COMMAND", color="sea_green1")
    k_mei.passives.extend([mei_p1, mei_p2, mei_p3])
    mei.equip_kata(k_mei)
    mei.description = "meidescription"
    mei.unlock_stage_id = 63

    ################################################
    # --- BLOOD-BROKEN GUARD FOOTSOLDIER (ACT 4) ---
    ################################################
    bb_foot = Entity("Blood-Broken Guard Footsoldier", is_player=False)
    bb_foot.max_hp = 37
    bb_foot.pace = 1
    k_bb = Kata("Blood-Broken Kata", "Guard Footsoldier", 1, 8, [0.4, 1.2, 1.2, 1.2, 1.2, 1.2, 1.2])
    # Skill I: Polearm Thrust ◈◈ (Eros)
    bb_s1_c1 = Chip(base_damage=4, effect_type="POISE_BLEED_SPECIAL_TYPE1", effect_val=2)
    bb_s1_c2 = Chip(base_damage=4, effect_type="POISE_BLEED_SPECIAL_TYPE1", effect_val=2)
    bb_s1_desc = "[On Hit] Inflict Bleed Potency\n       [On Hit] Gain Poise Potency\n       [On Hit] Gain Poise Count"
    bb_s1_insp = "◈ Base Damage: 4\n       [On Hit] Inflict 2 Bleed Potency\n       [On Hit] Gain 2 Poise Potency\n       [On Hit] Gain 2 Poise Count\n       ◈ Base Damage: 4\n       [On Hit] Inflict 2 Bleed Potency\n       [On Hit] Gain 2 Poise Potency\n       [On Hit] Gain 2 Poise Count"
    bb_s1 = ChipSkill("Polearm Thrust ◈◈", 1, EL_EROS, [bb_s1_c1, bb_s1_c2], description=bb_s1_desc, inspect_description=bb_s1_insp)
    # Skill II: Wide Sweep ◈◈ (Eros)
    bb_s2_c1 = Chip(base_damage=5, effect_type="POISE_BLEED_SPECIAL_TYPE1", effect_val=3)
    bb_s2_c2 = Chip(base_damage=7, effect_type="POISE_BLEED_SPECIAL_TYPE2", effect_val=2)
    bb_s2_desc = "[On Hit] Inflict Bleed Potency\n       [On Hit] Inflict Bleed Count\n       [On Hit] Gain Poise Potency\n       [On Hit] Gain Poise Count"
    bb_s2_insp = "◈ Base Damage: 5\n       [On Hit] Inflict 3 Bleed Potency\n       [On Hit] Gain 3 Poise Potency\n       [On Hit] Gain 3 Poise Count\n       ◈ Base Damage: 7\n       [On Hit] Inflict 2 Bleed Count\n       [On Hit] Gain 2 Poise Potency\n       [On Hit] Gain 2 Poise Count"
    bb_s2 = ChipSkill("Wide Sweep ◈◈", 2, EL_EROS, [bb_s2_c1, bb_s2_c2], description=bb_s2_desc, inspect_description=bb_s2_insp)
    # Skill III: Cleave ◈◈◈ (Philia)
    bb_s3_c1 = Chip(base_damage=4, effect_type="SWITCH_RANDOM_TYPE1")
    bb_s3_c2 = Chip(base_damage=4, effect_type="SWITCH_RANDOM_TYPE1")
    bb_s3_c3 = Chip(base_damage=12, effect_type="APPLY_STATUS_CRITICAL")
    bb_s3_c3.status_effect = scd.bleed_8
    bb_s3_desc = "[On Critical Hit] Inflict Bleed Potency\n       [On Hit] Switches to a new random target"
    bb_s3_insp = "◈ Base Damage: 4\n       [On Hit] Switches to a new random target\n       ◈ Base Damage: 4\n       [On Hit] Switches to a new random target\n       ◈ Base Damage: 12\n       [On Critical Hit] Inflict 8 Bleed Potency"
    bb_s3 = ChipSkill("Cleave ◈◈◈", 3, EL_PHILIA, [bb_s3_c1, bb_s3_c2, bb_s3_c3], description=bb_s3_desc, inspect_description=bb_s3_insp)
    k_bb.skill_pool_def = [(bb_s1, 4), (bb_s2, 3), (bb_s3, 2)]
    # Passives
    bb_p1 = Passive("Intangible Form", "Take -50% Base Damage from skills. Take 200% Damage from the Status Effects Bleed and Rupture (counts Unique Effects)", "PASSIVE_INTANGIBLE_FORM", color="grey74")
    bb_p2 = Passive("Frontline Fighter", "If this unit is the first of their team to take damage this turn, this unit deals +5 Final Damage this turn.\nAt the start of turn, gain 1 Haste for the next turn. After activating, this effect can occur once again every 2 turns", "PASSIVE_FRONTLINE_FIGHTER", color="red")
    k_bb.passives.extend([bb_p1, bb_p2])
    bb_foot.equip_kata(k_bb)
    bb_foot.description = "bloodbrokenguardfootsoldier"
    bb_foot.unlock_stage_id = 64

    #################################################
    # --- JADE RAIN MONASTERY FOOTSOLDIER (ACT 4) ---
    #################################################
    jr_foot = Entity("Jade Rain Monastery Footsoldier", is_player=False)
    jr_foot.max_hp = 33
    jr_foot.pace = 1
    k_jr = Kata("Monastery Arts", "Jade Rain Footsoldier", 1, 8, [1.2, 1.2, 1.2, 0.4, 1.2, 1.2, 1.2])
    # Skill I: Double Cut ◈◈ (Agape)
    jr_s1_c1 = Chip(base_damage=4, effect_type="APPLY_STATUS")
    jr_s1_c1.status_effect = scd.rupture_3
    jr_s1_c2 = Chip(base_damage=2, effect_type="APPLY_STATUS")
    jr_s1_c2.status_effect = scd.paralysis_2
    jr_s1_desc = "[Combat Start] This unit takes -2 Final Damage this turn\n       [On Hit] Inflict Rupture Potency\n       [On Hit] Inflict Paralysis"
    jr_s1_insp = "◈ Base Damage: 4\n       [On Hit] Inflict 3 Rupture Potency\n       ◈ Base Damage: 2\n       [On Hit] Inflict 2 Paralysis"
    jr_s1 = ChipSkill("Double Cut ◈◈", 1, EL_AGAPE, [jr_s1_c1, jr_s1_c2], description=jr_s1_desc, inspect_description=jr_s1_insp, effect_type="BUFF_DEF_FLAT", effect_val=2)
    # Skill II: Break Down ◈◈◈◈ (Agape)
    jr_s2_c1 = Chip(base_damage=3, effect_type="APPLY_STATUS")
    jr_s2_c1.status_effect = scd.bind_1
    jr_s2_c2 = Chip(base_damage=3, effect_type="APPLY_RUPTURE_HEAVY_STACKS")
    jr_s2_c3 = Chip(base_damage=3, effect_type="APPLY_RUPTURE_HEAVY_STACKS")
    jr_s2_c4 = Chip(base_damage=3, effect_type="APPLY_STATUS")
    jr_s2_c4.status_effect = scd.bind_1
    jr_s2_desc = "[On Hit] Inflict Rupture Potency\n       [On Hit] Inflict Rupture Count\n       [On Hit] Inflict Bind next turn"
    jr_s2_insp = "◈ Base Damage: 3\n       [On Hit] Inflict 1 Bind next turn\n       ◈ Base Damage: 3\n       [On Hit] Inflict 2 Rupture Potency\n       [On Hit] Inflict 2 Rupture Count\n       ◈ Base Damage: 3\n       [On Hit] Inflict 2 Rupture Potency\n       [On Hit] Inflict 2 Rupture Count\n       ◈ Base Damage: 3\n       [On Hit] Inflict 1 Bind next turn"
    jr_s2 = ChipSkill("Break Down ◈◈◈◈", 2, EL_AGAPE, [jr_s2_c1, jr_s2_c2, jr_s2_c3, jr_s2_c4], description=jr_s2_desc, inspect_description=jr_s2_insp)
    # Skill III: Retreating Fog Step ◈◈◈◈◈ (Pragma)
    jr_s3_c1 = Chip(base_damage=1, effect_type="FOG_STEP_SPECIAL", effect_val=20)
    jr_s3_c2 = Chip(base_damage=1, effect_type="APPLY_STATUS")
    jr_s3_c2.status_effect = scd.paralysis_2
    jr_s3_c3 = Chip(base_damage=1, effect_type="FOG_STEP_SPECIAL", effect_val=20)
    jr_s3_c4 = Chip(base_damage=1, effect_type="APPLY_STATUS")
    jr_s3_c4.status_effect = scd.paralysis_2
    jr_s3_c5 = Chip(base_damage=1, effect_type="FOG_STEP_SPECIAL", effect_val=20)
    jr_s3_desc = "[On Hit] If target has Rupture, this unit takes -20% Final Damage text turn\n       [On Hit] Inflict Paralysis\n       [On Hit] Switches to a new random target (Prioritizes units with Rupture)"
    jr_s3_insp = "◈ Base Damage: 1\n       [On Hit] If target has Rupture, this unit takes -20% Final Damage text turn\n       [On Hit] Switches to a new random target (Prioritizes units with Rupture)\n       ◈ Base Damage: 1\n       [On Hit] Inflict 2 Paralysis\n       ◈ Base Damage: 1\n       [On Hit] If target has Rupture, this unit takes -20% Final Damage text turn\n       [On Hit] Switches to a new random target (Prioritizes units with Rupture)\n       ◈ Base Damage: 1\n       [On Hit] Inflict 2 Paralysis\n       ◈ Base Damage: 1\n       [On Hit] If target has Rupture, this unit takes -20% Final Damage text turn\n       [On Hit] Switches to a new random target (Prioritizes units with Rupture)"
    jr_s3 = ChipSkill("Retreating Fog Step ◈◈◈◈◈", 3, EL_PRAGMA, [jr_s3_c1, jr_s3_c2, jr_s3_c3, jr_s3_c4, jr_s3_c5], description=jr_s3_desc, inspect_description=jr_s3_insp)
    k_jr.skill_pool_def = [(jr_s1, 4), (jr_s2, 3), (jr_s3, 2)]
    # Passives
    jr_p1 = Passive("Intangible Form", "Take -50% Base Damage from skills. Take 200% Damage from the Status Effects Bleed and Rupture (counts Unique Effects)", "PASSIVE_INTANGIBLE_FORM", color="grey74")
    jr_p2 = Passive("Blind Spots", "If this unit is the first of their team to take damage this turn, this unit takes -5 Final Damage next turn.\nWhen there is at least one unit with this passive, at the start of turn, all allied units with Bind gain 2 Bind next turn. After activating, this effect can occur once again every 2 turns", "PASSIVE_BLIND_SPOTS", color="green")
    k_jr.passives.extend([jr_p1, jr_p2])
    jr_foot.equip_kata(k_jr)
    jr_foot.description = "jaderainmonasteryfootsoldier"
    jr_foot.unlock_stage_id = 65

    ####################################
    # --- IBARA NINJA (ACT 4 BOSS) --- #
    ####################################
    ibara = Entity("Ibara Ninja", is_player=False)
    ibara.max_hp = 800
    ibara.pace = 2
    k_ibara = Kata("Ibara Arts", "Ibara Ninja", 1, 14, [1.3, 1.0, 1.0, 1.0, 1.1, 0.9, 0.4])
    # Skill I: Artery Slit (Philautia)
    ib_s1_desc = "[On Hit] If this unit has 3+ Invisibility and target has Bleed, Inflict 2 Bleed Count\n       [On Hit] If this unit has 3+ Invisibility, Inflict 5 Bleed Potency\n       [On Hit] Inflict 2 Bleed Count"
    ib_s1 = Skill("Artery Slit", 1, EL_PHILAUTIA, 4, ib_s1_desc, effect_type="IBARA_ACT4_SPECIAL1")
    # Skill II: Assassination Technique (Eros)
    ib_s2_desc = "Prioritizes targeting units who are not “Benikawa” or “Shigemura”\n       [On Use] If this unit does not have 2+ Invisibility, lose all Invisibility, then this unit takes +5 Final Damage this turn and the next turn (this effect cannot stack)\n       [On Hit] Gain 8 Poise Potency"
    ib_s2 = Skill("Assassination Technique", 2, EL_EROS, 15, ib_s2_desc, effect_type="IBARA_ACT4_SPECIAL2")
    ib_s2.target_priority = "NOT_BENI_SHIGE"
    # Skill III: Trail Of Bloodlust (Eros)
    ib_s3_desc = "Prioritizes targeting units who are “Benikawa” or “Shigemura”\n       [Combat Start] If this unit has 2+ Invisibility, gain 1 Invisibility (this effect can stack)\n       [On Critical Hit] Inflict 4 Bleed Potency\n       [On Critical Hit] Inflict 4 Bleed Count\n       [On Critical Hit] Gain 1 Invisibility"
    ib_s3 = Skill("Trail Of Bloodlust", 3, EL_EROS, 15, ib_s3_desc, effect_type="IBARA_ACT4_SPECIAL3")
    ib_s3.target_priority = "IS_BENI_SHIGE"
    # Skill IV: ??? (Philautia)
    ib_s4_desc = "[Combat Start] When hit, reflect [(Invisibility Count*50%)*Final Received Damage] back to the attacker (this effect cannot stack)\n       [Combat Start] This unit does not take any damage\n       [On Use] Gain 12 Poise Potency"
    ib_s4 = Skill("???", 4, EL_PHILAUTIA, 0, ib_s4_desc, effect_type="IBARA_ACT4_SPECIAL4")
    k_ibara.skill_pool_def = [(ib_s1, 4), (ib_s2, 1), (ib_s3, 1), (ib_s4, 1)]
    # Passives
    ib_p1 = Passive("Thorn / Outcast", "When this unit’s HP reaches 500, ends the battle. Deals +30% Base Damage against units who are not “Benikawa” or “Shigemura”. Deals -50% Base Damage and takes +50% Base Damage from units who are “Benikawa” or “Shigemura”", "PASSIVE_IBARA_THORN", color="purple4")
    ib_p2 = Passive("Invisibility", "Battle Start: Gain 4 Invisibility, then gain 1 Invisibility at turn start from then on\nWhen this unit is hit by a unit who is not “Benikawa” or “Shigemura”, inflict 4 Rupture Potency to the attacker (once per skill / activates only for one chip per skill).\nWhen this unit is hit by a unit who is “Benikawa” or “Shigemura”, there is a 50% chance to lose 1 Invisibility. If the chance fails, the next hit received by the aforementioned units will have a 100% chance instead\nWhenever this unit’s Invisibility reaches 0, instantly gain 5 Bind and 4 Invisibility", "PASSIVE_IBARA_INVISIBILITY", color="purple4")
    k_ibara.passives.extend([ib_p1, ib_p2])
    ibara.equip_kata(k_ibara)
    ibara.description = "ibaraninjadescription"
    ibara.unlock_stage_id = 66

    ##############################################################
    # --- TEN THOUSAND BLOSSOM BROTHERHOOD LINEBREAKER (ACT 4) ---
    ##############################################################
    ttbb_lb = Entity("Ten Thousand Blossom Brotherhood Linebreaker", is_player=False)
    ttbb_lb.max_hp = 40
    ttbb_lb.pace = 2
    k_ttbb_lb = Kata("Brotherhood Arts", "Brotherhood Linebreaker", 1, 7, [1.0, 1.4, 1.4, 1.0, 1.4, 1.4, 1.4])
    # Skill I: Ancient Bladework (Pragma)
    lb_s1_c1 = Chip(base_damage=8, effect_type="POISE_RUPTURE_SINKING_SPECIAL1", effect_val=3)
    lb_s1_desc = "[On Use] Gain 2 Poise Potency\n       [On Use] Gain 2 Poise Count\n       [On Hit] Inflict 2 Rupture Potency\n       [On Hit] Inflict 2 Sinking Potency"
    lb_s1_insp = "◈ Base Damage: 8\n       [On Use] Gain 3 Poise Potency\n       [On Use] Gain 3 Poise Count\n       [On Hit] Inflict 3 Rupture Potency\n       [On Hit] Inflict 3 Sinking Potency"
    lb_s1 = ChipSkill("Ancient Bladework", 1, EL_PRAGMA, [lb_s1_c1], description=lb_s1_desc, inspect_description=lb_s1_insp, effect_type="POISE_RUPTURE_SINKING_SPECIAL1", effect_val=2)
    # Skill II: Flying Slashes ◈◈◈ (Agape)
    lb_s2_c1 = Chip(base_damage=5, effect_type="POISE_PARALYSIS_SPECIAL1", effect_val=3)
    lb_s2_c2 = Chip(base_damage=5, effect_type="POISE_PARALYSIS_SPECIAL1", effect_val=3)
    lb_s2_c3 = Chip(base_damage=5, effect_type="BIND_HASTE_SPECIAL_TYPE1", effect_val=4)
    lb_s2_desc = "[On Use] Gain Poise Count\n       [On Critical Hit] Inflict Paralysis\n       [On Critical Hit] Inflict Bind next turn\n       [On Critical Hit] Gain Haste next turn\n       [On Critical Hit] Switches to a new random target"
    lb_s2_insp = "◈ Base Damage: 5\n       [On Use] Gain 3 Poise Count\n       [On Critical Hit] Inflict 3 Paralysis\n       [On Critical Hit] Switches to a new random target\n       ◈ Base Damage: 5\n       [On Use] Gain 3 Poise Count\n       [On Critical Hit] Inflict 3 Paralysis\n       [On Critical Hit] Switches to a new random target\n       ◈ Base Damage: 5\n       [On Critical Hit] Inflict 4 Bind next turn\n       [On Critical Hit] Gain 4 Haste next turn"
    lb_s2 = ChipSkill("Flying Slashes ◈◈◈", 2, EL_AGAPE, [lb_s2_c1, lb_s2_c2, lb_s2_c3], description=lb_s2_desc, inspect_description=lb_s2_insp, effect_type="POISE_PARALYSIS_SPECIAL1")
    # Skill III: Break The Enemy ◈◈ (Ludus)
    lb_s3_c1 = Chip(base_damage=3, effect_type="APPLY_STATUS")
    lb_s3_c1.status_effect = scd.rupture_6
    lb_s3_c2 = Chip(base_damage=12, effect_type="BREAKTHEENEMY_SPECIAL")
    lb_s3_desc = "[On Use] Take +5 Final Damage this turn\n       [On Hit] Inflict Bind next turn\n       [On Hit] Inflict Rupture Potency\n       [On Hit] Inflict Rupture Count"
    lb_s3_insp = "◈ Base Damage: 3\n       [On Hit] Inflict 6 Rupture Potency\n       ◈ Base Damage: 12\n       [On Hit] Inflict 4 Rupture Count\n       [On Hit] Inflict 4 Bind next turn\n       [On Use] Take +5 Final Damage this turn"
    lb_s3 = ChipSkill("Break The Enemy ◈◈", 3, EL_LUDUS, [lb_s3_c1, lb_s3_c2], description=lb_s3_desc, inspect_description=lb_s3_insp, effect_type="BREAKTHEENEMY_SPECIAL")
    k_ttbb_lb.skill_pool_def = [(lb_s1, 3), (lb_s2, 2), (lb_s3, 2)]
    lb_p1 = Passive("Fading Form", "Take -50% Base Damage from skills. Take 300% Damage from the Status Effects Bleed and Rupture (counts Unique Effects). When taking damage from a skill that is not the element Eros or Agape, take -1 Final Damage next turn (this effect can stack up to 3 times, max -3 Final Damage)", "PASSIVE_FADING_FORM", color="grey74")
    lb_p2 = Passive("Nostalgia Of A Brotherhood", "The first 3 allied units to hit any unit from “Ten Thousand Blossom Brotherhood” instantly gains (6-Order of attacker) Rupture Potency", "PASSIVE_BROTHERHOOD", color="hot_pink")
    k_ttbb_lb.passives.extend([lb_p1, lb_p2])
    ttbb_lb.equip_kata(k_ttbb_lb)
    ttbb_lb.description = "tenthousandblossombrotherhoodlinebreaker"
    ttbb_lb.unlock_stage_id = 68

    ###########################################################
    # --- TEN THOUSAND BLOSSOM BROTHERHOOD DEFENDER (ACT 4) ---
    ###########################################################
    ttbb_df = Entity("Ten Thousand Blossom Brotherhood Defender", is_player=False)
    ttbb_df.max_hp = 60
    ttbb_df.pace = 2
    k_ttbb_df = Kata("Brotherhood Arts", "Brotherhood Defender", 1, 7, [1.0, 1.4, 1.4, 1.0, 1.4, 1.4, 1.4])
    # Skill I: Dreadful Bash (Ludus)
    df_s1_c1 = Chip(base_damage=11, effect_type="RUPTURE_SINKING_SPECIAL_TYPE1", effect_val=6)
    df_s1_desc = "[On Hit] Inflict 6 Rupture Potency\n       [On Hit] Inflict 6 Sinking Potency"
    df_s1_insp = "◈ Base Damage: 11\n       [On Hit] Inflict 6 Rupture Potency\n       [On Hit] Inflict 6 Sinking Potency"
    df_s1 = ChipSkill("Dreadful Bash", 1, EL_LUDUS, [df_s1_c1], description=df_s1_desc, inspect_description=df_s1_insp)
    # Skill II: Form a Line (Philautia)
    df_s2_c1 = Chip(base_damage=5, effect_type="FORMALINE_SPECIAL")
    df_s2_desc = "Let X = Amount of this unit’s allies from “Ten Thousand Blossom Brotherhood”\n       [On Use] All units from X gain X Poise Potency\n       [On Use] All units from X gain 2 Poise Count\n       [On Use] All units from X deal +X Final Damage this turn (Max +4 Final Damage)\n       [On Hit] Target deals -X Final Damage this turn and the next turn"
    df_s2 = ChipSkill("Form a Line", 2, EL_PHILAUTIA, [df_s2_c1], description=df_s2_desc, inspect_description=df_s2_desc, effect_type="FORMALINE_SPECIAL")
    # Skill III: Isolate The Enemy ◈◈◈ (Ludus)
    df_s3_c1 = Chip(base_damage=4, effect_type="ISOLATETHEENEMY_SPECIAL_TYPE1")
    df_s3_c2 = Chip(base_damage=4, effect_type="ISOLATETHEENEMY_SPECIAL_TYPE2")
    df_s3_c3 = Chip(base_damage=7, effect_type="ISOLATETHEENEMY_SPECIAL_TYPE3")
    df_s3_desc = "[On Hit] If target has Bind, deal +Base Damage\n       [On Hit] If target has Paralysis, deal +Base Damage\n       [On Hit] If target has Rupture, deal +Base Damage\n       [On Hit] Inflict Sinking Count\n       [On Hit] Switches to a new random target"
    df_s3_insp = "◈ Base Damage: 4\n       [On Hit] If target has Bind, deal +3 Base Damage\n       [On Hit] If target has Paralysis, deal +3 Base Damage\n       [On Hit] Switches to a new random target\n       ◈ Base Damage: 4\n       [On Hit] If target has Rupture, deal +2 Base Damage\n       [On Hit] If target has Bind, deal +2 Base Damage\n       [On Hit] If target has Paralysis, deal +2 Base Damage\n       [On Hit] Switches to a new random target\n       ◈ Base Damage: 7\n       [On Hit] If target has Rupture, deal +3 Base Damage\n       [On Hit] Inflict 5 Sinking Count"
    df_s3 = ChipSkill("Isolate The Enemy ◈◈◈", 3, EL_LUDUS, [df_s3_c1, df_s3_c2, df_s3_c3], description=df_s3_desc, inspect_description=df_s3_insp)
    k_ttbb_df.skill_pool_def = [(df_s1, 4), (df_s2, 2), (df_s3, 2)]
    df_p1 = Passive("Fading Form", "Take -70% Base Damage from skills. Take 300% Damage from the Status Effects Bleed and Rupture (counts Unique Effects). When taking damage from a skill that is not the element Eros or Agape, take -2 Final Damage next turn (this effect can stack up to 5 times, max -10 Final Damage)", "PASSIVE_FADING_FORM", color="grey74")
    df_p2 = Passive("Nostalgia Of A Camaraderie", "On the first 3 times an ally of this unit from “Ten Thousand Blossom Brotherhood” takes damage from a skill, instantly heals (6-Order of allied unit attacker, minimum 0) HP (counts self, but does not heal self, this effect cannot stack)", "PASSIVE_CAMARADERIE", color="hot_pink")
    k_ttbb_df.passives.extend([df_p1, df_p2])
    ttbb_df.equip_kata(k_ttbb_df)
    ttbb_df.description = "tenthousandblossombrotherhooddefender"
    ttbb_df.unlock_stage_id = 69

    ######################################
    # --- ZHAO FENG (ACT 4 FINAL BOSS) ---
    ######################################
    zhao = Entity("Zhao Feng", is_player=False)
    zhao.max_hp = 578
    zhao.pace = 4
    k_zhao = Kata("General's Arts", "Zhao Feng", 1, 42, [1.1, 1.0, 1.0, 1.1, 1.0, 1.0, 1.0])
    # Skill I: Leading The Vanguard Upward (I)
    zhao_s1_desc = "[Combat Start] All units in the field with Rupture gain [(Rupture Count+Potency)/3] Blossom (Max +3, this effect occurrence does not stack)\n       [On Hit] Inflict 2 Rupture Potency\n       [On Hit] Inflict 2 Sinking Potency"
    zhao_s1 = Skill("Leading The Vanguard Upward (I)", 1, EL_PRAGMA, 5, zhao_s1_desc, effect_type="ZHAOFENG_SPECIAL_1")
    # Skill II: Hanging / Deflecting [挂] (II)
    zhao_s2_desc = "[Combat Start] All units in the field with Rupture gain [(Rupture Count+Potency)/3] Malice (Max +3, this effect occurrence does not stack)\n       [On Hit] Inflict 2 Rupture Count\n       [On Hit] Inflict 2 Sinking Count"
    zhao_s2 = Skill("Hanging / Deflecting [挂] (II)", 2, EL_LUDUS, 5, zhao_s2_desc, effect_type="ZHAOFENG_SPECIAL_2")
    # Skill III: “Liao” [撩] ◈◈ (III)
    zh_s3_c1 = Chip(base_damage=4, effect_type="ZHAOFENG_SPECIAL_3")
    zh_s3_c2 = Chip(base_damage=4, effect_type="ZHAOFENG_SPECIAL_4")
    zh_s3_desc = "[On Hit] If target has 5+ (Rupture Potency+Count), deal +10% Base Damage\n       [On Hit] If target has 5+ (Blossom+Malice), deal +10% Base Damage\n       [On Hit] Inflict Rupture Potency"
    zh_s3_insp = "◈ Base Damage: 4\n       [On Hit] If target has 5+ (Rupture Potency+Count), deal +10%Base Damage\n       [On Hit] Inflict 4 Rupture Potency\n       ◈ Base Damage: 4\n       [On Hit] If target has 5+ (Blossom+Malice), deal +10%Base Damage\n       [On Hit] Inflict 4 Rupture Potency"
    zhao_s3 = ChipSkill("“Liao” [撩] ◈◈", 3, EL_EROS, [zh_s3_c1, zh_s3_c2], description=zh_s3_desc, inspect_description=zh_s3_insp)
    # EX 1: Encroaching Malice ◈◈ (II)
    zh_ex1_c1 = Chip(base_damage=5, effect_type="ZHAOFENG_SPECIAL_5")
    zh_ex1_c2 = Chip(base_damage=5, effect_type="ZHAOFENG_SPECIAL_6")
    zh_ex1_desc = "[On Hit] Heal for (Malice on target)*2 (max 20 HP)\n       [On Hit] If target has 5+ (Rupture Potency+Count), deal +20% Base Damage\n       [On Hit] Inflict Malice\n       [On Hit] Switches to a new random target (Prioritizes units with Malice)"
    zh_ex1_insp = "◈ Base Damage: 5\n       [On Hit] Heal for (Malice on target)*2 (max 20 HP)\n       [On Hit] If target has 5+ (Rupture Potency+Count), deal +%20Base Damage\n       [On Hit] Switches to a new random target (Prioritizes units with Malice)\n       ◈ Base Damage: 5\n       [On Hit] Heal for (Malice on target)*2 (max 20 HP)\n       [On Hit] Inflict 3 Malice"
    zhao_ex1 = ChipSkill("Encroaching Malice ◈◈", 2, EL_EROS, [zh_ex1_c1, zh_ex1_c2], description=zh_ex1_desc, inspect_description=zh_ex1_insp)
    # EX 2: Embrace The Moon [怀中抱月] ◈◈◈◈ (III)
    zh_ex2_c1 = Chip(base_damage=4, effect_type="ZHAOFENG_SPECIAL_8")
    zh_ex2_c2 = Chip(base_damage=3, effect_type="ZHAOFENG_SPECIAL_9")
    zh_ex2_c3 = Chip(base_damage=3, effect_type="ZHAOFENG_SPECIAL_9")
    zh_ex2_c4 = Chip(base_damage=10, effect_type="ZHAOFENG_SPECIAL_10")
    zh_ex2_desc = "[Combat Start] All units in the field with Blossom gain 3 Bind instantly\n       [Combat Start] All units in the field with Rupture gain [(Rupture Count+Potency)/3] Blossom (Max 5)\n       [On Hit] Inflict Blossom\n       [On Hit] Switches to a new random target (Prioritizes units without Blossom)"
    zh_ex2_insp = "[Combat Start] All units in the field with Blossom gain 3 Bind instantly\n       [Combat Start] All units in the field with Rupture gain [(Rupture Count+Potency)/3] Blossom (Max 5)\n       ◈ Base Damage: 4\n       [On Hit] Inflict 2 Blossom\n       [On Hit] Switches to a new random target (Prioritizes units without Blossom)\n       ◈ Base Damage: 3\n       [On Hit] Inflict 3 Blossom\n       [On Hit] Switches to a new random target (Prioritizes units without Blossom)\n       ◈ Base Damage: 3\n       [On Hit] Inflict 3 Blossom\n       [On Hit] Switches to a new random target (Prioritizes units without Blossom)\n       ◈ Base Damage: 10\n       [On Hit] Inflict 4 Blossom\n       [On Hit] Switches to a new random target (Prioritizes units without Blossom)"
    zhao_ex2 = ChipSkill("Embrace The Moon [怀中抱月] ◈◈◈◈", 3, EL_PRAGMA, [zh_ex2_c1, zh_ex2_c2, zh_ex2_c3, zh_ex2_c4], description=zh_ex2_desc, inspect_description=zh_ex2_insp, effect_type="ZHAOFENG_SPECIAL_7")
    k_zhao.skill_pool_def = [(zhao_s1, 5), (zhao_s2, 5), (zhao_s3, 3)]
    # Store EX skills so the engine can append them cleanly
    zhao.appendable_skills = {"EX1": zhao_s3, "EX2": zhao_ex1, "EX3": zhao_ex2}
    zh_p1 = Passive("Crumbling Form Of A General", "Take -30% Base Damage from skills. Take 150% Damage from the Status Effects Bleed and Rupture (counts Unique Effects). This unit is immune to Paralysis and Bind. When this unit is present, all allied units cannot suffer from the effects of Rupture, and their Rupture Count cannot be decreased by normal means.", "PASSIVE_CRUMBLING_FORM", color="hot_pink")
    zh_p2 = Passive("Zhao Feng [赵锋]", "Rift Aptitude -20\nAkasuke’s HP cannot go below 1 until all other allied units have been defeated\nCombat Start: All units in the field (including self) Rupture Potency and Count / 2", "PASSIVE_ZHAOFENG_CORE", color="hot_pink")
    zh_p3 = Passive("The Vanguard Who Breaks Through Enemy Lines", "At turn 3, if there are none of this unit’s allies, summon a “Ten Thousand Blossom Brotherhood Linebreaker” or “Ten Thousand Blossom Brotherhood Defender” with 50 fixed Max HP. When there are none of this unit's allies, this unit can summon again 2 turns after the ally dies\nTally the amount of turns passed and this unit is able to append skills based on:\nAfter two turns, if this unit has never reached 280 or less HP, draw the skill “Liao” [撩] into deck. Otherwise, draw the skill Encroaching Malice instead\nAfter four turns, if this unit has never reached 280 or less HP, draw the skill “Liao” [撩] into deck. Otherwise, draw the skill Embrace The Moon [怀中抱月] instead\nAfter four turns, reset the Tally", "PASSIVE_ZHAOFENG_VANGUARD", color="hot_pink")
    k_zhao.passives.extend([zh_p1, zh_p2, zh_p3])
    zhao.equip_kata(k_zhao)
    zhao.description = "zhaofengdescription"
    zhao.unlock_stage_id = 70

    ######################################################
    # --- IBARA NINJA - 'KAGEROU THE UNTOUCHABLE' (EPILOGUE)
    ######################################################
    kagerou = Entity("Ibara Ninja - 'Kagerou The Untouchable'", is_player=False)
    kagerou.max_hp = 325
    kagerou.pace = 2
    k_kag = Kata("Untouchable Arts", "Kagerou", 1, 12, [1.4, 1.2, 1.2, 1.2, 1.4, 1.2, 0.5])
    # Skill I: Vital Artery Slit ◈◈ (Eros)
    kag_s1_c1 = Chip(base_damage=4, effect_type="KAGEROU_SPECIAL_1")
    kag_s1_c2 = Chip(base_damage=4, effect_type="KAGEROU_SPECIAL_2")
    kag_s1_desc = "[On Use] Gain Flickering Invisibility\n       [On Use] Gain Leaking Bloodlust\n       [On Hit] If target has Bleed, Inflict Bleed Potency\n       [On Hit] Inflict Bleed Count\n       [On Hit] Switches to a new random target"
    kag_s1_insp = "◈ Base Damage: 4\n       [On Use] Gain 1 Flickering Invisibility\n       [On Hit] If target has Bleed, Inflict Bleed 5 Potency\n       [On Hit] Switches to a new random target\n       ◈ Base Damage: 4\n       [On Use] Gain 5 Leaking Bloodlust\n       [On Hit] Inflict 3 Bleed Count"
    kag_s1 = ChipSkill("Vital Artery Slit ◈◈", 1, EL_EROS, [kag_s1_c1, kag_s1_c2], description=kag_s1_desc, inspect_description=kag_s1_insp)
    # Skill II: Desperate Assassination Technique (Eros)
    kag_s2_desc = "Prioritizes targeting units who are “Benikawa” or “Shigemura”\n       [Combat Start] Gain 10 Poise Potency\n       [On Hit] Gain 10 Poise Potency"
    kag_s2 = Skill("Desperate Assassination Technique", 2, EL_EROS, 13, kag_s2_desc, effect_type="KAGEROU_SPECIAL_3")
    kag_s2.target_priority = "IS_BENI_SHIGE"
    # Skill III: Leaking Bloodlust ◈◈◈◈ (Philautia)
    kag_s3_c1 = Chip(base_damage=4, effect_type="KAGEROU_SPECIAL_4")
    kag_s3_c2 = Chip(base_damage=4, effect_type="KAGEROU_SPECIAL_4")
    kag_s3_c3 = Chip(base_damage=4, effect_type="KAGEROU_SPECIAL_5")
    kag_s3_c4 = Chip(base_damage=8, effect_type="KAGEROU_SPECIAL_6")
    kag_s3_desc = "[Combat Start] Gain 1 Flickering Invisibility (this skill effect occurrence cannot stack)\n       [On Use] Gain Leaking Bloodlust\n       [On Critical Hit] Inflict Bleed Potency\n       [On Critical Hit] Gain Leaking Bloodlust\n       [On Hit] Switches to a new random target"
    kag_s3_insp = "[Combat Start] Gain 1 Flickering Invisibility (this skill effect occurrence cannot stack)\n       ◈ Base Damage: 4\n       [On Use] Gain 3 Leaking Bloodlust\n       [On Critical Hit] Inflict Bleed 6 Potency\n       [On Hit] Switches to a new random target\n       ◈ Base Damage: 4\n       [On Use] Gain 3 Leaking Bloodlust\n       [On Critical Hit] Inflict Bleed 6 Potency\n       [On Hit] Switches to a new random target\n       ◈ Base Damage: 4\n       [On Critical Hit] Gain 6 Leaking Bloodlust\n       [On Hit] Switches to a new random target\n       ◈ Base Damage: 8\n       [On Critical Hit] Inflict Bleed 6 Potency\n       [On Critical Hit] Gain 6 Leaking Bloodlust"
    kag_s3 = ChipSkill("Leaking Bloodlust ◈◈◈◈", 3, EL_PHILAUTIA, [kag_s3_c1, kag_s3_c2, kag_s3_c3, kag_s3_c4], description=kag_s3_desc, inspect_description=kag_s3_insp, effect_type="KAGEROU_SPECIAL_CS")
    # Skill IV: Specialty: Heat Haze (Philautia)
    kag_s4_desc = "[Combat Start] When hit, reflect (Flickering Invisibility Count*75)% Final Received Damage back to the attacker (max 375% Final Damage per hit, this effect cannot stack)\n       [On Use] Gain 1 Flickering Invisibility\n       [On Use] Gain 10 Leaking Bloodlust\n       [On Use] Gain 20 Poise Potency"
    kag_s4 = Skill("Specialty: Heat Haze", 4, EL_PHILAUTIA, 0, kag_s4_desc, effect_type="KAGEROU_SPECIAL_7")
    k_kag.skill_pool_def = [(kag_s1, 2), (kag_s2, 5), (kag_s3, 2), (kag_s4, 1)]
    # Passives
    kag_p1 = Passive("Cornered Thorn / Outcast", "This unit’s HP does not go below 1 until it has 99 Leaking Bloodlust\nDeals +30% Base Damage against units who are not “Benikawa” or “Shigemura”. Deals -50% Base Damage and takes +50% Base Damage from units who are “Benikawa” or “Shigemura”\nWhen units who are “Benikawa” or “Shigemura” hit this unit, this unit takes +5 Base Damage from the next Eros element attack from a unit who is not “Benikawa” or “Shigemura” (this effect does not stack)", "PASSIVE_KAGEROU_THORN", color="thistle3")
    kag_p2 = Passive("Flickering Invisibility", "Battle Start: Gain 5 Flickering Invisibility\nWhen this unit is hit by a unit who is not “Benikawa” or “Shigemura”, inflict (Flickering Invisibility Count) Rupture Potency to the attacker (max 5, once per skill / activates only for one chip per skill).\nWhen this unit is hit by a unit who is “Benikawa” or “Shigemura”, there is a 50% chance to lose 1 Flickering Invisibility if the very next unit to hit this hit is not “Benikawa” or “Shigemura”. If the chance fails, the next hit received by any unit will have a 100% chance instead\nWhenever this unit’s Flickering Invisibility reaches 0, instantly gain 5 Bind, 30 Leaking Bloodlust, and 5 Flickering Invisibility", "PASSIVE_KAGEROU_INVISIBILITY", color="thistle3")
    k_kag.passives.extend([kag_p1, kag_p2])
    kagerou.equip_kata(k_kag)
    kagerou.description = "ibaraninjadescription"
    kagerou.unlock_stage_id = 66
    
    ################################################
    # Append to existing return list in stages.py: #
    ################################################
    return [thief, fresh, hool, lead, benikawa, ninja, double, slender, bulky, spike, chain, h_lead, upper, kuro, 
            sp_kiryoku, c_kiryoku, ayako, sumiko, inf_heiwa, inf_kiryoku, inf_kasa, inf_lead, hisayuki, inf_council, inf_disc, 
            raven, falcon, eagle, raven_inj, falcon_inj, hench, mascot, rip_hench, rip_lead, adam, guard, guard_leader, luoxia_student, natsume, gf_gangster, gf_leader, bw_gangster, bw_leader, tmg_gangster, tmg_leader, miyu, mei, bb_foot, jr_foot, ibara, ttbb_lb, ttbb_df, zhao, kagerou]