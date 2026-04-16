#TODO: Make lock functional (change numbers, test combination)
#If numbers are changed with a click that increments it and gives a remainder of ten, we can skip making sure there arent bad inputs or that the number doesnt go above nine
#I think that clicking the rectangle above the lock should be the submit button


import pygame
import Classes_and_functions

pygame.init()
screen = pygame.display.set_mode((500, 600))
clock = pygame.time.Clock()
running = True

testroom_locked = pygame.image.load('images/testroom_locked.png').convert()
testroom_unlocked = pygame.image.load('images/testroom_unlocked.png').convert()

font = pygame.font.SysFont("Arial", 48)

test_unlocked = False #makes the door start locked

key = Classes_and_functions.Item('images/key.png','key')
screwdriver = Classes_and_functions.Item('images/screwdriver.png','screwdriver')

inventory = Classes_and_functions.Inventory()
inventory.add_item(screwdriver)
inventory.add_item(key)

testlock = Classes_and_functions.NumberLock('images/testlock.png', (460,255),(500,330))
testlock.add_digit(9, (130, 300), (116,292), (172,369))
testlock.add_digit(5, (220, 300), (202,291), (258,368))
testlock.add_digit(3, (300, 300), (280,290), (336,367))
testlock.add_digit(6, (380, 300), (361,289), (417,366))

#function to check if something is within a box (Like a mouse click)
#takes in tuples for every input (coordinate pairs)
def mouse_between(top_left, bottom_right):
    return (top_left[0] <= event.pos[0] <= bottom_right[0]) and (top_left[1] <= event.pos[1] <= bottom_right[1])

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #detects if mouse is hovering over lock when clicking, then shows lock, if it clicks the lock while displaying it, it hides the lock
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if testlock.show_lock == True:
                    for digit in testlock.digits:
                        if mouse_between(digit.top_left, digit.bottom_right):
                            digit.increment_code()
                if mouse_between(testlock.top_left, testlock.bottom_right):
                    testlock.show_lock = not testlock.show_lock

    if testlock.check_code():
        test_unlocked = True
        testlock.show_lock = False
    
    screen.fill("black") #wipes previous screen

    #render game here
    screen.blit(pygame.image.load("images/inventory.png").convert(), (0,500))
    inventory.render_items()

    if test_unlocked == True:
        screen.blit(testroom_unlocked, (0,0))
    else:
        screen.blit(testroom_locked, (0,0))

    if testlock.show_lock == True:
        testlock.render_lock()

    #gets mouse position
    mouse_position = pygame.mouse.get_pos()

    #----Displays Mouse Position----
    MOUSE_POS_DEBUG = font.render(str(mouse_position), True, (0, 0, 0))
    screen.blit(MOUSE_POS_DEBUG, (0,0))
    #---Comment Out When Unneeded---




    pygame.display.flip() #shows screen

    clock.tick(60) #sets FPS to 60

pygame.quit()