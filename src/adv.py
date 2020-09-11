from room import Room
from player import Player
from inventory import Inventory


# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons. Just inside the entrance, you notice a torch giving off a faint light",
                     [Inventory(
                         "Torch", "It\s a torch. What do you think it does\?")],
                     isLit=True
                     ),

    'foyer':    Room("Foyer",
                     """Dim light filters in from the south. Dusty passages run north and east."""
                     [Inventory(
                         "Note", "The note is written in what appears to be ancient runes. You are able to decipher it: My friends, what is here is yours")],
                     isLit=True
                     ),

    'overlook': Room("Grand Overlook",
                     """A steep cliff appears before you, falling into the darkness. Ahead to the north, you can make out a doorway, but there is no way across the chasm.""",
                     isLit=True
                     ),

    'narrow':   Room("Narrow Passage",
                     """The narrow passage bends here from west to north. The smell of gold permeates the air."""
                     [Inventory(
                         "Key", "This is a silver key encrusted with diamonds")],
                     isLit=False
                     ),

    'treasure': Room("Treasure Chamber",
                     """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south.""",
                     [Inventory(
                         "Chest", "There is a large, open chest in the center of the room. Sadly, it is empty.")],
                     isLit=False
                     )
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
character = Player(room["outside"])
no_path = 'You can\'t go that way!!'


# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.

while True:
    character_location = character.location
    print("\n")
    print("####################################################")
    print(f"{character.location.name}")
    print(f"{character.location.description}")
    print("\n")
    character_input = input(
        "Chose a direction: [N]orth, [S]outh, [E]ast, [W]west, [I]nventory or [Q]uit:  ")
    print("####################################################")
    print("\n")

# First, we need to check and see if the player has opened their backpack
# If they have, then we can give them the option to drop or examine items.

if character_input.lower() == 'i':
    adjust_inventory = True
    while adjust_inventory is True:
        adjust_inventory_prompt = input(
            "Would you like to check your bag?  [Y]es or [N]o:  ")
        if adjust_inventory_prompt.lower() == 'y':
            adjust_inventory = True
            inventory_list = character.inventory.copy()

            # Show the contents of their inventory
            inventory_list = []
            for item in character.inventory:
                inventory_list.append(item.name)
            print(
                f"You open your backpack and find: \n {str(inventory_list)[1: -1]}")

            # Time to drop some items
            for item in character.inventory:
                remove_prompt = input(f"Drop {item.name}? [Y]es, [N]o:  ")

                # if they say yes, then we remove it from our inventory, and add it to the rooms inventory
                if remove_prompt.lower() == "y":
                    character.inventory.remove(item)
                    character.location.inventory.append(item)
                print(
                    f"You drop {item.name} onto the floor. \n Your bag now contains:\n {character.items}")

        elif adjust_inventory_prompt.lower() == "n":
            adjust_inventory = False

        else:
            pass


# If the user enters a cardinal direction, attempt to move to the room there.
    if character_input.lower() == "n":
        if character_location.n_to is not None:
            character.location = character.location.n_to
        else:
            print(no_path)

    elif character_input.lower() == "s":
        if character_location.s_to is not None:
            character.location = character.location.s_to
        else:
            print(no_path)

    elif character_input.lower() == "e":
        if character_location.e_to is not None:
            character.location = character.location.e_to
        else:
            print(no_path)

    elif character_input.lower == "w":
        if character_location.w_to is not None:
            character.location = character.location.w_to
        else:
            print(no_path)


# If the user enters "q", quit the game.
    elif character_input.lower() == "q":
        print('Thank you for playing. Come again soon! \n \n')
        exit()


# Print an error message if the movement isn't allowed.
    else:
        print('Please Make a Valid Selection')
