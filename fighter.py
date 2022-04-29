"""This code is for the player controlled character: Shades"""

import pygame

class Fighter():
    """
    """
    
    def __init__(self, x, y, name, max_hp, strength):
        """
        """
        self.name = name
        self.max_hp = max_hp
        self.current_hp = max_hp
        self.strength = strength
        self.dead = False
        #self.sprite = pygame.image.load()
        #self.rectangle = self.sprite.get_rect()
        #self.rectangle.cent = (x, y)

    def draw(self):
        """
        """
        pass
    def animate(self):
        """
        """
        pass
    def idle(self):
        """
        """
        pass
    def attack(self):
        """
        """
        pass
    def block(self):
        """
        """
        pass
    def hurt(self):
        """
        """
        pass
    def death(self):
        """
        """
    def reset(self):
        """
        """
        pass
    