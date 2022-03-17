import pygame
import random
import assets.colors as colors
from config.settings import DEFAULT_SIZE

class Food :
    def __init__(self, screen_parent):
        self.screen_parent      = screen_parent
        self.x                  = random.randint(1, 24)*DEFAULT_SIZE
        self.y                  = random.randint(1, 19)*DEFAULT_SIZE
        self.body               = pygame.Surface((40, 40), pygame.SRCALPHA)
        pygame.draw.circle(self.body , colors.RED, [20, 20], 40)

    def display(self):
        self.screen_parent.blit(self.body, (self.x, self.y))
        pygame.display.flip()

    def change_position(self):
        self.x = random.randint(1, 24)*DEFAULT_SIZE
        self.y = random.randint(1, 19)*DEFAULT_SIZE