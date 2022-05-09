"""Class used for window display."""
import pygame
from button_controls import Button

class GameView():
    """
    GameView class for displayign visuals.

    """

    def __init__(self):
        """
        Constructs all the necessary attributes for the GameView class.

        Attributes:
            panel: An int representing the size of the panel.
            width: An int representing the width of the game window.
            height: An int representing the height of the game window.
            surface: Produces the window that displays the game.
        """
        self.panel_ = 618/2
        self.width = 1103
        self.height = 618 + self.panel_
        self.surface = pygame.display.set_mode([self.width, self.height])

    def background(self, image):
        """
        Generate the background of the display.

        Args:
            image: A .png file that is used as a background.
        """
        self.surface.blit(image,(0,0))

    def panel(self, image):
        """

        """
        self.surface.blit(image, (0,self.height - self.panel_))

    def display_character(self, image, x_coor, y_coor):
        """
        Generate the characters in the display.

        Args:
            image: A .png file that depicts a character.
            x_coor: An int representing the image's x coordinate on the
            display.
            y_coor: An int representing the image's y coordinate on the
            display.
        """
        start_img = pygame.image.load(image).convert_alpha()
        img = pygame.transform.scale(start_img, \
            (start_img.get_width() * 6, start_img.get_height() * 6))
        rect = img.get_rect()
        rect.center = (x_coor, y_coor)
        self.surface.blit(img, (rect.x, rect.y))

    def empty_screen(self, ch1, ch2):
        """
        Display an empty string.
        """
        game = GameView()
        background_img = pygame.image.load("img/background.png").convert_alpha()
        panel_img = pygame.image.load("img/panel.png").convert_alpha()
        attack_img = pygame.image.load("img/attack_button.png").convert_alpha()
        block_img = pygame.image.load("img/block_button.png").convert_alpha()
        heal_img = pygame.image.load("img/heal_button.png").convert_alpha()

        game.background(background_img)
        game.panel(panel_img)
        game.health_bar(ch1, 150, 650)
        game.health_bar(ch2, 850, 650)

        attack_button_start = game.draw_button("img/attack_button.png", 150, 675, 111, 27)
        block_button_start = game.draw_button("img/block_button.png", 150, 710, 111, 27)
        heal_button_start = game.draw_button("img/heal_button.png", 150, 745, 111, 27)
        restart_button_start = game.draw_button("img/restart_button.png", 850, 0, 303, 303)

        attack_button = Button(self.surface, attack_button_start)
        block_button = Button(self.surface, block_button_start)
        heal_button = Button(self.surface, heal_button_start)
        restart_button = Button(self.surface, restart_button_start)

    def end_screen(self):
        """
        Display the end screen.
        """
        game = GameView()
        background_img = pygame.image.load("img/background.png").convert_alpha()
        panel_img = pygame.image.load("img/panel.png").convert_alpha()

        game.background(background_img)
        game.panel(panel_img)

    def health_bar(self, character, x_coor, y_coor):
        """
        Display an image that represents the current health level of a fighter.

        Args:
            character: An instance of the Fighter class that represents a
            fighter.
            x_coor: An int representing the x coordinate of the image on the
            display.
            y_coor: An int representing the y coordinate of the image on the
            display.
        """
        current_hp = character.current_hp
        max_hp = character.max_hp
        ratio = current_hp / max_hp
        pygame.draw.rect(self.surface, (255, 0, 0), (x_coor, y_coor, 175, 20))
        pygame.draw.rect(self.surface, (0, 128, 0), (x_coor, y_coor, 175 * \
        ratio, 20))

    def draw_button(self, image, x_coor, y_coor, x_size, y_size):
        """
        Display an image representing a button that the player can press. The
        function will also resize an image.

        Args:
            image: A .png file that represents a button.
            x_coor: An int representing the x coordinate of the image on the
            display.
            y_coor: An int representing the y coordinate of the image on the
            display.
            x_size: An int representing the size an image transforms in the x
            direction.
            y_size: An int representing the size an image transforms in the y
            direction.
        """
        start_img = pygame.image.load(image).convert_alpha()
        img = pygame.transform.scale(start_img, (x_size, y_size))
        rect = img.get_rect()
        rect.topleft = (x_coor, y_coor)
        self.surface.blit(img, (rect.x, rect.y))
        return rect
