import pytest
from fighter import Fighter

fighter_test = Fighter("test", 100, 15, -10)
enemy_test = Fighter("test", 100, 15, -10)

def test_attack():
    fighter_test.attack(enemy_test)
    assert 82 <= enemy_test.current_hp <= 88

def test_attack_death():
    enemy_test.death = False
    enemy_test.current_hp = 10
    fighter_test.attack(enemy_test)
    assert enemy_test.death == True

def test_attack_block():
    enemy_test.current_hp = 70
    enemy_test.block_status = True
    fighter_test.attack(enemy_test)
    assert 62 <= enemy_test.current_hp <= 70

def test_block_true():
    assert fighter_test.block(True) == True

def test_block_false():
    assert fighter_test.block(False) == False

def test_block_death():
    fighter_test.death = False
    fighter_test.current_hp = 0
    fighter_test.block(True)
    assert fighter_test.death == True

def test_reverse_block():
    enemy_test.block(True)
    fighter_test.reverse_block(enemy_test)
    assert enemy_test.block_status == False

def test_heal():
    fighter_test.current_hp = 80
    fighter_test.heal()
    assert fighter_test.current_hp == 88

def test_heal_under_limit():
    fighter_test.potion_count = 3
    fighter_test.current_hp = 80
    fighter_test.heal()
    assert fighter_test.current_hp == 88

def test_heal_over_limit():
    fighter_test.potion_count = 4
    assert fighter_test.heal() == None

def test_heal_death():
    enemy_test.death = False
    enemy_test.current_hp = 0
    enemy_test.heal()
    assert enemy_test.death == True
