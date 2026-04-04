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
inventory = []
class ClickableObject:
    def __init__(self, name, description, usable):
        self.name = name
        self.description = description
        self.usable = True if usable else False


    def click(self, inventory):
        if self.usable:
            print(f'You picked up the {self.name} and added it to your inventory.')
            inventory.append(self)
        else:
            print(f'You clicked on {self.name}. {self.description}')

###########Inventory and testing code below###########
screwdriver = ClickableObject('screwdriver', 'A tool used for turning screws.', True)
door = ClickableObject('door', 'A sturdy wooden door. It seems to be locked.', False)
print(screwdriver.description)
print(door.description)
screwdriver.click(inventory)
door.click(inventory)
print(f'Inventory: {[item.name for item in inventory]}')