# Item List for Adventure Game
# Can add/remove items at will

from item import Item
from item import Treasure
from item import LightSource

item_list = {

    "sword": Item("sword", "A worn, but still sharp looking blade"),
    "ring": Item("ring", "a golden band. at first glance, appears to be nothing special"),
    "hammer": Item("hammer", "A simple looking sledgehammer"),
    "gold": Treasure("gold", "a pile of gold", 50000),
    "gem": Treasure("gemstone", "a bright, shiny gemstone", 1000),
    "torch": LightSource("torch", "This looks like it could light your way")
}
