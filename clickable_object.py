'''class Clickable_Object:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    
    def usable_item(self):
        return False
    
    def inventory(self):
        self.inventory = []

    def click(self, usable_item):
        if self.usable_item():
            print(f'You picked up the {self.name} and added it to your inventory.')
            usable_item.append(self)
        else:
            print(f'You clicked on {self.name}. {self.description}')'''

class ClickableObject:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def is_usable(self):
        return False

    def click(self, inventory):
        if self.is_usable():
            print(f'You picked up the {self.name} and added it to your inventory.')
            inventory.append(self)
        else:
            print(f'You clicked on {self.name}. {self.description}')