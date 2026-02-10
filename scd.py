from entities import Kata, Skill, ELEMENT_NAMES, EL_EROS, EL_PHILIA, EL_STORGE, EL_AGAPE, EL_LUDUS, EL_PRAGMA, EL_PHILAUTIA, StatusEffect
# Common Status Effects Definitions for easy reuse
bleed_1 = StatusEffect("Bleed", "[red]💧︎[/red]", 1, "Upon dealing damage, Take fixed damage equal to amount of Potency, then reduce count by 1. Max Potency or Count: 99", duration=1, type="DEBUFF")
bleed_2 = StatusEffect("Bleed", "[red]💧︎[/red]", 2, "Upon dealing damage, Take fixed damage equal to amount of Potency, then reduce count by 1. Max Potency or Count: 99", duration=1, type="DEBUFF")
bleed_3 = StatusEffect("Bleed", "[red]💧︎[/red]", 3, "Upon dealing damage, Take fixed damage equal to amount of Potency, then reduce count by 1. Max Potency or Count: 99", duration=1, type="DEBUFF")
bleed_4 = StatusEffect("Bleed", "[red]💧︎[/red]", 4, "Upon dealing damage, Take fixed damage equal to amount of Potency, then reduce count by 1. Max Potency or Count: 99", duration=1, type="DEBUFF")
bleedcount_1 = StatusEffect("Bleed", "[red]💧︎[/red]", 1, "Upon dealing damage, Take fixed damage equal to amount of Potency, then reduce count by 1. Max Potency or Count: 99", duration=1, type="DEBUFF")
bleedcount_2 = StatusEffect("Bleed", "[red]💧︎[/red]", 1, "Upon dealing damage, Take fixed damage equal to amount of Potency, then reduce count by 1. Max Potency or Count: 99", duration=2, type="DEBUFF")
bleedcount_3 = StatusEffect("Bleed", "[red]💧︎[/red]", 1, "Upon dealing damage, Take fixed damage equal to amount of Potency, then reduce count by 1. Max Potency or Count: 99", duration=3, type="DEBUFF")
bind_1 = StatusEffect("Bind", "[dim gold1]⛓[/dim gold1]", 1, "Deal -(10%*Count) of base damage with skills. Lose 1 count every new turn. Max count: 5", duration=1, type="DEBUFF")
poise_1 = StatusEffect("Poise", "[light_cyan1]༄[/light_cyan1]", 1, "Boost Critical Hit chance by (Potency*5)% for the next 'Count' amount of hits. Max potency or count: 99", duration=0, type="BUFF")
poise_2 = StatusEffect("Poise", "[light_cyan1]༄[/light_cyan1]", 2, "Boost Critical Hit chance by (Potency*5)% for the next 'Count' amount of hits. Max potency or count: 99", duration=0, type="BUFF")
poise_3 = StatusEffect("Poise", "[light_cyan1]༄[/light_cyan1]", 3, "Boost Critical Hit chance by (Potency*5)% for the next 'Count' amount of hits. Max potency or count: 99", duration=0, type="BUFF")
poisecount_2 = StatusEffect("Poise", "[light_cyan1]༄[/light_cyan1]", 0, "Boost Critical Hit chance by (Potency*5)% for the next 'Count' amount of hits. Max potency or count: 99", duration=2, type="BUFF")

# --- KATA ID REGISTRY ---
KATA_ID_MAP = {
    1: "Akasuke (Default)",
    2: "Yuri (Default)",
    3: "Benikawa (Default)",
    4: "Shigemura (Default)",
    5: "Naganohara (Default)",
    6: "Heiwa Seiritsu High School Student (Yuri)",
    7: "Heiwa Seiritsu High School Student (Naganohara)",
    8: "‘Iron Fist Of Heiwa’ Delinquent Leader",
    9: "Heiwa Seiritsu’s Upperclassman | ‘Crusher’",
    10: "Heiwa Seiritsu’s Upperclassman | ‘Chain Reaper Of Heiwa’",
    11: "Kasakura High School Disciplinary Committee President",
    12: "Kasakura High School Disciplinary Committee Member"
}

KATA_NAME_TO_ID = {v: k for k, v in KATA_ID_MAP.items()}

