rooms = {
    "entrance": {
        "id": 1,
        "description": "The cell you woke up in, there's nothing here but the doors to the North and East",
        "item": "key",
        "connectors": ["dark hallway", "closet", 0, 0],
    },
    "dark hallway": {
        "id": 2,
        "description": "Leads into the rest of the stage",
        "item": "strange stone",
        "connectors": [0, 0, "entrance", 0],
    },
    "closet": {
        "id": 3,
        "description": "Storage",
        "item": "broom",
        "connectors": [0, 0, 0, "entrance"],
    },
}

playing = True
current_room = "entrance"
inventory = []

movement = "nesw"
actions = "hpim"

opening_description = """You wake up in a cold, damp room. A single candle candle burns.
There are heavy wooden doors to the North and East"""

help_message = """Input map:
Movement: n - North, e - East, s - South, w - West
Actions:  p - Pick up item, i - Display inventory, q - Quit game"""

separator = "-" * 48
bottom_line = "-" * 15 + "Press 'h' for Help" + "-" * 15


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


def move_room(move):
    """Changes value of current_room with converted idx"""
    idx = convert_idx(move)
    global current_room

    if rooms[current_room]["connectors"][idx] != 0:
        current_room = rooms[current_room]["connectors"][idx]
        return f"{separator}\nYou move to the {current_room}\n\n{rooms[current_room]['description']}\n{bottom_line}"
    else:
        return f"{separator}\nCan't go that way\n{bottom_line}"


def pick_item(item):
    """Checks inventory before appending to inventory list"""
    print(item)
    if item not in inventory:
        inventory.append(item)
        return f"{separator}\nAcquired {item}\n{separator}"
    else:
        print(f"{separator}\nItem already acquired\n{separator}")


while playing:
    """Main game loop"""
    user_input = input("What do you do?\n-> ")

    if user_input in movement:
        print(move_room(user_input))
    elif user_input == "p":
        print(pick_item(rooms[current_room]["item"]))
    elif user_input == "i":
        print(f"{separator}\nInventory:\n{'\n'.join(inventory)}\n{separator}")
    elif user_input == "h":
        print(help_message)
    elif user_input == "q":
        playing = False
