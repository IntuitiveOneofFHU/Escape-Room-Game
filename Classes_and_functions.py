import pygame
pygame.init()
screen = pygame.display.set_mode((500, 600))
font = pygame.font.SysFont("Arial", 48)
#Classes and functions will be made here and imported into the pygame file to reduce clutter


class LockDigit:
#class that contains everything a numberlock needs for a individual digit to be displayed on it
    def __init__(self, location, top_left, bottom_right, max_num=9):
    #max_num is how high the number can go before looping back to zero, default 9
        self.top_left = top_left
        self.bottom_right = bottom_right
        self.cur_code = 0
        self.location = location
        self.max_num = max_num
    def increment_code(self):
        self.cur_code = (self.cur_code + 1) % (self.max_num+1)

class NumberLock:
    def __init__(self, image, top_left, bottom_right):
        self.answer = []
        self.digits = []
        self.top_left = top_left
        self.bottom_right = bottom_right
        self.image = image
        self.show_lock = False
    def add_digit(self, answer, location, top_left, bottom_right):
        self.answer.append(answer)
        self.digits.append(LockDigit(location, top_left, bottom_right))
    def render_lock(self):
        screen.blit(pygame.image.load(self.image).convert_alpha(), (0,0))
        for digit in self.digits:
            screen.blit(font.render(str(digit.cur_code), True, (0,0,0)), digit.location)
    def check_code(self):
        for index, answer in enumerate(self.answer):
            if answer == self.digits[index].cur_code:
                correct = True
            else:
                correct = False
                break
        return correct

class Item:
    def __init__(self, image, name):
        self.image = image
        self.name = name

class Inventory:
    def __init__(self):
        self.items = []
    def add_item(self, item):
        self.items.append(item)
    def render_items(self):
        for index, item in enumerate(self.items):
            screen.blit(pygame.image.load(item.image).convert_alpha(), (25+index*75,525))

class ClickableItem:
    def __init__(self, item, top_left, bottom_right, visible=True):
        self.item = item
        self.visible = visible
        self.top_left = top_left
        self.bottom_right = bottom_right
    def click(self, inventory):
        if self.visible == True:
            inventory.items.append(self.item)
            self.visible = False

class ClickableObject:
    def __init__(self, name, description, top_left, bottom_right):
        self.name = name
        self.description = description
        self.top_left = top_left
        self.bottom_right = bottom_right

    def click(self):
        print(f'You clicked on {self.name}. {self.description}')