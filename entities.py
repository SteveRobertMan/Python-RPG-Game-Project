import random

# --- Constants and Element Colors ---
EL_EROS = 0      # Red
EL_PHILIA = 1    # Orange
EL_STORGE = 2    # Yellow
EL_AGAPE = 3     # Green
EL_LUDUS = 4     # Cyan
EL_PRAGMA = 5    # Blue
EL_PHILAUTIA = 6 # Purple

ELEMENT_NAMES = ["Eros", "Philia", "Storge", "Agape", "Ludus", "Pragma", "Philautia"]

def get_element_color(el_idx):
    colors = ["red3", "dark_orange", "gold1", "chartreuse1", "turquoise2", "blue", "purple"]
    if 0 <= el_idx < len(colors): return colors[el_idx]
    return "white"

def get_tier_roman(tier):
    return ["", "I", "II", "III", "IV", "V"][tier] if 0 < tier <= 5 else str(tier)

def to_subscript(number):
    sub_map = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
    return str(number).translate(sub_map)

class Material:
    def __init__(self, name, description, save_id):
        self.name = name
        self.description = description
        self.save_id = save_id

MATERIALS_DB = {
    "Microchip": Material(
        "Microchip", 
        "A complex computing unit. Essential for unlocking the true potential of high-level Katas.", 
        "01"
    ),
    "Microprocessor": Material(
        "Microprocessor", 
        "A common electronic component found in old tech. Used to unlock basic Kata capabilities.", 
        "02"
    ),
    "Cafeteria Melon Bread": Material(
        "Cafeteria Melon Bread",
        "A sweet, fluffy bread with a cookie-crust top. Yuri's favorite snack.",
        "03"
    ),
    "Vending Machine Coffee": Material(
        "Vending Machine Coffee",
        "Bitter and heartless cold coffee sold in vending machines throughout Kasakura High School. Students often cram exams on these.",
        "04"
    ),
    "Sports Water Bottle": Material(
        "Sports Water Bottle",
        "A bottle athelete students across all the four major schools commonly use to replenish themselves with cool water during long workout sessions.",
        "05"
    ),
    "Yunhai Herbal Powder": Material(
        "Yunhai Herbal Powder",
        "An intricate mix of Yunhai Region's local medicinal herbal specialities grounded and mixed in a traditional laboratory. Used to make wound-treating salves and disease-curing supplements.",
        "06"
    ),
    "Jade Microchip": Material(
        "Jade Microchip", 
        "A complex computing unit upgraded with help of the Yunhai Association Industrial Sectors' Jade production lines. Essential for unlocking the true potential of higher-level Katas.", 
        "07"
    ),
}

class StatusEffect:
    def __init__(self, name, symbol, potency, description, duration=3, type="DEBUFF"):
        self.name = name
        self.symbol = symbol
        self.potency = potency
        self.description = description
        self.duration = duration
        self.type = type # "DEBUFF", "BUFF", "UNIQUEDEBUFF", "UNIQUEBUFF"
