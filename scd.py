from entities import Kata, Skill, ELEMENT_NAMES, EL_EROS, EL_PHILIA, EL_STORGE, EL_AGAPE, EL_LUDUS, EL_PRAGMA, EL_PHILAUTIA, StatusEffect
# Common Status Effects Definitions for easy reuse
bleed_1 = StatusEffect("Bleed", "[red]💧︎[/red]", 1, "Upon dealing damage, Take fixed damage equal to Potency, then reduce count by 1. Max Potency or Count: 99", duration=1, type="DEBUFF")
bleed_2 = StatusEffect("Bleed", "[red]💧︎[/red]", 2, "Upon dealing damage, Take fixed damage equal to Potency, then reduce count by 1. Max Potency or Count: 99", duration=1, type="DEBUFF")
bleed_3 = StatusEffect("Bleed", "[red]💧︎[/red]", 3, "Upon dealing damage, Take fixed damage equal to Potency, then reduce count by 1. Max Potency or Count: 99", duration=1, type="DEBUFF")
bleed_4 = StatusEffect("Bleed", "[red]💧︎[/red]", 4, "Upon dealing damage, Take fixed damage equal to Potency, then reduce count by 1. Max Potency or Count: 99", duration=1, type="DEBUFF")
bleedcount_1 = StatusEffect("Bleed", "[red]💧︎[/red]", 1, "Upon dealing damage, Take fixed damage equal to Potency, then reduce count by 1. Max Potency or Count: 99", duration=1, type="DEBUFF")
bleedcount_2 = StatusEffect("Bleed", "[red]💧︎[/red]", 1, "Upon dealing damage, Take fixed damage equal to Potency, then reduce count by 1. Max Potency or Count: 99", duration=2, type="DEBUFF")
bleedcount_3 = StatusEffect("Bleed", "[red]💧︎[/red]", 1, "Upon dealing damage, Take fixed damage equal to Potency, then reduce count by 1. Max Potency or Count: 99", duration=3, type="DEBUFF")
bind_1 = StatusEffect("Bind", "[dim gold1]⛓[/dim gold1]", 1, "Deal -(10*Count)% base damage with skills. Lose 1 count every new turn. Max Count: 5", duration=1, type="DEBUFF")
bind_2 = StatusEffect("Bind", "[dim gold1]⛓[/dim gold1]", 1, "Deal -(10%*Count) of base damage with skills. Lose 1 count every new turn. Max count: 5", duration=2, type="DEBUFF")
poise_1 = StatusEffect("Poise", "[light_cyan1]༄[/light_cyan1]", 1, "Boost Critical Hit chance by (Potency*5)% for the next 'Count' amount of hits. Max potency or count: 99", duration=0, type="BUFF")
poise_2 = StatusEffect("Poise", "[light_cyan1]༄[/light_cyan1]", 2, "Boost Critical Hit chance by (Potency*5)% for the next 'Count' amount of hits. Max potency or count: 99", duration=0, type="BUFF")
poise_3 = StatusEffect("Poise", "[light_cyan1]༄[/light_cyan1]", 3, "Boost Critical Hit chance by (Potency*5)% for the next 'Count' amount of hits. Max potency or count: 99", duration=0, type="BUFF")
poisecount_2 = StatusEffect("Poise", "[light_cyan1]༄[/light_cyan1]", 0, "Boost Critical Hit chance by (Potency*5)% for the next 'Count' amount of hits. Max potency or count: 99", duration=2, type="BUFF")
rupture_1 = StatusEffect("Rupture", "[medium_spring_green]✧[/medium_spring_green]", 1, "Upon getting hit by a skill, Take extra fixed damage equal to the amount of Potency, then reduce count by 1. Max Potency or Count: 99", duration=1, type="DEBUFF")
rupture_2 = StatusEffect("Rupture", "[medium_spring_green]✧[/medium_spring_green]", 2, "Upon getting hit by a skill, Take extra fixed damage equal to the amount of Potency, then reduce count by 1. Max Potency or Count: 99", duration=1, type="DEBUFF")
rupture_3 = StatusEffect("Rupture", "[medium_spring_green]✧[/medium_spring_green]", 3, "Upon getting hit by a skill, Take extra fixed damage equal to the amount of Potency, then reduce count by 1. Max Potency or Count: 99", duration=1, type="DEBUFF")
rupture_4 = StatusEffect("Rupture", "[medium_spring_green]✧[/medium_spring_green]", 4, "Upon getting hit by a skill, Take extra fixed damage equal to the amount of Potency, then reduce count by 1. Max Potency or Count: 99", duration=1, type="DEBUFF")
rupturecount_2 = StatusEffect("Rupture", "[medium_spring_green]✧[/medium_spring_green]", 1, "Upon getting hit by a skill, Take extra fixed damage equal to the amount of Potency, then reduce count by 1. Max Potency or Count: 99", duration=2, type="DEBUFF")
rupturecount_3 = StatusEffect("Rupture", "[medium_spring_green]✧[/medium_spring_green]", 1, "Upon getting hit by a skill, Take extra fixed damage equal to the amount of Potency, then reduce count by 1. Max Potency or Count: 99", duration=3, type="DEBUFF")
haste_1 = StatusEffect("Haste", "[yellow1]🢙[/yellow1]", 0, "Deal +(10*Count)% base damage with skills. Lose 1 count every new turn. Max count: 5", duration=1, type="BUFF")
fairylight_1 = StatusEffect("Fairylight", "[spring_green1]𒀭[/spring_green1]", 1, "Unique Rupture (Counts As Rupture)\nUpon getting hit by a skill, Take extra fixed damage equal to the amount of Fairylight Potency. On turn end, reduce Fairylight Count by half. Max Potency or Count: 99", duration=1, type="UNIQUEDEBUFF")
fairylight_2 = StatusEffect("Fairylight", "[spring_green1]𒀭[/spring_green1]", 2, "Unique Rupture (Counts As Rupture)\nUpon getting hit by a skill, Take extra fixed damage equal to the amount of Fairylight Potency. On turn end, reduce Fairylight Count by half. Max Potency or Count: 99", duration=1, type="UNIQUEDEBUFF")
fairylight_3 = StatusEffect("Fairylight", "[spring_green1]𒀭[/spring_green1]", 3, "Unique Rupture (Counts As Rupture)\nUpon getting hit by a skill, Take extra fixed damage equal to the amount of Fairylight Potency. On turn end, reduce Fairylight Count by half. Max Potency or Count: 99", duration=1, type="UNIQUEDEBUFF")
pierce_affinity_1 = StatusEffect("Pierce Affinity", "[light_yellow3]➾[/light_yellow3]", 0, "Take +Base Damage from any skill that can inflict Pierce Affinity and -Base Damage from any skill that cannot inflict Pierce Affinity based on stack amount. Upon getting hit by a skill, reduce count by 1. Max Count: 5", duration=1, type="DEBUFF")
pierce_affinity_2 = StatusEffect("Pierce Affinity", "[light_yellow3]➾[/light_yellow3]", 0, "Take +Base Damage from any skill that can inflict Pierce Affinity and -Base Damage from any skill that cannot inflict Pierce Affinity based on stack amount. Upon getting hit by a skill, reduce count by 1. Max Count: 5", duration=2, type="DEBUFF")
pierce_affinity_3 = StatusEffect("Pierce Affinity", "[light_yellow3]➾[/light_yellow3]", 0, "Take +Base Damage from any skill that can inflict Pierce Affinity and -Base Damage from any skill that cannot inflict Pierce Affinity based on stack amount. Upon getting hit by a skill, reduce count by 1. Max Count: 5", duration=3, type="DEBUFF")

