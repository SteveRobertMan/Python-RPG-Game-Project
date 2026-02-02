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
    return ["", "I", "II", "III"][tier] if 0 < tier <= 3 else str(tier)

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
        "A common electronic component found in old tech. Used to enhance basic Kata capabilities.", 
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
    )
}

class StatusEffect:
    def __init__(self, name, symbol, potency, description, duration=3, type="DEBUFF"):
        self.name = name
        self.symbol = symbol
        self.potency = potency
        self.description = description
        self.duration = duration
        self.type = type # "DOT", "REGEN", "DEBUFF", "BUFF"

class Skill:
    def __init__(self, name, tier, element_idx, base_damage, description="", effect_type=None, effect_val=0):
        self.name = name
        self.tier = tier 
        self.element = element_idx
        self.base_damage = base_damage
        self.description = description
        self.effect_type = effect_type
        self.effect_val = effect_val
        # Optional field for complex effects (like attaching a StatusEffect object)
        self.status_effect = None 

class Kata:
    def __init__(self, name, owner_name, rarity, rift_aptitude, resistances):
        self.name = name
        self.owner_name = owner_name
        self.rarity = rarity
        self.rift_aptitude = rift_aptitude
        self.resistances = resistances
        self.skill_pool_def = [] 

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
        
        self.kata = None
        self.hand = []
        self.deck = []
        self.discard_pile = []
        self.intent = None 
        self.auto_target = None 
        
        self.temp_modifiers = {
            "final_dmg_reduction": 0, 
            "outgoing_dmg_mult": 1.0,
            "incoming_dmg_mult": 1.0,
            "incoming_dmg_flat": 0 
        }
        
        # --- MECHANICS FOR NEXT HIT ---
        self.next_hit_taken_flat_bonus = 0
        self.next_hit_deal_flat_bonus = 0
        
        # Hidden Flags (Status effects that are invisible or special)
        self.nerve_disruption_turns = 0
        
        # Pending modifiers applied at start of NEXT turn
        self.next_turn_modifiers = {}
        
        self.status_effects = []

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
            "incoming_dmg_flat": 0
        }

    def apply_next_turn_modifiers(self):
        """Apply any pending next-turn modifiers at the start of the turn."""
        if "outgoing_dmg_mult" in self.next_turn_modifiers:
            self.temp_modifiers["outgoing_dmg_mult"] *= self.next_turn_modifiers["outgoing_dmg_mult"]
            del self.next_turn_modifiers["outgoing_dmg_mult"]

    def add_status_effect(self, new_effect):
        """
        Safely adds or merges a StatusEffect object.
        Respects Caps: Bleed (99 Potency/Count), Bind (5 Count).
        """
        # Find existing effect by name
        existing = next((e for e in self.status_effects if e.name == new_effect.name), None)
        
        if existing:
            if new_effect.name == "Bleed":
                # Bleed Logic: Merge Potency (Max) and Count (Sum), Cap at 99
                existing.potency = min(99, max(existing.potency, new_effect.potency))
                existing.duration = min(99, existing.duration + new_effect.duration)
            elif new_effect.name == "Bind":
                # Bind Logic: Sum Duration, Cap at 5
                existing.duration = min(5, existing.duration + new_effect.duration)
            else:
                # Standard Logic: Refresh duration to the highest value, stack potency if needed
                # (Default behavior for generic buffs/debuffs)
                existing.duration = max(existing.duration, new_effect.duration)
                # If you want potency to stack (e.g. Strength Up + Strength Up), uncomment below:
                # existing.potency += new_effect.potency
        else:
            # Apply Initial Caps for new effects
            if new_effect.name == "Bleed":
                new_effect.potency = min(99, new_effect.potency)
                new_effect.duration = min(99, new_effect.duration)
            elif new_effect.name == "Bind":
                new_effect.duration = min(5, new_effect.duration)
                
            self.status_effects.append(new_effect)

    def use_and_replace_skill(self, skill):
        if skill in self.hand:
            self.hand.remove(skill)
        self.discard_pile.append(skill)
        self.draw_skills(1)