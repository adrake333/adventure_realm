from src.entities import *
from src.story import *
from src.encounters import *
from src.items import *
import sys
import random

def create_character():
    print("Welcome to the Adventure Realm!")
    name = input("What is your name, traveler? ")

    player = None
    while player is None:
        print("\nGroggy, you begin to wake up. As you open your eyes in a haze, you see before you a weapon.")
        print("As you begin to reach for this weapon, it starts to materialize before you.")
        print("What weapon do you see materializing in your hands?")
        print("\nChoose your weapon:")
        print("1. Broadsword and Shield (High Health & Defense)")
        print("2. Shortbow (High Attack)")
        print("3. Staff (Magic)")

        choice = input("> ").strip()

        if choice == "1":
            player = Warrior(name)
        elif choice == "2":
            player = Archer(name)
        elif choice == "3":
            player = Wizard(name)
        else:
            print("Invalid choice, please select 1, 2, or 3.")

    return player

def run_combat(player, enemies):
#presentation
    while len(enemies) > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        if hasattr(player, "mana"):
            print(f"Current Stats: {player.health} HP, {player.mana} Mana")
        else:
            print(f"Current Vitality: {player.health} HP")
        print("\n--- Targets ---")
        for i, monster in enumerate(enemies):
            print(f"{i + 1}. {monster.name} ({monster.health} HP)")
#actions
        actions = ["1. Attack", "2. Inventory"]
        if hasattr(player, "mana") and player.mana > 0:
            actions.append("3. Fireball")
        while True:
            turn_over = False
            print("\n--- Actions ---")
            for action in actions:
                print(action)

            action_choice = input("> ").strip()
            valid_actions = [a[0] for a in actions]

            if action_choice not in valid_actions:
                print("Invalid choice, please select from the available actions.")
                continue
#attack
            elif action_choice == "1":
                if len(enemies) == 1:
                    player.attack(enemies[0])
                    turn_over = True
                    break
                while True:
                    print("\nWho would you like to attack?")
                    target_choice = input("> ").strip()
                    if target_choice.isdigit():
                        choice_idx = int(target_choice)
                        if 0 < choice_idx <= len(enemies):
                            target = enemies[choice_idx - 1]
                            player.attack(target)
                            turn_over = True
                            break
                        else:
                            print("That enemy doesn't exist!")
                    else:
                        print("Invalid target, please select from the available targets.")
                break
#inventory           
            elif action_choice == "2":
                if len(player.inventory) == 0:
                    print("Your inventory is empty!")
                else:
                    while True:
                        print("\nWhat would you like to use?")
                        for i, item in enumerate(player.inventory):
                            print(f"{i + 1}. {item.name}.")
                        print("0. Return.")
                        item_choice = input("> ").strip()
                        if item_choice == "0":
                            break
                        if item_choice.isdigit():
                            choice_idx = int(item_choice)
                            if 0 < choice_idx <= len(player.inventory):
                                item = player.inventory[choice_idx - 1]
                                player.use_item(item)
                                turn_over = True
                                break
                            else:
                                print("That item doesn't exist!")
                        else:
                            print("Invalid item, please select from your inventory.")
#fireball            
            elif action_choice == "3":
                if len(enemies) == 1:
                    player.fireball(enemies[0])
                    turn_over = True
                    break
                while True:
                    print("\nWho would you like to target?")
                    target_choice = input("> ").strip()
                    if target_choice.isdigit():
                        choice_idx = int(target_choice)
                        if 0 < choice_idx <= len(enemies):
                            target = enemies[choice_idx - 1]
                            player.fireball(target)
                            turn_over = True
                            break
                        else:
                            print("That enemy doesn't exist!")
                    else:
                        print("Invalid target, please select from the available targets.")
                break
            
            if turn_over:
                break
        
#loot drop
        for e in enemies:
            if e.health <= 0:
                loot = e.drop_loot()
                if loot is not None:
                    if isinstance(loot, Coins):
                        player.loot_coins(loot)
                    else:
                        player.add_to_inventory(loot)
#experience
                player.exp_gained += e.exp
                while player.exp_gained >= player.exp_to_level:
                    player.level_up()

#clean up dead enemies
        enemies = [e for e in enemies if e.health > 0]

#transition
        if len(enemies) > 0:
            print("\n--- Enemy Turn ---")
            for monster in enemies:
                monster.act(player)
                if player.health <= 0:
                    print("You have fallen in battle...")
                    input("Press Enter to acccept your fate...")
                    sys.exit()

###START GAME###

player = create_character()
player.describe()
story_tutorial_start()
run_combat(player, get_tutorial_encounter())
story_tutorial_end()
story_cave_1()
run_combat(player, get_random_encounter())
story_cave_2()
path = get_choice(player, "Do you go left or right?", ["left", "right"])
if path == "left":
    print("\nYou head left at the fork and come to a closed door.")
    print("You hear enemies approaching from behind the door...")
    run_combat(player, get_random_encounter())
elif path == "right":
    print("\nYou heead right down the path and continue to an open cavern.")
    print("You look around and find a treasure chest hidden in the corner!")
    loot_options = [Healing_Potion, Mana_Potion, Coins]
    for _ in range(3):
        chosen_class = random.choice(loot_options)
        if chosen_class == Coins:
            loot = Coins("Gold", random.randint(10, 30))
            player.loot_coins(loot)
        elif chosen_class == Healing_Potion:
            loot = Healing_Potion("Health Potion", heal_amount = 50)
            player.add_to_inventory(loot)
        elif chosen_class == Mana_Potion:
            loot = Mana_Potion("Mana Potion", mana_restored = 2)
            player.add_to_inventory(loot)
story_bonfire()
story_cave_3()
run_combat(player, get_random_encounter())
story_cave_4()
path = get_choice(player, "Do you go left or right?... ", ["left", "right"]
    if path == "left":
        story_cave_4l()
        run_combat(player, get_random_encounter())
    if path == "right":
        story_cave_4r()
        run_combat(player, get_random_encounter())
story_bonfire()
story_cave_5()
run_combat(player, get_random_encounter())
story_cave_6()
run_combat(player, get_boss_encounter())
story_final()
