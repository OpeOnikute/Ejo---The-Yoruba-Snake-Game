# -*- coding: cp1252 -*-
import pygame
import pyganim
import os
# import time
import random
# import health

pygame.init()

images_path = os.getcwd() + "\images\\"

# Setting the display width and height
display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Ejo')


# colours
white = (255, 255, 255)
black = (0, 0, 0)
grey = (220, 220, 220)
red = (200, 0, 0)
light_red = (255, 20, 20)
green = (0, 140, 0)
light_green = (0, 240, 0)
yellow = (255, 255, 128)
light_yellow = (255, 255, 228)

# loading the animations
game_overAnim = pyganim.PygAnimation([(images_path + 'game_over2.png', 150), (images_path + 'game_over3.png', 100)])
bonusAnim = pyganim.PygAnimation([(images_path+'bonus_text1.png', 150), (images_path+'bonus_text2.png', 100)])

# loading the images
icon = pygame.image.load(images_path + 'snake_head.png')
img = pygame.image.load(images_path+'snake.png')
eba = pygame.image.load(images_path+'eba2.png')
bgd = pygame.image.load(images_path+'bgd.png')
snakeBody = pygame.image.load(images_path+'body.png')
welcome_screen = pygame.image.load(images_path+'welcome.png')
game_over_face = pygame.image.load(images_path+'face005.png')
skin = pygame.image.load(images_path+'skin.png')
bgdside = pygame.image.load(images_path+'bgd_side.png')

# setting the game icon to the snake head
pygame.display.set_icon(icon)

# initializing the timing functionality and some standard variables
clock = pygame.time.Clock()
AppleThickness = 30
block_size = 20
FPS = 30
direction = 'right'

# Loading the fonts to be used
extra_small_font = pygame.font.SysFont(r'comicsans', 15)
small_font = pygame.font.SysFont(r'comicsans', 20)
# small2font = pygame.font.Font(r'C:\Users\Ope O\Downloads\Fonts\eyelevation6.ttf', 40)
small2font = pygame.font.SysFont(r'comicsans', 40)
med_font = pygame.font.SysFont(r'comicsans', 50)
# med_fontButton = pygame.font.Font(r'C:\Users\Ope O\Downloads\Fonts\eyelevation6.ttf', 50)
med_fontButton = pygame.font.SysFont(r'comicsans', 50)
# med_fontButton2 = pygame.font.Font(r'C:\Users\Ope O\Downloads\Fonts\eyelevation6.ttf', 80)
med_fontButton2 = pygame.font.SysFont(r'comicsans', 80)
large_font = pygame.font.SysFont(r'comicsans', 80)
# rendering the font for the copyright display at the bottom.
sign = extra_small_font.render('©2017.', True, white)


def message_to_screen(msg, color, y_displace=0, x_displace=0, size="small", font=None, font_size=None):
    """
    :param msg:
    :param color:
    :param y_displace:
    :param x_displace:
    :param size:
    :param font:
    :param font_size:
    :return:
    """
    text_surf, text_rect = text_objects(msg, color, size, font, font_size)
    text_rect.center = (display_width / 2)+x_displace, (display_height /2)+y_displace
    # flashSurf = pygame.Surface((text_surf.get_width(), text_surf.get_height()))
    # flashSurf = flashSurf.convert_alpha()

    gameDisplay.blit(text_surf, text_rect)
    # origSurf = text_surf.copy()


def pause():

    paused = True
    message_to_screen('Paused', black, -100, size='large')
    message_to_screen('Press C to continue or Q to quit.', black, 25)

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
    text = small_font.render('Score: ' + str(score), True, white)
    gameDisplay.blit(text, [display_width - 765,20])


def game_controls():
    """
    :return:
    """

    gcont = True

    while gcont:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                    
        gameDisplay.fill(white)
        # message_to_screen(msg,
        #                   color,
        #                 y_displace=0,
        #                   x_displace=0,
        #                   size = "small", font = None, fontSize = None)
        message_to_screen('CONTROLS', green, y_displace=-150, x_displace=0, size='large')
        message_to_screen('Move Snake: Up, Down, Left and Right arrows', black, y_displace=10, x_displace=0, size='small')
        message_to_screen('Pause: P ', black, y_displace=50, x_displace=0, size='small')

        text_to_button('Play', yellow, light_yellow, 250,455,80,40, size='small', action='play')
            
        # text_to_button('Quit', black, white, 612.5,457,80,40 ,  size = 'small', action = 'quit')
        
        text_to_button('Quit', red, light_red, 450, 455, 80, 40,  size='small', action='quit')
        pygame.display.update()


