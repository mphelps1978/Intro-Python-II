from room import Room
from player import Player
from inventory import Inventory
from item import Item
from item import Treasure
from item import LightSource
from room_list import room
from item_list import item_list
# There's got to be an easier way to do this...


# Link rooms together
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']
room['workroom'].s_to = room['overlook']
room['secret'].s_to = room['treasure']

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

def game_loop():
    name = input("What shall I call you?\n")
    player = Player(name, room['outside'])
    end = False
    win = False

    print(f"Welcome, brave {player.name} - Your destiny awaits!")
    selected = None

    while end == False and win == False:
        # Activate Secret Rooms!
        if player.location.new_passage == True:
            if player.location.name == 'Grand Overlook':
                room['overlook'].n_to = room['workroom']
            if player.location.name == 'Treasure Chamber':
                room['treasure'].n_to = room['secret']

        # define win condition
        if player.money >= 10000:
            win = True
            break

        # Check lightsources and adjust the room light accordingly (ie, do we have a torch?)
        if item_list['torch'] in player.inventory:
            player.location.illuminate()
        else:
            player.location.deluminate()

        print("\n")

        # If secret room discovered, we need to get the new description of the room
        if player.location.new_passage == True:
            print(player.location.alt_desc)
        else:
            print(player.location.description)

        action = input("What would you like to do?\n\n")
        split = action.split()

        # Quitting the game
        if action == 'q' or action == 'quit':
            end = True

        # Search the room
        elif action == 'search':
            player.location.search_room()

        # movement
        elif action == 'n' or action == 's' or action == 'e' or action == 'w':
            player.location = player.move(action)

        # Item use
        elif len(split) > 1:
            selected = split[1]
            if 'get' in action:
                player.take_item(item_list[selected])
            elif 'drop' in action:
                player.drop_item(item_list[selected])
            elif 'use' in action:
                player.use_item(item_list[selected])
            elif 'examine' in action:
                if selected != 'room':
                    player.examine_item(item_list[selected])
                else:
                    player.current_room.describe()

        # if they just say examine, it confuses us
        elif action == 'examine':
            print('What do you want to look at?')

        # inventory check
        elif action == "inventory" or action == 'i':
            player.print_inventory()

        # the only possible commands
        elif action in ['help', 'h', '?']:
            print(
                "Travel or search by using 't' or 's'. Travel 'n' 's' 'e' or 'w' .\nGet an item with 'get [name of item]' and drop with 'drop [name of item]. Use 'q' or 'quit' to end the game.\n")
        else:
            print(
                "I don't understand what you mean. Use 'h' to see list of available options")


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


# Room inventory
# first we need to check if the current room has anything in it
# if it does:
# show the item
# give the player the option to pick up the item
# if the player picks up the item:
# Remove the item from the room inventory
# Append the item to the character inventory

if len(character.location.inventory) != 0:
    room_contents = character.location.inventory.copy()

    for item in room_contents:
        item_picked_up = False
        print(f'you see the following items in the room: {item.name}')

        while item_picked_up is False:
            get_prompt = input(f"Pick up {item.name}? [Y]es or [N]o:  ")

            if get_prompt.lower() == "y":
                character.inventory.append(item)
                character.location.items.remove(item)
                item_picked_up = True

            elif get_prompt.lower() == "n":
                item_picked_up = True

        else:
            pass

    else:
        print("After a thorough search, you find nothing of use in this room")
