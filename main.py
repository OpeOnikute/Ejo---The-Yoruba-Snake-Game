# -*- coding: cp1252 -*-
import pygame
import pyganim
import time
import random
import health

pygame.init()

# Setting the display width and height
display_width =  800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Ejo')


# colours
white = (255,255,255)
black = (0,0,0)
grey = (220,220,220)
red = (200, 0,0)
light_red = (255, 20, 20)
green = (0, 140, 0)
light_green = (0, 240, 0)
yellow = (255, 255, 128)
light_yellow = (255, 255, 228)

# loading the animations
gameOverAnim = pyganim.PygAnimation([('game_over2.png', 150),('game_over3.png', 100)])
bonusAnim = pyganim.PygAnimation([('bonus_text1.png', 150),('bonus_text2.png', 100)])

# loading the images
icon = pygame.image.load('snakeHead.png')
img = pygame.image.load('snake.png')
eba = pygame.image.load('eba2.png')
bgd = pygame.image.load('bgd.png')
snakeBody = pygame.image.load('body.png')
welcome_screen = pygame.image.load('welcome.png')
game_over_face = pygame.image.load('face005.png')
skin = pygame.image.load('skin.png')
bgdside = pygame.image.load('bgd_side.png')

# setting the game icon to the snake head
pygame.display.set_icon(icon)

# initializing the timing functionality and some standard variables
clock = pygame.time.Clock()
AppleThickness = 30
block_size = 20
FPS = 30
direction = 'right'

# Loading the fonts to be used
extra_smallfont = pygame.font.SysFont('comicsansms', 15)
smallfont = pygame.font.SysFont('comicsansms', 20)
small2font = pygame.font.Font(r'C:\Users\Ope O\Downloads\Fonts\eyelevation6.ttf', 40)
medfont = pygame.font.SysFont('comicsansms', 50)
medfontButton = pygame.font.Font(r'C:\Users\Ope O\Downloads\Fonts\eyelevation6.ttf', 50)
medfontButton2 = pygame.font.Font(r'C:\Users\Ope O\Downloads\Fonts\eyelevation6.ttf', 80)
largefont = pygame.font.SysFont('comicsansms', 80)

# rendering the font for the copyright display at the bottom.
sign = extra_smallfont.render('©2015.' , True, white)

def message_to_screen(msg, color, y_displace=0, x_displace=0, size = "small", font = None, fontSize = None, blink=False):
    textSurf, textRect = text_objects(msg, color, size, font, fontSize)
    textRect.center = (display_width / 2)+x_displace, (display_height /2)+y_displace
##    flashSurf = pygame.Surface((textSurf.get_width(), textSurf.get_height()))
##    flashSurf = flashSurf.convert_alpha()

    gameDisplay.blit(textSurf, textRect)
##    origSurf = textSurf.copy()


    
def pause():

    paused = True
    message_to_screen('Paused',
                        black,
                      -100,
                      size = 'large')
    message_to_screen('Press C to continue or Q to quit.',
                      black,
                      25)
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        
        pygame.display.update()
        clock.tick(5)


def score_update(score):
    """
    :param score:
    :return:
    """
    text = smallfont.render('Score: ' + str(score), True, white)
    gameDisplay.blit(text, [display_width - 765,20])


def game_controls():
    """
    :return:
    """
    gcont  = True

    while gcont:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                    
        gameDisplay.fill(white)
##        message_to_screen(msg,
##                          color,
##                          y_displace=0,
##                          x_displace=0,
##                          size = "small", font = None, fontSize = None)
        message_to_screen('CONTROLS',
                           green,
                           y_displace=-150,
                           x_displace = 0, 
                           size = 'large')
        message_to_screen('Move Snake: Up, Down, Left and Right arrows',
                          black,
                          y_displace = 10,
                          x_displace = 0,
                          size = 'small')
        message_to_screen('Pause: P ',
                          black,
                          y_displace = 50 ,
                          x_displace = 0,
                          size = 'small')

        text_to_button('Play', yellow, light_yellow, 250,455,80,40, size = 'small', action = 'play')

            
        # text_to_button('Quit', black, white, 612.5,457,80,40 ,  size = 'small', action = 'quit')
        
        text_to_button('Quit', red, light_red, 450,455,80,40 ,  size = 'small', action = 'quit')
        pygame.display.update()



