import copy
from entities import Entity, Kata, Skill, StatusEffect
from entities import EL_EROS, EL_PHILIA, EL_STORGE, EL_AGAPE, EL_LUDUS, EL_PRAGMA, EL_PHILAUTIA
import config
import scd
from player_state import player
from scd import bleed_1, bleed_2, bleed_3, bind_1, rupture_1, rupture_2, rupture_3, rupturecount_2, bleedcount_2, bind_4, pierce_affinity_1
from entities import Chip, ChipSkill

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
        # In the original code, the node spawned her simply as "Ayame Benikawa". 
        # The database names her "Ayame Benikawa (Sparring)". We rename it here to match standard text.
        enemy = spawn("Ayame Benikawa (Sparring)")
        if enemy:
            enemy.name = "Ayame Benikawa"
            enemies.append(enemy)

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

    # Return ignoring any potential NoneType errors from typos in db
    return [e for e in enemies if e is not None]

def get_enemy_database():
    # Existing enemies
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
    # FIXED: Added APPLY_STATUS flag and mapped bleed_1
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
    # FIXED: Added APPLY_STATUS flag and mapped bleed_2
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
    # FIXED: Added APPLY_STATUS flags and mapped bleed_1 / bleed_2
    hl1 = Skill("Headbutting", 1, EL_PHILIA, 5, "[On Hit] Inflict 1 Bleed Potency", effect_type="APPLY_STATUS")
    hl1.status_effect = bleed_1
    hl2 = Skill("Chained Bat Combo", 2, EL_PRAGMA, 5, "[On Hit] Inflict 2 Bleed Potency", effect_type="APPLY_STATUS")
    hl2.status_effect = bleed_2
    # FIXED: Corrected text typo from 'take +1' to 'take -1' and used AOE_BUFF_DEF_FLAT
    hl3 = Skill("Rally", 3, EL_PRAGMA, 0, "[On Use] All allied units of this unit take -1 Final Damage this turn", effect_type="AOE_BUFF_DEF_FLAT", effect_val=1)
    k_hlead.skill_pool_def = [(hl1, 4), (hl2, 3), (hl3, 2)]
    k_hlead.rift_aptitude = 1
    h_lead.equip_kata(k_hlead)
    h_lead.description = "A more experienced Heiwa Seiritsu thug student who has enough respect and proficiency with makeshift weapons to lead a small unit of thugs."
    h_lead.unlock_stage_id = 18

    upper = Entity("Heiwa Seiritsu Upperclassman Fighter", is_player=False)
    upper.max_hp = 1523
    res_up = [1.0, 1.2, 1.0, 1.1, 1.1, 1.2, 0.7]
    k_up = Kata("Upperclassman Style", "Upperclassman", 1, "0", res_up)
    # FIXED: Added APPLY_STATUS flags and mapped the corresponding generic statuses
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
    # FIXED: Mapped straight to the existing hardcoded unique flags in battle_system.py
    ku1 = Skill("Chained Limb Flurry", 1, EL_PRAGMA, 5, "[On Hit] Inflict 2 Bleed Potency\n      [On Hit] Inflict 2 Bleed Count", effect_type="APPLY_BLEED_HEAVY_STACKS")
    ku2 = Skill("Heavy Chain Whip", 2, EL_AGAPE, 6, "[On Hit] Inflict 3 Bleed Potency\n      [On Hit] Inflict 1 Bind next turn", effect_type="APPLY_BLEED_AND_BIND")
    ku3 = Skill("Pull In For A Beatdown", 3, EL_AGAPE, 8, "[On Hit] Inflict 3 Bleed Potency\n        [On Hit] Inflict 2 Bind next turn", effect_type="APPLY_BLEED_AND_BIND_HEAVY")
    k_ku.skill_pool_def = [(ku1, 3), (ku2, 4), (ku3, 2)]
    k_ku.rift_aptitude = 6
    kuro.equip_kata(k_ku)
    kuro.description = "The true identity of the Heiwa Seiritsu Upperclassman: 'Chain Reaper Of Heiwa' Kurogane, has been revealed. A veteran hotblooded gangster on the run who tortures his opponents with masterful chain movements paired with his reckless fighting style. His motives are taking down Kasakura’s key figures and extracting information about the existence of “Katas”."
    kuro.unlock_stage_id = 21

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
    ck3 = Skill("Rush In", 3, EL_PHILIA, 9, "[On Hit] Inflict 2 Rupture Count\n      [On Hit] Inflict 2 Fairylight Potency", effect_type="KIRYOKU_COUNCIL_SPECIAL")
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
    ay3 = Skill("Shukuchi (Incomplete)", 3, EL_PRAGMA, 10, "[On Hit] Inflict 3 Rupture Count\n      [On Hit] Inflict 4 Fairylight Potency", effect_type="AYAKO_SPECIAL")
    k_ayako.skill_pool_def = [(ay1, 3), (ay2, 3), (ay3, 3)]
    ayako.equip_kata(k_ayako)
    ayako.description = "Serving as the Security Head of the Kiryoku Student Council, Ayako is a feral, battle-hungry warrior who wields a solid oak bokken with devastating power. She fights using chaotic, bouncing trajectories and explosive acceleration that makes meeting her head-on incredibly dangerous. Fiercely protective of her empathic 'Queen', she relies on her overwhelming speed and predatory instincts to effortlessly overwhelm seasoned fighters."
    ayako.unlock_stage_id = 28

    sumiko = Entity("‘Lake Strider’ Fairy Sumiko", is_player=False)
    sumiko.max_hp = 143
    k_sumiko = Kata("Lake Strider", "Sumiko", 1, 6, [1.0, 1.2, 1.3, 0.7, 0.7, 1.1, 1.0])
    su1 = Skill("Distancing", 1, EL_PRAGMA, 5, "[On Hit] If target has Fairylight, inflict 5 Rupture Potency.", effect_type="FAIRYLIGHT_SPECIAL1", effect_val=5)
    su2 = Skill("Protection By The Fairies", 2, EL_LUDUS, 5, "[On Use] All ally units deal -8 Final Damage this turn\n      [On Hit] Gain 2 Haste next turn", effect_type="SUMIKO_SPECIAL_1")
    su3 = Skill("Shukuchi (Incomplete)", 3, EL_PRAGMA, 9, "[On Hit] Inflict 4 Rupture Count\n      [On Hit] Inflict 5 Rupture Potency\n      [On Hit] Gain 2 Haste next turn", effect_type="SUMIKO_SPECIAL_2")
    k_sumiko.skill_pool_def = [(su1, 3), (su2, 3), (su3, 3)]
    sumiko.equip_kata(k_sumiko)
    sumiko.description = "The calculating Treasurer of the Kiryoku Student Council, Sumiko controls the battlefield with an eerie, sisterly calmness. She utilizes a terrifying footwork technique called Shukuchi to seamlessly glide across the floor, instantly closing the distance between herself and her target without any visible inertia. Despite her ferocity in close-quarters combat, she prioritizes defense and spatial control, meticulously keeping threats pushed far away from her President, who is currently sleeping."
    sumiko.unlock_stage_id = 29

    inf_heiwa = Entity("Infiltrating Heiwa Seiritsu High School Student", is_player=False)
    inf_heiwa.max_hp = 37
    k_inf_heiwa = Kata("Fake Delinquent", "Heiwa Infiltrator", 1, 0, [1.4, 1.3, 1.4, 1.7, 1.4, 1.4, 1.3])
    ih1 = Skill("Panicked Kick", 1, EL_PRAGMA, 7, "[On Hit] Inflict 2 Bleed Count", effect_type="APPLY_STATUS")
    ih1.status_effect = bleedcount_2
    ih2 = Skill("Metal Bat Swing", 2, EL_EROS, 8, "[On Hit] Inflict 2 Bleed Potency\n      [On Hit] Inflict 2 Rupture Potency", effect_type="BLEED_RUPTURE_SPECIAL_TYPE1", effect_val=2)
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

    hisayuki = Entity("Hisayuki Tadamasa", is_player=False)
    hisayuki.max_hp = 255
    k_hisayuki = Kata("Battering Ram", "Hisayuki", 1, 5, [1.2, 0.5, 0.5, 1.5, 1.0, 1.0, 1.0])
    hi1 = Skill("Following Orders", 1, EL_STORGE, 7, "[On Use] This unit takes -40% damage next turn\n      [On Hit] If this unit has Haste, gain 1 Bind next turn. Otherwise, gain 1 Haste next turn", effect_type="HISAYUKI_SPECIAL_1")
    hi2 = Skill("Pick Up Speed", 2, EL_LUDUS, 11, "[Combat Start] If this unit has Bind, take +50% damage for the turn\n      [On Hit] If this unit has no Haste, gain 3 Haste next turn, otherwise, gain 1 Haste next turn", effect_type="HISAYUKI_SPECIAL_2")
    hi3 = Skill("Human Battering Ram", 3, EL_EROS, 14, "[On Hit] If this unit has Haste, deal +10% damage for every stack of Haste on self (Max +50%), then remove all Haste on self", effect_type="HISAYUKI_SPECIAL_3")
    k_hisayuki.skill_pool_def = [(hi1, 4), (hi2, 2), (hi3, 2)]
    hisayuki.equip_kata(k_hisayuki)
    hisayuki.description = "Encountered in the bowels of the cruise ship, this terrifying combatant acts as an unstoppable, linear human battering ram to protect the weapon thieves. Despite possessing monstrous durability and the ability to accelerate into bone-crushing tackles, he speaks in robotic, military-style commands while humbly claiming to be just an 'ordinary student'. It took Shigemura absorbing his full-speed tackle to create a brief, desperate opening for the rest of the team to finally take him down."
    hisayuki.unlock_stage_id = 33

    inf_lead = Entity("Infiltrating Heiwa Seiritsu Delinquent Leader", is_player=False)
    inf_lead.max_hp = 55
    k_inf_lead = Kata("Fake Leader", "Infiltrator Leader", 1, 1, [1.2, 1.2, 1.3, 1.6, 1.4, 1.3, 1.0])
    il1 = Skill("Wrapping Chains", 1, EL_EROS, 6, "[On Hit] Inflict 2 Bleed Potency\n      [On Hit] Inflict 2 Bleed Count", effect_type="APPLY_BLEED_HEAVY_STACKS")
    il2 = Skill("Metal Bat Desperation", 2, EL_PHILAUTIA, 9, "[On Hit] Inflict 3 Bleed Potency\n      [On Hit] Inflict 3 Rupture Potency", effect_type="BLEED_RUPTURE_SPECIAL_TYPE1", effect_val=3)
    il3 = Skill("Rally", 3, EL_EROS, 0, "[On Use] All allied units of this unit take -3 Final Damage this turn", effect_type="AOE_BUFF_DEF_FLAT", effect_val=3)
    k_inf_lead.skill_pool_def = [(il1, 3), (il2, 3), (il3, 3)]
    inf_lead.equip_kata(k_inf_lead)
    inf_lead.description = "Acting as squad commanders for the ship's infiltration forces, these washed-up gang leaders don the customized, untidy uniforms of Heiwa's notorious Upperclassmen. They bark aggressive orders and wield heavier, lethal blunt weapons to coordinate the theft of the ship's armory and suppress any interference. Despite their intimidating posturing, they possess none of the mythic, monstrous strength of the real Heiwa legends and rely entirely on intimidation."
    inf_lead.unlock_stage_id = 34

    inf_council = Entity("Infiltrating Kiryoku Gakuen Student Council Combatant", is_player=False)
    inf_council.max_hp = 53
    k_inf_council = Kata("Fake Council", "Fake Council", 1, 1, [1.1, 1.5, 1.5, 1.0, 1.2, 1.5, 1.3])
    ic1 = Skill("Baton Smack", 1, EL_AGAPE, 7, "[On Hit] Inflict 2 Rupture Potency\n      [On Hit] Inflict 2 Rupture Count", effect_type="APPLY_RUPTURE_HEAVY_STACKS")
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
    id1 = Skill("Bokken Violence", 1, EL_LUDUS, 6, "[On Use] Gain 2 Poise Potency\n      [On Use] Gain 2 Poise Count", effect_type="GAIN_POISE_SPECIAL", effect_val=2)
    id2 = Skill("Stun Baton", 2, EL_PHILAUTIA, 8, "[On Hit] Inflict 2 Bind\n      [On Hit] Inflict 2 Rupture Potency", effect_type="BIND_RUPTURE_SPECIAL_TYPE1", effect_val=2)
    id3 = Skill("Discipline", 3, EL_EROS, 10, "[On Use] Gain 4 Poise Potency\n      [On Use] Gain 4 Poise Count", effect_type="GAIN_POISE_SPECIAL", effect_val=4)
    k_inf_disc.skill_pool_def = [(id1, 3), (id2, 3), (id3, 3)]
    inf_disc.equip_kata(k_inf_disc)
    inf_disc.description = "Wearing the iconic white kimono uniforms of Kasakura’s Disciplinary Committee, these impostors use the guise of authority to restrict access to the ship's lower levels. They wield standard-issue bokkens and stun batons with practiced cruelty, completely lacking the honorable resolve of Yuri's true subordinates. Their mimicry shatters the moment they clash with genuine fighters, easily falling to Benikawa and Shigemura's superior battle IQ and speed."
    inf_disc.unlock_stage_id = 34

    raven = Entity("Raven", is_player=False)
    raven.max_hp = 115
    k_raven = Kata("Shadow Assassin", "Raven", 1, 6, [1.0, 1.1, 1.1, 1.0, 1.2, 1.2, 1.5])
    rv1 = Skill("Silent Step", 1, EL_PHILAUTIA, 3, "[Combat Start] This unit takes -6 Final Damage this turn", effect_type="BUFF_DEF_FLAT", effect_val=6)
    rv2 = Skill("Blind Spot Strike", 2, EL_PRAGMA, 7, "[On Hit] Target will take +6 Final Damage from the next attack\n      [On Hit] Gain 4 Poise Potency\n      [On Hit] Gain 4 Poise Count", effect_type="RAVEN_SPECIAL_1")
    rv3 = Skill("Disorient", 3, EL_PHILAUTIA, 10, "[On Hit] Target deals -70% damage next turn\n      [On Hit] Gain 6 Poise Potency", effect_type="RAVEN_SPECIAL_2")
    k_raven.skill_pool_def = [(rv1, 4), (rv2, 2), (rv3, 3)]
    raven.equip_kata(k_raven)
    raven.description = "One of the three rogue ninja mercenaries hired to secure the cruise ship's massive weapons supply in the lower decks. Operating outside many iron rules of the honorable ninja code, Raven utilizes blistering speed, stealth, and lethal trickery to disorient the Kasakura team. His fluid, shadow-like movements make him a highly dangerous adversary in the narrow, dimly lit corridors of the ship."
    raven.unlock_stage_id = 35

    falcon = Entity("Falcon", is_player=False)
    falcon.max_hp = 113
    k_falcon = Kata("Aerial Assassin", "Falcon", 1, 6, [1.3, 1.0, 1.0, 1.0, 1.4, 1.0, 1.5])
    fa1 = Skill("Assault Flow", 1, EL_EROS, 5, "[On Hit] Target will take +4 Final Damage from the next attack", effect_type="ON_HIT_NEXT_TAKEN_FLAT", effect_val=4)
    fa2 = Skill("Aerial Strike", 2, EL_LUDUS, 9, "[On Use] If this unit does not have Haste, gain 3 Haste next turn\n      [On Hit] Inflict 4 Rupture Potency", effect_type="FALCON_SPECIAL_1")
    fa3 = Skill("Incapacitate", 3, EL_PHILAUTIA, 10, "[On Hit] Target deals -70% damage next turn\n      [On Hit] Gain 2 Haste next turn\n      [On Hit] Inflict 2 Bind next turn", effect_type="FALCON_SPECIAL_2")
    k_falcon.skill_pool_def = [(fa1, 3), (fa2, 3), (fa3, 3)]
    falcon.equip_kata(k_falcon)
    falcon.description = "Operating alongside Raven, Falcon is a highly skilled mercenary ninja who infiltrated the Goodwill Trip to oversee the underground weapon heist. He specializes in relentless, coordinated aerial assaults and precision strikes, attempting to overwhelm the Kasakura students before they can react. Unbound by traditional clan loyalties, he fights with a ruthless pragmatism that forces Benikawa and Shigemura to rely on their own deeply ingrained ninja training."
    falcon.unlock_stage_id = 36

    eagle = Entity("Eagle", is_player=False)
    eagle.max_hp = 60
    k_eagle = Kata("Veteran Assassin", "Eagle", 1, 6, [0.9, 1.1, 1.1, 0.9, 1.0, 1.8, 1.8])
    ea1 = Skill("Pressuring", 1, EL_PHILAUTIA, 7, "[On Hit] Target will take +5 Final Damage from the next attack\n      [On Hit] Target deals -50% damage next turn", effect_type="EAGLE_SPECIAL_1")
    ea2 = Skill("Under Control", 2, EL_PHILAUTIA, 6, "[On Use] Gain 3 Poise Potency\n      [On Use] Gain 3 Poise Count\n      [On Hit] Inflict 2 Rupture Potency\n      [On Hit] Inflict 5 Rupture Count", effect_type="EAGLE_SPECIAL_2")
    ea3 = Skill("Tactical Retreat", 3, EL_STORGE, 10, "[On Use] Deal 0 damage, heal this unit’s ally with the lowest HP by supposed final damage amount, then heal the rest of this unit’s allies by half the healed amount (can include self)\n      [On Use] All of this unit’s allies gain 3 Haste next turn", effect_type="EAGLE_SPECIAL_3")
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

    # --- Riposte Gang & Misc ---
    hench = Entity("Unknown Faction Henchman", is_player=False)
    hench.max_hp = 75
    k_hench = Kata("Rapier Guard", "Henchman", 1, 3, [1.3, 1.1, 1.1, 1.1, 0.8, 0.8, 1.0])
    he1 = Skill("Pierce", 1, EL_LUDUS, 5, "[On Hit] Inflict 1 Pierce Affinity", effect_type="APPLY_STATUS")
    he1.status_effect = pierce_affinity_1
    he2 = Skill("Counter", 2, EL_EROS, 7, "[Combat Start] If this unit takes damage this turn, deal +20% damage next turn", effect_type="COUNTER_SKILL_TYPE1", effect_val=20)
    he3 = Skill("Brutal Counter", 3, EL_EROS, 8, "[Combat Start] If this unit takes damage this turn, deal +40% damage next turn\n      [On Hit] Inflict 2 Pierce Affinity", effect_type="COUNTER_SKILL_SPECIAL_TYPE1")
    k_hench.skill_pool_def = [(he1, 4), (he2, 3), (he3, 2)]
    hench.equip_kata(k_hench)
    hench.description = "These well-dressed captors guard Kagaku Shamiko’s hotel room, armed with thin rapiers and clad in identical sandy-colored long coats. Operating under strict orders not to harm their VIP prisoner, they become complacent and easily panicked when she fakes a choking emergency. This fatal hesitation allows a Kata-empowered Kagaku to swiftly dismantle them using nothing but a heavy silver breakfast tray and a broken broomstick."
    hench.unlock_stage_id = 38

    mascot = Entity("Deadly Laser Beam World-Threatening Monster", is_player=False)
    mascot.max_hp = 30
    k_mascot = Kata("Mascot Suit", "Monster", 1, 600, [1.0]*7)
    ma1 = Skill("“Thermal Laser Of Destruction”", 1, EL_AGAPE, 15520, "[Combat Start] Reduce this unit’s Kata Rift Aptitude to 0\n      [On Hit] Reduce Damage to 0", effect_type="JOKE_SKILL")
    ma2 = Skill("“Imprenetrable Armor Of The Abyssal Scale”", 2, EL_PRAGMA, 0, "[Combat Start] Reduce this unit’s Kata Rift Aptitude to 0\n      [Combat Start] This unit takes -12000 Final Damage from “Divine” element attacks\n      [Combat Start] This unit deals back %300 damage when taking “Darkness” element damage attacks")
    ma3 = Skill("“Roar Which Tears The Heavens”", 3, EL_EROS, 51000, "[Combat Start] Reduce this unit’s Kata Rift Aptitude to 0\n      [On Use] Targets all “Disbehaving Junior” units", effect_type="JOKE_SKILL")
    k_mascot.skill_pool_def = [(ma1, 3), (ma2, 3), (ma3, 3)]
    mascot.equip_kata(k_mascot)
    mascot.description = "Despite the terrifying title, this 'beast' is actually just an embarrassingly highly motivated Kasakura High senior sweating inside a cheap, goofy Godzilla mascot costume. Stationed in the tropical jungle during the island's Scavenger Hunt, he acts as the highly dramatic guardian of a marked coconut to test the students' teamwork. He possesses zero actual combat prowess, enthusiastically throwing himself to the ground in defeat after taking a single, slow-motion mock punch from Akasuke."
    mascot.unlock_stage_id = 39

    rip_hench = Entity("Riposte Gang Henchman", is_player=False)
    rip_hench.max_hp = 55
    k_rip_hench = Kata("Gang Henchman Rapier", "Riposte Henchman", 1, 4, [1.2, 1.1, 1.1, 1.1, 0.9, 0.9, 1.1])
    rh1 = Skill("Graceful Pierce", 1, EL_LUDUS, 7, "[On Hit] Inflict 1 Pierce Affinity", effect_type="APPLY_STATUS")
    rh1.status_effect = pierce_affinity_1
    rh2 = Skill("Elegant Counter", 2, EL_AGAPE, 6, "[Combat Start] If this unit takes damage this turn, deal +30% damage next turn\n      [On Hit] Inflict 3 Pierce Affinity", effect_type="COUNTER_SKILL_SPECIAL_TYPE3")
    rh3 = Skill("Riposte", 3, EL_STORGE, 10, "[On Use] Gain 10 Riposte\n      [On Hit] If target has Pierce Affinity, gain 10 Riposte", effect_type="RIPOSTE_GAIN_SPECIAL_1")
    k_rip_hench.skill_pool_def = [(rh1, 4), (rh2, 3), (rh3, 2)]
    rip_hench.equip_kata(k_rip_hench)
    rip_hench.description = "The standard foot soldiers of the notorious Absconder syndicate, these ruthless thugs flood the hotel corridors in their signature sandy coats. They fight using a highly dangerous, sacrificial counter-attacking style, willingly absorbing heavy blunt force trauma just to create a split-second opening for a lethal rapier thrust. Their unnatural toughness and sheer numbers make them incredibly dangerous to fight recklessly, forcing the Kasakura vanguard to rely on flawless, one-hit knockouts."
    rip_hench.unlock_stage_id = 41

    rip_lead = Entity("Riposte Gang Squad Leader", is_player=False)
    rip_lead.max_hp = 75
    k_rip_lead = Kata("Veteran Henchman Rapier", "Riposte Leader", 1, 6, [1.1, 1.0, 1.0, 1.2, 0.9, 0.9, 1.0])
    rl1 = Skill("Stylish Vital Pierce", 1, EL_EROS, 9, "[On Hit] If target has Pierce Affinity, inflict 2 Pierce Affinity. Otherwise, inflict 1 Pierce Affinity", effect_type="PIERCE_AFFINITY_INFLICT_SPECIAL_1")
    rl2 = Skill("Breakthrough", 2, EL_AGAPE, 9, "[Combat Start] All of this unit’s allies deal +4 Final Damage this turn\n      [On Use] Gain 10 Riposte\n      [On Hit] Inflict 2 Pierce Affinity", effect_type="RIPOSTE_SQUAD_LEADER_SPECIAL_1")
    rl3 = Skill("Balestra Riposte", 3, EL_LUDUS, 12, "[On Use] Fix this unit’s Riposte stack to 30\n      [On Hit] Inflict 3 Pierce Affinity", effect_type="RIPOSTE_SQUAD_LEADER_SPECIAL_2")
    k_rip_lead.skill_pool_def = [(rl1, 3), (rl2, 3), (rl3, 3)]
    rip_lead.equip_kata(k_rip_lead)
    rip_lead.description = "Seasoned veteran criminals of the underworld, these dark-coated enforcers lead the syndicate's defensive lines during the grueling hotel siege. Their rapier stances are significantly lower and more refined than the standard henchmen, allowing them to effortlessly parry and deliver devastating counter-strikes to vital points. Their overwhelming proficiency stalled the Kasakura strike team completely, forcing Akasuke to temporarily borrow their exact Kata just to beat them at their own ruthless game."
    rip_lead.unlock_stage_id = 41

    adam = Entity("Adam", is_player=False)
    adam.max_hp = 295
    k_adam = Kata("Executive Rapier", "Adam", 1, 9, [1.0, 1.0, 1.0, 1.15, 1.15, 1.0, 1.15])
    ad1 = Skill("En Garde", 1, EL_PRAGMA, 6, "[On Use] If this unit does not have Haste, gain 2 Haste next turn\n      [On Hit] Inflict 2 Pierce Affinity\n      [On Hit] Gain 10 Riposte", effect_type="ADAM_SPECIAL_1")
    ad2 = Skill("Advance-Lunge", 2, EL_LUDUS, 10, "[Combat Start] All of this unit’s allies deal +3 Final Damage this turn\n      [Combat Start] All of this unit’s allies take -2 Final Damage this turn\n      [On Hit] Gain 5 Riposte for every stack of Pierce Affinity the target has\n      [On Hit] Inflict 3 Pierce Affinity", effect_type="ADAM_SPECIAL_2")
    ad3 = Skill("Fleche Riposte (Incomplete)", 3, EL_LUDUS, 35, "[Combat Start] This unit takes +3 Final Damage this turn\n      [Combat Start] This unit deals -20 Base Damage this turn\n      [On Hit] Inflict 5 Pierce Affinity\n      [On Hit] Fix this unit’s Riposte stack to 50", effect_type="ADAM_SPECIAL_3")
    k_adam.skill_pool_def = [(ad1, 4), (ad2, 3), (ad3, 2)]
    adam.equip_kata(k_adam)
    adam.description = "A remarkably young and immensely talented Executive of the Riposte Gang, Adam flawlessly blends the grace of a high-class chef with the lethal precision of a master swordsman. He wields his rapier with terrifying perfection, capable of holding off six Kata-enhanced fighters simultaneously through sheer battle IQ and unnatural physical toughness before finally reaching his limit. Despite his criminal allegiance and composed demeanor, he possesses a surprisingly naive loyalty to his terrifying Boss and showed genuine, polite hospitality toward his captive."
    adam.unlock_stage_id = 42

    guard = Entity("Infiltrating Yunhai Border Guard", is_player=False)
    guard.max_hp = 62
    k_guard = Kata("Yunhai Guard", "Yunhai", 1, 1, [1.1, 0.8, 0.9, 1.2, 1.0, 1.0, 1.3])
    
    # Skill I: Metal Baton ◈ ◈
    s1_c1 = Chip(base_damage=2, effect_type="APPLY_STATUS")
    s1_c1.status_effect = scd.rupturecount_2
    s1_c2 = Chip(base_damage=3, effect_type="APPLY_STATUS")
    s1_c2.status_effect = scd.rupture_1
    
    s1_desc_brief = "[On Hit] Inflict Rupture Count and Rupture Potency"
    s1_desc_inspect = "◈ Base Damage: 2\n[On Hit] Inflict 2 Rupture Count\n◈ Base Damage: 3\n[On Hit] Inflict 1 Rupture Potency"
    
    g_s1 = ChipSkill("Metal Baton ◈ ◈", 1, EL_AGAPE, [s1_c1, s1_c2], description=s1_desc_brief, inspect_description=s1_desc_inspect)

    # Skill II: Pinning ◈ ◈
    s2_c1 = Chip(base_damage=5, effect_type="RUPTURE_DAMAGE_BUFF_TYPE2", effect_val=2)
    s2_c2 = Chip(base_damage=1, effect_type="APPLY_STATUS")
    s2_c2.status_effect = scd.rupture_2
    
    s2_desc_brief = "[On Hit] Inflict Rupture Potency, deals +Final Damage if target has Rupture"
    s2_desc_inspect = "◈ Base Damage: 5\n[On Hit] If target has Rupture, deal +2 Final Damage\n◈ Base Damage: 1\n[On Hit] Inflict 2 Rupture Potency"
    
    g_s2 = ChipSkill("Pinning ◈ ◈", 2, EL_STORGE, [s2_c1, s2_c2], description=s2_desc_brief, inspect_description=s2_desc_inspect)

    k_guard.skill_pool_def = [(g_s1, 4), (g_s2, 4)]
    guard.equip_kata(k_guard)
    guard.description = "infiltratingyunhaiborderguarddesc"
    guard.unlock_stage_id = 49

    # Append to existing return list in stages.py:
    return [thief, fresh, hool, lead, benikawa, ninja, double, slender, bulky, spike, chain, h_lead, upper, kuro, 
            sp_kiryoku, c_kiryoku, ayako, sumiko, inf_heiwa, inf_kiryoku, inf_kasa, inf_lead, hisayuki, inf_council, inf_disc, 
            raven, falcon, eagle, raven_inj, falcon_inj, hench, mascot, rip_hench, rip_lead, adam, guard]