# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, location, inventory=[]):
        self.location = location
        self.inventory = inventory

    def __str__(self):
        return(f"{self.inventory}")

    def __reduce__(self):
        return(f"{self.inventory}")
