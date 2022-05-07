import pygame
import random
import time
from fighter import Fighter
from button_controls import Button
from game_view import GameView

pygame.init()

panel = 614/2
width = 1097
height = 614 + panel

screen = pygame.display.set_mode([width,height], pygame.RESIZABLE)
pygame.display.set_caption("Shades's Adventure")

game_over = 0
current_fighter = 1

background_img = pygame.image.load("img/background.png").convert_alpha()
panel_img = pygame.image.load("img/panel.png").convert_alpha()
attack_img = pygame.image.load("img/attack_button.png").convert_alpha()
block_img = pygame.image.load("img/block_button.png").convert_alpha()
heal_img = pygame.image.load("img/heal_button.png").convert_alpha()
target_img = pygame.image.load("img/test_target.png").convert_alpha()

run = True

while run:
    game = GameView()

    shades = Fighter("Shades", 100, 15, -5, 150, 300)
    goon = Fighter("Goon", 75, 10, -3, 825, 300)

    game.background(background_img)
    game.panel(panel_img)

    game.display_character("img/shades_0.png", 450, 350)
    game.display_character("img/sprite.png", 900, 350)

    attack_button_start = game.draw_button("img/attack_button.png", 150, 675, 60, 21)
    block_button_start = game.draw_button("img/block_button.png", 150, 700, 60, 21)
    heal_button_start = game.draw_button("img/heal_button.png", 150, 725, 60, 21)
    restart_button_start = game.draw_button("img/restart_button.jpg", 900, 100, 30, 30)

    attack_button = Button(screen, attack_button_start)
    block_button = Button(screen, block_button_start)
    heal_button = Button(screen, heal_button_start)
    restart_button = Button(screen, restart_button_start)

    #Shades actions
    attack = False
    block = False
    heal = False
    target = None
    pygame.mouse.set_visible(True)

    if attack_button.get_button():
        target = goon
        attack = True
    if block_button.get_button():
        block = True
    if heal_button.get_button():
        heal = True

    if game_over == 0:    
        if shades.death == False:
            if current_fighter == 1:
                time.sleep(1.25)
                if attack == True:
                    shades.attack(target)
                    print("Shades attacked goon!")
                    print("Goon Health: ", goon.current_hp)
                    #game.display_character("img/shades_attack_1.png", 450, 350)
                    #time.sleep(0.25)
                    #game.display_character("img/shades_attack_2.png", 450, 350)
                    current_fighter += 1
                    cooldown = 0
                if block == True:
                    shades.block(True)
                    print("Shades Blocked!")
                    current_fighter += 1
                    cooldown = 0
                if heal == True:
                    shades.heal()
                    if shades.potion_count > 3:
                        current_fighter = 1
                        cooldown = 0
                    print("Shades Healed!")

        else:
            game_over = 1

        if goon.death == False:
            if current_fighter == 2:
                time.sleep(2)
                if shades.current_hp <= 20:
                    goon.attack(shades)
                    cooldown = 0
                    print("Goon attacked you!")
                    print("Shades Health: ", shades.current_hp)
                    #game.display_character("img/goon_attack_1.png", 450, 350)
                    #time.sleep(0.25)
                    #game.display_character("img/goon_attack_2.png", 450, 350)
                if goon.current_hp <= 25:
                    rand_low_health = random.randint(0,2)
                    if rand_low_health == 0 or rand_low_health == 1:
                        goon.heal()
                        cooldown = 0
                        if goon.potion_count > 3:
                            current_fighter = 2
                        print("Goon Healed")
                    else:
                        goon.block(True)
                        cooldown = 0
                        print("Goon Blocked!")
                else:
                    rand_action = random.randint(0,4)
                    if rand_action == 0 or rand_action == 1 or rand_action == 2:
                        goon.attack(shades)
                        cooldown = 0
                        print("Goon attacked you!")
                        print("Shades Health: ", shades.current_hp)
                        #game.display_character("img/goon_attack_1.png", 450, 350)
                        #time.sleep(0.25)
                        #game.display_character("img/goon_attack_2.png", 450, 350)
                    if rand_action == 3:
                        goon.block(True)
                        cooldown = 0
                        print("Goon Blocked!")
        else:
            game_over = 2

    if current_fighter >= 2:
        current_fighter = 1

    if game_over != 0:
        if game_over == 1:
            #add screen.blit lose
            print("You Lost!")
        if game_over == 2:
            #add screen.blit victory
            print("You win")
        if restart_button.get_button():
            shades.reset()
            goon.reset()
            current_player = 1
            game_over = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            clicked = True
        else:
            clicked = False
    pygame.display.update()
pygame.quit()