class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class Healing_Potion(Item):
    def __init__(self, name, heal_amount):
        super().__init__(name, f"Heals for {heal_amount} HP")
        self.heal_amount = heal_amount

    def use(self, target):
        target.health += self.heal_amount
        print(f"{target.name} used {self.name} and healed {self.heal_amount} HP!")

class Mana_Potion(Item):
    def __init__(self, name, mana_restored):
        super().__init__(name, f"Restores {mana_restored} Mana")
        self.mana_restored = mana_restored

    def use(self, target):
        target.mana += mana_restored
        print(f"{target.name} used {self.name} and restored {mana_restored} Mana!")

class Coins(Item):
    def __init__(self, name, amount):
        super().__init__(name, f"A small pile of {amount} coins")
        self.amount = amount
