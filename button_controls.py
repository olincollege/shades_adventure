""""""
import pygame

class Button():
    """
    """

    def __init__(self, surface, rect):
        self.rect = rect
        self.clicked = False
        self.surface = surface

    def get_button(self):
        """
        """
        action = False
        mouse_pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                action = True
                self.clicked = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        return action
        