def get_choice(player, prompt, valid_options):
    while True:
        choice = input(f"{prompt} (or enter 'i' for inventory): ").lower()
        if choice == 'i':
            player.show_inventory()
            continue
        if choice in valid_options:
            return choice
        print("Invalid choice traveler.")

def story_tutorial_start(player):
    print("\nAs your firmly grasp your weapon you begin to look around.")
    print("You are standing in a dimly lit cave. A torch lights up ahead of you.")
    print("The torch is held by a small, angry looking goblin!")
    print("When prompted for input, please type just the digit for your selection.")

def story_tutorial_end(player):
    print("\nYou have slain the goblin and are now ready to begin exploring the cave.")
    print("Now that you have a healing potion, you can select inventory during combat to use items.")
    print("Collect loot, fight monsters, and find your way out of this cave to survive!")

def story_cave_1(player):
    print("\nYou begin making your way forward through the only exit from the room you can find.")
    print("The floor is slightly damp and you can tell there has been recent traffic in addition to the goblin you fought.")
    print("Up ahead you hear footsteps approaching and brace yourself for combat.")

def story_cave_2(player):
    print("\nYou have managed to survive your first real fight!")
    print("Spurred on by hope you press forward.")
    print("After a short while you come to a dimly lit split in the cave.")
    
def story_bonfire(player):
    print("\nYou build a small fire and rest your feet.")
    get_choice(player, "Press enter when you are ready to continue...", [""])

def story_cave_3(player):
    print("\nAfter a brief respite, you gather your things and press on.")
    print("You move forward at a careful pace, watching where you plant your feet so as not to make noise or trip.")
    print("Ahead of you, there are some enemies around a stalagmite chatting.")
    print("You charge in and take them by surprise!")

def story_cave_4(player):
    print("\nHaving defeated your enemies you gather any potions and gold and press on.")
    print("You begin to wonder where you are, what's going on with all these orcs, goblins, and kobolds.")
    print("How did you get here? Where does this cave lead?")
    print("So caught up in your thoughts you nearly walk face-first into the wall ahead of you.")
    print("You see the path extends to your left and right, another fork in the road...")

def story_cave_4l(player):
    print("\nYou turn left, determined to make sense of all this one way or another.")
    print("You hear voices ahead as you ready your weapon for another fight.")

def story_cave_4r(player):
    print("\nYou turn right, unsure what this could all mean.")
    print("You walk for quite some time before you come upon some more enemies.")
    print("Before you have a chance to hide, they spot you... and charge!")

def story_cave_5(player):
    print("\nYou gather your things and prepare to continue your journey, searching for an exit to the cave.")
    print("You walk slowly and carefully for what feels like hours, though it has only been minutes.")
    print("The last words of a fallen enemy ringing in your ears...")
    print("\n'Gungar will be sure to end you. He will use shards of your bones as his toothpicks for months to come...'")
    print("\nObviously Gungar will need to be dealt with... but... are you strong enough to handle him?")
    print("As you walk, pondering your near future, you hear the faint sound of footsteps approaching.")
    print("You ready yourself for combat, and charge as they round the corner!")

def story_cave_6(player):
    print("\nYou noticed on these enemies, they had an insignia branded into their armor.")
    print("It appears to be an orc skull inside a crescent moon.")
    print("You assume these must be some of Gungar's guards.")
    print("\nYou rifle through their belongings and find battle plans, and a crude map.")
    print("The battle plans seem to detail an overwhelming assault on a nearby settlement! You must escape and warn them!")
    print("You begin to look at the map and realize it is a map of the cave system you're in.")
    print("Finding the turns and rooms you've explored, you're able to pinpoint where you are now.")
    print("The only problem... There's one way out... And it's through the War Room.")
    print("\nYou can only assume Gungar is in there and your chances of a stealthy escape are nil.")
    print("You approach the door to the War Room and steal your resolve. You brace for a tough fight and grip your weapon tight.")
    print("You burst through the door and charge at the nearest living creature ready to fight!")
    print("Gungar lets out a road and raises his club... The battle for your life has begun.")

def story_final(player):
    print("\nGungar kneals, clutching at his chest as he heaves heavy breaths from the fight.")
    print("'You.. cannot stop.. the coming tide.... The orcs.. will rise.. and wipe out.. humanity....'")
    print("Gungar falls, coughs, and goes lifeless before you. A wave of relief floods your consciousness.")
    print("As the adrenaline fades, the pain of recent combat begins to come to life. Everything hurts.")
    print("\nYou sturdy yourself and begin limping towards the exit, expecting little to no resistance.")
    print("The remainder of the enemies were formed to scouting parties and have gone to gather intel for the time being.")
    print("You walk through the exit and shield your eyes from the sunlight.")
    print(f"\n'You look you've been through the ringer {player.name}.' A voice rings clearly over the sounds of surrounding nature.")
    print("'You could have come.. a little sooner!' You laugh as you work your way towards your friend's horse, excited to have a speedy trip home.")
    print("'A wizard is never late!' Your old friend says as you mount the horse with him.")
    print("\n\n--- CONGRATULATIONS!!! You have survived Gungar and escaped the cave. Thanks for playing! ---")
