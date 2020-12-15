import pygame
from time import sleep
import sys
from pygame.locals import QUIT


class Gui ():

    width = 500
    height = 400
    window_caption = "Braille Pi"

    dot_locations = {
        1: {
            "x": 100,
            "y": 100
        },
        2: {
            "x": 200,
            "y": 100
        },
        3: {
            "x": 100,
            "y": 200
        },
        4: {
            "x": 200,
            "y": 200
        },
        5: {
            "x": 100,
            "y": 300
        },
        6: {
            "x": 200,
            "y": 300
        }

    }

    def __init__(self):
        pygame.init()

        self.DISPLAY = pygame.display.set_mode(
            (self.width, self.height), 0, 32)
        pygame.display.set_caption(self.window_caption)
        WHITE = (255, 255, 255)
        self.DISPLAY.fill(WHITE)

    def update(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

    def draw_dot_hash(self, dot_hash):
        WHITE = (255, 255, 255)
        self.DISPLAY.fill(WHITE)

        for index, dot in enumerate(dot_hash, start=1):
            print(index, dot)
            try:
                #                print(self.dot_locations[index])
                BLACK = (0, 0, 0)
                if dot == "0":
                    pygame.draw.circle(
                        self.DISPLAY, BLACK, (self.dot_locations[index]["x"], self.dot_locations[index]["y"]), 30, 5)
                elif dot == "1":
                    pygame.draw.circle(
                        self.DISPLAY, BLACK, (self.dot_locations[index]["x"], self.dot_locations[index]["y"]), 30, 30)

            except KeyError:
                print("Key Error")

        self.update()
