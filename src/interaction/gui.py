import pygame
import sys
from pygame.locals import QUIT
from time import sleep


class Gui ():

    """The Gui class contains all code regarding the Graphical User Interface.

    Attributes:
        width           (Int)       The width of the screen.
        height          (Int)       The height of the screen.
        window_caption  (String)    The caption of the GUI window.
        dot_radius      (Int)       The radius of the dots.
        dot_border      (Int)       The thickness of the dot's border.
        dot_locations   (dict)      A dictionary of where each dot will be drawn.
    """
    WHITE = (255, 255, 255)
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
        """Initialises the GUI object."""

        # Initates Screen
        pygame.init()
        screen_info = (pygame.display.Info())
        pygame.display.set_caption(self.window_caption)

        # Fetches screen width and height dimensions
        self.width = screen_info.current_w
        self.height = screen_info.current_h
        self.DISPLAY = pygame.display.set_mode((self.width, self.height))
        self.DISPLAY.fill(self.WHITE)

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

    def show_welcome_screen(self):
        self.DISPLAY.fill(self.WHITE)

        font_size = int(self.height/4)
        scale_text = pygame.font.Font('freesansbold.ttf', font_size)
        text = "{}".format("Welcome!")
        text_surface = scale_text.render(text, True, (0, 0, 0))
        text_surface, text_rect = text_surface, text_surface.get_rect()
        text_x = self.width/2
        text_y = self.height/2
        text_rect.center = (text_x, text_y)
        self.DISPLAY.blit(text_surface, text_rect)

        sleep(0.1)
        self.update()
        sleep(0.1)

    def update(self):
        """Updates the screen."""
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

    def draw_dot_hash(self, dot_hash, letter):
        """Draws the 6 dots to the screen.

        Parameters:
            dot_hash    (String) The dot hash of what has been entered by user i.e. 100000 represents Dot 1.
            letter      (String) The letter which represents the dot.
        """

        self.DISPLAY.fill(self.WHITE)

        # Drawing the dots to the screen
        for index, dot in enumerate(dot_hash, start=1):
            try:

                BLACK = (0, 0, 0)
                YELLOW = (247, 211, 92)
                GREEN = (76, 167, 78)
                RED = (200, 50, 32)
                WHITE = (191, 64, 191) # RGB code is for purple,
                BLUE = (56, 139, 224)

                dot_colour_scheme = {
                    1: BLUE,
                    2: RED,
                    3: WHITE,
                    4: GREEN,
                    5: BLACK,
                    6: YELLOW,
                }

                if dot == "0":
                    pygame.draw.circle(
                        self.DISPLAY, dot_colour_scheme[index], (self.dot_locations[index]["x"], self.dot_locations[index]["y"]), self.dot_radius, self.dot_border)
                elif dot == "1":
                    pygame.draw.circle(
                        self.DISPLAY, dot_colour_scheme[index], (self.dot_locations[index]["x"], self.dot_locations[index]["y"]), self.dot_radius, self.dot_radius)

            except KeyError:
                print("Key Error")

        # Drawing the letter to the screen.
        font_size = int(self.height/2)
        scale_text = pygame.font.Font('freesansbold.ttf', font_size)
        current_temp = letter.upper()
        text = "{}".format(current_temp).lower()
        text_surface = scale_text.render(text, True, (0, 0, 0))
        text_surface, text_rect = text_surface, text_surface.get_rect()
        text_x = self.width/4*3
        text_y = self.height/2
        text_rect.center = (text_x, text_y)
        self.DISPLAY.blit(text_surface, text_rect)

        self.update()