# --- MASTER STATUS EFFECT DESCRIPTIONS ---
STATUS_DESCS = {
    # DUAL STACK EFFECTS
    "Bleed": "Upon dealing damage, Take fixed damage equal to Potency, then reduce count by 1. Max Potency or Count: 99",
    "Rupture": "Upon getting hit by a skill, Take extra fixed damage equal to the amount of Potency, then reduce count by 1. Max Potency or Count: 99",
    "Fairylight": "Unique Rupture (Counts As Rupture)\nUpon getting hit by a skill, Take extra fixed damage equal to the amount of Potency. On turn end, reduce Count by half, and if this unit has Rupture, gain Rupture Potency based on Count lost this way. Max Potency or Count: 99",
    "Poise": "Boost Critical Hit chance by (Potency*5)% for the next 'Count' amount of hits. Max potency or count: 99",
    "Sinking": "Upon getting hit by a skill, add Potency to an 'LS' (Low Sanity) tally and reduce Count by 1. Next turn, before attacking, each hit has an LS% chance to deal -(LS/2)% Final Damage. LS resets to 0 at turn end. Max LS: 90. Max Potency or Count: 99",
    "Acceleration": "Unique Poise (Counts As Poise)\nBoost Critical Hit chance by (Potency*5)%. When taking damage, reduce Final Damage by 1-3, then also reduce Count (max 2 times per turn) by the same amount. Count cannot go below 1 this way. Max potency or count: 99",
    # DURATION ONLY EFFECTS
    "Bind": "Deal -(10*Count)% base damage with skills. Lose 1 count every new turn. Max Count: 5",
    "Haste": "Deal +(10*Count)% base damage with skills. Lose 1 count every new turn. Max count: 5",
    "Pierce Fragility": "Take +Base Damage from any skill related to Pierce Fragility based on stack amount. Upon getting hit by a skill, reduce count by 1. Max Count: 5",
    "Riposte": "Take -5% damage for every 10 stacks owned (max -25%). When taking damage, reduce stack count by 1-4 stacks. For every 10 cumulative stacks reduced this way, gain 1 Haste next turn, then reset the count. At end of turn, reduce stack count by 25%. Max Count: 50",
    "Paralysis": "When attacking, decrease the Tier for Comparative Defense of target by exactly 1. Reduce count by 1 at end of skill usage. Max count: 99",
    "Overheat": "Apply the following effects when owning at least 1 Count:\nDeal -25% Base Damage with attacks, and take +30% Base Damage from attacks. When attacking, fix Critical Strike chance to 0%. At turn end, reduce count by 1. Max count: 3",
    "Cloud Sword [云]": "Apply the following effects when owning at least 1 Count:\nCritical Hit damage +20%, tally amount of Critical Hits this unit performs throughout battle (Max 9). On next Critical Hit with an Agape element skill, does not count towards Tally; instead multiplies Final Damage by ×(Tally+1), resets the Tally, then removes this status effect. Max Count: 1",
    "Invisibility": "Turn Start and End: Fix this unit’s Poise Count exactly to Invisibility Count if Poise Count is lower. Max Count: 5",
    "Blossom": "Upon taking damage, gain (Count/3) Rupture Potency, then take fixed damage according to gained amount (Max 5 Damage), then reduce count by 1. Max Count: 99",
    "Malice": "Upon taking damage, gain (Count/3) Sinking Potency, then take fixed damage according to gained amount (Max 5 Damage), then reduce count by 1. Max Count: 99",
    "Flickering Invisibility": "Takes -Count Base Damage from skills (max -5). Apply the following effects when owning at least 1 Count:\nTurn Start and End: Fix this unit’s Poise Count to exactly 1. Max Count: 5",
    "Leaking Bloodlust": "Deal and take +(Count/11) Final Damage (Max +/- 5). Take +(Count/33)x more damage from the effects of Bleed (min +1x, max +3x). At 99 Count, deal and take +30% Final Damage from Critical Hits. Max Count: 99"
}

class Skill:
    def __init__(self, name, tier, element_idx, base_damage, description="", effect_type=None, effect_val=0):
        self.name = name
        self.tier = tier 
        self.element = element_idx
        self.base_damage = base_damage
        self.description = description
        self.effect_type = effect_type
        self.effect_val = effect_val
        self.status_effect = None 
        self.alt_status_effect = None

class Chip:
    def __init__(self, base_damage, effect_type=None, effect_val=0):
        self.base_damage = base_damage
        self.effect_type = effect_type
        self.effect_val = effect_val
        self.status_effect = None
        self.alt_status_effect = None

class ChipSkill(Skill):
    def __init__(self, name, tier, element_idx, chips, description="", inspect_description="", effect_type=None, effect_val=0):
        # We sum the base damage for UI / generic checks, but true damage is calculated per chip
        total_dmg = sum(c.base_damage for c in chips)
        super().__init__(name, tier, element_idx, total_dmg, description, effect_type, effect_val)
        self.chips = chips
        self.inspect_description = inspect_description

class Passive:
    def __init__(self, name, description, effect_type="", effect_val=0, color="tan"):
        self.name = name
        self.description = description
        self.effect_type = effect_type
        self.effect_val = effect_val
        self.color = color

class Kata:
    def __init__(self, name, owner_name, rarity, rift_aptitude, resistances, description=""):
        self.name = name
        self.owner_name = owner_name
        self.rarity = rarity
        self.rift_aptitude = rift_aptitude
        self.resistances = resistances
        self.skill_pool_def = [] 
        self.source_key = None
        self.description = description
        self.passives = []
        
    def generate_deck(self):
        deck = []
        if not self.skill_pool_def:
            return deck
        for skill_obj, count in self.skill_pool_def:
            for _ in range(count):
                deck.append(skill_obj)
        random.shuffle(deck)
        return deck

