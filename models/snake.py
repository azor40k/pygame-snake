import pygame
import random
import config.settings as settings
import assets.colors as colors

class Snake:
    def __init__(self, screen):
        self.screen_parent  = screen
        self.direction      = 'down'
        self.body           = pygame.Surface((40, 40), pygame.SRCALPHA)
        pygame.draw.circle(self.body , colors.GREEN, [20, 20], 40)
        self.length = 1
        self.x = [random.randint(1, 24)*settings.DEFAULT_SIZE]
        self.y = [random.randint(1, 19)*settings.DEFAULT_SIZE]

    def snake_direction(self, direction):
        self.direction = direction

    def move(self):
        # update body tail
        for i in range(self.length-1,0,-1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]

        # update body direction
        if self.direction == 'left':
            self.x[0] -= settings.DEFAULT_SIZE
        if self.direction == 'right':
            self.x[0] += settings.DEFAULT_SIZE
        if self.direction == 'up':
            self.y[0] -= settings.DEFAULT_SIZE
        if self.direction == 'down':
            self.y[0] += settings.DEFAULT_SIZE

        self.display()

    def display(self):
        self.screen_parent.fill(colors.BLACK)
        for i in range(self.length):
            self.screen_parent.blit(self.body, (self.x[i], self.y[i]))

        pygame.display.flip()

    def increase_length(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)