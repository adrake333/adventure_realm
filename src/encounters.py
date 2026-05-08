import random
from src.entities import Tutorial_Goblin, Goblin, Orc, Kobold, Gungar

def get_random_encounter():
    encounters = [
        [Goblin("Crazy Goblin"), Goblin("Hungry Goblin"), Goblin("Angry Goblin")],
        [Orc("Iron Orc"), Orc("Rock Orc")],
        [Kobold("Fire-spitter Kobold"), Kobold("Flame-toungue Kobold")],
        [Orc("Angry Orc"), Goblin("Sneaky Goblin"), Kobold("Bold Kobold")],
        [Orc("Angry Orc"), Goblin("Crazy Goblin"), Goblin("Hungry Goblin"), Goblin("Angry Goblin")],
        [Kobold("Fire-spitter Kobold"), Kobold("Flame-tongue Kobold"), Goblin("Lizard-like Goblin")]
    ]
    return random.choice(encounters)

def get_tutorial_encounter():
    return [Tutorial_Goblin("Weak Goblin")]

def get_boss_encounter():
    return [Gungar("Gungar the Destroyer")]