class Entity:
    def __init__(self, name, is_player=False):
        self.name = name
        self.is_player = is_player
        self.max_hp = 100
        self.hp = 100
        self.resistances = [1.0] * 7

        self.pace = 1
        self.slot_targets = []
        self.turn_committed_skills = []
        
        self.kata = None
        self.hand = []
        self.deck = []
        self.discard_pile = []
        self.intent = None
        self.intents = []
        self.auto_target = None
        self.passives = []
        
        self.temp_modifiers = {
            "final_dmg_reduction": 0, 
            "outgoing_dmg_mult": 1.0,
            "incoming_dmg_mult": 1.0,
            "incoming_dmg_flat": 0,
            "outgoing_dmg_flat": 0,
            "rupture_immunity": False
        }
        self.next_hit_taken_flat_bonus = 0
        self.next_hit_deal_flat_bonus = 0
        self.nerve_disruption_turns = 0
        self.next_turn_modifiers = {}
        self.status_effects = []
        self.riposte_loss_tracker = 0
        self.pending_bind = 0
        self.pending_haste = 0
        self.reflect_vibrant_invis_active = False

    def equip_kata(self, kata_obj):
        self.kata = kata_obj
        self.resistances = kata_obj.resistances
        self.refresh_deck()

    def refresh_deck(self):
        if self.kata:
            self.deck = self.kata.generate_deck()
            self.discard_pile = []
            self.hand = []

    def draw_skills(self, amount=2):
        for _ in range(amount):
            if not self.deck:
                self.reshuffle_discard()
            if not self.deck:
                break
            card = self.deck.pop(0)
            self.hand.append(card)

    def reshuffle_discard(self):
        if self.discard_pile:
            self.deck.extend(self.discard_pile)
            self.discard_pile = []
            random.shuffle(self.deck)

    def reset_turn_modifiers(self):
        self.temp_modifiers = {
            "final_dmg_reduction": 0, 
            "outgoing_dmg_mult": 1.0,
            "incoming_dmg_mult": 1.0,
            "incoming_dmg_flat": 0,
            "outgoing_dmg_flat": 0,
            "rupture_immunity": False
        }
        self.next_hit_taken_flat_bonus = 0
        self.next_hit_deal_flat_bonus = 0
        self.nerve_disruption_turns = 0

    def apply_next_turn_modifiers(self):
        for k, v in self.next_turn_modifiers.items():
                    if "mult" in k:
                        self.temp_modifiers[k] = self.temp_modifiers.get(k, 1.0) * v
                    else:
                        self.temp_modifiers[k] = self.temp_modifiers.get(k, 0) + v
        self.next_turn_modifiers = {}

    def apply_status_effect(self, new_effect):
        existing = next((e for e in self.status_effects if e.name == new_effect.name), None)
        
        if existing:
            if new_effect.name in ["Bleed", "Rupture", "Fairylight", "Poise", "Sinking", "Acceleration"]:
                if new_effect.potency > 0 and new_effect.duration <= 0:
                    new_effect.duration = 1
                elif new_effect.duration > 0 and new_effect.potency <= 0:
                    new_effect.potency = 1
                new_effect.potency = min(99, new_effect.potency)
                new_effect.duration = min(99, new_effect.duration)
            elif new_effect.name in ["Bind", "Haste", "Pierce Fragility"]:
                new_effect.duration = min(5, new_effect.duration)
            elif new_effect.name == "Riposte":
                new_effect.duration = min(50, new_effect.duration)
            elif new_effect.name in ["Overheat"]:
                new_effect.duration = min(3, new_effect.duration)
            elif new_effect.name in ["Cloud Sword [云]"]:
                new_effect.duration = min(1, new_effect.duration)
                
            self.status_effects.append(new_effect)

    def use_and_replace_skill(self, skill):
        if skill in self.hand:
            self.hand.remove(skill)
        self.discard_pile.append(skill)

    def get_lowest_hp_ally(self, all_allies):
        living = [u for u in all_allies if u.hp > 0 and u != self]
        if not living: return self 
        return min(living, key=lambda u: u.hp)

    def apply_aoe_buff(self, all_allies, mod_key, value):
        for ally in all_allies:
            if ally.hp > 0:
                ally.temp_modifiers[mod_key] += value