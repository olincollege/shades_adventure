"""Class used to track mouse on window."""
import pygame

class Button():
    """
    Button class for tracking where the mouse is as well as where it clicks on
    the display.
    """

    def __init__(self, surface, rect):
        """
        Constructs all the necessary attributes for the Button class.

        Attributes:
            surface: The game window.
            rect: An instance of GameView that uses the draw_button method to
            get the dimensions of a button.
            clicked: A boolean that determines if the button is clicked.
        """
        self.surface = surface
        self.rect = rect
        self.clicked = False

    def get_button(self):
        """
        Determine the mouse position and if it has clicked within the boundary
        of a given rectangle.
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
        