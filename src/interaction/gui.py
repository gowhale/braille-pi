import pygame
from time import sleep
import sys
from pygame.locals import QUIT


class Gui ():

    width = 500
    height = 400
    window_caption = "Braille Pi"
    dot_radius = 50
    dot_border = 10

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
        screen_info = (pygame.display.Info())
        self.width = screen_info.current_w
        self.height = screen_info.current_h
#         print(width,height)

        self.DISPLAY = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.window_caption)
        WHITE = (255, 255, 255)
        self.DISPLAY.fill(WHITE)

        row_two = int(self.height / 2)
        row_one = int(row_two / 2)
        row_three = int(row_two / 2 * 3)

        self.dot_locations[1]["y"] = row_one
        self.dot_locations[2]["y"] = row_one
        self.dot_locations[3]["y"] = row_two
        self.dot_locations[4]["y"] = row_two
        self.dot_locations[5]["y"] = row_three
        self.dot_locations[6]["y"] = row_three

        cell_height = (row_three-row_one)

        col_one = int((self.width / 4) - (cell_height * 0.4))
        col_two = int((self.width / 4) + (cell_height * 0.4))

        self.dot_locations[1]["x"] = col_one
        self.dot_locations[2]["x"] = col_two
        self.dot_locations[3]["x"] = col_one
        self.dot_locations[4]["x"] = col_two
        self.dot_locations[5]["x"] = col_one
        self.dot_locations[6]["x"] = col_two

    def update(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

    def close_gui(self):
        pygame.quit()
        sys.exit()

    def draw_dot_hash(self, dot_hash, letter):
        WHITE = (255, 255, 255)
        self.DISPLAY.fill(WHITE)

        for index, dot in enumerate(dot_hash, start=1):
            # print(index, dot)
            try:
                #                print(self.dot_locations[index])
                BLACK = (0, 0, 0)
                if dot == "0":
                    pygame.draw.circle(
                        self.DISPLAY, BLACK, (self.dot_locations[index]["x"], self.dot_locations[index]["y"]), self.dot_radius, self.dot_border)
                elif dot == "1":
                    pygame.draw.circle(
                        self.DISPLAY, BLACK, (self.dot_locations[index]["x"], self.dot_locations[index]["y"]), self.dot_radius, self.dot_radius)

            except KeyError:
                print("Key Error")

        font_size = int(self.height/2)
        scale_text = pygame.font.Font('freesansbold.ttf', font_size)
        current_temp = letter.upper()
        text = "{}".format(current_temp)
        text_surface = scale_text.render(text, True, (0, 0, 0))
        text_surface, text_rect = text_surface, text_surface.get_rect()
        text_x = self.width/4*3
        text_y = self.height/2
        text_rect.center = (text_x, text_y)
        self.DISPLAY.blit(text_surface, text_rect)

        self.update()

# test = Gui()
# test.close_gui()