def get_kata_data_by_name(name):
    """
    SCD = Stage Content Database
    The Central Database.
    Returns a dictionary: {"kata_obj": Kata, "max_hp": int, "description": str}
    Returns None if name not found.
    Note: Resistances: [Eros, Philia, Storge, Agape, Ludus, Pragma, Philautia]
    """

    # --- Akasuke DEFAULT ---
    if name == "Akasuke (Default)":
        res = [1.0, 1.0, 1.2, 0.8, 0.8, 1.0, 1.2]
        desc = (
            "Akasuke Hanefuji is a student of Kasakura High School, one of the most renowned educational institutes of the east. He wears a red coat with a white shirt underneath, black trousers, black tie and an eye patch over one of his red eyes, he has a strong sense of duty and protection for his peers. Akasuke’s hobbies include cooking and training as a karateka at his school’s club dojo, where he is also the club captain."
        )
        k = Kata("Kasakura High School Student", "Akasuke", 1, "I", res, desc)
        k.source_key = name      
        s1 = Skill("Fist Adjustment", 1, EL_STORGE, 4, "")
        s2 = Skill("Flicker Step", 2, EL_PRAGMA, 5, "[On Use] Take -2 Final Damage for the turn", effect_type="BUFF_DEF_FLAT", effect_val=2)
        s3 = Skill("Relentless Barrage", 3, EL_EROS, 8, "If the target has 50%- HP, deal +50% damage", effect_type="COND_EXECUTE", effect_val=1.5)
        k.skill_pool_def = [(s1, 5), (s2, 3), (s3, 1)]


        return {"kata_obj": k, "max_hp": 72, "description": desc}

    # --- Akasuke 'Iron Fist Of Heiwa' --- #
    elif name == "‘Iron Fist Of Heiwa’ Delinquent Leader":
        res = [1.4, 0.7, 1.3, 0.7, 1.6, 1.6, 1.0]
        desc = (
            "Akasuke Hanefuji here has enrolled in Heiwa Seiritsu, embracing a reckless, dirty-fighting style honed "
            "in the school's violent environment. His crimson hair is longer, wilder, and unkempt, the eyepatch more "
            "prominent against a scarred, cocky grin, uniform untucked and battle-stained, radiating an aggressive, "
            "taunting aura that deliberately exploits embarrassing weaknesses in opponents.\n"
            "He favors rapid, overwhelming flurries of jabs and punches to deny any chance of defense or counter, "
            "playing dirty with feints, low blows, and psychological taunts. When merged with original karate precision "
            "and fight theory, these become unconventional, yet lethal combos—turning raw aggression into a dangerously "
            "unpredictable and devastatingly effective style."
        )
        k = Kata("‘Iron Fist Of Heiwa’ Delinquent Leader", "Akasuke", 2, "I", res, desc)
        k.source_key = name      
        desc_s1 = "[On Hit] If target has no Bleed, Inflict 3 Bleed Count. Otherwise, inflict 1 Bleed Potency"
        s1 = Skill("Jab Flurry", 1, EL_AGAPE, 6, desc_s1, effect_type="BLEED_COUNT_OPENER", effect_val=3)
        s1.status_effect = bleedcount_3
        s1.alt_status_effect = bleed_1
        desc_s2 = "[On Hit] If target has Bleed, Inflict 3 Bleed Potency"
        s2 = Skill("Cheap Nose Shot", 2, EL_PRAGMA, 9, desc_s2, effect_type="BLEED_POTENCY_STACKER", effect_val=3)
        s2.status_effect = bleed_3
        # Base damage is 0 because this is a buff/utility skill
        desc_s3 = "[On Use] All allies deal +2 Final Damage this turn\n       [On Use] All allies from 'Heiwa Seiritsu' take -2 Final Damage this turn"
        s3 = Skill("Rally", 3, EL_EROS, 0, desc_s3, effect_type="HEIWA_RALLY_EFFECT", effect_val=2)
        k.skill_pool_def = [(s1, 5), (s2, 3), (s3, 1)]

        return {
            "kata_obj": k,
            "max_hp": 89,
            "description": desc
        }

    # --- YURI DEFAULT ---
    elif name == "Yuri (Default)":
        desc = (
            "Inami Yuri is a student of Kasakura High School, one of the most renowned educational institutes of the east. She has silver hair tied into a ponytail, wears a white windbreaker jacket over a black tracksuit, and has clear sapphire blue eyes that are always beaming with confidence. Yuri’s hobbies include running and training as a judoka at her school’s club dojo, where she is also the club captain."
        )
        res = [1.0, 0.7, 1.3, 1.0, 0.7, 1.3, 1.0]
        k = Kata("Kasakura High School Student", "Yuri", 1, "I", res, desc)
        k.source_key = name      
        s1 = Skill("Steady Footing", 1, EL_LUDUS, 3, "")
        s2 = Skill("Iron Grip", 2, EL_STORGE, 7, "")
        s3 = Skill("Lock & Throw", 3, EL_PHILIA, 7, "[On Hit] Target deals -15% damage for this turn", effect_type="DEBUFF_ATK_MULT", effect_val=0.85)
        k.skill_pool_def = [(s1, 5), (s2, 3), (s3, 1)]

        return {"kata_obj": k, "max_hp": 63, "description": desc}
    
