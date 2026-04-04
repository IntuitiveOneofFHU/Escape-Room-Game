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

testlock = NumLock_object.NumberLock([6,8,1,3], 'images/testlock.png', (460,255),(500,330))

show_lock = False

#function to check if something is within a box (Like a mouse click)
#takes in tuples for every input (coordinate pairs)
def is_between(point, top_left, bottom_right):
    if (top_left[0] <= point[0] <= bottom_right[0]) and (top_left[1] <= point[1] <= bottom_right[1]):
        return True
    else:
        return False

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #detects if mouse is hovering over lock when clicking, then shows lock, if it clicks the lock while displaying it, it hides the lock
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and is_between(event.pos, testlock.top_left, testlock.bottom_right) == True:
                if show_lock == False:
                    show_lock = True
                else:
                    show_lock = False
    
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