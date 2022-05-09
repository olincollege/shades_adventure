import pytest
from fighter import Fighter

fighter_test = Fighter("test", 100, 15, -10)
enemy_test = Fighter("test", 100, 15, -10)

def test_attack():
    """
    Test if using attack results in enemy_test.current_hp decreasing
    in value. 
    """
    fighter_test.attack(enemy_test)
    assert 82 <= enemy_test.current_hp <= 88

def test_attack_death():
    """
    Test that attack properly updates enemy_test.death from False to
    True when enemy_test.current_hp reaches 0.
    """
    enemy_test.death = False
    enemy_test.current_hp = 10
    fighter_test.attack(enemy_test)
    assert enemy_test.death == True

def test_attack_block():
    """
    Test that attack reduces enemy_test.current_hp less than usually
    when enemy_test.block_status is True.
    """
    enemy_test.current_hp = 70
    enemy_test.block_status = True
    fighter_test.attack(enemy_test)
    assert 62 <= enemy_test.current_hp <= 70

def test_block_true():
    """
    Test that block returns fighter_test.block_status as True when
    input is True.
    """
    assert fighter_test.block(True) == True

def test_block_false():
    """
    Test that block returns fighter_test.block_status as False when
    input is False.
    """
    assert fighter_test.block(False) == False

def test_block_death():
    """
    Test that block properly updates enemy_test.death from False to
    True when enemy_test.current_hp reaches 0.
    """
    fighter_test.death = False
    fighter_test.current_hp = 0
    fighter_test.block(True)
    assert fighter_test.death == True

def test_reverse_block():
    """
    Test that reverse_block changes enemy_test.block_status back to False when
    it is True.
    """
    enemy_test.block(True)
    fighter_test.reverse_block(enemy_test)
    assert enemy_test.block_status == False

def test_heal():
    """
    Test that heal adds the correct value to fighter_test.current_hp.
    """
    fighter_test.current_hp = 80
    fighter_test.heal()
    assert fighter_test.current_hp == 88

def test_heal_under_limit():
    """
    Test that heal runs while fighter_test.potion_count is less than 3.
    """
    fighter_test.potion_count = 2
    fighter_test.current_hp = 80
    fighter_test.heal()
    assert fighter_test.current_hp == 88

def test_heal_under_limit_3():
    """
    Test that heal runs while fighter_test.potion_count is equal to 3.
    """
    fighter_test.potion_count = 3
    fighter_test.current_hp = 80
    fighter_test.heal()
    assert fighter_test.current_hp == 88

def test_heal_over_limit():
    """
    Test that heal does not run while fighter_test.potion_count is over 3.
    """
    fighter_test.potion_count = 4
    assert fighter_test.heal() == None

def test_heal_death():
    """
    Test that heal properly updates enemy_test.death from False to
    True when enemy_test.current_hp reaches 0.
    """
    enemy_test.death = False
    enemy_test.current_hp = 0
    enemy_test.heal()
    assert enemy_test.death == True
