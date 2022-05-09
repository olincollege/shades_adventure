"""Main file used to run game."""
import random
import time
import pygame
from fighter import Fighter
from button_controls import Button
from game_view import GameView

def main():
    """
    Run a game of Shades' Adventure.
    """

    pygame.init()

    panel = 618/2
    width = 1103
    height = 618 + panel

    screen = pygame.display.set_mode([width,height])
    pygame.display.set_caption("Shades's Adventure")

    start_game = False
    game_over = 0
    current_fighter = 1


    starting_screen_img = pygame.image.load("img/start_screen_test.png").convert_alpha()
    background_img = pygame.image.load("img/background.png").convert_alpha()
    panel_img = pygame.image.load("img/panel.png").convert_alpha()

    shades = Fighter("Shades", 100, 15, -5)
    goon = Fighter("Goon", 100, 12, -3)


    run = True

    while run:
        game = GameView()

        # load starting screen
        game.background(starting_screen_img)
        start_button_start = game.draw_button("img/start_button.png", 500, 500, 250, 250)
        start_button = Button(screen, start_button_start)

        if start_button.get_button():
            start_game = True
        # start game
        if start_game:
            # render display
            game.background(background_img)
            game.panel(panel_img)

            game.display_character("img/shades.png", 150, 350)
            game.display_character("img/goon.png", 900, 400)

            game.health_bar(shades, 150, 650)
            game.health_bar(goon, 850, 650)

            attack_button_start = game.draw_button("img/attack_button.png", 150, 675, 111, 27)
            block_button_start = game.draw_button("img/block_button.png", 150, 710, 111, 27)
            heal_button_start = game.draw_button("img/heal_button.png", 150, 745, 111, 27)
            restart_button_start = game.draw_button("img/restart_button.png", 850, 0, 303, 303)

            attack_button = Button(screen, attack_button_start)
            block_button = Button(screen, block_button_start)
            heal_button = Button(screen, heal_button_start)
            restart_button = Button(screen, restart_button_start)

            # Shades' actions
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
                if not shades.death:
                    if current_fighter == 1:
                        if attack:
                            shades.attack(target)
                            shades.reverse_block(target)
                            game.empty_screen(shades, goon)
                            game.display_character("img/shades_attack.png", 250, 350)
                            game.display_character("img/goon.png", 900, 400)
                            pygame.display.update()
                            time.sleep(.75)
                            game.empty_screen(shades, goon)
                            game.display_character("img/shades.png", 250, 350)
                            game.display_character("img/goon.png", 900, 400)
                            pygame.display.update()
                            time.sleep(1.25)
                            current_fighter = 2
                        if block:
                            shades.block(True)
                            time.sleep(1.25)
                            current_fighter = 2
                        if heal:
                            shades.heal()
                            time.sleep(1.25)
                            current_fighter = 2
                        if restart_button.get_button():
                            shades.reset()
                            goon.reset()
                            current_fighter = 1
                            game_over = 0
                            game.health_bar(shades, 150, 650)
                            game.health_bar(goon, 850, 650)

                else:
                    game_over = 1

                if not goon.death:
                    if current_fighter == 2:
                        if shades.current_hp <= 20:
                            goon.attack(shades)
                            goon.reverse_block(shades)
                            game.empty_screen(shades, goon)
                            game.display_character("img/goon_attack.png", 900, 400)
                            game.display_character("img/attack_button.png", 925, 725)
                            game.display_character("img/shades.png", 250, 350)
                            pygame.display.update()
                            time.sleep(.75)
                            game.empty_screen(shades, goon)
                            game.display_character("img/goon.png", 900, 400)
                            game.display_character("img/shades.png", 250, 350)
                            game.empty_screen(shades, goon)
                            time.sleep(1)
                        if goon.current_hp <= 25:
                            rand_low_health = random.randint(0,2)
                            if rand_low_health in (0,1):
                                goon.heal()
                                game.display_character("img/goon_attack.png", 900, 400)
                                game.display_character("img/shades.png", 250, 350)
                                game.display_character("img/heal_button.png", 925, 725)
                                pygame.display.update()
                                time.sleep(1)
                            else:
                                goon.block(True)
                                game.display_character("img/goon_attack.png", 900, 400)
                                game.display_character("img/shades.png", 250, 350)
                                game.display_character("img/block_button.png", 925, 725)
                                pygame.display.update()
                                time.sleep(1)
                        else:
                            rand_action = random.randint(0,4)
                            if rand_action in (0,1,2):
                                goon.attack(shades)
                                goon.reverse_block(shades)
                                game.empty_screen(shades, goon)
                                game.display_character("img/goon_attack.png", 900, 400)
                                game.display_character("img/attack_button.png", 925, 725)
                                game.display_character("img/shades.png", 250, 350)
                                pygame.display.update()
                                time.sleep(0.75)
                                game.empty_screen(shades, goon)
                                game.display_character("img/goon.png", 900, 400)
                                game.display_character("img/shades.png", 250, 350)
                                pygame.display.update()
                                time.sleep(1)
                            if rand_action == 3:
                                goon.block(True)
                                game.display_character("img/block_button.png",\
                                     925, 725)
                                pygame.display.update()
                                time.sleep(1)
                        current_fighter = 1
                else:
                    game_over = 2

            # end game and load end screen
            if game_over != 0:
                if game_over == 1:
                    game.end_screen()
                    restart_button_start = game.draw_button(\
                        "img/restart_button.png", 500, 600, 303, 303)
                    restart_button = Button(screen, restart_button_start)
                    game.display_character("img/goon.png", 900, 400)
                    game.display_character("img/lose_button.png", 500, 500)
                    game.display_character("img/shades_dead.png", 250, 350)
                    pygame.display.update()
                    if restart_button.get_button():
                        shades.reset()
                        goon.reset()
                        current_fighter = 1
                        game_over = 0
                        game.health_bar(shades, 150, 650)
                        game.health_bar(goon, 850, 650)
                if game_over == 2:
                    game.end_screen()
                    restart_button_start = game.draw_button("img/restart_button.png", 500, 600, 303, 303)
                    restart_button = Button(screen, restart_button_start)
                    game.display_character("img/shades.png", 250, 350)
                    game.display_character("img/win.png", 500, 500)
                    game.display_character("img/goon_dead.png", 900, 400)
                    pygame.display.update()
                    if restart_button.get_button():
                        shades.reset()
                        goon.reset()
                        current_fighter = 1
                        game_over = 0
                        game.health_bar(shades, 150, 650)
                        game.health_bar(goon, 850, 650)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.display.update()
    pygame.quit()

if __name__ == '__main__':
    main()
