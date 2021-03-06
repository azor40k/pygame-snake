import pygame
import time
import assets.colors as colors
import config.settings as settings

from pygame.locals import *
from models.food import Food 
from models.snake import Snake 

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.snake = Snake(self.screen)
        self.snake.display()
        self.food = Food(self.screen)
        self.food.display()

    def game_reset(self):
        self.screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
        self.snake = Snake(self.screen)
        self.food = Food(self.screen)

    def game_collision(self, x1, y1, x2, y2):
        if x1 == x2 and y1 == y2:
            return True
        return False

    def game_score(self):
        font = pygame.font.SysFont('arial', 20)
        message = font.render(f"Score: {self.snake.length}", True, colors.WHITE)
        text_position = message.get_rect(center=(settings.SCREEN_WIDTH/2, settings.SCREEN_HEIGHT*.05))
        self.screen.blit(message, text_position)
        pygame.display.flip()

    def game_play(self):
        self.snake.move()
        self.food.display()
        self.game_score()
        pygame.display.flip()

        # eat food
        for i in range(self.snake.length):
            if self.game_collision(self.snake.x[i], self.snake.y[i], self.food.x, self.food.y):
                self.snake.increase_snake()
                self.food.change_position()
                print(f'bigger snake: {self.snake.length}')

        # self collision
        for i in range(3, self.snake.length):
            if self.game_collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                raise "Collision Death"

        # border collision
        if not (0 <= self.snake.x[0] <= settings.SCREEN_WIDTH and 0 <= self.snake.y[0] <= settings.SCREEN_HEIGHT):
            raise "Border Death"

    def game_over(self):
        print(settings.GAME_OVER_MESSAGE)
        font = pygame.font.SysFont('arial', 50)
        message = font.render(settings.GAME_OVER_MESSAGE, True, colors.RED)
        text_position = message.get_rect(center=(settings.SCREEN_WIDTH/2, settings.SCREEN_HEIGHT/2))
        self.screen.blit(message, text_position)
        pygame.display.flip()

    def game_run(self):
        print(settings.GAME_START_MESSAGE)
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
                        if (event.key == K_LEFT or event.key == K_q) and self.snake.direction != "right":
                            self.snake.snake_direction("left")

                        if (event.key == K_RIGHT or event.key == K_d) and self.snake.direction != "left":
                            self.snake.snake_direction("right")

                        if (event.key == K_UP or event.key == K_z) and self.snake.direction != "down":
                            self.snake.snake_direction("up")

                        if (event.key == K_DOWN or event.key == K_s) and self.snake.direction != "up":
                            self.snake.snake_direction("down")

                elif event.type == QUIT:
                    game_running = False
            try:
                if not game_done:
                    self.game_play()

            except Exception as e:
                self.game_over()
                game_done = True
                self.game_reset()

            time.sleep(self.snake.speed)