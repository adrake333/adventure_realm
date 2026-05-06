from src.entities import Warrior, Archer, Wizard

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
    while len(enemies) > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        if hasattr(player, "mana"):
            print(f"Current Stats: {player.health} HP, {player.mana} Mana")
        else:
            print(f"Current Vitality: {player.health} HP")
        print("\n--- Targets ---")
        for i, monster in enumerate(enemies):
            print(f"{i + 1}. {monster.name} ({monster.health} HP)")
        actions = ["1. Attack", "2. Inventory"]
        if hasattr(player, "mana") and player.mana > 0:
            actions.append("3. Magic")
        while True:
            print("\n--- Actions ---")
            for action in actions:
                print(action)

            action_choice = input("> ").strip()
            valid_actions = [a[0] for a in actions]

            if action_choice not in valid_actions:
                print("Invalid choice, please select from the available actions.")
                continue
            elif action_choice == "1":
                print("Who would you like to attack?")
                break
            elif action_choice == "2":
                print("What would you like to use?")
                break
            elif action_choice == "3":
                print("What spell would you like to use?")
                break
            else:
                print("Invalid choice, please select from the available actions.")

        enemies = [e for e in enemies if e.health > 0]

        if len(enemies) > 0:
            print("\n--- Enemy Turn ---")
            for monster in enemies:
                monster.act(player)

current_player = create_character()
current_player.describe()
