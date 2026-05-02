#TODO: Make lock functional (change numbers, test combination)
#If numbers are changed with a click that increments it and gives a remainder of ten, we can skip making sure there arent bad inputs or that the number doesnt go above nine
#I think that clicking the rectangle above the lock should be the submit button


import pygame
import Classes_and_functions
from Classes_and_functions import room_list
from Classes_and_functions import inventory
from Classes_and_functions import bottom_text
pygame.mixer.init()


pygame.init()
pygame.mixer.music.load('labyrinth_escape.ogg')
pygame.mixer.music.set_volume(0.5) # Ears will no longer bleed when the music starts
pygame.mixer.music.play(-1)  # Loops the music indefinitely
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)


pygame.init()
screen = pygame.display.set_mode((500, 650))
clock = pygame.time.Clock()
running = True

font = pygame.font.SysFont("Arial", 48)

victory_room = Classes_and_functions.Room('victory','images/victory.png')
room1 = Classes_and_functions.Room('room1','images/room1/room1.png')
room2 = Classes_and_functions.Room('room2','images/room2/room2.png')

room1_door1 = Classes_and_functions.Door((231,218),"images/room1/door1.png","images/room1/door1_open.png", victory_room)
room1_door2 = Classes_and_functions.Door((0,216),"images/room1/door2.png","images/room1/door2_open.png", room2)
basic_key = Classes_and_functions.Item('images/key.png','key')
room1_key = Classes_and_functions.ClickableItem(basic_key,(120,337),'images/room1/key.png')
room1_door2_keylock = Classes_and_functions.ItemLock(basic_key, (22,350), (32,360), room1_door2)
room1.add_door(room1_door1)
room1.add_door(room1_door2)
room1.add_object(room1_key)
room1.add_nonrender(room1_door2_keylock)

room2_door1 = Classes_and_functions.Door((399,160),'images/room2/door1.png','images/room2/door1_open.png', room1, True)
room2_door2 = Classes_and_functions.Door((0,203),'images/room2/door2.png','images/room2/door2_open.png', 0)
green_die = Classes_and_functions.ClickableObject('a green die', 'It reads 6', (188,342),(195,355))
red_die = Classes_and_functions.ClickableObject('a red die', 'it reads 3', (270,347),(280,356))
brown_die = Classes_and_functions.ClickableObject('a brown die', 'it reads 5',(315,328),(328,340))
yellow_die = Classes_and_functions.ClickableObject('a yellow die', 'it reads 1',(228,361),(240,370))
room2.add_door(room2_door1)
room2.add_door(room2_door2)
room2.add_nonrender(green_die)
room2.add_nonrender(red_die)
room2.add_nonrender(brown_die)
room2.add_nonrender(yellow_die)

room2_lock = Classes_and_functions.NumberLock('images/room2/lock.png', (72,332), (110,378), (269,148), (387,197), room2_door2)
room2_lock.add_digit(1, (130, 300), (116,292), (172,369), 6)
room2_lock.add_digit(5, (220, 300), (202,291), (258,368), 6)
room2_lock.add_digit(3, (300, 300), (280,290), (336,367), 6)
room2_lock.add_digit(6, (380, 300), (361,289), (417,366), 6)
room2.add_lock(room2_lock)

room_list.add_room(room1)
room_list.add_room(room2)
room_list.add_room(room3)
room_list.add_room(victory_room)

room_list.change_room(room1)


while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #detects if mouse is hovering over lock when clicking, then shows lock, if it clicks the lock while displaying it, it hides the lock
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                room_list.click(event.pos)

    mouse_position = pygame.mouse.get_pos()

test_unlocked = False #makes the door start locked

testlock = NumLock_object.NumberLock([9,5,3,6], 'images/testlock.png', (460,255),(500,330))

show_lock = False

