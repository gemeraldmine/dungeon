import rooms
from messages import *


def convert_idx(move):
    """Convert movement input to index for room selection"""
    if move == "n":
        idx = 0
    elif move == "e":
        idx = 1
    elif move == "s":
        idx = 2
    elif move == "w":
        idx = 3
    else:
        idx = 4

    return idx


def move_room(move, current_room):
    """Changes value of current_room with converted idx"""
    idx = convert_idx(move)

    if rooms.rooms[current_room]["connectors"][idx] != 0:
        current_room = rooms.rooms[current_room]["connectors"][idx]
        if rooms.rooms[current_room]["item_count"] == 1:
            return (
                current_room,
                f"{separator}\nYou move to the {current_room}\n\n{rooms.rooms[current_room]['description']}\n{separator}",
            )
        else:
            return (
                current_room,
                f"{separator}\nYou move to the {current_room}\n\n{rooms.rooms[current_room]['description2']}\n{separator}",
            )
    else:
        return current_room, f"{separator}\nCan't go that way\n{separator}"


def pick_item(item, current_room, inventory):
    """Checks inventory before appending to inventory list"""
    if rooms.rooms[current_room]["item_count"] == 1:
        inventory.append(item)
        rooms.rooms[current_room]["item_count"] -= 1
        if item == "Note":
            return f"{note_message}"
        else:
            return f"{separator}\nAcquired {item}\n{separator}"
    else:
        print(f"{separator}\nNo items to acquire\n{separator}")


def check_win_condition(current_room, inventory):
    """Checks if player has won or lost when entering dragon room"""
    if current_room == "Dragon's Chasm":
        if len(inventory) == 6:
            print(f"{separator}\n{win_message}\n{separator}\nThank you for playing!!")
            return True
        else:
            print(f"{separator}\nYOU LOSE!\n{separator}")
            return True
    return False
