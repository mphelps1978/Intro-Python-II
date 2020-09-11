# item class deffinitions.

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f'{self.name}, {self.description}'

    def on_drop(self):
        print(f'You have dropped {self.name}')

    def on_take(self):
        print(f'You have picked up {self.name}')


class Treasure(Item):
    def __init__(self, name, description, value):
        super().__init__(name, description)
        self.value = value

    def __str__(self):
        return f"{self.name} is worth ${self.value}"


class LightSource(Item):
    def __init__(self, name, description):
        super().__init__(name, description)

    def on_drop(self):
        print(f"It's not wise to drop your source of light!")