#function to check if something is within a box (Like a mouse click)
#takes in tuples for every input (coordinate pairs)
def mouse_between(top_left, bottom_right):
    if (top_left[0] <= event.pos[0] <= bottom_right[0]) and (top_left[1] <= event.pos[1] <= bottom_right[1]):
        return True
    else:
        return False

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #detects if mouse is hovering over lock when clicking, then shows lock, if it clicks the lock while displaying it, it hides the lock
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if mouse_between(first_digit_topleft, first_digit_bottomleft):
                    testlock.cur_code[0] = (testlock.cur_code[0] + 1) % 10
                elif mouse_between(second_digit_topleft, second_digit_bottomleft):
                    testlock.cur_code[1] = (testlock.cur_code[1] + 1) % 10
                elif mouse_between(third_digit_topleft, third_digit_bottomleft):
                    testlock.cur_code[2] = (testlock.cur_code[2] + 1) % 10
                elif mouse_between(fourth_digit_topleft, fourth_digit_bottomleft):
                    testlock.cur_code[3] = (testlock.cur_code[3] + 1) % 10
                elif mouse_between(testlock.top_left, testlock.bottom_right):
                    show_lock = not show_lock

    
    screen.fill("black") #wipes previous screen

    #render game here
    screen.blit(pygame.image.load("images/inventory.png").convert(), (0,500))
    inventory.render_items()
    bottom_text.render()

    room_list.render()

    room_list.cursor_render(mouse_position)
    if test_unlocked == True:
        screen.blit(testroom_unlocked, (0,0))
    else:
        screen.blit(testroom_locked, (0,0))

    first_digit = font.render(str(testlock.cur_code[0]), True, (0, 0, 0))
    second_digit = font.render(str(testlock.cur_code[1]), True, (0, 0, 0))
    third_digit = font.render(str(testlock.cur_code[2]), True, (0, 0, 0))
    fourth_digit = font.render(str(testlock.cur_code[3]), True, (0, 0, 0))


    first_digit_topleft = (116,292)
    first_digit_bottomleft = (172,369)
    second_digit_topleft = (202,291)
    second_digit_bottomleft = (258,368)
    third_digit_topleft = (280,290)
    third_digit_bottomleft = (336,367)
    fourth_digit_bottomleft = (417,366)
    fourth_digit_topleft = (361,289)
    
    if testlock.cur_code == testlock.answer:
        test_unlocked = True
        show_lock = False

    #gets mouse position
    mouse_position = pygame.mouse.get_pos()

    #----Displays Mouse Position----
    MOUSE_POS_DEBUG = font.render(str(mouse_position), True, (0, 0, 0))
    screen.blit(MOUSE_POS_DEBUG, (0,0))
    #---Comment Out When Unneeded---

    if show_lock == True:
        screen.blit(testlock.load_image(), (0,0))
        screen.blit(first_digit, (130, 300))
        screen.blit(second_digit, (220, 300))
        screen.blit(third_digit, (300, 300))
        screen.blit(fourth_digit, (380, 300))


    pygame.display.flip() #shows screen

    clock.tick(60) #sets FPS to 60

pygame.quit()
#TODO: Make lock functional (change numbers, test combination)
#If numbers are changed with a click that increments it and gives a remainder of ten, we can skip making sure there arent bad inputs or that the number doesnt go above nine
#I think that clicking the rectangle above the lock should be the submit button


import pygame
import NumLock_object

pygame.init()
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
running = True

testroom_locked = pygame.image.load('images/testroom_locked.png').convert()
testroom_unlocked = pygame.image.load('images/testroom_unlocked.png').convert()

font = pygame.font.SysFont("Arial", 48)

test_unlocked = False #makes the door start locked

testlock = NumLock_object.NumberLock([9,5,3,6], 'images/testlock.png', (460,255),(500,330))

show_lock = False

#function to check if something is within a box (Like a mouse click)
#takes in tuples for every input (coordinate pairs)
def mouse_between(top_left, bottom_right):
    if (top_left[0] <= event.pos[0] <= bottom_right[0]) and (top_left[1] <= event.pos[1] <= bottom_right[1]):
        return True
    else:
        return False

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #detects if mouse is hovering over lock when clicking, then shows lock, if it clicks the lock while displaying it, it hides the lock
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if mouse_between(first_digit_topleft, first_digit_bottomleft):
                    testlock.cur_code[0] = (testlock.cur_code[0] + 1) % 10
                elif mouse_between(second_digit_topleft, second_digit_bottomleft):
                    testlock.cur_code[1] = (testlock.cur_code[1] + 1) % 10
                elif mouse_between(third_digit_topleft, third_digit_bottomleft):
                    testlock.cur_code[2] = (testlock.cur_code[2] + 1) % 10
                elif mouse_between(fourth_digit_topleft, fourth_digit_bottomleft):
                    testlock.cur_code[3] = (testlock.cur_code[3] + 1) % 10
                elif mouse_between(testlock.top_left, testlock.bottom_right):
                    show_lock = not show_lock
    
    screen.fill("black") #wipes previous screen

    #render game here
    if test_unlocked == True:
        screen.blit(testroom_unlocked, (0,0))
    else:
        screen.blit(testroom_locked, (0,0))

    first_digit = font.render(str(testlock.cur_code[0]), True, (0, 0, 0))
    second_digit = font.render(str(testlock.cur_code[1]), True, (0, 0, 0))
    third_digit = font.render(str(testlock.cur_code[2]), True, (0, 0, 0))
    fourth_digit = font.render(str(testlock.cur_code[3]), True, (0, 0, 0))


    first_digit_topleft = (116,292)
    first_digit_bottomleft = (172,369)
    second_digit_topleft = (202,291)
    second_digit_bottomleft = (258,368)
    third_digit_topleft = (280,290)
    third_digit_bottomleft = (336,367)
    fourth_digit_bottomleft = (417,366)
    fourth_digit_topleft = (361,289)
    
    if testlock.cur_code == testlock.answer:
        test_unlocked = True
        show_lock = False

    #gets mouse position
    mouse_position = pygame.mouse.get_pos()

    #----Displays Mouse Position----
    ##MOUSE_POS_DEBUG = font.render(str(mouse_position), True, (0, 0, 0))
    ##screen.blit(MOUSE_POS_DEBUG, (0,0))
    #---Comment Out When Unneeded---




    pygame.display.flip() #shows screen

    clock.tick(60) #sets FPS to 60

pygame.quit()