import pygame
pygame.init()
screen = pygame.display.set_mode((500, 650))
font = pygame.font.SysFont("Arial", 48)
#Classes and functions will be made here and imported into the pygame file to reduce clutter

#function to check if something is within a box (Like a mouse click)
#takes in tuples for every input (coordinate pairs)
def mouse_between(top_left, bottom_right, mouse_pos):
    return (top_left[0] <= mouse_pos[0] <= bottom_right[0]) and (top_left[1] <= mouse_pos[1] <= bottom_right[1])

class RoomContainer:
    def __init__(self):
        self.rooms = []
    def add_room(self, room):
        self.rooms.append(room)
    def change_room(self, input_room):
        for room in self.rooms:
            if room.name == input_room.name:
                room.activate()
            else:
                room.deactivate()
    def render(self):
        for room in self.rooms:
            room.render()
    def click(self, mouse_pos):
        for room in self.rooms:
            if room.active:
                room.click(mouse_pos)

class Room:
    def __init__(self, name, image):
        self.name = name
        self.objects = []
        self.doors = []
        self.image = pygame.image.load(image).convert_alpha()
        self.active = False
    def add_object(self, obj):
        self.objects.append(obj)
    def add_door(self, door):
        self.doors.append(door)
    def activate(self):
        self.active = True
    def deactivate(self):
        self.active = False
    def render(self):
        if self.active:
            screen.blit(self.image, (0,0))
            for obj in self.objects:
                obj.render()
            for door in self.doors:
                door.render()
    def click(self, mouse_pos):
        for object in self.objects:
            if mouse_between(object.top_left, object.bottom_right, mouse_pos):
                object.click()
                
        for door in self.doors:
            if mouse_between(door.top_left, door.bottom_right, mouse_pos):
                door.click()
                

class Door:
    def __init__(self, top_left, bottom_right, locked_image, unlocked_image, connected_room):
        self.open = False
        self.top_left = top_left
        self.bottom_right = bottom_right
        self.locked_image = pygame.image.load(locked_image).convert_alpha()
        self.unlocked_image = pygame.image.load(unlocked_image).convert_alpha()
        self.connected_room = connected_room
    def open(self):
        self.open = True
    def render(self):
        if self.open:
            screen.blit(self.unlocked_image, self.top_left)
        else:
            screen.blit(self.locked_image, self.top_left)
    def click(self):
        if self.open:
            room_list.change_room(self.connected_room)


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
    def render(self):
        if self.show_lock:
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
        print(f"added {item.name}")
    def render_items(self):
        for index, item in enumerate(self.items):
            screen.blit(pygame.image.load(item.image).convert_alpha(), (25+index*75,525))

class ClickableItem:
    def __init__(self, item, top_left, bottom_right, image, visible=True):
        self.item = item
        self.image = pygame.image.load(image).convert_alpha()
        self.visible = visible
        self.top_left = top_left
        self.bottom_right = bottom_right
    def render(self):
        if self.visible:
            screen.blit(self.image, self.top_left)
    def click(self):
        if self.visible == True:
            self.visible = False
            inventory.add_item(self.item)


class ClickableObject:
    def __init__(self, name, description, top_left, bottom_right):
        self.name = name
        self.description = description
        self.top_left = top_left
        self.bottom_right = bottom_right

    def click(self):
        print(f'You clicked on {self.name}. {self.description}')

class BottomText():
    def __init__(self):
        self.timer = 0
        self.text = ''
    def render(self):
        if self.timer < 250:
            self.timer += 1
            if self.timer < 30:
                screen.blit(font.render(str(self.text),True,(self.timer*8.5,self.timer*8.5,self.timer*8.5)), (0,600))
            elif self.timer < 220:
                screen.blit(font.render(str(self.text),True,(255,255,255)), (0,600))
            else:
                screen.blit(font.render(str(self.text),True,((250-self.timer)*8.5,(250-self.timer)*8.5,(250-self.timer)*8.5)), (0,600))
    def update_text(self,text):
        self.text = text
        self.timer = 0

inventory = Inventory()
room_list = RoomContainer()