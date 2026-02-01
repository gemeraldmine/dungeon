print("Welcome to the dungeon, we've got fun and games")


while True:
    u_choice = input("Enter command: ").lower
    while u_choice != "q":
        if u_choice == "n":
            print("You moved North")
            u_choice = input("Enter command: ").lower()

        elif u_choice == "s":
            print("You moved South")
            u_choice = input("Enter command: ").lower()

    print("Done")
