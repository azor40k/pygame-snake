import pygame
import random
import config.settings as settings
import assets.colors as colors

class Food :
    def __init__(self, parent_screen):
        self.parent_screen      = parent_screen
        self.x = self.y         = 120
        self.body             = pygame.Surface((40, 40), pygame.SRCALPHA)
        pygame.draw.circle(self.body , colors.red, [20, 20], 40)

    def draw(self):
        self.parent_screen.blit(self.body, (self.x, self.y))
        pygame.display.flip()

    def move(self):
        self.x = random.randint(1,24)*settings.default_size
        self.y = random.randint(1,19)*settings.default_size