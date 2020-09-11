from room import Room
from player import Player
from inventory import inventory
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
                player.get_item(item_list[selected])
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
            player.display_inventory()

        # the only possible commands
        elif action in ['help', 'h', '?']:
            print(
                "Travel or search by using 't' or 's'. Travel 'n' 's' 'e' or 'w' .\nGet an item with 'get [name of item]' and drop with 'drop [name of item]. Use 'q' or 'quit' to end the game.\n")
        else:
            print(
                "I don't understand what you mean. Use 'h' to see list of available options")

    # Winner, Winner, Chicken Dinner!
    if win == True:
        print(
            f"Congratulations, {player.name}! You've found the treasure and won!")

    # Quitters Never win
    elif end == True:
        print('Thanks for playing\n')


# Let's Do it!!!
game_loop()
