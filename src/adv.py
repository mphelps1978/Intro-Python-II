from room import Room
from player import Player


# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
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
character = Player(room['outside'])
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
        "Chose a direction: [N]orth, [S]outh, [E]ast, [W]west, or [Q]uit:")
    print("####################################################")
    print("\n")
#
# If the user enters a cardinal direction, attempt to move to the room there.
    if character_input == 'n' or 'N':
        if character_location.n_to is not None:
            character.location = character.location.n_to
        else:
            print(no_path)
    elif character_input == 's' or 'S':
        if character_location.n_to is not None:
            character.location = character.location.s_to
        else:
            print(no_path)
    elif character_input == 'e' or 'E':
        if character_location.e_to is not None:
            character.location = character.location.e_to
        else:
            print(no_path)
    elif character_input == 'w' or 'W':
        if character_location.w_to is not None:
            character.location = character.location.w_to
        else:
            print(no_path)


# If the user enters "q", quit the game.
    elif character_input == 'q' or 'Q':
        print('Thank you for playing. Come again soon! \n \n')
        exit()


# Print an error message if the movement isn't allowed.
    else:
        print('Please Make a Valid Selection')
