import random
from src.items import Coins, Healing_Potion, Mana_Potion

class Character:
    def __init__(self, name, health, defense, attack_power):
        self.name = name
        self.max_health = health
        self.health = health
        self.defense = defense
        self.attack_power = attack_power

    def describe(self):
        print(f"{self.name} is level {self.level} and has {self.health} health, {self.defense} defense, and {self.attack_power} power.")

    def get_attack_damage(self):
        low = self.attack_power - 2
        high = self.attack_power + 5
        return random.randint(max(0, low), high)

    def attack(self, target):
        damage = self.get_attack_damage()
        target.take_damage(damage)

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
        self.level = 1
        self.exp_gained = 0
        self.exp_to_level = 10
        self.inventory = []
        self.coins = 0

    def level_up(self):
        self.max_health = int(self.max_health * 1.1)
        self.health = self.max_health
        self.defense += 1
        self.attack_power += 2
        if hasattr(self, "mana"):
            self.max_mana += 2
            self.mana = self.max_mana
        self.level += 1
        self.exp_to_level *= 2
        print("You have gained a level!")
        self.describe()
        input("Press enter to continue.")

    def add_to_inventory(self, item):
        self.inventory.append(item)
        print(f"{item} has been added to your inventory!")

    def loot_coins(self, item):
        self.coins += item.amount
        print(f"You have found {item.amount} {item.name}!")

    def use_item(self, item):
        if item in self.inventory:
            item.use(self)
            self.inventory.remove(item)
        else:
            print("You don't have that item!")

    def heal(self, amount):
        self.health = min(self.health + amount, self.max_health)
        print(f"{self.name} healed! Current health: {self.health}/{self.max_health}")

    def restore_mana(self, amount):
        if self.max_mana == 0:
            print(f"{self.name} has no use for mana!")
        self.mana = min(self.mana + amount, self.max_mana)
        print(f"{self.name} has recharged! Current mana: {self.mana}/{self.max_mana}")

    def show_inventory(self):
        if len(self.inventory) == 0:
            print("Your inventory is empty")
            return
        else:
            while True:
                print("\nWhat would you like to use?")
                for i, item in enumerate(self.inventory):
                    print(f"{i + 1}. {item.name}.")
                print("0. Return.")
                item_choice = input("> ").strip()
                if item_choice == "0":
                    break
                if item_choice.isdigit():
                    choice_idx = int(item_choice)
                    if 0 < choice_idx <= len(self.inventory):
                        item = self.inventory[choice_idx - 1]
                        self.use_item(item)
                        break
                    else:
                        print("That item doesn't exist!")
                else:
                    print("Invalid item, please select from your inventory.")

class Warrior(Player):
    def __init__(self, name):
        super().__init__(name, health = 150, defense = 5, attack_power = 8)

class Archer(Player):
    def __init__(self, name):
        super().__init__(name, health = 150, defense = 2, attack_power = 12)

class Wizard(Player):
    def __init__(self, name):
        super().__init__(name, health = 120, defense = 0, attack_power = 10)
        self.mana = 10
        self.max_mana = 10

    def fireball(self, target):
        print(f"{self.name} casts a fireball!")
        if self.mana > 0:
            self.mana -= 1
            target.take_damage(self.attack_power * 2)
        else:
            print(f"{self.name} has no mana remaining!")


#ENEMIES
class Enemy(Character):
    def __init__(self, name, health, defense, attack_power):
        super().__init__(name, health, defense, attack_power)

    def act(self, target):
        self.attack(target)

class Goblin(Enemy):
    def __init__(self, name):
        super().__init__(name, health = 25, defense = 0, attack_power = 3)
        self.exp = 2

    def drop_loot(self):
        loot_options = ["coins", "nothing", "nothing"]
        choice = random.choice(loot_options)
        if choice == "coins":
            amount = random.randint(1, 7)
            return Coins("Gold", amount)
        else:
            return None

class Orc(Enemy):
    def __init__(self, name):
        super().__init__(name, health = 40, defense = 1, attack_power = 5)
        self.exp = 5

    def rage(self,target):
        print(f"{self.name} rages, gaining defense and attacking twice!")
        self.defense += 1
        if self.defense > 5:
            self.defense = 5
        self.attack(target)
        self.attack(target)

    def act(self, target):
        if self.health < 20 and random.random() < 0.45:
            self.rage(target)
        else:
            self.attack(target)

    def drop_loot(self):
        loot_options = ["coins", "health_potion", "nothing"]
        choice = random.choice(loot_options)
        if choice == "coins":
            amount = random.randint(3,8)
            return Coins("Gold", amount)
        elif choice == "health_potion":
            return Healing_Potion("Health Potion", heal_amount = 50)
        else:
            return None

class Kobold(Enemy):
    def __init__(self, name):
        super().__init__(name, health = 35, defense = 0, attack_power = 4)
        self.breath_uses = 2
        self.exp = 4

    def fire_breath(self, target):
        print(f"{self.name} uses it's fire breath!")
        self.breath_uses -= 1
        target.take_damage(12)

    def act(self, target):
        if self.breath_uses > 0 and random.random() < 0.35:
            self.fire_breath(target)
        else:
            self.attack(target)

    def drop_loot(self):
        loot_options = ["coins", "health_potion", "mana_potion", "nothing"]
        choice = random.choice(loot_options)
        if choice == "coins":
            amount = random.randint(1, 7)
            return Coins("Gold", amount)
        elif choice == "health_potion":
            return Healing_Potion("Health Potion", heal_amount = 50)
        elif choice == "mana_potion":
            return Mana_Potion("Mana Potion", mana_restored = 2)
        else:
            return None

class Tutorial_Goblin(Enemy):
    def __init__(self, name):
        super().__init__(name, health = 15, defense = 0, attack_power = 3)
        self.exp = 1

    def drop_loot(self):
        return Healing_Potion("Health Potion", heal_amount = 50)