def randAppleGen():
    """
    :return:
    """
    randAppleX = round(random.randrange(40, display_width-AppleThickness-40))#/10)*10     #Eating with the Apple and regenerating a new apple somewhere else
    randAppleY = round(random.randrange(30, display_height-AppleThickness-30))#/10)*10

    return randAppleX, randAppleY
 
def text_to_button(msg, color, inactive_color, buttonx, buttony, buttonwidth, buttonheight, size = None, action = None, blink = False):
    """
    :param msg:
    :param color:
    :param inactive_color:
    :param buttonx:
    :param buttony:
    :param buttonwidth:
    :param buttonheight:
    :param size:
    :param action:
    :param blink:
    :return:
    """

    textSurf, textRect = text_objects_button(msg, color, size)
    textSize = textSurf.get_width()
    
    # textRect.center = ((buttonx+(buttonwidth/2)), buttony+(buttonheight/2))
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    gameDisplay.blit(textSurf, (buttonx, buttony))
    if buttonx + textSize > cur[0] > buttonx and buttony + textSurf.get_height() > cur[1] > buttony:
        textSurf2, textRect2 = text_objects_button(msg, inactive_color, size)
        gameDisplay.blit(textSurf2, (buttonx-2, buttony-2))
        
        
        if click[0] == 1 and action != None:
            if action == 'quit':
                pygame.quit()
                quit()
            if action == 'controls':
                game_controls()
            if action == 'play':
                gameLoop()
            if action == 'main':
                game_intro()

        # pygame.display.update()


def game_intro():
    intro  = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                    
        
        gameDisplay.fill(white)

        gameDisplay.blit(welcome_screen,  (0,0))
        gameDisplay.blit(sign, [display_width/2 - 50,display_height-20])

        text_to_button('Play', yellow, light_yellow, 298,440,80,40, size = 'medium2', action = 'play')

        text_to_button('Controls', black, light_green, 102,467,100,40,  size = 'small', action = 'controls')
        text_to_button('Controls', green, light_green, 100,465,100,40,  size = 'small', action = 'controls')
        
        text_to_button('Quit', red, white, 520,465,80,40 ,  size = 'small', action = 'quit')
        text_to_button('Quit', black, light_red, 522,467,80,40 ,  size = 'small', action = 'quit')
        text_to_button('Quit', red, light_red, 521,465,80,40 ,  size = 'small', action = 'quit')
        
        pygame.display.update()
        clock.tick(FPS)

##def button(text, x, y, width, height, inactive_color, active_color, action = None):
##    cur = pygame.mouse.get_pos()
##    click = pygame.mouse.get_pressed()
##    
##    if x + width > cur[0] > x and y + height > cur[1] > y:
##        pygame.draw.rect(gameDisplay, active_color, (x,y,width,height))
##        pygame.draw.line(gameDisplay, black, (x, y),(x+width, y),3)
##        pygame.draw.line(gameDisplay, black, (x+width, y),(x+width, y+height),3)
##        pygame.draw.line(gameDisplay, black, (x+width, y+height),(x, y+height),3)
##        pygame.draw.line(gameDisplay, black, (x, y+height),(x, y),3)
##        
##        if click[0] == 1 and action != None:
##            if action == 'quit':
##                pygame.quit()
##                quit()
##            if action == 'controls':
##                game_controls()
##            if action == 'play':
##                gameLoop()
##            if action == 'main':
##                game_intro()
##            
##    else:
##        pygame.draw.rect(gameDisplay, inactive_color, (x,y,width,height))
##        pygame.draw.line(gameDisplay, black, (x, y),(x+width, y),3)
##        pygame.draw.line(gameDisplay, black, (x+width, y),(x+width, y+height),3)
##        pygame.draw.line(gameDisplay, black, (x+width, y+height),(x, y+height),3)
##        pygame.draw.line(gameDisplay, black, (x, y+height),(x, y),3)
##
##    text_to_button(text, white, x,y,width,height)