# --- YURI HEIWA SEIRITSU ---
    elif name == "Heiwa Seiritsu High School Student (Yuri)":
        desc = (
            "Inami Yuri here has enrolled in Heiwa Seiritsu, fully embracing the school's brutal, weapon-heavy "
            "delinquent culture. Her silver ponytail is now let loose, streaked with dirt and blood from constant fights. "
            "She wears the Heiwa uniform in classic delinquent fashion: sleeves rolled up, shirt untucked, and often "
            "carries makeshift weapons that feel like Heiwa tradition—spiked metal bats slung over her shoulder or "
            "chains wrapped tightly around her fists for extra impact.\n"
            "Her fighting style is ferocious and pragmatic: experienced with improvised weapons, she swings spiked bats "
            "in wide, crushing arcs and uses chain-wrapped fists to deliver bone-breaking punches in close quarters. "
            "When weapons feel too predictable or 'not fun enough,' her judo roots take over—she seamlessly transitions "
            "to grapples, hip throws, and powerful slams, hurling opponents into walls, floors, or other fighters "
            "with ruthless force."
        )
        res = [0.5, 1.2, 1.5, 1.5, 0.7, 1.1, 1.4]
        k = Kata("Heiwa Seiritsu High School Student", "Yuri", 1, "I", res, desc)
        k.source_key = name      
        desc_s1 = "[On Hit] Inflict 2 Bleed Potency"
        s1 = Skill("Spike Bat Trick", 1, EL_EROS, 3, desc_s1, effect_type="APPLY_STATUS")
        s1.status_effect = bleed_2
        desc_s2 = "[On Hit] If target has Bleed, Inflict 3 Bleed Potency"
        s2 = Skill("Chained Throw", 2, EL_PHILAUTIA, 7, desc_s2, effect_type="BLEED_POTENCY_STACKER", effect_val=3)
        s2.status_effect = bleed_3
        desc_s3 = "[On Hit] Inflict 2 Bleed Potency\n[On Use] Take -3 Final Damage this turn"
        s3 = Skill("Metal Wrapped Knee", 3, EL_AGAPE, 7, desc_s3, effect_type="BLEED_POTENCY_DEF_BUFF", effect_val=3)
        s3.status_effect = bleed_2
        k.skill_pool_def = [(s1, 5), (s2, 3), (s3, 1)]

        return {
            "kata_obj": k,
            "max_hp": 70,
            "description": desc
        }

