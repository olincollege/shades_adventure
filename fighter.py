"""This code is for the fighters in the game"""

import random

class Fighter():
    """
    Fighter class for both player controlled character and NPC.

    Attributes:
        name: A string representing the name of a fighter.
        max_hp: An int representing the maximum amount of health a fighter
        can have.
        strength: An int representing the amount of damage a fighter can do
        to an opponent.
        block_: An int representing the amount of damage a fighter can
        deflect from an opponent.
    """

    def __init__(self, name, max_hp, strength, block_):
        """
        Constructs all the necessary attributes for the Fighter class.

        Attributes:
            name: A string representing the name of a fighter.
            max_hp: An int representing the maximum amount of health a fighter
            can have.
            current_hp: An int representing the current amount of health a
            fighter has.
            strength: An int representing the amount of damage a fighter can do
            to an opponent.
            block_: An int representing the amount of damage a fighter can
            deflect from an opponent.
            potion_count: An int representing the number of times a fighter has
            healed.
            death: A boolean that determines if a player is alive or not.
        """
        self.name = name
        self.max_hp = max_hp
        self.current_hp = max_hp
        self.strength = strength
        self.block_ = block_
        self.block_status = False
        self.potion_count = 0
        self.death = False

    def attack(self, target):
        """
        Determine the amount of damage done to an opponent.

        Args:
            target: The instance of the Fighter class of the enemy target.
        """
        added_damage = random.randint(-3,3)
        if target.block_status:
            added_block = random.randint(-3, 0)
            total_damage = self.strength + added_damage + target.block_\
            + added_block
            if total_damage < 0:
                total_damage = 0
        else:
            total_damage = self.strength + added_damage
        target.current_hp -= total_damage
        if target.current_hp < 1:
            target.death = True

    def block(self, status):
        """
        Determine if fighter is blocking.

        Args:
            status: A boolean saying whether or not the fighter is blocking.
        """
        self.block_status = status
        if self.current_hp < 1:
            self.death = True
        return self.block_status

    def reverse_block(self, target):
        """
        Update opponent's block_status to False.

        Args:
            target: An instance of the Fighter class representing the opponent.
        """
        if target.block_status:
            target.block_status = False

    def heal(self):
        """
        Increase the value of current_hp by 8. This method only adds to
        current_hp the first three times it is run.
        """
        if self.potion_count <= 3:
            if self.current_hp < 1:
                self.death = True
            else:
                potion = 8
                damage_taken = self.max_hp - self.current_hp
                if damage_taken < potion:
                    potion = damage_taken
                self.current_hp += potion
                self.potion_count += 1

    def reset(self):
        """
        Reset fighter instance at the end of a game.
        """
        self.death = False
        self.current_hp = self.max_hp
        self.potion_count = 0
