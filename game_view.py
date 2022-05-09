""""""
import pygame
from button_controls import Button

class GameView():
    """
    GameView class for displayign visuals.

    Attributes:
    """

    def __init__(self):
        """

        """
        self.panel_ = 618/2
        self.width = 1103
        self.height = 618 + self.panel_
        self.surface = pygame.display.set_mode([self.width, self.height])

    def background(self, image):
        """

        """
        self.surface.blit(image,(0,0))

    def panel(self, image):
        """

        """
        self.surface.blit(image, (0,self.height - self.panel_))

    def display_character(self, image, x_coor, y_coor):
        """

        """
        start_img = pygame.image.load(image).convert_alpha()
        img = pygame.transform.scale(start_img, \
            (start_img.get_width() * 6, start_img.get_height() * 6))
        rect = img.get_rect()
        rect.center = (x_coor, y_coor)
        self.surface.blit(img, (rect.x, rect.y))

    def empty_screen(self, ch1, ch2):
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
        game = GameView()
        background_img = pygame.image.load("img/background.png").convert_alpha()
        panel_img = pygame.image.load("img/panel.png").convert_alpha()

        game.background(background_img)
        game.panel(panel_img)

        restart_button_start = game.draw_button("img/restart_button.png", 500, 600, 303, 303)
        restart_button = Button(self.surface, restart_button_start)

    def health_bar(self, character, x_coor, y_coor):
        """

        """
        current_hp = character.current_hp
        max_hp = character.max_hp
        ratio = current_hp / max_hp
        pygame.draw.rect(self.surface, (255, 0, 0), (x_coor, y_coor, 175, 20))
        pygame.draw.rect(self.surface, (0, 128, 0), (x_coor, y_coor, 175 * ratio, 20))

    def draw_button(self, image, x_coor, y_coor, x_size, y_size):
        """

        """
        start_img = pygame.image.load(image).convert_alpha()
        img = pygame.transform.scale(start_img, (x_size, y_size))
        rect = img.get_rect()
        rect.topleft = (x_coor, y_coor)
        self.surface.blit(img, (rect.x, rect.y))
        return rect
        