# --- KATA ID REGISTRY ---
KATA_ID_MAP = {
    1: "Kasakura High School Student Akasuke",
    2: "Kasakura High School Student Yuri",
    3: "Kasakura High School Student Benikawa",
    4: "Kasakura High School Student Shigemura",
    5: "Kasakura High School Student Naganohara",
    6: "Heiwa Seiritsu High School Student Yuri",
    7: "Heiwa Seiritsu High School Student Naganohara",
    8: "‘Iron Fist Of Heiwa’ Delinquent Leader Akasuke",
    9: "Heiwa Seiritsu’s Upperclassman | ‘Crusher’ Benikawa",
    10: "Heiwa Seiritsu’s Upperclassman | ‘Chain Reaper Of Heiwa’ Shigemura",
    11: "Kasakura High School Disciplinary Committee President Yuri",
    12: "Kasakura High School Disciplinary Committee Member Benikawa",
    13: "Kasakura High School Disciplinary Committee Vice President Shigemura",
    14: "Kasakura High School Student Natsume",
    15: "Kasakura High School Student Hana",
    16: "Kasakura High School Student Kagaku",
    17: "Kiryoku Gakuen Self-Defense Club President",
    18: "Kiryoku Gakuen Student Council ‘Lesser Fairy’ Yuri",
    19: "Kiryoku Gakuen Student Council Fairy | ‘Forest Guardian’ Benikawa",
    20: "Kiryoku Gakuen Student Council Fairy | ‘Lake Strider’ Hana",
    21: "Heiwa Seiritsu Student – Goodwill Infiltrator Shigemura",
    22: "Riposte Gang Squad Leader Naganohara Tsukimiyama",
    23: "Riposte Gang Executive Hanefuji Akasuke"
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
    if name == "Kasakura High School Student Akasuke":
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
    elif name == "‘Iron Fist Of Heiwa’ Delinquent Leader Akasuke":
        res = [1.4, 0.7, 1.3, 0.7, 1.6, 1.6, 1.0]
        desc = (
            "Akasuke Hanefuji here has enrolled in Heiwa Seiritsu, embracing a reckless, dirty-fighting style honed "
            "in the school's violent environment. His crimson hair is longer, wilder, and unkempt, the eyepatch more "
            "prominent against a scarred, cocky grin, uniform untucked and battle-stained, radiating an aggressive, "
            "taunting aura that deliberately exploits embarrassing weaknesses in opponents.\n\n"
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
        desc_s3 = "[On Use] All allies deal +2 Final Damage this turn\n      [On Use] All allies from 'Heiwa Seiritsu' take -2 Final Damage this turn"
        s3 = Skill("Rally", 3, EL_EROS, 0, desc_s3, effect_type="HEIWA_RALLY_EFFECT", effect_val=2)
        k.skill_pool_def = [(s1, 5), (s2, 3), (s3, 1)]

        return {
            "kata_obj": k,
            "max_hp": 89,
            "description": desc
        }

    # --- YURI DEFAULT ---
    elif name == "Kasakura High School Student Yuri":
        desc = (
            "Inami Yuri is a student of Kasakura High School, one of the most renowned educational institutes of the east. She has silver hair tied into a ponytail, wears a white windbreaker jacket over a black tracksuit, and has clear sapphire blue eyes that are always beaming with confidence. Yuri’s hobbies include running and training as a judoka at her school’s club dojo, where she is also the club captain."
        )
        res = [1.0, 0.7, 1.3, 1.0, 0.7, 1.3, 1.0]
        k = Kata("Kasakura High School Student", "Yuri", 1, "I", res, desc)
        k.source_key = name      
        s1 = Skill("Steady Footing", 1, EL_LUDUS, 3, "")
        s2 = Skill("Iron Grip", 2, EL_STORGE, 7, "")
        s3 = Skill("Lock & Throw", 3, EL_PHILIA, 7, "[On Hit] Target deals -15% damage this turn", effect_type="DEBUFF_ATK_MULT", effect_val=0.85)
        k.skill_pool_def = [(s1, 5), (s2, 3), (s3, 1)]

        return {"kata_obj": k, "max_hp": 63, "description": desc}
    
# --- YURI HEIWA SEIRITSU ---
    elif name == "Heiwa Seiritsu High School Student Yuri":
        desc = (
            "Inami Yuri here has enrolled in Heiwa Seiritsu, fully embracing the school's brutal, weapon-heavy "
            "delinquent culture. Her silver ponytail is now let loose, streaked with dirt and blood from constant fights. "
            "She wears the Heiwa uniform in classic delinquent fashion: sleeves rolled up, shirt untucked, and often "
            "carries makeshift weapons that feel like Heiwa tradition—spiked metal bats slung over her shoulder or "
            "chains wrapped tightly around her fists for extra impact.\n\n"
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
    elif name == "Kasakura High School Disciplinary Committee President Yuri":
        desc = (
            "Inami Yuri leads Kasakura's Disciplinary Committee with a calm, calculating, and compassionate demeanor. "
            "Her silver ponytail is neatly tied back, sapphire eyes sharp yet serene, clad in a pristine white kimono "
            "adorned with youthful silver leaf and wave patterns; she wields Masayoshi Kouhei's exact wooden bokken, "
            "carrying spares tucked into her sash for prolonged battles.\n\n"
            "She speaks in an archaic, formal manner—precise, authoritative—while pushing subordinates with intense "
            "physical training regimens far beyond Masayoshi’s original ‘mindset’ focus, forging unbreakable bodies "
            "for her unique 'blitz' strategy: reckless, overwhelming rushes that catch foes off-guard and end fights "
            "in seconds alongside her Committee.\n\n"
            "Despite the stoic facade, she shows immense camaraderie and sportsmanship to all that she meets. "
            "Her deep, almost robotic respect for the Student Council President is unwavering, blending Yuri's loyalty "
            "with Kouhei's unyielding discipline into a formidable guardian of order."
        )
        res = [1.4, 1.0, 1.0, 1.1, 0.6, 0.4, 1.3]
        k = Kata("Kasakura High School Disciplinary Committee President", "Yuri", 4, "I", res, desc)
        k.source_key = name      
        s1 = Skill("Bokken Strike", 1, EL_PRAGMA, 5, "[On Use] Gain 3 Poise Potency", effect_type="GAIN_STATUS")
        s1.status_effect = poise_3
        s2 = Skill("Suriage", 2, EL_LUDUS, 7, "[On Use] Gain 2 Poise Count", effect_type="GAIN_STATUS")
        s2.status_effect = poisecount_2
        desc_s3 = "[On Use] Gain 2 Poise Potency\n      [On Hit] Gain 4 Poise Potency"
        s3 = Skill("Cascading Twin Cut", 3, EL_STORGE, 11, desc_s3, effect_type="GAIN_POISE_SPECIAL_1")
        k.skill_pool_def = [(s1, 5), (s2, 3), (s3, 1)]

        return {"kata_obj": k, "max_hp": 91, "description": desc}

    # --- BENIKAWA DEFAULT ---
    elif name == "Kasakura High School Student Benikawa":
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
    elif name == "Heiwa Seiritsu’s Upperclassman | ‘Crusher’ Benikawa":
        res = [0.9, 0.9, 0.9, 0.9, 1.7, 1.6, 1.6]
        desc = (
            "Ayame Benikawa here has long enrolled in Heiwa Seiritsu and rose on her own to become one of its feared "
            "‘Upperclassmen’ of the school’s legends. Her ginger hair is cropped short and messy, falling unevenly beside "
            "her face, and her purple eyes are cold, distant, almost careless—betraying none of the playful energy of "
            "her base form. She stands with a perpetual slouch, shoulders rounded, posture deliberately non-threatening "
            "until the moment she strikes, giving her an unpredictable, almost ghostly presence.\n\n"
            "Her body lacks the exaggerated bulk of someone like the original ‘Crusher’ “Upperclassman Tetsuo”, but "
            "every muscle is compact, dense, and terrifyingly efficient—honed through years of controlled, legitimate "
            "training rather than raw size. Her feats speak for themselves: bare fists shatter bones without effort, "
            "thin arms punch clean through plascrete walls, and single strikes crumple steel pipes. She fights with "
            "brutal, minimalist precision—quiet, emotionless, heartless—exploiting any opening with sudden, devastating "
            "force.\n\n"
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
    elif name == "Kasakura High School Disciplinary Committee Member Benikawa":
        res = [1.3, 1.2, 1.2, 0.8, 1.0, 1.0, 0.9]
        desc = (
            "Ayame Benikawa, a member of Kasakura High School’s Disciplinary Committee serves loyally under President Inami Yuri, who she dearly looks up to. "
            "Her ginger hair is tied in a neat, practical ponytail with a few loose strands framing her face, purple eyes sharp and focused rather than playful, exuding quiet respect and discipline. "
            "She wears a variant of the Disciplinary Committee white kimono uniform—similar in cut to Yuri's but with muted gray accents and fewer silver leaf/wave patterns to clearly denote her rank as one of many members; a wooden bokken is always at her side, polished and ready.\n\n"
            "Benikawa idolizes President Yuri's proficiency with the bokken, studying her techniques obsessively and aspiring to match her versatility—whether facing a single powerful opponent or swarms of fodder enemies. "
            "She loves fighting as fiercely as her base self, but maintains strict courtesy and self-control until combat begins—work and duty always come first.\n\n"
            "She fights with controlled aggression: precise bokken strikes, rapid counters, and disciplined footwork, preferring clean, efficient finishes over flashy displays. "
            "Beneath the formal exterior, her enthusiasm for battle still shines through in subtle grins and eager stances, but she channels it into protecting the committee and upholding Yuri's vision of order."
        )
        k = Kata("Kasakura High School Disciplinary Committee Member", "Benikawa", 2, "I", res, desc)
        k.source_key = name      
        s1 = Skill("Quick Draw", 1, EL_AGAPE, 4, "[On Use] Gain 2 Poise Potency", effect_type="GAIN_STATUS")
        s1.status_effect = poise_2
        s2 = Skill("Nuki Waza", 2, EL_PRAGMA, 5, "[On Hit] All allies (including self) with Poise gain 1 Poise Count", effect_type="ON_HIT_PROVIDE_POISE_TYPE1", effect_val=1)
        s3 = Skill("Zanshin", 3, EL_LUDUS, 8, "[On Hit] All allies (including self) with Poise gain 2 Poise Potency and 2 Poise Count", effect_type="ON_HIT_PROVIDE_POISE_TYPE2", effect_val=2)
        k.skill_pool_def = [(s1, 5), (s2, 3), (s3, 1)]

        return {"kata_obj": k, "max_hp": 79, "description": desc}

    # --- SHIGEMURA DEFAULT ---
    elif name == "Kasakura High School Student Shigemura":
        res = [1.4, 1.4, 0.8, 0.8, 0.8, 0.8, 0.8]
        desc = (
            "Fuyuyama Shigemura is a student of Kasakura High School, one of the most renowned educational institutes of the east. He has short, neatly trimmed brown hair that falls slightly over his sharp violet eyes, giving him a perpetually calm and detached appearance. Shigemura possesses a sharp mind and keen observational skills, often noticing details others miss, and carries himself with an air of quiet confidence that rarely breaks into overt emotion."
        )
        k = Kata("Kasakura High School Student", "Shigemura", 1, "I", res, desc)
        k.source_key = name
        s1 = Skill("Calibrated Strike", 1, EL_STORGE, 5, "")
        s2 = Skill("Block", 2, EL_LUDUS, 0, "[Combat Start] Take -4 Dmg this turn", effect_type="BUFF_DEF_FLAT", effect_val=4)
        s3 = Skill("Defensive Overhaul", 3, EL_AGAPE, 5, "[On Use] All allies take -3 Dmg this turn", effect_type="AOE_BUFF_DEF_FLAT", effect_val=3)
        k.skill_pool_def = [(s1, 5), (s2, 3), (s3, 1)]

        return {"kata_obj": k, "max_hp": 81, "description": desc} 

    # --- SHIGEMURA (HEIWA SEIRITSU) ---
    elif name == "Heiwa Seiritsu’s Upperclassman | ‘Chain Reaper Of Heiwa’ Shigemura":
        desc = (
            "Fuyuyama Shigemura has long enrolled in Heiwa Seiritsu and rose on his own to become one of its most "
            "feared ‘Upperclassmen’ of the school’s legends. His short brown hair is kept neat and disciplined, but "
            "his violet eyes are now colder, emptier—devoid of the usual detached occasional amusement, replaced by "
            "a quiet, sadistic patience. He slouches slightly, posture loose and unassuming, chains draped across "
            "his shoulders and wrapped around his arms like casual accessories, giving him an almost ghostly, "
            "unthreatening silhouette until he moves.\n\n"
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
            "For every 3 Base Damage reduced this way, inflict 1 Bind to target next turn."
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

    # --- SHIGEMURA KASAKURA DISCIPLINARY COMMITTEE ---
    elif name == "Kasakura High School Disciplinary Committee Vice President Shigemura":
        res = [1.5, 1.0, 1.0, 1.2, 0.7, 0.7, 1.2]
        desc = (
            "Fuyuyama Shigemura, the vice president of Kasakura High School’s Disciplinary Committee serves loyally under President Inami Yuri as her close colleague and trusted subordinate. "
            "His short brown hair remains neatly trimmed, violet eyes calm and observant, but with a subtle spark of quiet admiration when watching President Yuri demonstrate bokken techniques. "
            "He wears the same white kimono Disciplinary Committee uniform as Yuri and Benikawa, though with much restrained silver accents—fewer patterns and a darker gray trim to clearly mark him as a member of unique rank.\n\n"
            "Shigemura is ever impressed by President Yuri's mastery of the bokken, often sparring with Benikawa after hours to sharpen his own skills while keeping his energetic colleague entertained and challenged. "
            "He fights with precise, efficient movements—favoring controlled strikes and counters over flashy displays—yet his calm exterior hides a deep competitive drive to match Yuri's level. "
            "His dry wit and unflappable nature make him a steady presence among the committee's more intense members."
        )
        k = Kata("Kasakura High School Disciplinary Committee Vice President", "Shigemura", 3, "I", res, desc)
        k.source_key = name
        s1 = Skill("Wrist Strike", 1, EL_PHILIA, 5, "[On Use] Gain 2 Poise Count", effect_type="GAIN_STATUS")
        s1.status_effect = poisecount_2
        s2 = Skill("Debana Waza", 2, EL_LUDUS, 5, "[On Hit] All allies (including self) with Poise gain 2 Poise Potency", effect_type="ON_HIT_PROVIDE_POISE_TYPE3", effect_val=2)
        s3 = Skill("Kigurai", 3, EL_STORGE, 9, "[On Hit] All allies (including self) with 2+ Poise Potency convert 1 Poise Potency to Count", effect_type="ON_HIT_CONVERT_POISE_TYPE1", effect_val=1)
        k.skill_pool_def = [(s1, 5), (s2, 3), (s3, 1)]

        return {"kata_obj": k, "max_hp": 80, "description": desc}

    # --- NAGANOHARA DEFAULT ---
    elif name == "Kasakura High School Student Naganohara":
        res = [1.0, 0.7, 1.3, 1.5, 1.1, 0.7, 1.1] 
        desc = (
            "Naganohara Tsukimiyama is a student of Kasakura High School, one of the most renowned educational institutes of the east. She has bright pink twintails that bounce energetically with every movement and large, sparkling golden eyes full of life and mischief. Naganohara’s hobbies include dragging her friends into fun (and sometimes chaotic) group activities, collecting cute accessories, and being the loudest cheerleader in any situation. Despite her bubbly exterior, she is fiercely loyal and surprisingly perceptive when it comes to her friends’ feelings."
        )
        k = Kata("Kasakura High School Student", "Naganohara", 1, "I", res, desc)
        k.source_key = name      
        s1 = Skill("Flail Around", 1, EL_PHILAUTIA, 3, "[Combat Start] Take -2 Final Damage this turn", effect_type="BUFF_DEF_FLAT", effect_val=2)
        s2 = Skill("Cheer Up!", 2, EL_STORGE, 8, "[On Use] Deal 0 damage, then heal lowest HP ally by supposed final damage", effect_type="SPECIAL_CONVERT_DMG_TO_HEAL_LOWEST", effect_val=0)
        s3 = Skill("Unmatched Energetic Slam!", 3, EL_LUDUS, 5, "[On Hit] Heal lowest HP ally by damage amount", effect_type="ON_HIT_HEAL_LOWEST_BY_DMG", effect_val=0)        
        k.skill_pool_def = [(s1, 5), (s2, 3), (s3, 1)]

        return {"kata_obj": k, "max_hp": 58, "description": desc}   

    elif name == "Heiwa Seiritsu High School Student Naganohara":
        res = [1.1, 0.8, 0.8, 1.1, 1.5, 1.3, 1.5]
        desc = (
            "Naganohara Tsukimiyama here has enrolled in Heiwa Seiritsu High School instead of Kasakura High School. "
            "Her pink twintails are tied higher and messier, giving a wild, untamed look that matches her short-tempered, "
            "aggressive demeanor.\n\n"
            "She favors close-quarters brawling—sluggish but devastatingly clean hits that rely on raw power and momentum. "
            "Despite her hot-headed nature, she retains her loyalty to her friends, a large, rowdy crew of fellow Heiwa delinquents."
        )
        k = Kata("Heiwa Seiritsu High School Student", "Naganohara", 1, "I", res, desc)
        k.source_key = name
        s1 = Skill("Slugger Punch", 1, EL_STORGE, 7, "[On Hit] Inflict 1 Bleed Potency", effect_type="APPLY_STATUS")
        s1.status_effect = bleed_1
        s2 = Skill("Simmer Down", 2, EL_AGAPE, 8, "[On Hit] Deal +2 Final Damage against targets with Bleed", effect_type="COND_TARGET_HAS_BLEED_DMG", effect_val=2)
        desc_s3 = "[On Hit] Deal +4 Final Damage against targets with Bleed\n      [On Hit] Inflict 2 Bleed Count"
        s3 = Skill("One-Handed Throw Down", 3, EL_PHILIA, 8, desc_s3, effect_type="COND_BLEED_DMG_AND_APPLY", effect_val=4)
        s3.status_effect = bleedcount_2
        k.skill_pool_def = [(s1, 5), (s2, 3), (s3, 1)]

        return {
            "kata_obj": k,
            "max_hp": 75,
            "description": desc
        }

# --- NATSUME DEFAULT ---
    elif name == "Kasakura High School Student Natsume":
        res = [1.2, 1.1, 1.2, 1.1, 0.7, 0.5, 0.9]
        desc = (
            "Yokubukai Natsume is a student of Kasakura High School, one of the most renowned educational institutes of the east. She has messy dark hair, perpetually tired eyes from staring at glowing monitors, and prefers to wear oversized hoodies or cozy pajamas wrapped in blankets rather than her school uniform. Natsume’s hobbies include gathering intelligence, operating as the school's brilliant 'Queen of Information' from behind a screen, and avoiding any form of outdoor physical activity at all costs."
        )
        k = Kata("Kasakura High School Student Natsume", "Natsume", 1, "I", res, desc)
        k.source_key = name
        s1 = Skill("Taser Dart", 1, EL_PRAGMA, 2, "[On Hit] Inflict 2 Bind next turn", effect_type="APPLY_STATUS")
        s1.status_effect = bind_2
        s2 = Skill("Drone Thrash", 2, EL_PHILIA, 4, "[On Hit] Inflict 1 Bind next turn", effect_type="APPLY_STATUS")
        s2.status_effect = bind_1
        desc_s3 = "[On Use] 2 Other random allies gain 1 Haste next turn\n      [On Use] 2 Random enemies gain 1 Bind next turn"
        s3 = Skill("Comms Support", 3, EL_PRAGMA, 0, desc_s3, effect_type="HASTE_BIND_SPECIAL_TYPE1", effect_val=2)
        k.skill_pool_def = [(s1, 5), (s2, 3), (s3, 1)]

        return {"kata_obj": k, "max_hp": 58, "description": desc}

    # --- HANA DEFAULT ---
    elif name == "Kasakura High School Student Hana":
        res = [0.8, 1.2, 0.8, 0.7, 1.2, 1.0, 1.2]
        desc = (
            "Hana Kaoru is a student of Kasakura High School, one of the most renowned educational institutes of the east. She has soft, flowing hair and gentle, highly observant eyes that radiate warmth, compassion, and an unwavering calmness. Hana’s hobbies include practicing self-defense and aikido at the school dojo—where her elegant, momentum-shifting throws earn high praise from her juniors—and offering empathetic, grounded support to her peers without ever losing her composure."
        )
        k = Kata("Kasakura High School Student Hana", "Hana", 1, "I", res, desc)
        k.source_key = name
        s1 = Skill("Swift Backhand", 1, EL_STORGE, 3, "[On Use] Gain 1 Haste next turn", effect_type="GAIN_STATUS")
        s1.status_effect = haste_1
        s2 = Skill("Clean Throw", 2, EL_STORGE, 7, "")
        desc_s3 = "[On Use] This unit deals -40% damage next turn.\n      [On Hit] Target deals -15% damage this turn."
        s3 = Skill("Rage", 3, EL_EROS, 12, desc_s3, effect_type="HANA_SPECIAL_RAGE")
        k.skill_pool_def = [(s1, 5), (s2, 3), (s3, 1)]

        return {"kata_obj": k, "max_hp": 77, "description": desc}

    # --- KAGAKU DEFAULT ---
    elif name == "Kasakura High School Student Kagaku":
        res = [1.2, 1.3, 1.2, 1.0, 0.8, 0.9, 0.7]
        desc = (
            "Kagaku Shamiko is a student of Kasakura High School, one of the most renowned educational institutes of the east. She wears a slightly wrinkled white lab coat over her standard uniform, has unkempt hair from pulling frequent all-nighters, and sharp eyes that are constantly analyzing the mechanics of the world around her. Kagaku’s hobbies include drinking excessive amounts of coffee, inventing groundbreaking technology like the Parallaxis Scorer, and passionately theorizing about the scientific mysteries of the multiverse."
        )
        k = Kata("Kasakura High School Student Kagaku", "Kagaku", 1, "I", res, desc)
        k.source_key = name
        desc_s1 = "[On Hit] Inflict 1 Bleed Potency\n      [On Hit] Inflict 1 Rupture Potency"
        s1 = Skill("Acid Flask Throw", 1, EL_AGAPE, 3, desc_s1, effect_type="BLEED_RUPTURE_SPECIAL_TYPE1", effect_val=1)
        s2 = Skill("Wrench Smack", 2, EL_EROS, 5, "")
        s3 = Skill("Hanefuji Healing Serum", 3, EL_AGAPE, 8, "[On Use] Deal 0 damage, then heal lowest HP ally by supposed final damage", effect_type="SPECIAL_CONVERT_DMG_TO_HEAL_LOWEST", effect_val=0)
        k.skill_pool_def = [(s1, 5), (s2, 3), (s3, 1)]

        return {"kata_obj": k, "max_hp": 60, "description": desc}

    # --- NAGANOHARA KIRYOKU ---
    elif name == "Kiryoku Gakuen Self-Defense Club President":
        res = [0.8, 1.4, 1.1, 0.8, 1.0, 1.0, 1.3]
        desc = (
            "Naganohara Tsukimiyama here has enrolled in Kiryoku Gakuen and proudly stands as the President of its renowned Self-Defense Club. Her signature pink twintails are braided tightly into practical loops to stay out of the way during intense spars, and her large golden eyes shine with an unbreakable, almost terrifying level of optimism. She trades her usual Kasakura uniform for a pristine white martial arts gi worn over a Kiryoku athletic top, featuring a captain’s armband that commands instant, eager respect from her hundreds of club members.\n\n"
            "As the club's president, she embodies Kiryoku's unique battle culture to its absolute peak: she experiences absolutely no frustration, hesitation, or fear in combat, only pure, adrenaline-fueled joy. She fights with a dynamic, highly acrobatic self-defense style—effortlessly redirecting her opponent’s momentum for devastating throws, sweeping trips, and precise joint locks—all while maintaining a beaming, radiant smile.\n\n"
            "Her leadership relies on boundless enthusiasm rather than strict discipline. She constantly cheers on both her club members and her opponents mid-fight, offering loud praises and constructive tips even as she flips them onto the mats."
        )
        k = Kata("Kiryoku Gakuen Self-Defense Club President", "Naganohara", 2, "I", res, desc)
        k.source_key = name
        s1 = Skill("Crosspunch", 1, EL_PHILIA, 4, "[On Hit] Inflict 2 Rupture Potency", effect_type="APPLY_STATUS")
        s1.status_effect = rupture_2
        s2 = Skill("Motivation!", 2, EL_LUDUS, 5, "[On Use] Deal 0 damage, then heal self and 2 other random allies by supposed final damage", effect_type="SPECIAL_CONVERT_DMG_TO_HEAL_RANDOM", effect_val=2)
        desc_s3 = "[On Use] 2 Other random allies gain 1 Haste next turn\n      [On Hit] If target has Rupture, inflict 2 Rupture Count. Otherwise, inflict 3 Rupture Potency."
        s3 = Skill("Feverish Strikes", 3, EL_AGAPE, 8, desc_s3, effect_type="NAGANOHARA_KIRYOKU_SPECIAL")
        k.skill_pool_def = [(s1, 5), (s2, 3), (s3, 1)]

        return {"kata_obj": k, "max_hp": 78, "description": desc}

    # --- YURI KIRYOKU ---
    elif name == "Kiryoku Gakuen Student Council ‘Lesser Fairy’ Yuri":
        res = [1.0, 1.3, 1.3, 0.7, 1.1, 1.0, 1.2]
        desc = (
            "Inami Yuri here has enrolled in Kiryoku Gakuen, serving within the school’s unique authoritative system as a dedicated enforcer for the Student Council. While the core executive members of the council are revered simply as the 'Fairies,' the elite students who work directly beneath them to manage daily operations and security are officially dubbed 'Lesser Fairies' for easier distinction. She wears the stylish Kiryoku uniform adorned with a specialized turquoise council armband, her signature silver ponytail held up by an array of brightly colored, sparkly hairpins that starkly contrast her usual tomboyish Kasakura self.\n\n"
            "In this timeline, Yuri fully embraces the eccentric, passionate culture of Kiryoku, revealing herself to be an absolute sucker for all things adorable. Her ultimate obsession and the object of her endless, energetic fangirling is her esteemed Student Council President, the 'Queen of Fairies.' Yuri spends her downtime loudly praising the Queen’s overwhelming cuteness to anyone who will listen, fiercely dedicating her life to ensuring the President's peace remains undisturbed.\n\n"
            "Despite her star-struck demeanor, she retains her monstrous physical strength. As a Lesser Fairy, she handles the heavy lifting of council duties—quite literally—dispatching intruders and rule-breakers with flawless, bone-rattling judo throws and grapples. She executes these devastating takedowns with a bright smile, cheerfully apologizing to her opponents and often yelling about how she needs to finish the fight quickly so she can go buy limited-edition sweets for her beloved President."
        )
        k = Kata("Kiryoku Gakuen Student Council ‘Lesser Fairy’", "Yuri", 2, "I", res, desc)
        k.source_key = name
        s1 = Skill("Gauge Opponent", 1, EL_PHILAUTIA, 3, "[On Hit] If target has Rupture, inflict 2 Rupture Count. Otherwise, inflict 2 Rupture Potency.", effect_type="RUPTURE_SPECIAL1", effect_val=2)
        s2 = Skill("‘Fairy Wand’ Striking", 2, EL_STORGE, 7, "[On Hit] Inflict 3 Rupture Potency", effect_type="APPLY_STATUS")
        s2.status_effect = rupture_3
        s3 = Skill("Cutesy Styled Takedown", 3, EL_AGAPE, 10, "[On Hit] If target has Rupture, deal +25% damage.", effect_type="RUPTURE_DAMAGE_BUFF_TYPE1", effect_val=25)
        k.skill_pool_def = [(s1, 5), (s2, 3), (s3, 1)]

        return {"kata_obj": k, "max_hp": 70, "description": desc}

    # --- BENIKAWA KIRYOKU ---
    elif name == "Kiryoku Gakuen Student Council Fairy | ‘Forest Guardian’ Benikawa":
        res = [1.3, 1.1, 1.1, 0.7, 1.3, 1.2, 1.0]
        desc = (
            "Ayame Benikawa here has enrolled in Kiryoku Gakuen, ascending to the elite core of the Student Council as the feared and revered 'Fairy' known as the ‘Forest Guardian’. Trading her traditional karate dougi and hidden ninja gear for the elaborate, slightly fantastical uniform of the Kiryoku council, her caramel hair remains in its signature high ponytail, but her bright purple eyes now gleam with a feral, predatory intensity. Fully embracing Kiryoku's culture, this version of Benikawa is a huge fan of cute things, reserving her deepest affection for the Student Council President—her beloved ‘little sister’, the 'Queen of Fairies'. She fiercely coddles and protects the President at all costs.\n\n"
            "In combat, this Benikawa perfectly mirrors the battle-drunk nature of her original self, completely losing herself in the chaotic heat and thrill of a fight. She has largely abandoned former evasive ninja techniques in favor of wielding a solid oak bokken. Her fighting style is overwhelmingly direct, abandoning feints to rush her opponents in a straight, blindingly fast line to deliver singular, decisive strikes. However, her innate ninja battle IQ hasn't vanished; it manifests in her terrifying precision, allowing her straightforward heavy swings to effortlessly pinpoint and crush vital gaps in any defense. With a wild, fang-baring grin, she becomes an unstoppable force, joyfully dismantling anyone foolish enough to disturb her precious little sister's peace."
        )
        k = Kata("Kiryoku Gakuen Student Council Fairy | ‘Forest Guardian’", "Benikawa", 4, "I", res, desc)
        k.source_key = name
        s1 = Skill("Warning Draw", 1, EL_EROS, 3, "[On Hit] Inflict 3 Rupture Count", effect_type="APPLY_STATUS")
        s1.status_effect = rupturecount_3
        s2 = Skill("Close Distance", 2, EL_LUDUS, 8, "[On Hit] If target has Rupture, inflict 2 Fairylight", effect_type="FAIRYLIGHT_APPLY", effect_val=2)
        desc_s3 = "[On Hit] If target has Rupture, inflict 3 Fairylight\n      [On Use] This unit takes +50% damage this turn"
        s3 = Skill("Shukuchi (Incomplete) – Dash", 3, EL_PRAGMA, 16, desc_s3, effect_type="BENIKAWA_KIRYOKU_SPECIAL")
        k.skill_pool_def = [(s1, 5), (s2, 3), (s3, 1)]

        return {"kata_obj": k, "max_hp": 83, "description": desc}

    # --- HANA KIRYOKU ---
    elif name == "Kiryoku Gakuen Student Council Fairy | ‘Lake Strider’ Hana":
        res = [1.2, 0.7, 1.2, 0.9, 1.2, 1.0, 0.9]
        desc = (
            "Kaoru Hana here has enrolled in Kiryoku Gakuen, ascending to the prestigious core of the Student Council as the revered Fairy known as the ‘Lake Strider’. Retaining her soft, flowing blonde hair and signature gentle demeanor, she trades her Kasakura uniform for the elegant, specialized attire of a Kiryoku Fairy officer. Her highly observant eyes remain calm and unwavering, perfectly suited for a serene tactician who governs the battlefield with tranquil authority rather than raw aggression.\n\n"
            "Mirroring the original universe's ‘Lake Strider’ Sumiko, this version of Hana is a master of playing it safe and slow. She boasts exceptional spatial awareness, making the grueling task of maintaining her preferred distance against multiple rushing opponents look like a simple, effortless dance. She remains strictly on the defensive, gracefully sidestepping and parrying to exhaust her foes, deliberately wearing them down while her calm gaze calculates the perfect, undeniable opening.\n\n"
            "When that fatal moment presents itself, Hana executes 'Shukuchi'—an advanced footwork technique that allows her to cross the battlefield in an almost instantaneous glide. Though she humbly admits her mastery of Shukuchi is currently incomplete, she has vowed to endlessly refine her training until she fully unlocks its terrifying potential. For now, even in its imperfect state, this sudden, explosive burst of offensive acceleration allows the usually passive 'Lake Strider' to completely control the flow of combat, stepping in to end exhausting battles in a single, breathtaking instant."
        )
        k = Kata("Kiryoku Gakuen Student Council Fairy | ‘Lake Strider’", "Hana", 3, "I", res, desc)
        k.source_key = name
        s1 = Skill("Penetrating Defenses", 1, EL_PHILIA, 5, "[On Hit] If target has Rupture, inflict 1 Fairylight", effect_type="FAIRYLIGHT_APPLY", effect_val=1)
        s2 = Skill("Maintain Distance", 2, EL_AGAPE, 7, "[On Hit] If target has Fairylight, inflict 4 Rupture Potency", effect_type="FAIRYLIGHT_SPECIAL1", effect_val=4)
        desc_s3 = "[On Hit] If target has Fairylight, inflict 2 Rupture Count, then this unit takes -30% damage this turn"
        s3 = Skill("Shukuchi (Incomplete) – Engagement", 3, EL_STORGE, 13, desc_s3, effect_type="HANA_KIRYOKU_SPECIAL")
        k.skill_pool_def = [(s1, 5), (s2, 3), (s3, 1)]

        return {"kata_obj": k, "max_hp": 89, "description": desc}

    # --- SHIGEMURA INFILTRATOR ---
    elif name == "Heiwa Seiritsu Student – Goodwill Infiltrator Shigemura":
        res = [0.8, 0.9, 0.8, 1.3, 1.1, 1.1, 1.4]
        desc = (
            "Shigemura Fuyuyama here has enrolled in Heiwa Seiritsu High School, operating in the shadows as an infiltrator during the Four-School Joint Cruise Trip. He retains his neatly trimmed brow hair, sharp violet eyes, and signature nonchalant, quiet demeanor. Unlike the loud, extroverted brawlers typical of Heiwa Seiritsu, he carries himself with a chillingly calm detachment, assessing his surroundings with a calculated, unreadable gaze before making his move.\n\n"
            "In combat, this version of Shigemura abandons complex weaponry for a brutally kinetic fighting style: he is a lethal runner. Once he locks onto a target, he darts off in a chosen direction, refusing to stop his legs as he builds up terrifying acceleration and momentum. He weaponizes his own mass, throwing his entire body into opponents like an unstoppable human battering ram. To facilitate this relentless assault, his body boasts incomprehensible toughness. He absorbs heavy blows and crashes through steel walls with a blank expression, and will never go down in a straight contest of strength—the only way to halt his rampaging momentum is through underhanded dirty tricks or precise, guaranteed techniques that exploit the anatomical flaws of the human body.\n\n"
            "Despite his overwhelming physical durability and devastating tackle strikes, he calmly and humbly insists he is merely an 'ordinary student,' claiming to be nowhere near the realm of Heiwa's elite 'Upperclassmen'. His loyalty, however, is absolute. Instead of shouting robotic, military-style acknowledgments, he speaks maturely of his enigmatic 'Boss'—and his even more mysterious 'Boss's Boss'—with a quiet and profound respect. He executes their deeply secretive agendas without question, turning his unbreakable, unstoppable body into the perfect, silent instrument of their will."
        )
        k = Kata("Heiwa Seiritsu Student – Goodwill Infiltrator", "Shigemura", 3, "I", res, desc)
        k.source_key = name
        desc_s1 = "[On Use] If this unit has Haste, gain 1 Haste next turn\n      [On Hit] Gain 1 Haste next turn"
        s1 = Skill("Tough Knuckles", 1, EL_LUDUS, 6, desc_s1, effect_type="HASTE_GAIN_SPECIAL_TYPE1", effect_val=1)
        desc_s2 = "[On Use] Gain 1 Haste next turn\n      [On Hit] If this unit has Haste, deal +20% base damage, then this unit takes damage based on the amount increased"
        s2 = Skill("Low Tackle", 2, EL_PHILIA, 8, desc_s2, effect_type="SHIGEMURA_INFILTRATOR_SPECIAL_1")
        desc_s3 = "[On Hit] If this unit has Haste, deal +15% damage for every stack of Haste on self (Max +75%), then remove all Haste on self"
        s3 = Skill("Maximized Ram", 3, EL_EROS, 9, desc_s3, effect_type="SHIGEMURA_INFILTRATOR_SPECIAL_2")
        k.skill_pool_def = [(s1, 5), (s2, 3), (s3, 1)]

        return {"kata_obj": k, "max_hp": 90, "description": desc}

    # --- NAGANOHARA RIPOSTE ---
    elif name == "Riposte Gang Squad Leader Naganohara Tsukimiyama":
        res = [1.1, 1.1, 1.0, 1.2, 1.3, 0.8, 1.1]
        desc = (
            "Naganohara Tsukimiyama here has strayed far from the moral path, rising through the criminal underworld to become a deeply respected Squad Leader of the notorious Absconder syndicate, the Riposte Gang. She trades her Kasakura uniform for the gang’s signature dark sandy yellow long coat, her bright pink twintails tied back securely for combat. Her slender, fairly smaller-than-average build perfectly suits the syndicate's lethal fighting philosophy, making her an elusive and dangerously underestimated target in the middle of a chaotic battlefield.\n\n"
            "In combat, Naganohara abandons her usual close combat brawling methods for the refined, deadly art of the rapier. She is blindingly fast and surprisingly tough, obsessively focusing her entire battle IQ on reading her opponent to find the perfect counterattack. True to the Riposte way, she is unafraid of taking a hit, willingly enduring damage to create a fatal opening before stepping into her opponent's guard to deliver a singular, devastating thrust. Her ruthless efficiency and unshakeable nerve have earned her the absolute loyalty of her subordinates, whom she leads in everything from full-frontal gang war assaults to secretive kidnapping and smuggling operations around school grounds.\n\n"
            "Despite her hardened criminal lifestyle, Naganohara's mind is occupied by only two people. The first is Hanefuji Akasuke, who in this timeline is a young, immensely talented Executive of the Riposte Gang. Having survived the underworld much longer than him, she harbors a deep, quiet pity for Akasuke, lamenting that someone so young and gifted was dragged into such a dark life. The second is her enigmatic 'Boss,' who her subordinates often whisper that whenever she comes to visit, Naganohara’s ruthless gang-leader facade completely melts away, and she spends the entire day smiling with the same innocent, radiant joy she had on the very first day she was admitted into the syndicate."
        )
        k = Kata("Riposte Gang Squad Leader", "Naganohara", 4, "I", res, desc)
        k.source_key = name
        desc_s1 = "[On Use] Gain 5 Riposte\n      [On Hit] Inflict 1 Pierce Affinity"
        s1 = Skill("Appel", 1, EL_STORGE, 5, desc_s1, effect_type="NAGANOHARA_RIPOSTE_APPEL")
        desc_s2 = "[On Use] Gain 10 Riposte\n      [On Hit] If this unit has 20+ Riposte, deal +40% damage, then take +50% more damage this turn.\n      [On Hit] Inflict 2 Pierce Affinity"
        s2 = Skill("Cede", 2, EL_LUDUS, 9, desc_s2, effect_type="NAGANOHARA_RIPOSTE_CEDE")
        desc_s3 = "[On Use] If this unit has 25+ Riposte, fix Riposte stack count to 50. Otherwise, gain 20 Riposte\n      [On Hit] Inflict 3 Pierce Affinity"
        s3 = Skill("Counter-Parry", 3, EL_PHILIA, 13, desc_s3, effect_type="NAGANOHARA_RIPOSTE_COUNTERPARRY")
        k.skill_pool_def = [(s1, 5), (s2, 3), (s3, 1)]

        return {"kata_obj": k, "max_hp": 74, "description": desc}

    # --- AKASUKE RIPOSTE ---
    elif name == "Riposte Gang Executive Hanefuji Akasuke":
        res = [1.2, 1.0, 1.1, 1.0, 1.4, 0.7, 1.0]
        desc = (
            "Hanefuji Akasuke here has strayed far from the light of Kasakura High, ascending rapidly through the violent underworld to become a feared Executive of the Absconder syndicate, the Riposte Gang. Trading his school uniform for the gang’s signature sandy-colored long coat—though retaining his iconic eyepatch—he has adapted his peerless martial arts talent into the refined, lethal counter-attacking rapier style of his syndicate. Recognizing his immense strength and unnatural battle IQ, the older gang members revere him, ensuring the young prodigy accompanies them on every major operation. In return, Akasuke constantly pushes himself on the frontlines to build trust and earn the complete acceptance of his hardened colleagues.\n\n"
            "Despite his ruthless position, Akasuke’s daily life within the syndicate harbors a surprising warmth. Outside of combat, he utilizes his exceptional culinary skills to cook for his seniors, sharing meals with them daily and forging a twisted but genuine camaraderie. However, the constant exposure to the dark elements of the underground world takes a heavy, exhausting toll on the young executive. He knows his immense strength is used for grim tasks: securing secretive kidnapping routes, crippling rival gangsters to the point of permanent immobility, and intimidating completely innocent people. He understands this is simply his job as an executive, but the weight of his actions leaves him perpetually tired.\n\n"
            "Self-aware enough to know he still has much to learn about surviving this dark world, Akasuke relies heavily on the wisdom of his peers. He frequently seeks guidance from trusted veterans like Squad Leader Naganohara, who watches over him with a quiet, knowing pity. Above all, Akasuke idolizes the gang's mysterious 'Boss.' Whenever the enigmatic leader occasionally visits, Akasuke studies her flawless, overwhelming fighting prowess with absolute reverence, dedicating his blood, sweat, and unyielding loyalty to following exactly in her footsteps."
        )
        k = Kata("Riposte Gang Executive", "Akasuke", 4, "I", res, desc)
        k.source_key = name
        desc_s1 = "[On Use] If this unit does not have Riposte, gain 10 Riposte. Otherwise, gain 5 Riposte\n      [On Hit] Inflict 1 Pierce Affinity"
        s1 = Skill("En Garde", 1, EL_LUDUS, 7, desc_s1, effect_type="AKASUKE_RIPOSTE_ENGARDE")
        desc_s2 = "[On Use] Gain 1 Haste next turn\n      [On Use] If this unit has 10+ Riposte, Gain 1 Haste next turn\n      [On Hit] If target has Pierce Affinity, gain 10 Riposte\n      [On Hit] Inflict 2 Pierce Affinity"
        s2 = Skill("Feint", 2, EL_STORGE, 6, desc_s2, effect_type="AKASUKE_RIPOSTE_FEINT")
        desc_s3 = "This skill deals +2% base damage for each stack of Riposte owned (Max +100%)\n      [On Use] Gain 10 Riposte\n      [On Hit] Inflict 3 Pierce Affinity"
        s3 = Skill("Prise De Fer", 3, EL_LUDUS, 15, desc_s3, effect_type="AKASUKE_RIPOSTE_PRISEDEFER")
        # Custom Skill Pool setup based on prompt!
        k.skill_pool_def = [(s1, 4), (s2, 3), (s3, 2)]

        return {"kata_obj": k, "max_hp": 80, "description": desc}