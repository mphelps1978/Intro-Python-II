# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items, isLit, naturalLight, correct_item, ius, alt_desc, detail, alt_detail):
        # General Room Properties
        self.name = name
        self.description = description
        self.new_passage = False
        self.items = items
        self.isLit = isLit
        self.naturalLight = naturalLight
        # Directional Properties
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None
        # Special Properties
        self.correct_item = correct_item
        self.item_use_success = ius
        self.item_use_failure = 'Not sure what you were expecting, but nothing happened.'
        self.alt_desc = alt_desc
        self.detail = detail
        self.alt_detail = alt_detail

    # General room descriptor - If there's no light, handle the situation accordingly
    def __str__(self):
        if self.isLit == True or self.naturalLight == True:
            return f"You have entered the {self.name}. {self.description}"
        else:
            return f"There is no light. You can't see a thing"

    # If the room is searched, reveal items - if they can see, that is
    def search_room(self):
        if self.isLit == True or self.naturalLight == True or "torch" in self.items:
            if len(self.items) > 0:
                print("In the room:")
                print(*self.items)
                print("\n")

            else:
                print("There is nothing here\n")
        else:
            print("It's pitch black. You can't see a thing")

    # If an item is picked up

    def remove_item(self, item):
        index = self.items.index(item)
        del self.items[index]

    # If an item is dropped from player inventory
    def add_item(self, current_item):
        self.items.append(current_item)

    # Let there be light!
    def illuminate(self):
        self.isLit = True

    # As it is given, so shall it be taken
    def deluminate(self):
        self.isLit = False

    # So you tried a tool did you? How'd that go?
    def failure(self):
        print(self.item_use_failure)

    # This time, it worked!!
    def success(self):
        print("\n")
        print(self.item_use_success)
        self.new_passage = True

    # And since it worked, we now have a new description
    def describe(self):
        if self.new_passage == False:
            print(self.detail)
        else:
            print(self.alt_detail)
