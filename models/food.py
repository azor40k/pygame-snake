import pygame
import random
import assets.colors as colors
from config.settings import DEFAULT_SIZE
from config.tools import Tools

class Food :
    def __init__(self, parent_screen):
        self.parent_screen      = parent_screen
        self.x                  = random.randint(1, 30)*DEFAULT_SIZE
        # self.x                  = Tools.position(1, 24)
        self.y                  = random.randint(1, 19)*DEFAULT_SIZE
        self.body               = pygame.Surface((40, 40), pygame.SRCALPHA)
        pygame.draw.circle(self.body , colors.red, [20, 20], 40)

    def display(self):
        self.parent_screen.blit(self.body, (self.x, self.y))
        pygame.display.flip()

    def change_position(self):
        self.x = random.randint(1, 30)*DEFAULT_SIZE
        self.y = random.randint(1, 19)*DEFAULT_SIZE