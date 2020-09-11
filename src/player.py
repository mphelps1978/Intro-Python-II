# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, location,):
        self.name = name
        self.location = location
        self.inventory = []
        self.money = 0

    def __str__(self):
        return(f"Current Location: {self.location}")

    # Defining movement method within character class
    def move(self, direction):
        attribute = direction + "_to"
        if hasattr(self.location, attribute) and getattr(self.location, attribute) != "None":
            return getattr(self.location, attribute)
        else:
            print("You slam into a wall. You can\'t go that way")
            return(self.location)

    # Self Explanitory, but showing characters current inventory and currency
    def display_inventory(self):
        print("\nCurrently in your backpack:")
        for item in self.inventory:
            print(item.name)
        print(f'You currently have {self.money} gold\n')

    # Defining a method to pick up items. If they have a value, then we add it to our gold count
    def get_item(self, item):
        if item.name in self.location.items:
            if hasattr(item, "value"):
                self.money += item.value
                self.items.append(item)
                item.on_take()
                self.location.remove_item(item.name)

            else:
                print("there is nothing here by that name")

    # We can pick up items, but we need to drop them now. If they have a value, we remove it from our gold count
    def drop_item(self, item):
        if item.name in self.items:
            if hasattr(item, "value"):
                self.money -= item.value
                index = self.items.index(item)
                item.on_drop()
                self.location.add_item(item.name)
                del self.inventory[index]

            else:
                print("You aren\t carrying that!")

    # Let's add to our gold count
    def add_money(self, amount):
        self.money += amount

    # And conversely, remove gold
    def lose_money(self, amount):
        self.money -= amount

    # Define a method by which we can use an item
    def use_item(self, item):
        if item.name == self.location.correct_item:
            self.drop_item(item)
            self.location.success()

        else:
            print(self.location.item_use_failure)

    # What am I looking at?
    def examine_item(self, item):
        if item in self.inventory or item.name in self.location.items:
            print(item)