def Snake(block_size, snakeList):
    ##functionality for rotation:
    if direction == 'right':
        head = pygame.transform.rotate(img, 270)
    if direction == 'left':
        head = pygame.transform.rotate(img, 90)
    if direction == 'up':
        head = img
    if direction == 'down':
        head = pygame.transform.rotate(img, 180)
    gameDisplay.blit(head,  (snakeList[-1][0], snakeList[-1][1]))
    for XnY in snakeList[:-1]:
        gameDisplay.blit(skin,  (XnY[0], XnY[1]))
       # pygame.draw.rect(gameDisplay, green, [XnY[0], XnY[1], block_size, block_size])
    

def text_objects(text, color, size = None,  font = None, fontSize = None):
    """
    :param text:
    :param color:
    :param size:
    :param font:
    :param fontSize:
    :return:
    """
    if size == 'small':
        textSurface = smallfont.render(text, True, color)
    elif size == 'medium':
        textSurface = medfontButton.render(text, True, color)
    elif size == 'large':
        textSurface = largefont.render(text, True, color)
    elif font != None:
        font = pygame.font.Font(r'C:\Users\Ope O\Downloads\Fonts' + '\\' + font , fontSize)
        textSurface = font.render(text, True, color)
        
    return textSurface, textSurface.get_rect()


def text_objects_button(text, color, size=None):
    """
    :param text:
    :param color:
    :param size:
    :return:
    """
    if size == 'small':
        textSurface = small2font.render(text, True, color)
    elif size == 'medium':
        textSurface = medfontButton.render(text, True, color)
    elif size == 'medium2':
        textSurface = medfontButton2.render(text, True, color)
    elif size == 'large':
        textSurface = largefont.render(text, True, color)

    return textSurface, textSurface.get_rect()


def health_bars(snake_health):
    """
    :param snake_health:
    :return:
    """
    if snake_health > 75:
        snake_health_color = green
    elif snake_health > 50:
        snake_health_color = yellow
    else:
        snake_health_color = red
    health_text = smallfont.render('Health: ', True, white)
    gameDisplay.blit(health_text,[display_width-210, 20])
    pygame.draw.rect(gameDisplay, black , (display_width-131, 25, 92, 22))
    pygame.draw.rect(gameDisplay, white , (display_width-130, 26, 90, 20))
    pygame.draw.rect(gameDisplay, snake_health_color , (display_width-130, 26, snake_health, 20))


def gameLoop():
    global direction
    global snakeLength
    direction = 'right'
    
    score_value = 1   

    gameExit = False
    gameOver = False

    lead_x = display_width/2
    lead_y = display_height/2

    lead_x_change = 10
    lead_y_change = 0

    snake_health = 90

    snakeList = []
    snakeLength = 1
    
    randAppleX, randAppleY = randAppleGen()
    
    # The event handling loop is:
    while not gameExit:
##        if gameOver == True:
##            pygame.display.update()

        while gameOver == True:
            gameOverAnim.play()
            gameDisplay.blit(bgd, (0,0))
            gameDisplay.blit(game_over_face, (300, 200))
            Snake(block_size, snakeList)
            gameDisplay.blit(bgdside, (0,0))
            gameDisplay.blit(sign, [display_width/2 - 30,display_height-20])
            health_bars(snake_health)
           # pygame.time.set_timer(Text1, 10)
           # pygame.time.set_timer(Text2, 90)
            
            
            gameOverAnim.blit(gameDisplay, (263, 352))