# --- YURI DISCIPLINARY COMMITTEE --- #
    elif name == "Kasakura High School Disciplinary Committee President":
        desc = (
            "Inami Yuri leads Kasakura's Disciplinary Committee with a calm, calculating, and compassionate demeanor. "
            "Her silver ponytail is neatly tied back, sapphire eyes sharp yet serene, clad in a pristine white kimono "
            "adorned with youthful silver leaf and wave patterns; she wields Masayoshi Kouhei's exact wooden bokken, "
            "carrying spares tucked into her sash for prolonged battles.\n"
            "She speaks in an archaic, formal manner—precise, authoritative—while pushing subordinates with intense "
            "physical training regimens far beyond Masayoshi’s original ‘mindset’ focus, forging unbreakable bodies "
            "for her unique 'blitz' strategy: reckless, overwhelming rushes that catch foes off-guard and end fights "
            "in seconds alongside her Committee.\n"
            "Despite the stoic facade, she shows immense camaraderie and sportsmanship to all that she meets. "
            "Her deep, almost robotic respect for the Student Council President is unwavering, blending Yuri's loyalty "
            "with Kouhei's unyielding discipline into a formidable guardian of order."
        )
        res = [1.4, 1.0, 1.0, 1.1, 0.6, 0.4, 1.3]
        k = Kata("Kasakura High School Disciplinary Committee President", "Yuri", 4, "I", res, desc)
        k.source_key = name      
        s1 = Skill("Bokken Strike", 1, EL_PRAGMA, 5, "[On Use] Gain 2 Poise Potency", effect_type="GAIN_STATUS")
        s1.status_effect = poise_2
        s2 = Skill("Suriage", 2, EL_LUDUS, 7, "[On Use] Gain 2 Poise Count", effect_type="GAIN_STATUS")
        s2.status_effect = poisecount_2
        desc_s3 = "[On Use] Gain 2 Poise Potency\n       [On Hit] Gain 4 Poise Potency"
        s3 = Skill("Cascading Twin Cut", 3, EL_STORGE, 11, desc_s3, effect_type="GAIN_POISE_SPECIAL_1")
        k.skill_pool_def = [(s1, 5), (s2, 3), (s3, 1)]

        return {"kata_obj": k, "max_hp": 91, "description": desc}

    # --- BENIKAWA DEFAULT ---
    elif name == "Benikawa (Default)":
        res = [1.3, 1.3, 0.7, 0.7, 0.9, 0.9, 1.0]
        desc = (
            "Benikawa Ayame is a student of Kasakura High School, known among her peers as a cheerful and highly talented member of the karate club. She wears a standard white karate dougi with a black belt tied firmly at the waist, caramel-colored hair pulled into a high ponytail, and bright purple eyes that sparkle with playful energy. Benikawa’s hobbies include practicing karate at the school dojo, where she often seeks out strong opponents for sparring, and exploring the city’s food stalls."
        )
        k = Kata("Kasakura High School Student", "Benikawa", 1, "I", res, desc)
        k.source_key = name      
        s1 = Skill("Palm Strike", 1, EL_PHILIA, 2, "If target >50% HP, deal +2 Dmg", effect_type="COND_HP_ABOVE_50_FLAT", effect_val=2)
        s2 = Skill("Roundhouse Kick", 2, EL_STORGE, 4, "")
        s3 = Skill("Vital Strike", 3, EL_PHILAUTIA, 8, "[On Hit] Target takes +4 Dmg from other attacks this turn", effect_type="DEBUFF_INCOMING_DMG_FLAT", effect_val=4)
        k.skill_pool_def = [(s1, 5), (s2, 3), (s3, 1)]

        return {"kata_obj": k, "max_hp": 70, "description": desc}

