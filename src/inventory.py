def inventory(player, item_list):
    print(f"Coin Purse: {player.money} gold")
    if len(player.inventory) > 0:
        print("\nYou open your backpack to find:\n")
        print(*player.items)
        drop = input("Examine or Drop item?\n")

        # What we can do with our inventory, and how it behaves -
        # first, determine what we're going to do and split it into 2 parts, the tool(item) and action(examine, drop, use)
        if "examine" in drop.lower() or 'drop' in drop.lower() or 'use' in drop.lower():
            split = drop.split()
            action = split[0]
            selected = split[1]

            # if they drop the item
            if action.lower == "drop":
                if selected in player.inventory:
                    index = player.inventory.index(selected)
                    item_list[selected].on_drop()
                    player.leave_item(index)
                    player.location.add_item(selected)
                    print(f"Now in the room: {player.location.items}")
                    print(f"In your backpack: {player.inventory}")
                    # Was it money? We need to deduct it from our players total
                    if hasattr(item_list[selected], "value") == True:
                        player.remove_money(item_list[selected].value)

            # If they use the item
            elif action == "use":
                # if the tool is the right one for the job
                if selected in player.items:
                    if player.location.correct_item == selected:
                        player.location.success()
                    else:
                        player.location.failure()

        else:
            print("You close your backpack.")

    else:
        print("\nYou aren\'t carrying anything in your backpack!")
