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
