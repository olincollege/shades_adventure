"""This code is for the fighters in the game"""

import random
import pygame

class Fighter():
    """
    Fighter class for both player controlled character and NPC's.
    
    Attributes:
        name: A string representing the name of the fighter.
        max_hp: An int representing the maximum health a fighter can have.
        strength: An int representing the strength of a fighter.
        block_: An int representing a fighter's ability to block.
        x: An int representing an x-coordinate.
        y: An int representing a y-coordinate.
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
        Determine the amount of damage done to an opponent.
        
        Args:
            target: The instance of the Fighter class of the enemy target.
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
        Determine the amount of damage done to fighter when attacked by an
        opponent.
        """
        added_block = random.randint(-3, 0)
        total_damage = self.strength + self.block_ + added_block
        self.current_hp -= total_damage
        if self.current_hp < 1:
            self.dead = True
            #Death animation
        #Add block animation after this

    def heal(self, potion):
        """
        Add health to player's current health.

        Args:
            potion: An int representing the amount of health rewarded back to
            the character.
        """
        damage_taken = self.max_hp - self.current_hp
        if damage_taken < potion:
            potion = damage_taken
        self.current_hp += potion

    def reset(self):
        """
        Reset Character stats at the end of a game.
        """
        self.death = False
        self.current_hp = self.max_hp
        #Add animation stuff
