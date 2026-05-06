from src.entities import Warrior, Archer, Wizard

def create_character():
    print("Welcome to the Adventure Realm!")
    name = input("What is your name, traveler? "

    player = None
    while player is None:
        print("\nGroggy, you begin to wake up. As you open your eyes in a haze, you see before you a weapon.")
        print("As you begin to reach for this weapon, it starts to materialize before you.")
        print("What weapon do you see materializing in your hands?"
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
            print("Invalid choise, please select 1, 2, or 3.")

    return player

current_player = select_class()
current_player = describe()