##            message_to_screen("Game Over",
##                              red,
##                              y_displace=180,
##                              x_displace = 25,
##                              size = None,
##                              font = 'BEARPAW_.ttf', 
##                              fontSize = 90,
##                               )
            
                
            message_to_screen('Score: ' + str((score_value-1)*2),
                              black,
                              y_displace = -220,
                              x_displace=10, 
                              size = None,
                              font = 'VIDEOPHREAK.ttf',
                              fontSize = 50)

            
            text_to_button('Play Again', black, light_yellow, 62,455,80,40, size = 'small', action = 'play')
            text_to_button('Play Again', yellow, light_yellow, 60,455,80,40, size = 'small', action = 'play')
            
           # text_to_button('Quit', black, white, 612.5,457,80,40 ,  size = 'small', action = 'quit')
            text_to_button('Quit', black, black, 622,455,80,40 ,  size = 'small', action = 'quit')
            text_to_button('Quit', red, light_red, 620,455,80,40 ,  size = 'small', action = 'quit')

           # button('Play Again', 150,400,100,40, black, light_green, action = 'play')
           # button('Controls', 350,400,100,40, black, light_green, action = 'controls')
           # button('Quit', 570,400,80,40 , black, light_green, action = 'quit')
            

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                    gameOver = False

            clock.tick(300)
            
            pygame.display.update()

               # if event.type == pygame.KEYDOWN:
               #     if event.key == pygame.K_q:
               #         gameExit = True
               #         gameOver = False
               #     if event.key == pygame.K_c:
               #         gameLoop()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direction = 'left'
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    direction = 'right'
                    lead_x_change = block_size
                    lead_y_change = 0 
                elif event.key == pygame.K_UP:
                    direction = 'up'
                    lead_y_change = -block_size
                    lead_x_change = 0 
                elif event.key == pygame.K_DOWN:
                    direction = 'down'
                    lead_y_change = block_size
                    lead_x_change = 0
                elif event.key == pygame.K_p:
                    pause()
        
        if lead_x >= display_width-35 or lead_x <= 25 or lead_y >= display_height-20 or lead_y <= 10:
             snake_health = 1
             pygame.display.update()
             gameOver = True
             
            

            # Code to write if you want the stuff to stop moving when you relase a key
            #if event.type == pygame.KEYUP:
            #    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            #        lead_x_change = 0

        
        lead_x += lead_x_change
        lead_y += lead_y_change
        
        # gameDisplay.fill(white)
        gameDisplay.blit(bgd, (0,0))
        
        # pygame.display.update()

        # pygame.draw.rect(gameDisplay, red, [randAppleX, randAppleY, AppleThickness, AppleThickness])

        gameDisplay.blit(eba, (randAppleX, randAppleY))
        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        if len(snakeList) > snakeLength:
               del snakeList[0]

        # collision detection for loop:
        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                snake_health = snake_health - 30
                if snake_health <= 0:
                    gameOver = True
            
        #displaying the game interface and the snake
        Snake(block_size, snakeList)
        gameDisplay.blit(bgdside, (0,0))
        gameDisplay.blit(sign, [display_width/2 - 30,display_height-20])
        score_update((score_value-1)*2)
        health_bars(snake_health)
        pygame.display.update()

        #And this is the code for when the snake 'eats' an apple
        if lead_x > randAppleX and lead_x < randAppleX + AppleThickness or lead_x + block_size > randAppleX and lead_x + block_size < randAppleX + AppleThickness:
            if lead_y > randAppleY and lead_y < randAppleY + AppleThickness:  
                randAppleX, randAppleY = randAppleGen()
                score_value += 4
                snakeLength += 4
            elif  lead_y + block_size > randAppleY and lead_y + block_size < randAppleY + AppleThickness:
               randAppleX, randAppleY = randAppleGen()
               snakeLength += 4
               score_value += 4

        # The bonus handling code:
        # bonus_text = medfont.render('Bonus:  +4', True, black)
        if score_value == 17 or score_value == 49 or score_value == 81 or score_value == 113 or score_value == 145:
            # gameDisplay.blit(bonus_text, [display_width/2 - 200, 100])
            bonusAnim.play()
            bonusAnim.blit(gameDisplay, (display_width*0.35, display_height*0.3))
            pygame.display.update()
            if score_value == 21 or score_value == 53 or score_value == 85 or score_value == 117 or score_value == 149:
                score_value = score_value + 4
                snakeLength = snakeLength + 4

        clock.tick(FPS)

    pygame.quit()
    quit()

game_intro()
gameLoop()
