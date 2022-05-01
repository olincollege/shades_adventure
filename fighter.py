"""This code is for the fighters in the game"""

<<<<<<< HEAD
import pygame
=======
>>>>>>> 615bdaeda6d56aa94ab11323e5a8b86d8fb7e0aa
import random
import pygame

class Fighter:
    """
    """
    
    def __init__(self, name, max_hp, strength, block_, x, y):
        """
        """
        self.name = name
        self.max_hp = max_hp
        self.current_hp = max_hp
        self.strength = strength
        self.block_ = block_
        self.dead = False
        self.image = pygame.image.load("img/sprite.png").convert_alpha()
        self.rectangle = self.image.get_rect()
        self.rectangle_center = (x, y)

    def draw(self):
        """
        """
        pass

    def animate(self):
        """
        """
        pass

    def attack(self, target):
        """
        """
        added_damage = random.randint(-3,3)
        total_damage = self.strength + added_damage
        target.current_hp -= total_damage
        if target.current_hp < 1:
            target.dead = True
            #Death animation
        #Add attack animation after this

    def block(self, target):
        """
        """
        added_block = random.randint(-3, 0)
        total_damage = self.strength + self.block_ + added_block
        self.current_hp -= total_damage
        if self.current_hp < 1:
            self.dead = True
            #Death animation
        #Add block animation after this

    def idle_animation(self):
        """
        """
        pass

    def hurt_animation(self):
        """
        """
        pass

    def death_animation(self):
        """
        """
        pass

    def reset(self):
        """
        """
        self.death = False
        self.current_hp = self.max_hp
        #Add animation stuff
    