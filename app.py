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
        pygame.display.set_caption(settings.game_caption)

        self.screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
        self.snake = Snake(self.screen)
        self.snake.draw()
        self.food = Food(self.screen)
        self.food.draw()

    def game_reset(self):
        self.screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
        self.snake = Snake(self.screen)
        self.food = Food(self.screen)


    def is_collision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2 + settings.default_size:
            if y1 >= y2 and y1 < y2 + settings.default_size:
                return True
        return False

    def play(self):
        self.snake.walk()
        self.food.draw()
        pygame.display.flip()

        # snake eating food scenario
        for i in range(self.snake.length):
            if self.is_collision(self.snake.x[i], self.snake.y[i], self.food.x, self.food.y):
                self.snake.increase_length()
                self.food.move()
                print('bigger snake')

        # snake colliding with itself
        for i in range(3, self.snake.length):
            if self.is_collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                raise "Collision Occurred"

        # snake colliding with the boundries of the window
        if not (0 <= self.snake.x[0] <= settings.screen_width and 0 <= self.snake.y[0] <= settings.screen_height):
            raise "Hit the boundry error"

    def game_over(self):
        font = pygame.font.SysFont('arial', 30)
        line1 = font.render(settings.game_over_message_1, True, colors.red)
        self.screen.blit(line1, (settings.screen_width/2, settings.screen_height/2))
        pygame.display.flip()

    def game_run(self):
        game_running = True
        game_pause = False

        while game_running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        game_running = False

                    if event.key == K_RETURN:
                        game_pause = False

                    if not game_pause:
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
                if not game_pause:
                    self.play()

            except Exception as e:
                self.game_over()
                game_pause = True
                self.game_reset()

            time.sleep(.1)

App().game_run()