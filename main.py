import rooms
from messages import *
import functions


def main():
    playing = True
    current_room = "Cell"
    inventory = []

    movement = "nesw"

    print(opening_description)

    while playing:
        """Main game loop"""
        if functions.check_win_condition(current_room, inventory):
            playing = False
            continue

        user_input = input("What do you do?\n-> ")

        if user_input in movement:
            current_room, message = functions.move_room(user_input, current_room)
            print(message)
        elif user_input == "p":
            print(
                functions.pick_item(
                    rooms.rooms[current_room]["item"], current_room, inventory
                )
            )
        elif user_input == "i":
            print(f"{separator}\nInventory:\n{'\n'.join(inventory)}\n{separator}")
        elif user_input == "h":
            print(help_message)
        elif user_input == "q":
            playing = False
        else:
            print(f"{separator}\nInvalid input\n{separator}")


if __name__ == "__main__":
    main()