# --- BENIKAWA (HEIWA SEIRITSU) ---
    elif name == "Heiwa Seiritsu’s Upperclassman | ‘Crusher’":
        res = [0.9, 0.9, 0.9, 0.9, 1.7, 1.6, 1.6]
        desc = (
            "Ayame Benikawa here has long enrolled in Heiwa Seiritsu and rose on her own to become one of its feared "
            "‘Upperclassmen’ of the school’s legends. Her ginger hair is cropped short and messy, falling unevenly beside "
            "her face, and her purple eyes are cold, distant, almost careless—betraying none of the playful energy of "
            "her base form. She stands with a perpetual slouch, shoulders rounded, posture deliberately non-threatening "
            "until the moment she strikes, giving her an unpredictable, almost ghostly presence.\n"
            "Her body lacks the exaggerated bulk of someone like the original ‘Crusher’ “Upperclassman Tetsuo”, but "
            "every muscle is compact, dense, and terrifyingly efficient—honed through years of controlled, legitimate "
            "training rather than raw size. Her feats speak for themselves: bare fists shatter bones without effort, "
            "thin arms punch clean through plascrete walls, and single strikes crumple steel pipes. She fights with "
            "brutal, minimalist precision—quiet, emotionless, heartless—exploiting any opening with sudden, devastating "
            "force.\n"
            "She inherited Tetsuo’s mindset: weapon-users are weak, reliant on “little toys”; strip them of their tools, "
            "and they become ‘nothing’. Yet she holds quiet respect for those who remain strong with or without weapons—"
            "particularly Yuri’s spiked bat and Fuyuyama’s chains—acknowledging true power that transcends tools."
        )
        k = Kata("Heiwa Seiritsu’s Upperclassman | ‘Crusher’", "Benikawa", 3, "I", res, desc)
        k.source_key = name      
        desc_s1 = "[On Hit] Inflict 2 Bleed Potency\n[On Hit] Inflict 2 Bleed Count"
        s1 = Skill("Disarm", 1, EL_STORGE, 8, desc_s1, effect_type="APPLY_BLEED_HEAVY_STACKS")
        s1.status_effect = bleed_2
        s1.alt_status_effect = bleedcount_2
        desc_s2 = "[On Use] Take -30% Base Damage this turn"
        s2 = Skill("Unfaltering Presence", 2, EL_PRAGMA, 4, desc_s2, effect_type="DEF_BUFF_BASE_PER", effect_val=3)
        desc_s3 = "[On Hit] Deal +50% Base Damage against targets with Bleed"
        s3 = Skill("Crusher", 3, EL_STORGE, 11, desc_s3, effect_type="COND_TARGET_HAS_BLEED_DMG_PER", effect_val=5)
        k.skill_pool_def = [(s1, 5), (s2, 3), (s3, 1)]

        return {
            "kata_obj": k,
            "max_hp": 90,
            "description": desc
        }

    # --- BENIKAWA (KASAKURA DISCIPLINARY COMMITTEE) ---
    elif name == "Kasakura High School Disciplinary Committee Member":
        res = [1.3, 1.2, 1.2, 0.8, 1.0, 1.0, 0.9]
        desc = (
            "Ayame Benikawa, a member in Kasakura High School’s Disciplinary Committee serves loyally under President Inami Yuri, who she dearly looks up to. "
            "Her ginger hair is tied in a neat, practical ponytail with a few loose strands framing her face, purple eyes sharp and focused rather than playful, exuding quiet respect and discipline. "
            "She wears a variant of the Disciplinary Committee white kimono uniform—similar in cut to Yuri's but with muted gray accents and fewer silver leaf/wave patterns to clearly denote her rank as one of many members; a wooden bokken is always at her side, polished and ready.\n"
            "Benikawa idolizes President Yuri's proficiency with the bokken, studying her techniques obsessively and aspiring to match her versatility—whether facing a single powerful opponent or swarms of fodder enemies. "
            "She loves fighting as fiercely as her base self, but maintains strict courtesy and self-control until combat begins—work and duty always come first.\n"
            "She fights with controlled aggression: precise bokken strikes, rapid counters, and disciplined footwork, preferring clean, efficient finishes over flashy displays. "
            "Beneath the formal exterior, her enthusiasm for battle still shines through in subtle grins and eager stances, but she channels it into protecting the committee and upholding Yuri's vision of order."
        )
        k = Kata("Kasakura High School Disciplinary Committee Member", "Benikawa", 2, "I", res, desc)
        k.source_key = name      
        s1 = Skill("Quick Draw", 1, EL_AGAPE, 4, "[On Use] Gain 3 Poise Potency", effect_type="GAIN_STATUS")
        s1.status_effect = poise_3
        s2 = Skill("Nuki Waza", 2, EL_PRAGMA, 5, "[On Hit] All allies (including self) with Poise gain 1 Poise Count", effect_type="ON_HIT_PROVIDE_POISE_TYPE1", effect_val=1)
        s3 = Skill("Zanshin", 3, EL_LUDUS, 8, "[On Hit] All allies (including self) with Poise gain 2 Poise Potency and 2 Poise Count", effect_type="ON_HIT_PROVIDE_POISE_TYPE2", effect_val=2)
        k.skill_pool_def = [(s1, 5), (s2, 3), (s3, 1)]

        return {"kata_obj": k, "max_hp": 79, "description": desc}

    # --- SHIGEMURA DEFAULT ---
    elif name == "Shigemura (Default)":
        res = [1.4, 1.4, 0.8, 0.8, 0.8, 0.8, 0.8]
        desc = (
            "Fuyuyama Shigemura is a student of Kasakura High School, one of the most renowned educational institutes of the east. He has short, neatly trimmed purple hair that falls slightly over his sharp violet eyes, giving him a perpetually calm and detached appearance. Shigemura possesses a sharp mind and keen observational skills, often noticing details others miss, and carries himself with an air of quiet confidence that rarely breaks into overt emotion."
        )
        k = Kata("Kasakura High School Student", "Shigemura", 1, "I", res, desc)
        k.source_key = name
        s1 = Skill("Calibrated Strike", 1, EL_STORGE, 5, "")
        s2 = Skill("Block", 2, EL_LUDUS, 0, "[Combat Start] Take -4 Dmg this turn", effect_type="BUFF_DEF_FLAT", effect_val=4)
        s3 = Skill("Defensive Overhaul", 3, EL_AGAPE, 5, "[On Use] All allies take -3 Dmg this turn", effect_type="AOE_BUFF_DEF_FLAT", effect_val=3)
        k.skill_pool_def = [(s1, 5), (s2, 3), (s3, 1)]

        return {"kata_obj": k, "max_hp": 81, "description": desc} 

    # --- SHIGEMURA (HEIWA SEIRITSU) ---
    elif name == "Heiwa Seiritsu’s Upperclassman | ‘Chain Reaper Of Heiwa’":
        desc = (
            "Fuyuyama Shigemura has long enrolled in Heiwa Seiritsu and rose on his own to become one of its most "
            "feared ‘Upperclassmen’ of the school’s legends. His short brown hair is kept neat and disciplined, but "
            "his violet eyes are now colder, emptier—devoid of the usual detached occasional amusement, replaced by "
            "a quiet, sadistic patience. He slouches slightly, posture loose and unassuming, chains draped across "
            "his shoulders and wrapped around his arms like casual accessories, giving him an almost ghostly, "
            "unthreatening silhouette until he moves.\n"
            "Despite inheriting the title ‘Chain Reaper,’ his personality remains eerily calm and composed—opposite "
            "the hotheaded, egotistic original “Upperclassman Kurogane”—making him far more threatening. He rarely "
            "speaks, rarely smiles; the only time his lips curve is when facing truly strong opponents, and only "
            "after he has broken them. He delights in torture—deliberate, methodical—using chains to leave precise, "
            "lingering marks, keeping victims conscious and in agony for as long as possible purely for his quiet "
            "satisfaction. He wraps chains around his own body to reinforce limbs, turning punches and grapples into "
            "bone-shattering impacts, or lashes them out with surgical precision to whip, bind, and reposition "
            "enemies at will."
        )
        res = [1.4, 1.1, 0.9, 1.4, 1.0, 1.1, 1.2]
        k = Kata("Heiwa Seiritsu’s Upperclassman | ‘Chain Reaper Of Heiwa’", "Shigemura", 4, "I", res, desc)
        k.source_key = name      
        desc_s1 = "[On Hit] Inflict 4 Bleed Potency"
        s1 = Skill("Chained Body Martial Arts", 1, EL_AGAPE, 7, desc_s1, effect_type="APPLY_STATUS")
        s1.status_effect = bleed_4
        # Logic: COND_REAPER_BLEED_SPECIAL (+40% Base at 2 Count, +40% at 5 Count)
        desc_s2 = (
            "[On Hit] Deal +40% Base Damage against targets with 2+ Bleed Count\n"
            "[On Hit] Deal Another +40% Base Damage against targets with 5+ Bleed Count"
        )
        s2 = Skill("Dual Lashing", 2, EL_LUDUS, 7, desc_s2, effect_type="COND_REAPER_BLEED_SPECIAL")
        # Logic: COND_REAPER_BIND_CONVERT_SPECIAL (Reduce dmg based on bleed total -> Apply Bind)
        desc_s3 = (
            "[On Hit] Deal -3 Base Damage for every 3 Bleed (Potency + Count) on target. (Max -9 Base Damage)\n"
            "For every 3 Base Damage reduced this way, also inflict 1 Bind to target."
        )
        s3 = Skill("Sadism", 3, EL_EROS, 13, desc_s3, effect_type="COND_REAPER_BIND_CONVERT_SPECIAL")
        s3.status_effect = bind_1 # Attached for the logic to grab
        # Deck Distribution (Custom: 3x S1, 4x S2, 2x S3)
        k.skill_pool_def = [(s1, 3), (s2, 4), (s3, 2)]

        return {
            "kata_obj": k,
            "max_hp": 80,
            "description": desc
        }

    # --- NAGANOHARA DEFAULT ---
    elif name == "Naganohara (Default)":
        res = [1.0, 0.7, 1.3, 1.5, 1.1, 0.7, 1.1] 
        desc = (
            "Naganohara Tsukimiyama is a student of Kasakura High School, one of the most renowned educational institutes of the east. She has bright pink twintails that bounce energetically with every movement and large, sparkling golden eyes full of life and mischief. Naganohara’s hobbies include dragging her friends into fun (and sometimes chaotic) group activities, collecting cute accessories, and being the loudest cheerleader in any situation. Despite her bubbly exterior, she is fiercely loyal and surprisingly perceptive when it comes to her friends’ feelings."
        )
        k = Kata("Kasakura High School Student", "Naganohara", 1, "I", res, desc)
        k.source_key = name      
        s1 = Skill("Flail Around", 1, EL_PHILAUTIA, 3, "[Combat Start] Take -2 Final Damage this turn", effect_type="BUFF_DEF_FLAT", effect_val=2)
        s2 = Skill("Cheer Up!", 2, EL_STORGE, 8, "[On Use] Deal 0 damage, then heal lowest HP ally by supposed base damage.", effect_type="SPECIAL_CONVERT_DMG_TO_HEAL_LOWEST", effect_val=0)
        s3 = Skill("Unmatched Energetic Slam!", 3, EL_LUDUS, 5, "[On Hit] Heal lowest HP ally by damage amount", effect_type="ON_HIT_HEAL_LOWEST_BY_DMG", effect_val=0)        
        k.skill_pool_def = [(s1, 5), (s2, 3), (s3, 1)]

        return {"kata_obj": k, "max_hp": 58, "description": desc}   

    elif name == "Heiwa Seiritsu High School Student (Naganohara)":
        res = [1.1, 0.8, 0.8, 1.1, 1.5, 1.3, 1.5]
        desc = (
            "Naganohara Tsukimiyama here has enrolled in Heiwa Seiritsu High School instead of Kasakura High School. "
            "Her pink twintails are tied higher and messier, giving a wild, untamed look that matches her short-tempered, "
            "aggressive demeanor.\n"
            "She favors close-quarters brawling—sluggish but devastatingly clean hits that rely on raw power and momentum. "
            "Despite her hot-headed nature, she retains her loyalty to her friends, a large, rowdy crew of fellow Heiwa delinquents."
        )
        k = Kata("Heiwa Seiritsu High School Student", "Naganohara", 1, "I", res, desc)
        k.source_key = name
        s1 = Skill("Slugger Punch", 1, EL_STORGE, 7, "[On Hit] Inflict 1 Bleed Potency", effect_type="APPLY_STATUS")
        s1.status_effect = bleed_1
        s2 = Skill("Simmer Down", 2, EL_AGAPE, 8, "[On Hit] Deal +2 Final Damage against targets with Bleed", effect_type="COND_TARGET_HAS_BLEED_DMG", effect_val=2)
        desc_s3 = "[On Hit] Deal +4 Final Damage against targets with Bleed\n       [On Hit] Inflict 2 Bleed Count"
        s3 = Skill("One-Handed Throw Down", 3, EL_PHILIA, 8, desc_s3, effect_type="COND_BLEED_DMG_AND_APPLY", effect_val=4)
        s3.status_effect = bleedcount_2
        k.skill_pool_def = [(s1, 5), (s2, 3), (s3, 1)]

        return {
            "kata_obj": k,
            "max_hp": 75,
            "description": desc
        }