import pygame

class Tools:
    def display_text(self, text_size, text_message, text_color, text_x, text_y):
        font = pygame.font.SysFont('arial', 20)
        message = font.render(f"Score: {self.snake.length-1}", True, colors.WHITE)
        text_position = message.get_rect(center=(settings.SCREEN_WIDTH/2, settings.SCREEN_HEIGHT*.05))
        self.screen.blit(message, text_position)
        pygame.display.flip()

