class Clickable_Object:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def click(self):
        if usable_item:
            print(f'You picked up the {self.name} and added it to your inventory.')
        else:
            print(f'You clicked on {self.name}. {self.description}')
