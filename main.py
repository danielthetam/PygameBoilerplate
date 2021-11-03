import pygame
import sys
from pygame import math
import os


class Game:
    def __init__(self, WINDOW_SIZE, title, icon_path):
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        pygame.init()
        self.clock = pygame.time.Clock()

        self.WINDOW_SIZE = WINDOW_SIZE
        self.display = pygame.display.set_mode(self.WINDOW_SIZE)
        pygame.display.set_caption(title)

        icon = pygame.image.load(icon_path)
        pygame.display.set_icon(icon)


    def render(self):
        self.display.fill((0, 0, 0))

        pygame.display.update()


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
        self.clock.tick(60)


if __name__ == '__main__':
    game = Game((800, 800), "Game", r"assets/icon.png")
    while True:
        game.run()