def randAppleGen():
    """
    :return:
    """
    rand_apple_x = round(random.randrange(40, display_width - AppleThickness - 40))
    rand_apple_y = round(random.randrange(30, display_height - AppleThickness - 30))

    return rand_apple_x, rand_apple_y


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

    text_surf, text_rect = text_objects_button(msg, color, size)
    text_size = text_surf.get_width()

    # text_rect.center = ((buttonx+(buttonwidth/2)), buttony+(buttonheight/2))
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    gameDisplay.blit(text_surf, (buttonx, buttony))

    if buttonx + text_size > cur[0] > buttonx and buttony + text_surf.get_height() > cur[1] > buttony:
        text_surf2, text_rect2 = text_objects_button(msg, inactive_color, size)
        gameDisplay.blit(text_surf2, (buttonx - 2, buttony - 2))

        if click[0] == 1 and action is not None:
            if action == 'quit':
                pygame.quit()
                quit()
            if action == 'controls':
                game_controls()
            if action == 'play':
                game_loop()
            if action == 'main':
                game_intro()
        # pygame.display.update()


def game_intro():

    intro = True

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

        gameDisplay.blit(welcome_screen, (0, 0))
        gameDisplay.blit(sign, [display_width/2 - 50,display_height-20])

        text_to_button('Play', yellow, light_yellow, 298, 440, 80, 40, size='medium2', action='play')

        text_to_button('Controls', black, light_green, 102,467,100,40,  size = 'small', action = 'controls')
        text_to_button('Controls', green, light_green, 100,465,100,40,  size = 'small', action = 'controls')
        
        text_to_button('Quit', red, white, 520,465,80,40 ,  size = 'small', action = 'quit')
        text_to_button('Quit', black, light_red, 522,467,80,40 ,  size = 'small', action = 'quit')
        text_to_button('Quit', red, light_red, 521,465,80,40 ,  size = 'small', action = 'quit')
        
        pygame.display.update()
        clock.tick(FPS)

# def button(text, x, y, width, height, inactive_color, active_color, action = None):
#    cur = pygame.mouse.get_pos()
#    click = pygame.mouse.get_pressed()
#
#    if x + width > cur[0] > x and y + height > cur[1] > y:
#        pygame.draw.rect(gameDisplay, active_color, (x,y,width,height))
#        pygame.draw.line(gameDisplay, black, (x, y),(x+width, y),3)
#        pygame.draw.line(gameDisplay, black, (x+width, y),(x+width, y+height),3)
#        pygame.draw.line(gameDisplay, black, (x+width, y+height),(x, y+height),3)
#        pygame.draw.line(gameDisplay, black, (x, y+height),(x, y),3)
#
#        if click[0] == 1 and action != None:
#            if action == 'quit':
#                pygame.quit()
#                quit()
#            if action == 'controls':
#                game_controls()
#            if action == 'play':
#                game_loop()
#            if action == 'main':
#                game_intro()
#
#    else:
#        pygame.draw.rect(gameDisplay, inactive_color, (x,y,width,height))
#        pygame.draw.line(gameDisplay, black, (x, y),(x+width, y),3)
#        pygame.draw.line(gameDisplay, black, (x+width, y),(x+width, y+height),3)
#        pygame.draw.line(gameDisplay, black, (x+width, y+height),(x, y+height),3)
#        pygame.draw.line(gameDisplay, black, (x, y+height),(x, y),3)
#
#    text_to_button(text, white, x,y,width,height)


def Snake(block_size, snake_list):
    """
    functionality for rotation
    :param block_size:
    :param snake_list:
    :return:
    """

    head = None
    
    if direction == 'right':
        head = pygame.transform.rotate(img, 270)
    if direction == 'left':
        head = pygame.transform.rotate(img, 90)
    if direction == 'up':
        head = img
    if direction == 'down':
        head = pygame.transform.rotate(img, 180)

    gameDisplay.blit(head, (snake_list[-1][0], snake_list[-1][1]))

    for XnY in snake_list[:-1]:
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

    text_surface = None

    if size == 'small':
        text_surface = small_font.render(text, True, color)
    elif size == 'medium':
        text_surface = med_fontButton.render(text, True, color)
    elif size == 'large':
        text_surface = large_font.render(text, True, color)
    elif font is not None:
        font = pygame.font.Font(r'C:\Users\Ope O\Downloads\Fonts' + '\\' + font , fontSize)
        text_surface = font.render(text, True, color)

    return text_surface, text_surface.get_rect()


def text_objects_button(text, color, size=None):
    """
    :param text:
    :param color:
    :param size:
    :return:
    """

    text_surface = None

    if size == 'small':
        text_surface = small2font.render(text, True, color)
    elif size == 'medium':
        text_surface = med_fontButton.render(text, True, color)
    elif size == 'medium2':
        text_surface = med_fontButton2.render(text, True, color)
    elif size == 'large':
        text_surface = large_font.render(text, True, color)

    return text_surface, text_surface.get_rect()


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
    health_text = small_font.render('Health: ', True, white)
    gameDisplay.blit(health_text,[display_width-210, 20])
    pygame.draw.rect(gameDisplay, black , (display_width-131, 25, 92, 22))
    pygame.draw.rect(gameDisplay, white , (display_width-130, 26, 90, 20))
    pygame.draw.rect(gameDisplay, snake_health_color , (display_width-130, 26, snake_health, 20))


