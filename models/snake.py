import pygame
import config.settings as settings
import assets.colors as colors

class Snake:
    def __init__(self, parent_screen):
        self.parent_screen  = parent_screen
        self.direction      = 'down'
        self.body           = pygame.Surface((40, 40), pygame.SRCALPHA)
        pygame.draw.circle(self.body , colors.green, [20, 20], 40)
        self.length = 1
        self.x = [40]
        self.y = [40]

    def snake_direction(self, direction):
        self.direction = direction

    def walk(self):
        # update body size
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
        for i in range(self.length):
            self.parent_screen.blit(self.body, (self.x[i], self.y[i]))
        pygame.display.flip()

    def increase_length(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)