import copy
from entities import Entity, Kata, Skill, StatusEffect
from entities import EL_EROS, EL_PHILIA, EL_STORGE, EL_AGAPE, EL_LUDUS, EL_PRAGMA, EL_PHILAUTIA
import config
import scd
from player_state import player

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
        enemies.append(spawn("Heiwa Seiritsu Upperclassman Fighter"))

    elif stage_id == 21:
        enemies.append(spawn("‘Chain Reaper Of Heiwa’ Kurogane"))

    # Return ignoring any potential NoneType errors from typos in db
    return [e for e in enemies if e is not None]

def get_enemy_database():
    # Existing enemies...
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
    ls2 = Skill("Block", 2, EL_LUDUS, 0, "[Combat Start] Take -4 Final Damage this turn.")
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

    # --- NEW ENEMIES DATABASE ENTRIES ---
    spike = Entity("Spike Bat Heiwa Seiritsu Delinquent", is_player=False)
    spike.max_hp = 30
    res_sp = [1.1, 1.6, 1.1, 1.2, 1.6, 1.6, 1.1]
    k_spike = Kata("Spike Bat Style", "Delinquent", 1, "0", res_sp)
    spi1 = Skill("Knock", 1, EL_STORGE, 5, "")
    spi2 = Skill("Sharp Swing", 2, EL_EROS, 5, "[On Hit] Inflict 1 Bleed Potency")
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
    ch2 = Skill("Cutting Fist", 2, EL_PRAGMA, 3, "[On Hit] Inflict 2 Bleed Potency")
    k_chain.skill_pool_def = [(ch1, 5), (ch2, 4)]
    k_chain.rift_aptitude = 0
    chain.equip_kata(k_chain)
    chain.description = "An older Heiwa Seiritsu thug student that wraps old metal chains around their fists which prove effective in leaving cuts when swung roughly enough at an opponent."
    chain.unlock_stage_id = 15

    h_lead = Entity("Heiwa Seiritsu Delinquent Leader Fighter", is_player=False)
    h_lead.max_hp = 40
    res_hl = [1.7, 1.7, 1.3, 1.3, 1.3, 1.3, 1.3]
    k_hlead = Kata("Leader Style", "Leader", 1, "0", res_hl)
    hl1 = Skill("Headbutting", 1, EL_PHILIA, 5, "[On Hit] Inflict 1 Bleed Potency")
    hl2 = Skill("Chained Bat Combo", 2, EL_PRAGMA, 5, "[On Hit] Inflict 2 Bleed Potency")
    hl3 = Skill("Rally", 3, EL_PRAGMA, 0, "[On Use] All allied units take +1 Final Damage this turn")
    k_hlead.skill_pool_def = [(hl1, 4), (hl2, 3), (hl3, 2)]
    k_hlead.rift_aptitude = 1
    h_lead.equip_kata(k_hlead)
    h_lead.description = "A more experienced Heiwa Seiritsu thug student who has enough respect and proficiency with makeshift weapons to lead a small unit of thugs."
    h_lead.unlock_stage_id = 18

    upper = Entity("Heiwa Seiritsu Upperclassman Fighter", is_player=False)
    upper.max_hp = 1523
    res_up = [1.0, 1.2, 1.0, 1.1, 1.1, 1.2, 0.7]
    k_up = Kata("Upperclassman Style", "Upperclassman", 1, "0", res_up)
    u1 = Skill("Chained Limb Combo", 1, EL_LUDUS, 14, "[On Hit] Inflict 2 Bleed Potency")
    u2 = Skill("Chain Whip", 2, EL_AGAPE, 15, "[On Hit] Inflict 3 Bleed Potency")
    u3 = Skill("Pull In And Thrash", 3, EL_AGAPE, 17, "[On Hit] Inflict 1 Bind next turn")
    k_up.skill_pool_def = [(u1, 3), (u2, 3), (u3, 3)]
    k_up.rift_aptitude = 5
    upper.equip_kata(k_up)
    upper.description = "One of Heiwa Seiritsu’s “Upperclassman” elite fighters from the legends told throughout campus. They are highly experienced veterans who follow the most brutal combat mindsets and calculatingly fight with their specialty weapons."
    upper.unlock_stage_id = 20

    kuro = Entity("‘Chain Reaper Of Heiwa’ Kurogane", is_player=False)
    kuro.max_hp = 150
    res_ku = [1.3, 1.3, 1.1, 1.6, 1.6, 1.1, 1.6]
    k_ku = Kata("Reaper Style", "Kurogane", 1, "0", res_ku)
    ku1 = Skill("Chained Limb Flurry", 1, EL_PRAGMA, 5, "[On Hit] Inflict 2 Bleed Potency\n     [On Hit] Inflict 2 Bleed Count")
    ku2 = Skill("Heavy Chain Whip", 2, EL_AGAPE, 6, "[On Hit] Inflict 3 Bleed Potency\n     [On Hit] Inflict 1 Bind next turn")
    ku3 = Skill("Pull In For A Beatdown", 3, EL_AGAPE, 8, "[On Hit] Inflict 3 Bleed Potency\n       [On Hit] Inflict 2 Bind next turn")
    k_ku.skill_pool_def = [(ku1, 3), (ku2, 4), (ku3, 2)]
    k_ku.rift_aptitude = 6
    kuro.equip_kata(k_ku)
    kuro.description = "The true identity of the Heiwa Seiritsu Upperclassman: “Chain Reaper Of  Heiwa” Kurogane, has been revealed. A veteran hotblooded gangster on the run who tortures his opponents with masterful chain movements paired with his reckless fighting style. His motives are taking down Kasakura’s key figures and extracting information about the existence of “Katas”."
    kuro.unlock_stage_id = 21

    return [thief, fresh, hool, lead, benikawa, ninja, double, slender, bulky, spike, chain, h_lead, upper, kuro]