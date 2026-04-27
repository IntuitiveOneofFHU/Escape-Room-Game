#TODO: Make lock functional (change numbers, test combination)
#If numbers are changed with a click that increments it and gives a remainder of ten, we can skip making sure there arent bad inputs or that the number doesnt go above nine
#I think that clicking the rectangle above the lock should be the submit button


import pygame
import Classes_and_functions
from Classes_and_functions import room_list
from Classes_and_functions import inventory



pygame.init()
screen = pygame.display.set_mode((500, 650))
clock = pygame.time.Clock()
running = True

testroom_locked = pygame.image.load('images/testroom_locked.png').convert()
testroom_unlocked = pygame.image.load('images/testroom_unlocked.png').convert()

font = pygame.font.SysFont("Arial", 48)

test_unlocked = False #makes the door start locked



bottom_text = Classes_and_functions.BottomText()

room1 = Classes_and_functions.Room('room1','images/room1/room1.png')
room1_door1 = Classes_and_functions.Door((231,218),(341,382),"images/room1/door1.png","images/room1/door1_open.png", 0)
room1_door2 = Classes_and_functions.Door((0,216),(84,463),"images/room1/door2.png","images/room1/door2_open.png", 0)
basic_key = Classes_and_functions.Item('images/key.png','key')
room1_key = Classes_and_functions.ClickableItem(basic_key,(120,337),(138,358), 'images/room1/key.png')
room1.add_door(room1_door1)
room1.add_door(room1_door2)
room1.add_object(room1_key)

##testroom = Classes_and_functions.Room()
##
##testdoor = Classes_and_functions.Door((400,65),(500,400))
##testroom.add_door(testdoor)

testlock = Classes_and_functions.NumberLock('images/testlock.png', (460,255),(500,330))
testlock.add_digit(9, (130, 300), (116,292), (172,369))
testlock.add_digit(5, (220, 300), (202,291), (258,368))
testlock.add_digit(3, (300, 300), (280,290), (336,367))
testlock.add_digit(6, (380, 300), (361,289), (417,366))
##testroom.add_object(testlock)
##testroom.active = True
##room_list.add_room(testroom)

room_list.add_room(room1)
room_list.change_room(room1)


while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #detects if mouse is hovering over lock when clicking, then shows lock, if it clicks the lock while displaying it, it hides the lock
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                room_list.click(event.pos)
                ##if testlock.show_lock == True:
                ##   for digit in testlock.digits:
                ##        if mouse_between(digit.top_left, digit.bottom_right):
                ##            digit.increment_code()
                ##if mouse_between(testlock.top_left, testlock.bottom_right):
                ##    testlock.show_lock = not testlock.show_lock
                ##    bottom_text.update_text("the lock out of this room")

    if testlock.check_code():
        test_unlocked = True
        testlock.show_lock = False
    
    screen.fill("black") #wipes previous screen

    #render game here
    screen.blit(pygame.image.load("images/inventory.png").convert(), (0,500))
    inventory.render_items()
    bottom_text.render()

    room_list.render()



    #----Displays Mouse Position----
    ##mouse_position = pygame.mouse.get_pos()
    ##MOUSE_POS_DEBUG = font.render(str(mouse_position), True, (0, 0, 0))
    ##screen.blit(MOUSE_POS_DEBUG, (0,0))
    #---Comment Out When Unneeded---




    pygame.display.flip() #shows screen

    clock.tick(60) #sets FPS to 60

pygame.quit()