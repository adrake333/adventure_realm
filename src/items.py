class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    
    def __str__(self):
        return self.name

class Healing_Potion(Item):
    def __init__(self, name, heal_amount):
        super().__init__(name, f"Heals for {heal_amount} HP")
        self.heal_amount = heal_amount

    def use(self, target):
        print(f"Using {self.name}...")
        target.heal(self.heal_amount)

class Mana_Potion(Item):
    def __init__(self, name, mana_restored):
        super().__init__(name, f"Restores {mana_restored} Mana")
        self.mana_restored = mana_restored

    def use(self, target):
        print(f"Using {self.name}...")
        target.restore_mana(self.mana_restored)

class Coins(Item):
    def __init__(self, name, amount):
        super().__init__(name, f"A small pile of {amount} coins")
        self.amount = amount
