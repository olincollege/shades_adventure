import pygame
import random
from fighter import Fighter
from button_controls import Button

pygame.init()

panel = 614/2
width = 1097
height = 614 + panel


screen = pygame.display.set_mode([width,height])
pygame.display.set_caption("Shades's Adventure")

game_over = 0
current_fighter = 1

background = pygame.image.load("img/background.png").convert_alpha()
panel_img = pygame.image.load("img/panel.png").convert_alpha()
attack_img = pygame.image.load("img/attack_button.png").convert_alpha()
block_img = pygame.image.load("img/block_button.png").convert_alpha()
heal_img = pygame.image.load("img/heal_button.png").convert_alpha()
target_img = pygame.image.load("img/test_target.png").convert_alpha()
#shades = pygame.image.load("").convert_alpha()
#goon = pygame.image.load("").convert_alpha()

def draw_background():
    screen.blit(background,(0,0))

def draw_panel():
    screen.blit(panel_img, (0,height - panel))

shades = Fighter("Shades", 100, 15, -5, 150, 300)
goon = Fighter("Goon", 75, 10, -3, 825, 300)
attack_button = Button(screen, 150, 675, attack_img, 60, 21)
block_button = Button(screen, 150, 700, block_img, 60, 21)
heal_button = Button(screen, 150, 725, heal_img, 60, 21)
target_one_button = Button(screen, 825, 675, target_img, 60, 21)

run = True

while run:
    draw_background()
    draw_panel()

    screen.blit(shades.image, shades.rectangle_center)
    screen.blit(goon.image, goon.rectangle_center)

    #attack_button.draw()
    #block_button.draw()
    #heal_button.draw()
    #target_one_button.draw()

    #Shades actions
    attack = False
    block = False
    heal = False
    target = None
    pygame.mouse.set_visible(True)

    if attack_button.draw():
        target = goon
        attack = True
    if block_button.draw():
        block = True
    if heal_button.draw():
        heal = True

    if game_over == 0:
        if shades.death == False:
            if current_fighter == 1:
                if attack == True:
                    shades.attack(target)
                    print("You attacked goon!")
                    print("Goon Health: ", goon.current_hp)
                    current_fighter += 1
                if block_button.draw():
                    shades.block()
                    print("Blocked!")
                    current_fighter += 1
                if heal_button.draw():
                    shades.heal()
                    print("Healed!")
                    current_fighter += 1
        else:
            game_over = 1
    
        if goon.death == False:
            if current_fighter == 2:
                if shades.current_hp <= 20:
                    goon.attack(shades)
                    print("Goon attacked you!")
                    print("Shades Health: ", shades.current_hp)
                if goon.current_hp <= 25:
                    rand_low_health = random.randint(0,1)
                    if rand_low_health == 0:
                        #goon.heal()
                        print("Goon Healed")
                    else:
                        goon.block()
                        print("Blocked!")
                else:
                    rand_action = random.randint(0,2)
                    if rand_action == 0:
                        goon.attack(shades)
                        print("Goon attacked you!")
                        print("Shades Health: ", shades.current_hp)
                    if rand_action == 1:
                        goon.block()
                        print("Blocked!")
                    if rand_action == 2:
                        #goon.heal()
                        print("Goon healed")
        else:
            game_over = 2
    
    if current_fighter > 2:
        current_fighter = 1

    if game_over != 0:
        if game_over == 1:
            #add screen.blit lose
            print("You Lost!")
        if game_over == 2:
            #add screen.blit victory
            print("You win")
        #add conditional for restart button
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            clicked = True
        else:
            clicked = False
    pygame.display.update()
<<<<<<< HEAD
pygame.quit()
=======

pygame.quit()
>>>>>>> 2aae20f1434de5e6b7b09af75d7cbc23c3e16c1d
