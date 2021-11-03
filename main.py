import pygame
import sys
from pygame import math


class Game:
    def __init__(self, WINDOW_SIZE, title, icon):
        self.WINDOW_SIZE = WINDOW_SIZE
        self.display = pygame.display.set_mode(self.WINDOW_SIZE)
        pygame.display.set_caption(title)
        pygame.display.set_icon(icon)

    def render(self):
        pass


    def event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                pass

            elif event.type == pygame.KEYUP:
                pass

    def update(self):
        pass

    def run(self):
        self.render()
        self.event_handler()
        self.update()


if __name__ == '__main__':
    game = Game((800, 800), "Game", r"assets/icon.png")
    game.run()
