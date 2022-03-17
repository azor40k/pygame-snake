import pygame
import time
import assets.colors as colors
import config.settings as settings

from pygame.locals import *
from models.food import Food 
from models.snake import Snake 

class App:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(settings.GAME_CAPTION)

        self.screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
        self.snake = Snake(self.screen)
        self.snake.display()
        self.food = Food(self.screen)
        self.food.display()

    def game_reset(self):
        self.screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
        self.snake = Snake(self.screen)
        self.food = Food(self.screen)


    def is_collision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2 + settings.DEFAULT_SIZE:
            if y1 >= y2 and y1 < y2 + settings.DEFAULT_SIZE:
                return True
        return False

    def play(self):
        self.snake.walk()
        self.food.display()
        pygame.display.flip()

        # snake eating food scenario
        for i in range(self.snake.length):
            if self.is_collision(self.snake.x[i], self.snake.y[i], self.food.x, self.food.y):
                self.snake.increase_length()
                self.food.change_position()
                print(f'bigger snake: {self.snake.length}')

        # snake colliding with itself
        for i in range(3, self.snake.length):
            if self.is_collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                raise "Collision Death"

        # snake colliding with the boundries of the window
        if not (0 <= self.snake.x[0] <= settings.SCREEN_WIDTH and 0 <= self.snake.y[0] <= settings.SCREEN_HEIGHT):
            raise "Boundary Death"

    def game_over(self):
        font = pygame.font.SysFont('arial', 30)
        message = font.render(settings.GAME_OVER_MESSAGE, True, colors.RED)
        self.screen.blit(message, (settings.SCREEN_WIDTH/2, settings.SCREEN_HEIGHT/2))
        pygame.display.flip()

    def game_run(self):
        game_running = True
        game_done = False

        while game_running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        game_running = False

                    if event.key == K_RETURN:
                        game_done = False

                    if not game_done:
                        if event.key == K_LEFT or event.key == K_q:
                            self.snake.snake_direction("left")

                        if event.key == K_RIGHT or event.key == K_d:
                            self.snake.snake_direction("right")

                        if event.key == K_UP or event.key == K_z:
                            self.snake.snake_direction("up")

                        if event.key == K_DOWN or event.key == K_s:
                            self.snake.snake_direction("down")

                elif event.type == QUIT:
                    game_running = False
            try:
                if not game_done:
                    self.play()

            except Exception as e:
                self.game_over()
                game_done = True
                self.game_reset()

            time.sleep(.1)

App().game_run()