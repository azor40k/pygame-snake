import pygame
import config.settings as settings

from pygame.locals import *
from models.game import Game

pygame.init()
screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
pygame.display.set_caption(settings.GAME_CAPTION)

Game(screen).game_run()