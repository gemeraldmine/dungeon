rooms = {
    "Cell": {
        "id": 1,
        "item_count": 0,
        "description2": "The cell you woke up in, there's nothing here but the door leading to the West.",
        "item": None,
        "connectors": [0, 0, 0, "Junk Storage Room"],
    },
    "Junk Storage Room": {
        "id": 2,
        "item_count": 1,
        "description": """Nothing but trash and refuse, with exits to the North and East,
although that rope looks useful""",
        "description2": """Nothing but trash and refuse, with exits to the North and East.""",
        "item": "Rope",
        "connectors": ["Hallway", "Cell", 0, 0],
    },
    "Hallway": {
        "id": 3,
        "item_count": 1,
        "description": """A long hallway. To the North is a charred door, to the West is
a strong iron-reinforced door, and to the East is a wooden door. 
There's a note on the ground.""",
        "description2": """A long hallway. To the North is a charred door, to the West is
a strong iron-reinforced door, and to the East is a wooden door.""",
        "item": "Note",
        "connectors": ["Burned Room", "Guard Room", "Junk Storage Room", "Armory"],
    },
    "Armory": {
        "id": 4,
        "item_count": 1,
        "description": "The armory is empty, save a shiny stone.",
        "description2": "The armory is empty.",
        "item": "Flashstone",
        "connectors": [0, "Hallway", 0, 0],
    },
    "Guard Room": {
        "id": 5,
        "item_count": 1,
        "description": """A guard once occupied this room. There is also a closet to the North.
It appears he left something behind.""",
        "description2": "A guard once occupied this room. There is also a closet to the North.",
        "item": "Grappling Hook",
        "connectors": ["Closet", 0, 0, "Hallway"],
    },
    "Closet": {
        "id": 6,
        "item_count": 1,
        "description": "This closet contains little besides a worn broom",
        "description2": "Just an empty closet, not even an Easter egg...",
        "item": "Broom",
        "connectors": [0, 0, "Guard Room", 0],
    },
    "Burned Room": {
        "id": 7,
        "item_count": 1,
        "description": """The dragon's chasm lies to the East.
Its flame has only spared a shield.""",
        "description2": "The dragon's chasm lies to the East. Are you prepared?",
        "item": "Shield",
        "connectors": [0, "Dragon's Chasm", "Hallway", 0],
    },
    "Dragon's Chasm": {
        "id": 8,
        "item_count": 1,
        "description": "Good luck!",
        "item": None,
        "connectors": None,
    },
}
