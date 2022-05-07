"""This code is for the fighters in the game"""

import random

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
    
    def __init__(self, name, max_hp, strength, block_):
        """

        """
        self.name = name
        self.max_hp = max_hp
        self.current_hp = max_hp
        self.strength = strength
        self.block_ = block_
        self.block_status = False
        self.potion_count = 0
        self.death = False
        #img = pygame.image.load('img/sprite.png').convert_alpha()
        #self.image = pygame.transform.scale(img, (img.get_width() * 3, img.get_height() * 3))
        #self.rectangle = self.image.get_rect()
        #self.rectangle_center = (x, y)

    def attack(self, target):
        """
        Determine the amount of damage done to an opponent.
        
        Args:
            target: The instance of the Fighter class of the enemy target.
        """
        added_damage = random.randint(-3,3)
        if target.block_status == True:
            added_block = random.randint(-3, 0)
            total_damage = self.strength + added_damage + target.block_\
            + added_block
        else:    
            total_damage = self.strength + added_damage
        target.current_hp -= total_damage
        if target.current_hp < 1:
            target.dead = True
            
    def block(self):
        """
        Determine the amount of damage done to fighter when attacked by an
        opponent.
        """
        self.block_status = True
        if self.current_hp < 1:
            self.death = True
        return self.block_status

    def heal(self, potion):
        """
        Add health to player's current health.

        Args:
            potion: An int representing the amount of health rewarded back to
            the character.
        """
        if self.potion_count < 3:
            if self.current_hp < 1:
                self.death = True
            else:
                potion = 8
                damage_taken = self.max_hp - self.current_hp
                if damage_taken < potion:
                    potion = damage_taken
                self.current_hp += potion
                self.potion_count += 1
        else:
            print("Out of potions")

    def reset(self):
        """
        Reset Character stats at the end of a game.
        """
        self.death = False
        self.current_hp = self.max_hp
        self.potion_count = 0
