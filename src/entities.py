class Character:
    def __init__(self, name, health, defense, attack_power):
        self.name = name
        self.health = health
        self.defense = defense
        self.attack_power = attack_power

    def describe(self):
        print(f"{self.name} has {self.health} health, {self.defense} defense, and {self.attack_power} power.")

    def attack(self, target):
        if self.attack_power <= target.defense:
            print("The attack had no effect!")
        else:
            target.take_damage(self.attack_power - target.defense)

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print(f"{self.name} has been defeated")
        else:
            print(f"{self.name} has taken {damage} damage!")


#PLAYER
class Player(Character):
    def __init__(self, name, health, defense, attack_power):
        super().__init__(name, health, defense, attack_power)
        self.exp_gained = 0

class Warrior(Player):
    def __init__(self, name):
        super().__init__(name, health = 50, defense = 2, attack_power = 8)

class Archer(Player):
    def __init__(self, name):
        super().__init__(name, health = 50, defense = 0, attack_power = 10)

class Wizard(Player):
    def __init__(self, name):
        super().__init__(name, health = 40, defense = 0, attack_power = 10)
        self.mana = 10

    def fireball(self, target):
        print(f"{self.name} casts a fireball!")
        if self.mana > 0:
            self.mana -= 1
            target.take_damage(15)
        else:
            print(f"{self.name} has no mana remaining!")


#ENEMIES
class Enemy(Character):
    def __init__(self, name, health, defense, attack_power):
        super().__init__(name, health, defense, attack_power)
        self.exp_value = 1

class Goblin(Enemy):
    def __init__(self, name):
        super().__init__(name, health = 25, defense = 0, attack_power = 3)

class Orc(Enemy):
    def __init__(self, name):
        super().__init__(name, health = 40, defense = 1, attack_power = 5)

class Kobold(Enemy):
    def __init__(self, name):
        super().__init__(name, health = 35, defense = 0, attack_power = 4)
        self.breath_uses = 2

    def fire_breath(self, target):
        print(f"{self.name} uses it's fire breath!")
        if self.breath_uses > 0:
            self.breath_uses -= 1
            target.take_damage(7)
        else:
            print(f"{self.name} has used all of its fire breath!")