def game_loop():
    global direction
    global snake_length
    direction = 'right'
    
    score_value = 1

    game_exit = False
    game_over = False

    lead_x = display_width/2
    lead_y = display_height/2

    lead_x_change = 10
    lead_y_change = 0

    snake_health = 90

    snake_list = []
    snake_length = 1

    rand_apple_x, rand_apple_y = randAppleGen()
    
    # The event handling loop is:
    while not game_exit:
        # if game_over == True:
        #     pygame.display.update()

        while game_over is True:
            game_overAnim.play()
            gameDisplay.blit(bgd, (0, 0))
            gameDisplay.blit(game_over_face, (300, 200))
            Snake(block_size, snake_list)
            gameDisplay.blit(bgdside, (0, 0))
            gameDisplay.blit(sign, [display_width / 2 - 30, display_height - 20])
            health_bars(snake_health)
            # pygame.time.set_timer(Text1, 10)
            # pygame.time.set_timer(Text2, 90)

            game_overAnim.blit(gameDisplay, (263, 352))
            # message_to_screen("Game Over",
            #                   red,
            #                   y_displace=180,
            #                   x_displace = 25,
            #                   size = None,
            #                   font = 'BEARPAW_.ttf',
            #                   fontSize = 90,
            #                    )

            message_to_screen('Score: ' + str((score_value-1)*2),
                              black,
                              y_displace=-220,
                              x_displace=10, 
                              size=None,
                              font='VIDEOPHREAK.ttf',
                              font_size=50)

            text_to_button('Play Again', black, light_yellow, 62, 455, 80, 40, size='small', action='play')
            text_to_button('Play Again', yellow, light_yellow, 60, 455, 80, 40, size='small', action='play')
            
            # text_to_button('Quit', black, white, 612.5,457,80,40 ,  size = 'small', action = 'quit')
            text_to_button('Quit', black, black, 622, 455, 80, 40,  size='small', action='quit')
            text_to_button('Quit', red, light_red, 620, 455, 80, 40,  size='small', action='quit')

            # button('Play Again', 150,400,100,40, black, light_green, action = 'play')
            # button('Controls', 350,400,100,40, black, light_green, action = 'controls')
            # button('Quit', 570,400,80,40 , black, light_green, action = 'quit')
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_exit = True
                    game_over = False

            clock.tick(300)
            
            pygame.display.update()

            # if event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_q:
            #         game_exit = True
            #         game_over = False
            #     if event.key == pygame.K_c:
            #         game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
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
            game_over = True
             
            # Code to write if you want the stuff to stop moving when you relase a key
            # if event.type == pygame.KEYUP:
            #    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            #        lead_x_change = 0

        lead_x += lead_x_change
        lead_y += lead_y_change
        
        # gameDisplay.fill(white)
        gameDisplay.blit(bgd, (0,0))
        
        # pygame.display.update()

        # pygame.draw.rect(gameDisplay, red, [rand_apple_x, rand_apple_y, AppleThickness, AppleThickness])

        gameDisplay.blit(eba, (rand_apple_x, rand_apple_y))
        snake_head = list()
        snake_head.append(lead_x)
        snake_head.append(lead_y)
        snake_list.append(snake_head)

        if len(snake_list) > snake_length:
            del snake_list[0]

        # collision detection for loop:
        for eachSegment in snake_list[:-1]:
            if eachSegment == snake_head:
                snake_health -= 30
                if snake_health <= 0:
                    game_over = True

        # displaying the game interface and the snake
        Snake(block_size, snake_list)
        gameDisplay.blit(bgdside, (0, 0))
        gameDisplay.blit(sign, [display_width / 2 - 30, display_height - 20])
        score_update((score_value-1)*2)
        health_bars(snake_health)
        pygame.display.update()

        # And this is the code for when the snake 'eats' an apple
        if (rand_apple_x < lead_x < rand_apple_x + AppleThickness) or (
                rand_apple_x < lead_x + block_size < rand_apple_x + AppleThickness):
            if rand_apple_y < lead_y < rand_apple_y + AppleThickness:
                rand_apple_x, rand_apple_y = randAppleGen()
                score_value += 4
                snake_length += 4
            elif rand_apple_y < lead_y + block_size < rand_apple_y + AppleThickness:
                rand_apple_x, rand_apple_y = randAppleGen()
                snake_length += 4
                score_value += 4

        # The bonus handling code:
        # bonus_text = med_font.render('Bonus:  +4', True, black)
        if score_value == 17 or score_value == 49 or score_value == 81 or score_value == 113 or score_value == 145:
            # gameDisplay.blit(bonus_text, [display_width/2 - 200, 100])
            bonusAnim.play()
            bonusAnim.blit(gameDisplay, (display_width*0.35, display_height*0.3))
            pygame.display.update()
            if score_value == 21 or score_value == 53 or score_value == 85 or score_value == 117 or score_value == 149:
                score_value += 4
                snake_length += 4

        clock.tick(FPS)

    pygame.quit()
    quit()

game_intro()
game_loop()
