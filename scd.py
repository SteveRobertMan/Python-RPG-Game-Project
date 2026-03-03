from entities import Kata, Skill, ELEMENT_NAMES, STATUS_DESCS, EL_EROS, EL_PHILIA, EL_STORGE, EL_AGAPE, EL_LUDUS, EL_PRAGMA, EL_PHILAUTIA, StatusEffect, Chip, ChipSkill
# Common Status Effects Definitions for easy reuse
bleed_1 = StatusEffect("Bleed", "[red]💧︎[/red]", 1, STATUS_DESCS["Bleed"], duration=1, type="DEBUFF")
bleed_2 = StatusEffect("Bleed", "[red]💧︎[/red]", 2, STATUS_DESCS["Bleed"], duration=1, type="DEBUFF")
bleed_3 = StatusEffect("Bleed", "[red]💧︎[/red]", 3, STATUS_DESCS["Bleed"], duration=1, type="DEBUFF")
bleed_4 = StatusEffect("Bleed", "[red]💧︎[/red]", 4, STATUS_DESCS["Bleed"], duration=1, type="DEBUFF")
bleed_8 = StatusEffect("Bleed", "[red]💧︎[/red]", 8, STATUS_DESCS["Bleed"], duration=1, type="DEBUFF")
bleedcount_1 = StatusEffect("Bleed", "[red]💧︎[/red]", 1, STATUS_DESCS["Bleed"], duration=1, type="DEBUFF")
bleedcount_2 = StatusEffect("Bleed", "[red]💧︎[/red]", 1, STATUS_DESCS["Bleed"], duration=2, type="DEBUFF")
bleedcount_3 = StatusEffect("Bleed", "[red]💧︎[/red]", 1, STATUS_DESCS["Bleed"], duration=3, type="DEBUFF")
bind_1 = StatusEffect("Bind", "[gold1]⛓[/gold1]", 1, STATUS_DESCS["Bind"], duration=1, type="DEBUFF")
bind_2 = StatusEffect("Bind", "[gold1]⛓[/gold1]", 1, STATUS_DESCS["Bind"], duration=2, type="DEBUFF")
bind_3 = StatusEffect("Bind", "[gold1]⛓[/gold1]", 1, STATUS_DESCS["Bind"], duration=3, type="DEBUFF")
bind_4 = StatusEffect("Bind", "[gold1]⛓[/gold1]", 1, STATUS_DESCS["Bind"], duration=4, type="DEBUFF")
haste_1 = StatusEffect("Haste", "[yellow1]🢙[/yellow1]", 0, STATUS_DESCS["Haste"], duration=1, type="BUFF")
poise_1 = StatusEffect("Poise", "[light_cyan1]༄[/light_cyan1]", 1, STATUS_DESCS["Poise"], duration=1, type="BUFF")
poise_2 = StatusEffect("Poise", "[light_cyan1]༄[/light_cyan1]", 2, STATUS_DESCS["Poise"], duration=1, type="BUFF")
poise_3 = StatusEffect("Poise", "[light_cyan1]༄[/light_cyan1]", 3, STATUS_DESCS["Poise"], duration=1, type="BUFF")
poisecount_2 = StatusEffect("Poise", "[light_cyan1]༄[/light_cyan1]", 0, STATUS_DESCS["Poise"], duration=2, type="BUFF")
poisecount_3 = StatusEffect("Poise", "[light_cyan1]༄[/light_cyan1]", 0, STATUS_DESCS["Poise"], duration=3, type="BUFF")
rupture_1 = StatusEffect("Rupture", "[medium_spring_green]✧[/medium_spring_green]", 1, STATUS_DESCS["Rupture"], duration=1, type="DEBUFF")
rupture_2 = StatusEffect("Rupture", "[medium_spring_green]✧[/medium_spring_green]", 2, STATUS_DESCS["Rupture"], duration=1, type="DEBUFF")
rupture_3 = StatusEffect("Rupture", "[medium_spring_green]✧[/medium_spring_green]", 3, STATUS_DESCS["Rupture"], duration=1, type="DEBUFF")
rupture_4 = StatusEffect("Rupture", "[medium_spring_green]✧[/medium_spring_green]", 4, STATUS_DESCS["Rupture"], duration=1, type="DEBUFF")
rupture_5 = StatusEffect("Rupture", "[medium_spring_green]✧[/medium_spring_green]", 5, STATUS_DESCS["Rupture"], duration=1, type="DEBUFF")
rupture_6 = StatusEffect("Rupture", "[medium_spring_green]✧[/medium_spring_green]", 6, STATUS_DESCS["Rupture"], duration=1, type="DEBUFF")
rupturecount_2 = StatusEffect("Rupture", "[medium_spring_green]✧[/medium_spring_green]", 1, STATUS_DESCS["Rupture"], duration=2, type="DEBUFF")
rupturecount_3 = StatusEffect("Rupture", "[medium_spring_green]✧[/medium_spring_green]", 1, STATUS_DESCS["Rupture"], duration=3, type="DEBUFF")
fairylight_1 = StatusEffect("Fairylight", "[spring_green1]𒀭[/spring_green1]", 1, STATUS_DESCS["Fairylight"], duration=1, type="UNIQUEDEBUFF")
fairylight_2 = StatusEffect("Fairylight", "[spring_green1]𒀭[/spring_green1]", 2, STATUS_DESCS["Fairylight"], duration=1, type="UNIQUEDEBUFF")
fairylight_3 = StatusEffect("Fairylight", "[spring_green1]𒀭[/spring_green1]", 3, STATUS_DESCS["Fairylight"], duration=1, type="UNIQUEDEBUFF")
pierce_fragility_1 = StatusEffect("Pierce Fragility", "[light_yellow3]▶[/light_yellow3]", 0, STATUS_DESCS["Pierce Fragility"], duration=1, type="DEBUFF")
pierce_fragility_2 = StatusEffect("Pierce Fragility", "[light_yellow3]▶[/light_yellow3]", 0, STATUS_DESCS["Pierce Fragility"], duration=2, type="DEBUFF")
pierce_fragility_3 = StatusEffect("Pierce Fragility", "[light_yellow3]▶[/light_yellow3]", 0, STATUS_DESCS["Pierce Fragility"], duration=3, type="DEBUFF")
paralysis_1 = StatusEffect("Paralysis", "[orange1]ϟ[/orange1]", 1, STATUS_DESCS["Paralysis"], duration=1, type="DEBUFF")
paralysis_2 = StatusEffect("Paralysis", "[orange1]ϟ[/orange1]", 1, STATUS_DESCS["Paralysis"], duration=2, type="DEBUFF")
paralysis_5 = StatusEffect("Paralysis", "[orange1]ϟ[/orange1]", 1, STATUS_DESCS["Paralysis"], duration=5, type="DEBUFF")
paralysis_7 = StatusEffect("Paralysis", "[orange1]ϟ[/orange1]", 1, STATUS_DESCS["Paralysis"], duration=7, type="DEBUFF")
acceleration_1 = StatusEffect("Acceleration", "[bold pale_turquoise1]>>[/bold pale_turquoise1]", 1, STATUS_DESCS["Acceleration"], duration=1, type="UNIQUEBUFF")
overheat_1 = StatusEffect("Overheat", "[indian_red]>>[/indian_red]", 0, STATUS_DESCS["Overheat"], duration=1, type="DEBUFF")
cloud_sword_1 = StatusEffect("Cloud Sword [云]", "[bold chartreuse1][云][/bold chartreuse1]", 0, STATUS_DESCS["Cloud Sword [云]"], duration=1, type="BUFF")
invisibility_1 = StatusEffect("Invisibility", "[purple4]⛆[/purple4]", 1, STATUS_DESCS["Invisibility"], duration=1, type="BUFF")
blossom_1 = StatusEffect("Blossom", "[hot_pink]❀[/hot_pink]", 0, STATUS_DESCS["Blossom"], duration=1, type="DEBUFF")
malice_1 = StatusEffect("Malice", "[hot_pink]♨[/hot_pink]", 0, STATUS_DESCS["Malice"], duration=1, type="DEBUFF")
flickering_invisibility_1 = StatusEffect("Flickering Invisibility", "[thistle3]⛆[/thistle3]", 0, STATUS_DESCS["Flickering Invisibility"], duration=1, type="BUFF")
leaking_bloodlust_1 = StatusEffect("Leaking Bloodlust", "[red3]✹[/red3]", 0, STATUS_DESCS["Leaking Bloodlust"], duration=1, type="BUFF")
hopeless_blossom_1 = StatusEffect("Hopeless Blossom", "[hot_pink]❁[/hot_pink]", 0, STATUS_DESCS["Hopeless Blossom"], duration=1, type="DEBUFF")
spirit_blade_1 = StatusEffect("Spirit Blade Unsealed [靈刃解封]", "[sea_green3]𖣐[/sea_green3]", 0, STATUS_DESCS["Spirit Blade Unsealed [靈刃解封]"], duration=1, type="BUFF")

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
    17: "Kiryoku Gakuen Self-Defense Club President Naganohara",
    18: "Kiryoku Gakuen Student Council ‘Lesser Fairy’ Yuri",
    19: "Kiryoku Gakuen Student Council Fairy | ‘Forest Guardian’ Benikawa",
    20: "Kiryoku Gakuen Student Council Fairy | ‘Lake Strider’ Hana",
    21: "Heiwa Seiritsu Student – Goodwill Infiltrator Shigemura",
    22: "Riposte Gang Squad Leader Naganohara",
    23: "Riposte Gang Executive Hanefuji Akasuke",
    24: "Kasakura High School Disciplinary Committee Member Kagaku",
    25: "Benikawa Ninja Clan – Ayame Benikawa",
    26: "Yunhai Association Enforcer Akasuke",
    27: "Yunhai Association Enforcer Naganohara",
    28: "Luoxia Gardening School Student Kagaku",
    29: "Luoxia Gardening School Student Hana",
    30: "Black Water Dock Gang Squad Leader Shigemura",
    31: "Black Water Dock Master Natsume",
    32: "Yunhai Association Enforcer Captain Inami Yuri",
    33: "Yunhai Association Enforcer Captain Kagaku Shamiko",
    34: "Ibara Ninja | ‘Naganohara Tsukimiyama The Untouchable’",
    35: "Yunhai Association Xiangyun | Yokubukai Natsume",
    36: "General Of The Ten Thousand Blossom Brotherhood | Kaoru Hana"
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
        desc_s3 = "[On Use] All allies deal +2 Final Damage this turn\n       [On Use] All allies from 'Heiwa Seiritsu' take -2 Final Damage this turn"
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
        s2 = Skill("Suriage", 2, EL_LUDUS, 7, "[On Use] Gain 3 Poise Count", effect_type="GAIN_STATUS")
        s2.status_effect = poisecount_3
        desc_s3 = "[On Use] Gain 2 Poise Potency\n       [On Hit] Gain 4 Poise Potency"
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
        s1 = Skill("Palm Strike", 1, EL_PHILIA, 2, "If target >50% HP, deal +2 Final Damage", effect_type="COND_HP_ABOVE_50_FLAT", effect_val=2)
        s2 = Skill("Roundhouse Kick", 2, EL_STORGE, 4, "")
        s3 = Skill("Vital Strike", 3, EL_PHILAUTIA, 8, "[On Hit] Target takes +4 Final Damage from other attacks this turn", effect_type="DEBUFF_INCOMING_DMG_FLAT", effect_val=4)
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
        s2 = Skill("Block", 2, EL_LUDUS, 0, "[Combat Start] This unit takes -4 Final Damage this turn", effect_type="BUFF_DEF_FLAT", effect_val=4)
        s3 = Skill("Defensive Overhaul", 3, EL_AGAPE, 5, "[On Use] All allies take -3 Final Damage this turn", effect_type="AOE_BUFF_DEF_FLAT", effect_val=3)
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
            "[On Hit] Deal +40% Base Damage against targets with 2+ Bleed Count\n       [On Hit] Deal Another +40% Base Damage against targets with 5+ Bleed Count"
        )
        s2 = Skill("Dual Lashing", 2, EL_LUDUS, 7, desc_s2, effect_type="COND_REAPER_BLEED_SPECIAL")
        # Logic: COND_REAPER_BIND_CONVERT_SPECIAL (Reduce dmg based on bleed total -> Apply Bind)
        desc_s3 = (
            "[On Hit] Deal -3 Base Damage for every 3 Bleed (Potency + Count) on target (Max -9 Base Damage); For every 3 Base Damage reduced this way, inflict 1 Bind to target next turn."
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
        desc_s3 = "[On Hit] Deal +4 Final Damage against targets with Bleed\n       [On Hit] Inflict 2 Bleed Count"
        s3 = Skill("One-Handed Throw Down", 3, EL_PHILIA, 8, desc_s3, effect_type="COND_BLEED_DMG_AND_APPLY", effect_val=4)
        s3.status_effect = bleedcount_2
        k.skill_pool_def = [(s1, 5), (s2, 3), (s3, 1)]

        return {
            "kata_obj": k,
            "max_hp": 75,
            "description": desc
        }

    # --- NAGANOHARA KIRYOKU ---
    elif name == "Kiryoku Gakuen Self-Defense Club President Naganohara":
        res = [0.8, 1.4, 1.1, 0.8, 1.0, 1.0, 1.3]
        desc = (
            "Naganohara Tsukimiyama here has enrolled in Kiryoku Gakuen and proudly stands as the President of its renowned Self-Defense Club. Her signature pink twintails are braided tightly into practical loops to stay out of the way during intense spars, and her large golden eyes shine with an unbreakable, almost terrifying level of optimism. She trades her usual Kasakura uniform for a pristine white martial arts gi worn over a Kiryoku athletic top, featuring a captain’s armband that commands instant, eager respect from her hundreds of club members.\n\n"
            "As the club's president, she embodies Kiryoku's unique battle culture to its absolute peak: she experiences absolutely no frustration, hesitation, or fear in combat, only pure, adrenaline-fueled joy. She fights with a dynamic, highly acrobatic self-defense style—effortlessly redirecting her opponent’s momentum for devastating throws, sweeping trips, and precise joint locks—all while maintaining a beaming, radiant smile.\n\n"
            "Her leadership relies on boundless enthusiasm rather than strict discipline. She constantly cheers on both her club members and her opponents mid-fight, offering loud praises and constructive tips even as she flips them onto the mats."
        )
        k = Kata("Kiryoku Gakuen Self-Defense Club President Naganohara", "Naganohara", 2, "I", res, desc)
        k.source_key = name
        s1 = Skill("Crosspunch", 1, EL_PHILIA, 4, "[On Hit] Inflict 2 Rupture Potency", effect_type="APPLY_STATUS")
        s1.status_effect = rupture_2
        s2 = Skill("Motivation!", 2, EL_LUDUS, 5, "[On Use] Deal 0 damage, then heal self and 2 other random allies by supposed final damage", effect_type="SPECIAL_CONVERT_DMG_TO_HEAL_RANDOM", effect_val=2)
        desc_s3 = "[On Use] 2 Other random allies gain 1 Haste next turn\n       [On Hit] If target has Rupture, inflict 2 Rupture Count. Otherwise, inflict 3 Rupture Potency."
        s3 = Skill("Feverish Strikes", 3, EL_AGAPE, 8, desc_s3, effect_type="NAGANOHARA_KIRYOKU_SPECIAL")
        k.skill_pool_def = [(s1, 5), (s2, 3), (s3, 1)]

        return {"kata_obj": k, "max_hp": 78, "description": desc}

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
        desc_s3 = "[On Use] 2 Other random allies gain 1 Haste next turn\n       [On Use] 2 Random enemies gain 1 Bind next turn"
        s3 = Skill("Comms Support", 3, EL_PRAGMA, 0, desc_s3, effect_type="HASTE_BIND_SPECIAL_TYPE1", effect_val=2)
        k.skill_pool_def = [(s1, 5), (s2, 3), (s3, 1)]

        return {"kata_obj": k, "max_hp": 58, "description": desc}

    # --- HANA DEFAULT ---
    elif name == "Kasakura High School Student Hana":
        res = [0.8, 1.2, 0.8, 0.7, 1.2, 1.0, 1.2]
        desc = (
            "Kaoru Hana is a student of Kasakura High School, one of the most renowned educational institutes of the east. She has soft, flowing hair and gentle, highly observant eyes that radiate warmth, compassion, and an unwavering calmness. Hana’s hobbies include practicing self-defense and aikido at the school dojo—where her elegant, momentum-shifting throws earn high praise from her juniors—and offering empathetic, grounded support to her peers without ever losing her composure."
        )
        k = Kata("Kasakura High School Student Hana", "Hana", 1, "I", res, desc)
        k.source_key = name
        s1 = Skill("Swift Backhand", 1, EL_STORGE, 3, "[On Use] Gain 1 Haste next turn", effect_type="GAIN_STATUS")
        s1.status_effect = haste_1
        s2 = Skill("Clean Throw", 2, EL_STORGE, 7, "")
        desc_s3 = "[On Use] This unit deals -40% damage next turn.\n       [On Hit] Target deals -15% damage this turn."
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
        desc_s1 = "[On Hit] Inflict 1 Bleed Potency\n       [On Hit] Inflict 1 Rupture Potency"
        s1 = Skill("Acid Flask Throw", 1, EL_AGAPE, 3, desc_s1, effect_type="BLEED_RUPTURE_SPECIAL_TYPE1", effect_val=1)
        s2 = Skill("Wrench Smack", 2, EL_EROS, 5, "")
        s3 = Skill("Hanefuji Healing Serum", 3, EL_AGAPE, 8, "[On Use] Deal 0 damage, then heal lowest HP ally by supposed final damage", effect_type="SPECIAL_CONVERT_DMG_TO_HEAL_LOWEST", effect_val=0)
        k.skill_pool_def = [(s1, 5), (s2, 3), (s3, 1)]

        return {"kata_obj": k, "max_hp": 60, "description": desc}

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
        s2 = Skill("Close Distance", 2, EL_LUDUS, 8, "[On Hit] If target has Rupture, inflict 2 Fairylight Potency", effect_type="FAIRYLIGHT_APPLY", effect_val=2)
        desc_s3 = "[On Hit] If target has Rupture, inflict 3 Fairylight Potency\n       [On Use] This unit takes +50% damage this turn"
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
        s1 = Skill("Penetrating Defenses", 1, EL_PHILIA, 5, "[On Hit] If target has Rupture, inflict 2 Fairylight Potency", effect_type="FAIRYLIGHT_APPLY", effect_val=2)
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
        desc_s1 = "[On Use] If this unit has Haste, gain 1 Haste next turn\n       [On Hit] Gain 1 Haste next turn"
        s1 = Skill("Tough Knuckles", 1, EL_LUDUS, 6, desc_s1, effect_type="HASTE_GAIN_SPECIAL_TYPE1", effect_val=1)
        desc_s2 = "[On Use] Gain 1 Haste next turn\n       [On Hit] If this unit has Haste, deal +20% base damage, then this unit takes damage based on the amount increased"
        s2 = Skill("Low Tackle", 2, EL_PHILIA, 8, desc_s2, effect_type="SHIGEMURA_INFILTRATOR_SPECIAL_1")
        desc_s3 = "[On Hit] If this unit has Haste, deal +15% damage for every stack of Haste on self (Max +75%), then remove all Haste on self"
        s3 = Skill("Maximized Ram", 3, EL_EROS, 9, desc_s3, effect_type="SHIGEMURA_INFILTRATOR_SPECIAL_2")
        k.skill_pool_def = [(s1, 5), (s2, 3), (s3, 1)]

        return {"kata_obj": k, "max_hp": 90, "description": desc}

    # --- NAGANOHARA RIPOSTE ---
    elif name == "Riposte Gang Squad Leader Naganohara":
        res = [1.1, 1.1, 1.0, 1.2, 1.3, 0.8, 1.1]
        desc = (
            "Naganohara Tsukimiyama here has strayed far from the moral path, rising through the criminal underworld to become a deeply respected Squad Leader of the notorious Absconder syndicate, the Riposte Gang. She trades her Kasakura uniform for the gang’s signature dark sandy yellow long coat, her bright pink twintails tied back securely for combat. Her slender, fairly smaller-than-average build perfectly suits the syndicate's lethal fighting philosophy, making her an elusive and dangerously underestimated target in the middle of a chaotic battlefield.\n\n"
            "In combat, Naganohara abandons her usual close combat brawling methods for the refined, deadly art of the rapier. She is blindingly fast and surprisingly tough, obsessively focusing her entire battle IQ on reading her opponent to find the perfect counterattack. True to the Riposte way, she is unafraid of taking a hit, willingly enduring damage to create a fatal opening before stepping into her opponent's guard to deliver a singular, devastating thrust. Her ruthless efficiency and unshakeable nerve have earned her the absolute loyalty of her subordinates, whom she leads in everything from full-frontal gang war assaults to secretive kidnapping and smuggling operations around school grounds.\n\n"
            "Despite her hardened criminal lifestyle, Naganohara's mind is occupied by only two people. The first is Hanefuji Akasuke, who in this timeline is a young, immensely talented Executive of the Riposte Gang. Having survived the underworld much longer than him, she harbors a deep, quiet pity for Akasuke, lamenting that someone so young and gifted was dragged into such a dark life. The second is her enigmatic 'Boss,' who her subordinates often whisper that whenever she comes to visit, Naganohara’s ruthless gang-leader facade completely melts away, and she spends the entire day smiling with the same innocent, radiant joy she had on the very first day she was admitted into the syndicate."
        )
        k = Kata("Riposte Gang Squad Leader", "Naganohara", 4, "I", res, desc)
        k.source_key = name
        desc_s1 = "[On Use] Gain 5 Riposte\n       [On Hit] Inflict 1 Pierce Fragility"
        s1 = Skill("Appel", 1, EL_STORGE, 5, desc_s1, effect_type="NAGANOHARA_RIPOSTE_APPEL")
        desc_s2 = "[On Use] Gain 10 Riposte\n       [On Hit] If this unit has 20+ Riposte, deal +40% damage, then take +50% more damage this turn.\n       [On Hit] Inflict 2 Pierce Fragility"
        s2 = Skill("Cede", 2, EL_LUDUS, 9, desc_s2, effect_type="NAGANOHARA_RIPOSTE_CEDE")
        desc_s3 = "[On Use] If this unit has 25+ Riposte, fix Riposte stack count to 50. Otherwise, gain 20 Riposte\n       [On Hit] Inflict 3 Pierce Fragility"
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
        desc_s1 = "[On Use] If this unit does not have Riposte, gain 10 Riposte. Otherwise, gain 5 Riposte\n       [On Hit] Inflict 1 Pierce Fragility"
        s1 = Skill("En Garde", 1, EL_LUDUS, 7, desc_s1, effect_type="AKASUKE_RIPOSTE_ENGARDE")
        desc_s2 = "[On Use] Gain 1 Haste next turn\n       [On Use] If this unit has 10+ Riposte, gain 1 Haste next turn\n       [On Hit] If target has Pierce Fragility, gain 10 Riposte\n       [On Hit] Inflict 2 Pierce Fragility"
        s2 = Skill("Feint", 2, EL_STORGE, 6, desc_s2, effect_type="AKASUKE_RIPOSTE_FEINT")
        desc_s3 = "This skill deals +2% base damage for each stack of Riposte owned (Max +100%)\n       [On Use] Gain 10 Riposte\n       [On Hit] Inflict 3 Pierce Fragility"
        s3 = Skill("Prise De Fer", 3, EL_LUDUS, 15, desc_s3, effect_type="AKASUKE_RIPOSTE_PRISEDEFER")
        # Custom Skill Pool setup based on prompt!
        k.skill_pool_def = [(s1, 4), (s2, 3), (s3, 2)]

        return {"kata_obj": k, "max_hp": 80, "description": desc}

    # --- KAGAKU DISCIPLINARY COMMITTEE ---
    elif name == "Kasakura High School Disciplinary Committee Member Kagaku":
        res = [1.1, 1.2, 1.2, 0.9, 0.9, 0.9, 1.1]
        desc = (
            "Kagaku Shamiko here serves as a frontline combatant in Kasakura High School’s Disciplinary Committee, a role that heavily contrasts her fundamentally laid-back nature. She begrudgingly wears the Committee’s standard white kimono uniform with muted gray accents denoting her rank, though she still lazily drapes her signature wrinkled white lab coat over her shoulders. Her unkempt hair and perpetually tired eyes remain unchanged, but instead of just carrying gadgets, she now keeps a standard-issue wooden bokken—tucked into her sash, ready for the physical altercations she desperately wishes to avoid.\n\n"
            "Despite her position in a highly active security faction, Kagaku is still the same lazy girl who wants nothing to do with fighting. Her presence on the frontlines is purely born out of gratitude. After being rescued from a violent group of Heiwa thugs by the Committee's President, Inami Yuri, Kagaku felt a deep debt to her savior. Knowing no other way to properly repay the fiercely disciplined President, Kagaku signed up to stand by her side. As a result, her daily life is a constant, exhausting tug-of-war between her innate desire to slack off in her lab and sudden, fierce spikes of overnight motivation to uphold her duties for Yuri.\n\n"
            "In battle, Kagaku fights with a reluctant but terrifyingly efficient style, utilizing her sharp analytical mind to calculate precise angles and leverage. She minimizes her own physical movement, relying on smart counters to end skirmishes as quickly as possible so she can go back to resting. Though she constantly complains about the grueling physical training regimens mandated by the President, her hidden combat talent and genuine efforts do not go unnoticed. Vice President Shigemura frequently observes her brilliant, low-energy takedowns from the sidelines, silently cheering her on and ensuring she stays just motivated enough to reach her true potential."
        )
        k = Kata("Kasakura High School Disciplinary Committee Member", "Kagaku", 2, "I", res, desc)
        k.source_key = name
        
        s1 = Skill("Heavy Draw", 1, EL_LUDUS, 5, "[On Use] Gain 2 Poise Potency", effect_type="GAIN_STATUS")
        s1.status_effect = poise_2
        
        s2 = Skill("Harai Waza", 2, EL_PHILAUTIA, 7, "[On Hit] All allies (including self) with 4+ Poise Potency convert 2 Poise Potency to Count", effect_type="ON_HIT_CONVERT_POISE_TYPE2", effect_val=2)
        
        s3 = Skill("Theory Of Discipline", 3, EL_EROS, 7, "[On Hit] All allies (including self) with Poise gain 4 Poise Count. Gain 4 Poise Potency instead if they do not have Poise", effect_type="ON_HIT_PROVIDE_POISE_TYPE4", effect_val=4)
        
        k.skill_pool_def = [(s1, 5), (s2, 3), (s3, 1)]

        return {"kata_obj": k, "max_hp": 71, "description": desc}

    # --- BENIKAWA NINJA CLAN ---
    elif name == "Benikawa Ninja Clan – Ayame Benikawa":
        res = [1.2, 0.6, 0.6, 1.4, 1.4, 1.2, 0.8]
        desc = (
            "Ayame Benikawa here has fully shed the need for secrecy, standing proudly as a true operative of the Benikawa Ninja Clan while fighting alongside her trusted Kasakura Vanguard. While she still wears her standard Kasakura High School formal uniform, she no longer bothers to conceal the hidden kunai strapped to her thighs, and her bright purple eyes—the undeniable mark of her bloodline—gleam with unrestricted, feral battle hunger. Free from the heavy burden of hiding her true nature from Akasuke, Yuri, and the rest of her friends, she can finally let loose and fight with her absolute, terrifying full strength.\n\n"
            "In combat, she completely abandons the strict, holding-back mindset she previously used to maintain her 'normal high schooler' cover. She seamlessly weaves her devastating, heavy-hitting karate strikes with lethal, shadow-stepping ninja arts, moving with blistering speed to systematically dismantle her opponents. She fights with a ruthless pragmatism, no longer afraid of looking 'too lethal' in front of her peers.\n\n"
            "However, the greatest advantage of her revealed identity is the freedom to openly utilize and hone her specialized Awakening: Nerve Rerouting and Pain Nullification. Having awakened this unique physical specialty only a few months prior to receiving her mission, her mastery over it is still incomplete—yet, by continuing to fight openly alongside the Vanguard, Benikawa treats the brutal battlefield as her ultimate training ground. She freely experiments with her techniques mid-fight, pushing her limits in a relentless, joyful drive to perfect her deadly arts."
        )
        k = Kata("Benikawa Ninja Clan", "Benikawa", 4, "I", res, desc)
        k.source_key = name
        
        desc_s1 = "[Combat Start] This unit takes +30% damage this turn\n       [On Hit] Target takes +4 Final Damage from other attacks this turn\n       [On Hit] If target has Bleed, Inflict 3 Bleed Potency\n       [On Hit] Inflict 1 Pierce Fragility"
        s1 = Skill("Break Vitals", 1, EL_PHILAUTIA, 9, desc_s1, effect_type="BENIKAWA_CLAN_SPECIAL_1")
        
        desc_s2 = "[Combat Start] This unit takes -30% damage for this turn, then takes -50% damage in the next turn\n       [On Use] If this unit does not have Poise, gain 4 Poise Count\n       [On Use] Gain 3 Poise Potency\n       [On Use] Gain 2 Haste next turn"
        s2 = Skill("Focus – Painlessness", 2, EL_LUDUS, 0, desc_s2, effect_type="BENIKAWA_CLAN_SPECIAL_2")
        
        desc_s3 = "[Combat Start] This unit takes +30% damage this turn\n       [On Hit] Target deals -15% damage this turn, then deals -25% damage next turn\n       [On Hit] If target has Bleed, inflict 3 Bleed Count and 3 Bleed Potency, then this unit gains 2 Haste next turn\n       [On Hit] If target has Pierce Fragility, inflict 2 Pierce Fragility, then this unit gains 3 Poise Potency and 2 Poise Count"
        s3 = Skill("Specialty – Chaotic Nervous Redefinition", 3, EL_PHILAUTIA, 14, desc_s3, effect_type="BENIKAWA_CLAN_SPECIAL_3")
        
        k.skill_pool_def = [(s1, 5), (s2, 3), (s3, 1)]

        return {"kata_obj": k, "max_hp": 58, "description": desc}

    # --- AKASUKE YUNHAI ASSOCIATION ---
    elif name == "Yunhai Association Enforcer Akasuke":
        res = [1.2, 0.8, 0.8, 1.0, 1.2, 1.0, 0.9]
        desc = "Akasuke Hanefuji here serves as a dedicated Enforcer within the Westward Megastructure's Yunhai Association. He trades his usual red coat for an immaculate white Tang Suit and a flowing, cloud-patterned cloak. His unruly red hair is pulled back tightly beneath a pristine white headband, though his signature black eyepatch remains, contrasting sharply with the uniform. Instead of relying purely on bare-knuckle brawling, he wields a traditional double-edged Jian with lethal grace.\n\nHe expertly blends the fluid, dance-like redirection of Yunhai swordsmanship with his own heavy, kinetic striking power, resulting in a highly aggressive suppression style that drops local gang threats in a single, perfectly calculated blow. Despite the rigid, insular discipline expected of the Association, his core remains unchanged: an overwhelming, compassionate sense of duty to protect the city's civilians from the shadows."
        k = Kata("Yunhai Association Enforcer", "Akasuke", 2, "I", res, desc)
        k.source_key = name
        s1 = Skill("Slicing", 1, EL_LUDUS, 7, "[On Hit] Inflict 2 Rupture Potency\n       [On Hit] Inflict 2 Rupture Count", effect_type="APPLY_RUPTURE_HEAVY_STACKS")
        s2 = Skill("Defensive", 2, EL_AGAPE, 5, "[Combat Start] All of this unit’s allies (including self) from “Yunhai Association” take -2 Final Damage this turn\n       [On Use] Gain 3 Poise Count\n       [On Hit] 2 Other random allies of this unit gains 2 Poise Count (Prioritizes units from “Yunhai Association”)", effect_type="YUNHAI_AKASUKE_SPECIAL1")
        s3 = Skill("Following The Shape", 3, EL_EROS, 10, "[Combat Start] All of this unit’s allies (including self) from “Yunhai Association” deal +2 Base Damage this turn\n       [On Hit] Inflict 2 Rupture Potency\n       [On Hit] Inflict 2 Rupture Count\n       [On Hit] 2 Other random allies of this unit gains 3 Poise Potency (Prioritizes units from “Yunhai Association”)", effect_type="YUNHAI_AKASUKE_SPECIAL2")
        k.skill_pool_def = [(s1, 5), (s2, 3), (s3, 1)]
        return {"kata_obj": k, "max_hp": 72, "description": desc}

    # --- NAGANOHARA YUNHAI ASSOCIATION ---
    elif name == "Yunhai Association Enforcer Naganohara":
        res = [0.9, 0.8, 0.8, 1.1, 1.1, 1.0, 1.2]
        desc = "Naganohara Tsukimiyama here proudly serves the Westward Megastructure as an unexpectedly cheerful Yunhai Association Enforcer. She trades her usual Kasakura uniform for a pristine white Tang Suit and a flowing, cloud-patterned cloak, though her signature pink twin-tails bounce just as energetically beneath her white uniform headband. Instead of acting with the strict, rigid stoicism typical of the Administration's guards, she wields her traditional Jian sword with a rhythmic, dance-like enthusiasm.\n\nDriven by a desperate courage to protect her peers and the city's civilians, she applies her terrifying adaptability to the Association's fluid swordsmanship, proving that an unbreakable, optimistic smile can be just as formidable as absolute discipline."
        k = Kata("Yunhai Association Enforcer", "Naganohara", 2, "I", res, desc)
        k.source_key = name
        s1 = Skill("Pointing", 1, EL_AGAPE, 6, "[On Hit] All of this unit’s allies from “Yunhai Association” deal +2 Final Damage\n       [On Hit] Inflict 2 Rupture Potency", effect_type="YUNHAI_NAGANOHARA_SPECIAL1")
        s2 = Skill("Offensive!", 2, EL_STORGE, 9, "[Combat Start] All of this unit’s allies from “Yunhai Association” gain 3 Poise Potency\n       [Combat Start] Gain 3 Poise Count", effect_type="YUNHAI_NAGANOHARA_SPECIAL2")
        s3 = Skill("Sensing Power", 3, EL_AGAPE, 0, "[Combat Start] All of this unit’s allies (including self) from “Yunhai Association” deal -3 Base Damage this turn, then deal +3 Base Damage next turn\n       [On Use] Gain 3 Poise Count", effect_type="YUNHAI_NAGANOHARA_SPECIAL3")
        k.skill_pool_def = [(s1, 5), (s2, 3), (s3, 1)]
        return {"kata_obj": k, "max_hp": 66, "description": desc}

    # --- KAGAKU LUOXIA GARDENING SCHOOL ---
    elif name == "Luoxia Gardening School Student Kagaku":
        res = [1.0, 1.0, 1.0, 0.8, 1.1, 1.2, 1.1]
        desc = "Kagaku Shamiko trades her modern Kasakura lab coat for the traditional green and white training uniform of the Luoxia Gardening School, though her hair remains a chaotic, unkempt green mess from long nights of obsessive research. In this timeline, she channels her 'mad scientist' genius entirely into bio-engineering and botany, utilizing Luoxia's advanced greenhouses to concoct bizarre, highly effective stamina serums and medicinal herbs.\n\nIn combat, she applies her hyper-analytical mind to the school's rigorous bare-handed martial arts, striking pressure points and breaking defenses with clinical, experimental efficiency rather than raw, mindless power."
        k = Kata("Luoxia Gardening School Student", "Kagaku", 2, "I", res, desc)
        k.source_key = name
        s1_c1 = Chip(base_damage=2, effect_type="APPLY_STATUS")
        s1_c1.status_effect = rupture_2
        s1_c2 = Chip(base_damage=2, effect_type="APPLY_STATUS")
        s1_c2.status_effect = rupturecount_2
        s1_desc = "[On Hit] Inflict Rupture Potency\n       [On Hit] Inflict Rupture Count"
        s1_insp = "◈ Base Damage: 2\n       [On Hit] Inflict 2 Rupture Potency\n       ◈ Base Damage: 2\n       [On Hit] Inflict 2 Rupture Count"
        s1 = ChipSkill("Basic Strikes ◈◈", 1, EL_PHILIA, [s1_c1, s1_c2], description=s1_desc, inspect_description=s1_insp)
        
        s2 = Skill("Energy Serum [能量精華液]", 2, EL_AGAPE, 0, "[On Use] Heals an ally of this unit with the least HP% (Prioritizes units from “Yunhai Region”)", effect_type="LUOXIA_KAGAKU_SPECIAL1")
        s2.inspect_description = "[On Use] Heals an ally of this unit with the least HP% (Prioritizes units from “Yunhai Region”) for 10% of this unit’s Max HP"
        
        s3_c1 = Chip(base_damage=3, effect_type="LUOXIA_KAGAKU_SPECIAL2")
        s3_c2 = Chip(base_damage=5, effect_type="LUOXIA_KAGAKU_SPECIAL3")
        s3_desc = "[On Hit] Heals self, then another ally of this unit with the least HP% (Prioritizes units from “Yunhai Region”)\n       [On Hit] Inflict Rupture Potency\n       [On Hit] Inflict Rupture Count"
        s3_insp = "◈ Base Damage: 3\n       [On Hit] Heals self, then another ally of this unit with the least HP% (Prioritizes units from “Yunhai Region”) for final damage dealt\n       [On Hit] Inflict Rupture 3 Potency\n       ◈ Base Damage: 5\n       [On Hit] Heals self, then another ally of this unit with the least HP% (Prioritizes units from “Yunhai Region”) for final damage dealt\n       [On Hit] Inflict Rupture 2 Count"
        s3 = ChipSkill("Steadfast Form ◈◈", 3, EL_PHILIA, [s3_c1, s3_c2], description=s3_desc, inspect_description=s3_insp)
        k.skill_pool_def = [(s1, 5), (s2, 3), (s3, 1)]
        return {"kata_obj": k, "max_hp": 61, "description": desc}

    # --- HANA LUOXIA GARDENING SCHOOL ---
    elif name == "Luoxia Gardening School Student Hana":
        res = [1.0, 1.2, 1.1, 0.9, 1.0, 1.0, 1.0]
        desc = "For Kaoru Hana, enrolling as a student at the Luoxia Gardening School is an absolute paradise. Wearing the traditional green and white uniform, she maintains her gentle, maiden-like demeanor, lovingly tending to rare Nepenthes cultivars and exotic medicinal herbs within the climate-controlled jade greenhouses. However, underneath her polite smile lies the insane physical conditioning of Luoxia's martial curriculum.\n\nShe defends her precious flowerbeds with devastating open-palm strikes and precise joint locks. Rowdy thugs who dare step on her meticulously tilled soil quickly learn the terrifying, bone-shattering strength hidden behind her motherly grace."
        k = Kata("Luoxia Gardening School Student", "Hana", 2, "I", res, desc)
        k.source_key = name
        s1 = Skill("Tend Soil", 1, EL_STORGE, 7, "[On Use] Gain 2 Poise Potency\n       [On Use] Gain 2 Poise Count\n       [On Critical Hit] Gain 2 Poise Potency", effect_type="GAIN_POISE_SPECIAL_4", effect_val=2)
        
        s2_c1 = Chip(base_damage=2, effect_type="LUOXIA_HEAL_TYPE1")
        s2_c2 = Chip(base_damage=3, effect_type="LUOXIA_HEAL_TYPE2")
        s2_c3 = Chip(base_damage=2, effect_type="LUOXIA_HEAL_TYPE2")
        s2_desc = "[On Hit] Heals a random ally of this unit (Can include self, Prioritizes units from “Yunhai Region”)\n       [On Hit] If target has Rupture, Heals a random ally of this unit (Can include self, Prioritizes units from “Yunhai Region”)"
        s2_insp = "◈ Base Damage: 2\n       [On Hit] Heals a random ally of this unit (Can include self, Prioritizes units from “Yunhai Region”) for Final Damage dealt\n       ◈ Base Damage: 3\n       [On Hit] If target has Rupture, Heals a random ally of this unit (Can include self, Prioritizes units from “Yunhai Region”) for Final Damage dealt\n       ◈ Base Damage: 2\n       [On Hit] If target has Rupture, Heals a random ally of this unit (Can include self, Prioritizes units from “Yunhai Region”) for Final Damage dealt"
        s2 = ChipSkill("Linked Punches ◈◈◈", 2, EL_AGAPE, [s2_c1, s2_c2, s2_c3], description=s2_desc, inspect_description=s2_insp)
        
        s3_c1 = Chip(base_damage=3, effect_type="LUOXIA_HANA_SPECIAL1")
        s3_c2 = Chip(base_damage=3, effect_type="LUOXIA_HANA_SPECIAL1")
        s3_c3 = Chip(base_damage=6, effect_type="LUOXIA_HANA_SPECIAL2")
        s3_desc = "[On Use] All of this unit’s allies (including self) from “Yunhai Region” deal +1 Final Damage this turn\n       [On Hit] Inflict Rupture Potency\n       [On Hit] If this unit has Poise, inflict Rupture Count\n       [On Hit] Target deals -10% Final Damage this turn"
        s3_insp = "◈ Base Damage: 3\n       [On Use] All of this unit’s allies (including self) from “Yunhai Region” deal +1 Final Damage this turn\n       [On Hit] If this unit has Poise, inflict 2 Rupture Count\n       ◈ Base Damage: 3\n       [On Use] All of this unit’s allies (including self) from “Yunhai Region” deal +1 Final Damage this turn\n       [On Hit] If this unit has Poise, inflict 2 Rupture Count\n       ◈ Base Damage: 6\n       [On Hit] Inflict 3 Rupture Potency\n       [On Hit] Target deals -10% Final Damage this turn"
        s3 = ChipSkill("Yank Out Intruding Weeds! ◈◈◈", 3, EL_EROS, [s3_c1, s3_c2, s3_c3], description=s3_desc, inspect_description=s3_insp)
        k.skill_pool_def = [(s1, 5), (s2, 3), (s3, 1)]
        return {"kata_obj": k, "max_hp": 81, "description": desc}

    # --- SHIGEMURA BLACK WATER DOCK ---
    elif name == "Black Water Dock Gang Squad Leader Shigemura":
        res = [0.9, 0.9, 0.9, 1.1, 1.2, 1.1, 1.3]
        desc = "Fuyuyama Shigemura has abandoned his quiet life to embrace the ruthless, nocturnal underworld of the Westward Megastructure, leading an elite squad of the dreaded Black Water Dock gang. He trades his usual Kasakura uniform for practical, dark street clothes, keeping his violet eyes sharp and calculating under the cover of midnight. While his peers rely on chaotic numbers and blind aggression, Shigemura applies his genius-level intellect and stoic observation skills to coordinate brutal, highly efficient ambushes against rival factions.\n\nHe wields the gang's signature Monk Spear—specially retrofitted with high-voltage tasers—with lethal precision, but his true terror lies in his unnatural physical density and unbothered demeanor. Rather than relying on stealth, he nonchalantly steps directly into the line of fire, casually absorbing heavy impacts and halting charging enemies dead in their tracks before delivering a devastating, electrified counter-thrust. Despite his criminal standing and seemingly apathetic attitude, he remains fiercely protective of his squad, ensuring his subordinates survive the grueling gang wars of Sector II."
        k = Kata("Black Water Dock Gang Squad Leader", "Shigemura", 3, "I", res, desc)
        k.source_key = name
        s1 = Skill("Inward Parry [拿]", 1, EL_LUDUS, 4, "[On Hit] Gain 4 Poise Potency\n       [On Hit] This unit and a random ally of this unit (Prioritizes units from “Black Water Dock”) takes -20% Base Damage this turn", effect_type="BLACKWATER_SHIGEMURA_TYPE1")
        s2 = Skill("Thrust – Core Attack", 2, EL_PRAGMA, 10, "[On Hit] Inflict 4 Rupture Potency", effect_type="APPLY_STATUS")
        s2.status_effect = rupture_4
        s3 = Skill("Showoff The Dock’s Spearplay", 3, EL_PRAGMA, 13, "[Combat Start] This unit and two random allies of this unit (Prioritizes units from “Black Water Dock”) deal +1 Final Damage this turn. If the selected ally(s) is from “Black Water Dock”, they deal +3 Final Damage instead\n       [Combat Start] This unit and all allies from “Black Water Dock” gain 3 Poise Count\n       [On Hit] Inflict 2 Paralysis", effect_type="BLACKWATER_SHIGEMURA_TYPE2")
        k.skill_pool_def = [(s1, 5), (s2, 3), (s3, 1)]
        return {"kata_obj": k, "max_hp": 70, "description": desc}

    # --- NATSUME BLACK WATER DOCK ---
    elif name == "Black Water Dock Master Natsume":
        res = [1.2, 0.9, 0.9, 1.1, 1.1, 1.0, 1.1]
        desc = "Yokubukai Natsume rules the nocturnal streets of Sector II as the undisputed Master of the Black Water Dock gang. Trading her high-tech monitors and comfortable beanbags for intimidating, dark underworld attire, her signature sleepy pink eyes now radiate the terrifying, lethargic confidence of an apex predator. Her messy dark blue hair falls freely as she casually rests a masterfully crafted, high-voltage Monk Spear over her shoulder, proving herself to be an unparalleled, albeit incredibly unmotivated, martial arts spear master.\n\nDespite her fearsome reputation, Natsume remains unapologetically lazy. In battle, she is exceptionally prideful, exerting only the absolute minimum effort required to execute flawless, devastating thrusts that effortlessly dismantle rival gangs. She achieves this overwhelming offensive pressure by relying entirely on her exceptionally close bond with her most trusted Squad Leader, Fuyuyama Shigemura.\n\nShe utilizes his dense, impenetrable physical defense solely to cover her blind spots, ensuring she never actually has to waste energy dodging an attack. Her absolute authority extends far beyond the battlefield; outside of combat, she treats her ruthless syndicate like personal attendants, regularly commanding Shigemura and her terrified underlings to run menial errands—from fetching her favorite late-night street food to meticulously polishing and maintaining her spear—while she comfortably naps away the responsibilities of leadership."
        k = Kata("Black Water Dock Master", "Natsume", 4, "I", res, desc)
        k.source_key = name
        s1 = Skill("Outward Parry [拦]", 1, EL_PRAGMA, 6, "[Combat Start] This skill’s effects only activate if there are at least 2 units from “Black Water Dock” in the team (counts self and defeated allies):\n       [On Use] Gain 3 Poise Potency\n       [On Use] Gain 2 Poise Count\n       [On Hit] All units from “Black Water Dock” take -2 Final Damage next turn", effect_type="BLACKWATER_NATSUME_TYPE1")
        
        s2_c1 = Chip(base_damage=8, effect_type="BLACKWATER_NATSUME_TYPE2")
        s2_c2 = Chip(base_damage=2, effect_type="BLACKWATER_NATSUME_TYPE3")
        s2_desc = "[Combat Start] This skill’s effects only activate if there are at least 2 units from “Black Water Dock” in the team (counts self and defeated allies):\n       [On Hit] Inflict Rupture Potency\n       [On Hit] Inflict Rupture Count\n       [On Hit] Inflict Paralysis\n       [On Hit] All units from “Black Water Dock” take -10% Final Damage this turn"
        s2_insp = "[Combat Start] This skill’s effects only activate if there are at least 2 units from “Black Water Dock” in the team (counts self and defeated allies):\n       ◈ Base Damage: 8\n       [On Hit] Inflict 3 Rupture Potency\n       [On Hit] Inflict 3 Rupture Count\n       ◈ Base Damage: 2\n       [On Hit] Inflict 2 Paralysis\n       [On Hit] All units from “Black Water Dock” take -10% Final Damage this turn"
        s2 = ChipSkill("Protect Your Master ◈◈", 2, EL_AGAPE, [s2_c1, s2_c2], description=s2_desc, inspect_description=s2_insp)
        
        s3_c1 = Chip(base_damage=1, effect_type="BLACKWATER_NATSUME_TYPE4")
        s3_c2 = Chip(base_damage=1, effect_type="BLACKWATER_NATSUME_TYPE5")
        s3_c3 = Chip(base_damage=1, effect_type="BLACKWATER_NATSUME_TYPE4")
        s3_c4 = Chip(base_damage=1, effect_type="BLACKWATER_NATSUME_TYPE6")
        s3_desc = "[Combat Start] This skill’s effects only activate if there are at least 2 units from “Black Water Dock” in the team (counts self and defeated allies):\n       [On Hit] Deals +Base Damage\n       [On Use] Gain Poise Potency\n       [On Use] Gain Poise Count\n       [On Critical Hit] Inflict Paralysis\n       [On Hit] Switches to a new random target"
        s3_insp = "[Combat Start] This skill’s effects only activate if there are at least 2 units from “Black Water Dock” in the team (counts self and defeated allies):\n       ◈ Base Damage: 1\n       [On Use] Gain 3 Poise Potency\n       [On Use] This chip deals +3 Base Damage\n       [On Hit] Inflict 1 Paralysis\n       [On Hit] Switches to a new random target\n       ◈ Base Damage: 1\n       [On Use] Gain 3 Poise Count\n       [On Use] This chip deals +3 Base Damage\n       [On Hit] Inflict 1 Paralysis\n       ◈ Base Damage: 1\n       [On Use] Gain 3 Poise Potency\n       [On Use] This chip deals +3 Base Damage\n       [On Hit] Inflict 1 Paralysis\n       [On Hit] Switches to a new random target\n       ◈ Base Damage: 1\n       [On Use] This chip deals +3 Base Damage\n       [On Hit] Inflict 2 Paralysis"
        s3 = ChipSkill("Twining Fools ◈◈◈◈", 3, EL_EROS, [s3_c1, s3_c2, s3_c3, s3_c4], description=s3_desc, inspect_description=s3_insp)
        k.skill_pool_def = [(s1, 5), (s2, 3), (s3, 1)]
        return {"kata_obj": k, "max_hp": 76, "description": desc}

    # --- YURI YUNHAI ASSOCIATION ---
    elif name == "Yunhai Association Enforcer Captain Inami Yuri":
        res = [0.9, 1.2, 1.2, 0.9, 1.0, 1.0, 1.2]
        desc = "Inami Yuri rises to the pinnacle of the Westward Megastructure's security as the formidable Captain of the Yunhai Association's 2nd Unit. Trading her usual rowdy brawler persona for an aura of absolute, unwavering discipline, she channels her natural confidence into a stoic, formal, and deeply cautious demeanor. Her signature silver ponytail is tied back with immaculate precision, and she commands instant respect in her pristine white Tang Suit and heavy, glittering cloud-patterned cloak.\n\nForsaking her bare-handed judo, Yuri wields a traditional Jian with fluid, hyper-aggressive elegance, capable of dismantling entire syndicates in the blink of an eye. Despite her rigid professionalism, her underlying kindness remains completely intact, especially when dealing with civilians or her closest confidant, Captain Kagaku.\n\nWhen the two fight side-by-side, their inhuman teamwork and telepathic synchronization create a seamless, suffocating vortex of steel that leaves enemies feeling as though they are being dismantled by a single, omnipresent force. Outside of their grueling shifts, Yuri's steadfast composure perfectly grounds her partner's loud charisma, making them an inseparable, complementary duo on the bustling streets of Sector II."
        k = Kata("Yunhai Association Enforcer Captain", "Yuri", 4, "I", res, desc)
        k.source_key = name
        s1 = Skill("Collapse / Snap [崩]", 1, EL_STORGE, 9, "[Combat Start] All of this unit’s allies with Poise gain 2 Poise Count. If affected units are from “Yunhai Association”, gain 3 Poise Count instead\n       [On Hit] Gain 3 Poise Potency\n       [On Critical Hit] Gain 3 Poise Potency", effect_type="YUNHAI_YURI_SPECIAL1")
        
        s2_c1 = Chip(base_damage=3, effect_type="APPLY_STATUS")
        s2_c1.status_effect = rupture_2
        s2_c2 = Chip(base_damage=4, effect_type="APPLY_STATUS")
        s2_c2.status_effect = rupturecount_2
        s2_c3 = Chip(base_damage=5, effect_type="RUPTURE_PARALYSIS_SPECIAL_TYPE2", effect_val=2)
        s2_desc = "[Combat Start] All of this unit’s allies with Poise gain 2 Poise Potency. If affected units are from “Yunhai Association”, gain 4 Poise Potency instead\n       [On Hit] Inflict Rupture Potency\n       [On Hit] Inflict Rupture Count\n       [On Hit] Inflict Paralysis"
        s2_insp = "[Combat Start] All of this unit’s allies with Poise gain 2 Poise Potency. If affected units are from “Yunhai Association”, gain 4 Poise Potency instead\n       ◈ Base Damage: 3\n       [On Hit] Inflict 2 Rupture Potency\n       ◈ Base Damage: 4\n       [On Hit] Inflict 2 Rupture Count\n       ◈ Base Damage: 5\n       [On Hit] Inflict 2 Rupture Potency\n       [On Hit] Inflict 2 Rupture Count\n       [On Hit] Inflict 2 Paralysis"
        s2 = ChipSkill("White snake [白蛇] ◈◈◈", 2, EL_PHILAUTIA, [s2_c1, s2_c2, s2_c3], description=s2_desc, inspect_description=s2_insp, effect_type="YUNHAI_YURI_CS1")
        
        s3_c1 = Chip(base_damage=2, effect_type="YUNHAI_YURI_SPECIAL2")
        s3_c2 = Chip(base_damage=3, effect_type="YUNHAI_YURI_SPECIAL3")
        s3_c3 = Chip(base_damage=6, effect_type="APPLY_STATUS_CRITICAL")
        s3_c3.status_effect = cloud_sword_1
        s3_desc = "[On Critical Hit] All of this unit’s allies from “Yunhai Association” deal +10% Final Damage this turn\n       [On Critical Hit] Heal self and all of this unit’s allies from “Yunhai Association”\n       [On Critical Hit] Inflict Paralysis\n       [On Critical Hit] Gain Cloud Sword [云]\n       [On Hit] Switches to a new random target"
        s3_insp = "◈ Base Damage: 2\n       [On Critical Hit] All of this unit’s allies from “Yunhai Association” deal +10% Final Damage this turn\n       [On Critical Hit] Inflict 2 Paralysis\n       [On Hit] Switches to a new random target\n       ◈ Base Damage: 3\n       [On Critical Hit] Heal self and all of this unit’s allies from “Yunhai Association” for Final Damage dealt\n       [On Critical Hit] Inflict 2 Paralysis\n       [On Hit] Switches to a new random target\n       ◈ Base Damage: 6\n       [On Critical Hit] Gain 1 Cloud Sword [云]"
        s3 = ChipSkill("Phoenix Nods Its Head [凤凰点头] ◈◈◈", 3, EL_AGAPE, [s3_c1, s3_c2, s3_c3], description=s3_desc, inspect_description=s3_insp)
        k.skill_pool_def = [(s1, 5), (s2, 2), (s3, 2)]
        return {"kata_obj": k, "max_hp": 83, "description": desc}

    # --- KAGAKU YUNHAI ASSOCIATION CAPTAIN ---
    elif name == "Yunhai Association Enforcer Captain Kagaku Shamiko":
        res = [0.8, 1.0, 0.9, 0.8, 1.0, 1.3, 1.1]
        desc = "Kagaku Shamiko abandons the isolation of her laboratory to become the radiant, highly charismatic Captain of the Yunhai Association's 1st Unit. Radiating a loud, boisterous confidence that naturally draws crowds of admiring locals, she wears her white Captain's uniform with a blatant, playful disregard for protocol—sleeves stubbornly rolled up to her elbows and pitch-black sunglasses casually perched on her nose. Her messy green hair is styled with a trendy, effortless flair that perfectly matches her highly sociable, fast-talking persona.\n\nWhile she acts like a slacking jokester to the public, her underlying 'mad scientist' genius is instead channeled into a terrifyingly high battle IQ; she wields her Jian with unorthodox, unpredictable mastery. Her true, overwhelming strength shines when she fights alongside her closest friend, Captain Yuri. Their bond is forged in absolute, platonic trust, resulting in a flawless combat rhythm that effortlessly traps and overwhelms their opponents. Once off-duty, Kagaku's vibrant, energetic nature effortlessly drags the stoic Yuri into the lively street markets to enjoy the local food, perfectly balancing her partner's rigid discipline."
        k = Kata("Yunhai Association Enforcer Captain", "Kagaku", 4, "I", res, desc)
        k.source_key = name
        
        s1 = Skill("Threading [穿]", 1, EL_EROS, 10, "[On Hit] Inflict 3 Rupture Count\n       [On Hit] Gain 4 Poise Count\n       [On Critical Hit] Applies to the very next ally of this unit to deal damage within this turn: if this unit is from “Yunhai Association”, deal +2 Base Damage. If this unit is a “Yunhai Association Enforcer Captain”, deal +4 Base Damage instead", effect_type="YUNHAI_KAGAKU_SPECIAL1")
        
        s2_c1 = Chip(base_damage=2, effect_type="YUNHAI_KAGAKU_SPECIAL2")
        s2_c2 = Chip(base_damage=2, effect_type="YUNHAI_KAGAKU_SPECIAL3")
        s2_c3 = Chip(base_damage=4, effect_type="YUNHAI_KAGAKU_SPECIAL2")
        s2_c4 = Chip(base_damage=4, effect_type="YUNHAI_KAGAKU_SPECIAL3")
        s2_desc = "[Combat Start] This unit and all of this unit’s allies with Poise from “Yunhai Association”, gain 5 Poise Potency\n       [On Critical Hit] Heals this unit and all of this unit’s allies with Poise from “Yunhai Association” by Final Damage dealt\n       [On Hit] Inflict Rupture Potency\n       [On Hit] Inflict Paralysis"
        s2_insp = "[Combat Start] This unit and all of this unit’s allies with Poise from “Yunhai Association”, gain 5 Poise Potency\n       ◈ Base Damage: 2\n       [On Critical Hit] Heals this unit and all of this unit’s allies with Poise from “Yunhai Association” by (Final Damage dealt*2)\n       [On Hit] Inflict 3 Rupture Potency\n       ◈ Base Damage: 2\n       [On Critical Hit] Heals this unit and all of this unit’s allies with Poise from “Yunhai Association” by (Final Damage dealt*2)\n       [On Hit] Inflict 1 Paralysis\n       ◈ Base Damage: 4\n       [On Critical Hit] Heals this unit and all of this unit’s allies with Poise from “Yunhai Association” by (Final Damage dealt*2)\n       [On Hit] Inflict 3 Rupture Potency\n       ◈ Base Damage: 4\n       [On Critical Hit] Heals this unit and all of this unit’s allies with Poise from “Yunhai Association” by (Final Damage dealt*2)\n       [On Hit] Inflict 1 Paralysis"
        s2 = ChipSkill("Show Off A Little ◈◈◈◈", 2, EL_AGAPE, [s2_c1, s2_c2, s2_c3, s2_c4], description=s2_desc, inspect_description=s2_insp, effect_type="YUNHAI_KAGAKU_CS1")
        
        s3 = Skill("Empty Stance [空站姿]", 3, EL_EROS, 0, "[Combat Start] This unit takes -40% Final Damage for this turn\n       [Combat Start] This unit does not suffer from the effects of Rupture this turn\n       [Combat Start] Gain 4 Haste next turn\n       [Combat Start] This unit and all of this unit’s allies from “Yunhai Association” gain 1 Cloud Sword [云]\n       [On Use] Applies to the very next ally of this unit to deal damage within this turn: if this unit is from “Yunhai Association”, deal +5 Base Damage. If this unit is a “Yunhai Association Enforcer Captain”, deal +7 Base Damage instead", effect_type="YUNHAI_KAGAKU_SPECIAL4")
        
        k.skill_pool_def = [(s1, 3), (s2, 3), (s3, 3)]
        return {"kata_obj": k, "max_hp": 90, "description": desc}

    # --- NAGANOHARA TSUKIMIYAMA THE UNTOUCHABLE ---
    elif name == "Ibara Ninja | ‘Naganohara Tsukimiyama The Untouchable’":
        res = [1.1, 1.2, 1.0, 1.0, 0.9, 0.7, 0.7]
        desc = "In a profoundly dark and unique timeline, Naganohara Tsukimiyama exists as a notorious Ibara ninja, bearing the infamous mantle of 'The Untouchable'. Stripped completely of her signature bubbly optimism and even entirely lacking the arrogant sadism of the original Kagerou, she operates with a hollow, terrifying efficiency. Clad in heavy, dark tactical mercenary gear, her once-bright golden eyes are now dead, calculating, and devoid of emotion.\n\nShe is a true combat anomaly, possessing not only masterful shinobi stealth but also the devastating Vibration abilities characteristic of Fuyuyama Shigemura. By synthesizing these traits, Naganohara birthed her ingenious 'Vibrant Invisibility'—an absolute technique that simultaneously conceals her presence, violently deflects incoming attacks through high-frequency shielding, accelerates her movements to imperceptible speeds, and completely shatters targets from the inside out upon contact.\n\nHowever, her brutal, lightning-fast approach to ending fights in the absolute worst ways stems from a deeply traumatic reality check. Despite her genius awakening and immense pride in her original techniques, she was once effortlessly dismantled and brutally beaten by a mysterious Propagator of the Seditious Garden, who broke through her impenetrable defenses moments after their fight began. This absolute, humbling defeat forever shattered her worldview.\n\nNow wandering the underworld as a cold, efficient mercenary, she abides by a single, despairing philosophy: 'Unrivaled Under Heavens Is A Heat Haze.' She fights with the bleak, absolute understanding that there is no true 'Strongest' in the world, and no matter how brilliantly a warrior may shine, they are all destined to eventually fall."
        k = Kata("Ibara Ninja | ‘The Untouchable’", "Naganohara", 4, "I", res, desc)
        k.source_key = name
        
        s1_c1 = Chip(base_damage=5, effect_type="KAGEROU_NAGANOHARA_SPECIAL1")
        s1_c2 = Chip(base_damage=7, effect_type="KAGEROU_NAGANOHARA_SPECIAL1")
        s1_desc = "[On Hit] If target has Bleed, Inflict Bleed Potency\n       [On Hit] Inflict Bleed Count\n       [On Hit] Gain Poise Potency\n       [On Critical Hit] If this unit has Vibrant Invisibility, gain Poise Potency"
        s1_insp = "◈ Damage: 5\n       [On Hit] If target has Bleed, Inflict 3 Bleed Potency\n       [On Hit] Inflict 3 Bleed Count\n       [On Hit] Gain 3 Poise Potency\n       [On Critical Hit] If this unit has Vibrant Invisibility, gain 5 Poise Potency\n       ◈ Damage: 7\n       [On Hit] If target has Bleed, Inflict 3 Bleed Potency\n       [On Hit] Inflict 3 Bleed Count\n       [On Hit] Gain 3 Poise Potency\n       [On Critical Hit] If this unit has Vibrant Invisibility, gain 5 Poise Potency"
        s1 = ChipSkill("Cutthroat Arm ◈◈", 1, EL_EROS, [s1_c1, s1_c2], description=s1_desc, inspect_description=s1_insp)
        
        s2_c1 = Chip(base_damage=10, effect_type="KAGEROU_NAGANOHARA_SPECIAL2")
        s2_c2 = Chip(base_damage=8, effect_type="KAGEROU_NAGANOHARA_SPECIAL2")
        s2_desc = "[Combat Start] Gain (Vibrant Invisibility Count*2) Poise Potency\n       [Combat Start] Take +(3-Vibrant Invisibility Count, min +0) Final Damage this turn\n       [On Critical Hit] If target has Bleed, deal +Final Damage\n       [On Critical Hit] Target deals -Final Damage this turn (this effect can stack)\n       [On Critical Hit] Gain Vibrant Invisibility"
        s2_insp = "[Combat Start] Gain (Vibrant Invisibility Count*2) Poise Potency\n       [Combat Start] Take +(3-Vibrant Invisibility Count, min +0) Final Damage this turn\n       ◈ Base Damage: 10\n       [On Critical Hit] Target deals -3 Final Damage this turn (this effect can stack)\n       [On Critical Hit] If target has Bleed, deal +5 Final Damage\n       [On Critical Hit] Gain 1 Vibrant Invisibility\n       ◈ Base Damage: 8\n       [On Critical Hit] Target deals -3 Final Damage this turn (this effect can stack)\n       [On Critical Hit] If target has Bleed, deal +5 Final Damage\n       [On Critical Hit] Gain 1 Vibrant Invisibility"
        s2 = ChipSkill("Breaker Blade ◈◈", 2, EL_EROS, [s2_c1, s2_c2], description=s2_desc, inspect_description=s2_insp, effect_type="KAGEROU_NAGANOHARA_CS1")
        
        s3 = Skill("Unrivaled Under Heavens Is A Heat Haze", 3, EL_PHILAUTIA, 0, "[Combat Start] Take -4 Final Damage this turn\n       [Combat Start] When hit, reflect (Vibrant Invisibility Count*60)% Final Received Damage back to the attacker (max 300% Final Damage per hit, this skill effect occurrence cannot stack), then inflict (Vibrant Invisibility Count) Bleed Potency back to the attacker (max 3 Bleed Potency per hit, this skill effect occurrence cannot stack)\n       [On Use] If this is the first ever skill usage during battle, gain 5 Vibrant Invisibility. Otherwise, gain 3 Vibrant Invisibility\n       [On Use] Gain 13 Poise Potency", effect_type="KAGEROU_NAGANOHARA_SPECIAL3")
        
        k.skill_pool_def = [(s1, 3), (s2, 3), (s3, 3)]
        return {"kata_obj": k, "max_hp": 72, "description": desc}

    # --- YUNHAI XIANGYUN YOKUBUKAI NATSUME ---
    elif name == "Yunhai Association Xiangyun | Yokubukai Natsume":
        res = [1.0, 1.0, 1.1, 1.1, 0.7, 0.9, 1.1]
        desc = "Yokubukai Natsume ascends to the terrifying, absolute pinnacle of the Westward Megastructure as a 'Xiangyun' Administrator. Draped in a regal, floor-length gray Changpao robe with her long, dark blue hair flowing freely in an unnatural wind, she wields a dark Jian that commands an oppressive, suffocating gravity over the entire city. With a mere flick of her wrist, she can suspend sweeping, indestructible walls of jet-black ink matter to effortlessly trap her foes.\n\nTo Enforcers Akasuke, Yuri, Kagaku, and Naganohara, her sudden rise to power is a chilling tragedy; she was once their close friend and fellow student at Luoxia Gardening School, only to vanish and seize the throne overnight, becoming an unrecognizable, dreadful deity. Yet, behind this cold, absolute facade, Natsume remains entirely sane, harboring a quiet, aching affection for the comrades she left behind.\n\nHowever, the true terror of this Kata lies beyond her political might. When the original timeline's Kagaku attempted to observe this alternate universe, she met unprecedented, active interference. This Xiangyun Natsume possesses a level of power so unfathomable that she can instinctively sense multiversal observation and effortlessly block it across space-time.\n\nUltimately, Kagaku suspects this Natsume did not claim her throne out of ambition or malice, but deliberately threw away her peaceful life to brace for a catastrophic war—isolating herself at the top of the world to prepare to fight an incomprehensible, lurking threat that the current Kasakura Vanguard cannot even begin to fathom."
        k = Kata("Yunhai Association Xiangyun", "Natsume", 4, "I", res, desc)
        k.source_key = name

        ex1 = Skill("Paint [畫]", 1, EL_LUDUS, 7, "[Combat Start] Add up all Sinking Potency + Count owned by all units in the field (excludes self), then gain (amount/10) Ink [墨] (max +4)\n       [On Hit] If this unit has Ink [墨], inflict 1 Ink [墨], then copy and distribute this unit’s owned Ink [墨] stacks between random units on the field (Prioritizes units with Sinking)", effect_type="YUNHAI_ADMIN_NATSUME_EX_HIT")
        k.appendable_skills = {"EX1": ex1}

        s1_desc = "[On Use] Gain 6 Poise Potency\n       [On Use] Gain 2 Poise Count\n       [On Hit] Inflict 5 Sinking Potency\n       [On Hit] Inflict 2 Sinking Count\n       [On Critical Hit] If this unit has 3+ Ink [墨], gain 2 Ink [墨]. Otherwise, gain 3 Ink [墨]"
        s1 = Skill("Coldness [寒冷]", 1, EL_LUDUS, 8, s1_desc, effect_type="YUNHAI_ADMIN_NATSUME_SPECIAL1")
        
        s2_c1 = Chip(base_damage=6, effect_type="YUNHAI_ADMIN_NATSUME_SPECIAL2")
        s2 = ChipSkill("Hidden Lotus Beneath Snow [雪下藏蓮] ◈", 2, EL_PRAGMA, [s2_c1], description="[Combat Start] If this unit has Ink [墨], append the skill Paint [畫]\n       [On Use] Gain 5 Poise Potency\n       [On Use] Gain 2 Poise Count\n       [On Hit] Inflict 4 Rupture Potency\n       [On Critical Hit] Consume 1 Ink [墨] to Retoss (max 3) this chip, then switches to a new random target (Prioritizes units with Sinking)", inspect_description="[Combat Start] If this unit has Ink [墨], append the skill Paint [畫]\n       ◈ Base Damage: 6\n       [On Use] Gain 5 Poise Potency\n       [On Use] Gain 2 Poise Count\n       [On Hit] Inflict 4 Rupture Potency\n       [On Critical Hit] Consume 1 Ink [墨] to Retoss (max 3) this chip, then switches to a new random target (Prioritizes units with Sinking)", effect_type="YUNHAI_ADMIN_NATSUME_CS1")
        
        s3_c1 = Chip(base_damage=9, effect_type="YUNHAI_ADMIN_NATSUME_SPECIAL3")
        s3 = ChipSkill("Echo of the Empty Valley [空谷迴響] ◈", 3, EL_AGAPE, [s3_c1], description="[Combat Start] If this unit has Ink [墨], append the skill Paint [畫]\n       [On Critical Hit] Deal +(Target’s Sinking Potency+Count/4) Final Damage (Max +6)\n       [On Critical Hit] Inflict 4 Sinking Potency\n       [On Critical Hit] Inflict 3 Sinking Count\n       [On Critical Hit] Consume 1 Ink [墨] to Retoss (max 3) this chip, then switches to a new random target (Prioritizes units with Sinking)", inspect_description="[Combat Start] If this unit has Ink [墨], append the skill Paint [畫]\n       ◈ Base Damage: 9\n       [On Critical Hit] Deal +(Target’s Sinking Potency+Count/4) Final Damage (Max +6)\n       [On Critical Hit] Inflict 4 Sinking Potency\n       [On Critical Hit] Inflict 3 Sinking Count\n       [On Critical Hit] Consume 1 Ink [墨] to Retoss (max 3) this chip, then switches to a new random target (Prioritizes units with Sinking)", effect_type="YUNHAI_ADMIN_NATSUME_CS1")
        
        k.skill_pool_def = [(s1, 5), (s2, 3), (s3, 1)]
        return {"kata_obj": k, "max_hp": 80, "description": desc}

    # --- GENERAL HANA ---
    elif name == "General Of The Ten Thousand Blossom Brotherhood | Kaoru Hana":
        res = [0.8, 1.1, 1.0, 0.8, 1.0, 1.1, 0.9]
        desc = "In the ancient, blood-soaked era of the original War of the Nine Armies, Kaoru Hana stands as the honorable General of the Ten Thousand Blossom Brotherhood. Unlike the rage-fueled, masculine war cries of the original Zhao Feng, Hana leads her forces with a gentle, quiet yet unyielding resolve; her soldiers affectionately insist on calling her 'Big Sis' amidst the carnage—an endearing title she long ago gave up trying to correct.\n\nEnveloped in a suffocating, glowing pink miasma, she wields a massive Jian blade on the frontlines. Through a flawless, harmonious blend of absolute peace of mind and unwavering determination, she can temporarily shatter her own sword to manifest a spiritually powered blade superweapon of unfathomable destructive force. While this technique elevates her peak strength to a level arguably beyond the original General's, Original Kagaku wisely notes that comparing two equally respectable war legends is a disservice to their shared history.\n\nWise, kind, and fiercely honorable, Hana understands that showing mercy on the battlefield is the ultimate disrespect to a mature adversary, and thus she strikes with lethal, unhesitating efficiency. However, her tale is a profound tragedy forged by the chaotic Phenomena energy of her era, which indiscriminately kept suffering fighters alive in a hellish cycle. By the time the ancient ceasefire birthed the Scroll of the Nine Armies, Hana had lost every single one of her beloved lieutenants and messengers, leaving her to eternally command a mindless, spectral horde. Yet, her spirit never falters.\n\nShe firmly believes that the political squabbles of future eras belong solely to the people of those eras. Bound to the ritual, her singular, eternal duty is simply to 'Destroy The Enemy.' She will continue to give her all, leading the Vanguard to break through enemy lines until the day her endless war finally ceases—and she can peacefully rest to reunite with her precious comrades once again."
        k = Kata("General Of The Ten Thousand Blossom Brotherhood", "Hana", 4, "I", res, desc)
        k.source_key = name
        
        # S1: Break Through ◈◈ (I) (Ludus)
        s1_desc = "[Combat Start] 2 Random allies of this unit take -2 and deal +2 Final Damage this turn (Prioritizes units using an Agape element skill)\n       [On Use] Select the current target and another random target for the following effect: Gain [(Rupture Count+Potency)/3] Hopeless Blossom\n       [On Hit] Inflict Rupture Potency\n       [On Hit] Inflict Rupture Count\n       [On Hit] Gain Poise Count"
        s1_ins = "[Combat Start] 2 Random allies of this unit take -2 and deal +2 Final Damage this turn (Prioritizes units using an Agape element skill)\n       ◈ Base Damage: 5\n       [On Use] Select the current target and another random target for the following effect: Gain [(Rupture Count+Potency)/3] Hopeless Blossom\n       [On Hit] Inflict 3 Rupture Potency\n       [On Hit] Gain 3 Poise Count\n       ◈ Base Damage: 5\n       [On Hit] Inflict 4 Rupture Count"
        s1_c1 = Chip(base_damage=5, effect_type="GENERAL_HANA_SPECIAL1")
        s1_c2 = Chip(base_damage=5, effect_type="APPLY_STATUS")
        s1_c2.status_effect = StatusEffect("Rupture", "[medium_spring_green]✧[/medium_spring_green]", 1, STATUS_DESCS.get("Rupture", ""), duration=4, type="DEBUFF")
        s1 = ChipSkill("Break Through ◈◈", 1, EL_LUDUS, [s1_c1, s1_c2], description=s1_desc, inspect_description=s1_ins, effect_type="GENERAL_HANA_CS1")
        
        # S2: Pointing A Path For The Lost (II) (Pragma)
        s2_desc = "[Combat Start] Select the current target and another 2 random targets for the following effect: Take +30% damage from the effects of Bleed and Rupture this turn\n       [On Use] Gain 5 Poise Potency\n       [On Use] Gain 5 Poise Count\n       [On Hit] If target has 1+ Incoming Final Damage Reduction modifier value, reduce it by / 2 (min 0)\n       [On Hit] If target has 1+ Outgoing Final Damage Increase modifier value, reduce it by / 2 (min 0)\n       [On Critical Hit] Inflict 4 Hopeless Blossom"
        s2 = Skill("Pointing A Path For The Lost", 2, EL_PRAGMA, 12, s2_desc, effect_type="GENERAL_HANA_SPECIAL2")
        
        # S3: The Immortal Points The Way [仙人指路] ◈◈◈◈ (III) (Agape)
        s3_desc = "[Combat Start] 3 Random allies of this unit take -2 and deal +2 Final Damage this turn (Prioritizes units using an Eros element skill)\n       [On Use] Select the current target and another 2 random targets for the following effect: Gain [(Rupture Count+Potency)/3] Hopeless Blossom\n       [On Use] Gain Poise Potency\n       [On Hit] Inflict Rupture Potency\n       [On Hit] Inflict Rupture Count\n       [On Critical Hit] Inflict Hopeless Blossom"
        s3_ins = "[Combat Start] 3 Random allies of this unit take -2 and deal +2 Final Damage this turn (Prioritizes units using an Eros element skill)\n       ◈ Base Damage: 3\n       [On Use] Select the current target and another 2 random targets for the following effect: Gain [(Rupture Count+Potency)/3] Hopeless Blossom\n       [On Use] Gain 5 Poise Potency\n       ◈ Base Damage: 3\n       [On Hit] Inflict 2 Rupture Potency\n       [On Hit] Inflict 2 Rupture Count\n       [On Critical Hit] Inflict 3 Hopeless Blossom\n       ◈ Base Damage: 3\n       [On Hit] Inflict 2 Rupture Potency\n       [On Hit] Inflict 2 Rupture Count\n       [On Critical Hit] Inflict 3 Hopeless Blossom\n       ◈ Base Damage: 3\n       [On Critical Hit] Inflict 4 Hopeless Blossom"
        s3_c1 = Chip(base_damage=3, effect_type="GENERAL_HANA_SPECIAL3")
        s3_c2 = Chip(base_damage=3, effect_type="GENERAL_HANA_SPECIAL4")
        s3_c3 = Chip(base_damage=3, effect_type="GENERAL_HANA_SPECIAL4")
        s3_c4 = Chip(base_damage=3, effect_type="APPLY_STATUS_CRITICAL")
        s3_c4.status_effect = StatusEffect("Hopeless Blossom", "[hot_pink]❁[/hot_pink]", 0, STATUS_DESCS.get("Hopeless Blossom", ""), duration=4, type="DEBUFF")
        s3 = ChipSkill("The Immortal Points The Way [仙人指路] ◈◈◈◈", 3, EL_AGAPE, [s3_c1, s3_c2, s3_c3, s3_c4], description=s3_desc, inspect_description=s3_ins, effect_type="GENERAL_HANA_CS2")

        # EX1: Move As A “Phantom [幻影]” (I) (Ludus)
        ex1_desc = "[On Use] All enemies gain [(Rupture Count+Potency)/2] Hopeless Blossom\n       [Combat Start] All allies of this unit deal +5% Base Damage this turn for each unit using either an Eros or Agape skill (Max +30%)\n       [Combat Start] When hit, this unit and 2 other allies of this unit deal +2 Final Damage next turn (this effect cannot stack)\n       [Combat Start] This unit takes -30% Final Damage from attacks. When hit, there is a 50% chance to take -60% Final Damage instead."
        ex1 = Skill("Move As A “Phantom [幻影]”", 1, EL_LUDUS, 0, ex1_desc, effect_type="GENERAL_HANA_SPECIAL5")

        # EX2: The Great Ocean Receives a Hundred Rivers [海纳百川有容乃大] ◈◈◈ (IV) (Pragma)
        ex2_desc = "[On Use] Select the current target and another 3 random targets for the following effect: Gain [(Rupture Count+Potency)/2]+10 Hopeless Blossom\n       [On Use] If this skill has already been used once during battle, gain Spirit Blade Unsealed [靈刃解封] next turn\n       [On Hit] Deal -30% Final Damage, then +5% Final Damage for every unit in the field using an Eros or Agape skill (Max +30%)\n       [On Hit] If target has Hopeless Blossom, heal self and another random ally of this unit for (Final Damage/2)\n       [On Hit] Inflict Rupture Potency\n       [On Hit] Switches to a new random target (Prioritizes units with Hopeless Blossom)"
        ex2_ins = "◈ Base Damage: 4\n       [On Use] Select the current target and another 3 random targets for the following effect: Gain [(Rupture Count+Potency)/2]+10 Hopeless Blossom\n       [On Hit] Deal -30% Final Damage, then +5% Final Damage for every unit in the field using an Eros or Agape skill (Max +30%)\n       [On Hit] Inflict 5 Rupture Potency\n       [On Hit] Switches to a new random target (Prioritizes units with Hopeless Blossom)\n       ◈ Base Damage: 5\n       [On Hit] Deal -30% Final Damage, then +5% Final Damage for every unit in the field using an Eros or Agape skill (Max +30%)\n       [On Hit] If target has Hopeless Blossom, heal self and another random ally of this unit for (Final Damage/2)\n       [On Hit] Switches to a new random target (Prioritizes units with Hopeless Blossom)\n       ◈ Base Damage: 10\n       [On Use] If this skill has already been used once during battle, gain Spirit Blade Unsealed [靈刃解封] next turn\n       [On Hit] Deal -30% Final Damage, then +5% Final Damage for every unit in the field using an Eros or Agape skill (Max +30%)\n       [On Hit] Inflict 5 Rupture Potency"
        s4_c1 = Chip(base_damage=4, effect_type="GENERAL_HANA_SPECIAL6")
        s4_c2 = Chip(base_damage=5, effect_type="GENERAL_HANA_SPECIAL7")
        s4_c3 = Chip(base_damage=10, effect_type="GENERAL_HANA_SPECIAL8")
        ex2 = ChipSkill("The Great Ocean Receives a Hundred Rivers [海纳百川有容乃大] ◈◈◈", 4, EL_PRAGMA, [s4_c1, s4_c2, s4_c3], description=ex2_desc, inspect_description=ex2_ins, effect_type="GENERAL_HANA_EX2")

        k.appendable_skills = {"EX1": ex1, "EX2": ex2}
        k.skill_pool_def = [(s1, 4), (s2, 3), (s3, 2)]

        return {"kata_obj": k, "max_hp": 84, "description": desc}