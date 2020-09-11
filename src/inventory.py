class Inventory:
    def __init__(self, name, description, isLightSource=bool):
        self.name = name
        self.description = description
        self.isLightSource = isLightSource

    def __str__(self):
        return(self.name)
