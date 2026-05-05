import random
from src.entities import Goblin, Orc, Kobold

def get_random_encounter():
    encounters = [
        [Goblin("Crazy Goblin"), Goblin("Hungry Goblin"), Goblin("Angry Goblin")],
        [Orc("Iron Orc"), Orc("Rock Orc")],
        [Kobold("Fire-spitter"), Kobold("Flame-toungue")],
        [Orc("Angry Orc"), Goblin("Sneaky Goblin"), Kobold("Bold Kobold")],
        [Orc("Angry Orc"), Goblin("Crazy Goblin"), Goblin("Hungry Goblin"), Goblin("Angry Goblin")],
        [Kobold("Fire-spitter"), Kobold("Flame-tongue"), Goblin("Lizard-like Goblin")]
    ]
    return random.choice(encounters)
