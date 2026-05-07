def get_choice(prompt, valid_options):
    while True:
        choice = input(f"{prompt} (or enter 'i' for inventory: ").lower().strip()
        if choice = 'i':
            player.show_inventory()
            continue
        if choice in valid_options:
            return choice
        print("Invalid choice traveler.")

def story_tutorial_start():
    print("\nAs your firmly grasp your weapon you begin to look around.")
    print("You are standing in a dimly lit cave. A torch lights up ahead of you.")
    print("The torch is held by a small, angry looking goblin!")
    print("When prompted for input, please type just the digit for your selection.")

def story_tutorial_end():
    print("\nYou have slain the goblin and are now ready to begin exploring the cave.")
    print("Now that you have a healing potion, you can select inventory during combat to use items.")
    print("Collect loot, fight monsters, and find your way out of this cave to survive!")

def story_cave_1():
    print("\nYou begin making your way forward through the only exit from the room you can find.")
    print("The floor is slightly damp and you can tell there has been recent traffic in addition to the goblin you fought.")
    print("Up ahead you hear footsteps approaching and brace yourself for combat.")

def story_cave_2():
    print("\nYou have managed to survive your first real fight!")
    print("Spurred on by hope you press forward.")
    print("After a short while you come to a dimly lit split in the cave.")
    
def story_bonfire():
    print("\nYou build a small fire and rest your feet.")
    input("Press enter when you are ready to continue...")

