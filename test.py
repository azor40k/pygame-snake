from django.conf import Settings
import pygame
import config.settings as settings
import assets.colors as colors

from pygame.locals import *


# Init game
pygame.init()
pygame.display.set_caption(settings.game_caption)

screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
game_close = False
game_time = pygame.time.Clock()

x1 = settings.screen_width/2
y1 = settings.screen_height/2
 
snake_block=10
snake_speed=30
 
x1_change = 0       
y1_change = 0

font_style = pygame.font.SysFont(None, 50)

def message(msg,color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [settings.screen_width/2, settings.screen_height/2])

while not game_close:
    for event in pygame.event.get():
        print(event)   # prints out all events
        if event.type == pygame.QUIT: game_over = True

        if event.type == pygame.KEYDOWN:
            print("KEYDOWN")
            if event.key == pygame.K_LEFT:
                x1_change = -snake_block
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = snake_block
                y1_change = 0
            elif event.key == pygame.K_UP:
                y1_change = -snake_block
                x1_change = 0
            elif event.key == pygame.K_DOWN:
                y1_change = snake_block
                x1_change = 0
 
    if x1 >= settings.screen_width or x1 < 0 or y1 >= settings.screen_height or y1 < 0:
        game_over = True
 
    x1 += x1_change
    y1 += y1_change

    screen.fill(colors.white)
    pygame.draw.rect(screen, colors.green, [200,150,10,10])
    pygame.display.update()
    game_time.tick(30)

# Close Screen
pygame.quit()
quit()