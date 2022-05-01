import pygame
from fighter import Fighter

pygame.init()

width = 256
height = 144

screen = pygame.display.set_mode([width,height])
pygame.display.set_caption("Shades's Adventure")

current_fighter = 1
total_fighers = 2
attack = False
clicked = False
game_over = 0

background = pygame.image.load("img/background.png").convert_alpha()
# shades = pygame.image.load("").convert_alpha()
# goon = pygame.image.load("").convert_alpha()

def draw_background():
    screen.blit(background,(0,0))

run = True

while run:
    draw_background()

    shades = Fighter("Shades", 100, 15, -5)
    goon = Fighter("Goon", 75, 10, -3)

    screen.blit(shades.image, shades.rectangle)
    screen.blit(goon.image, goon.image)

    # Shades actions
    attack = False
    pygame.mouse.set_visible(True)
    pos = pygame.mouse.get_pos()
    if goon.rectangle.collidepoint(pos):
       if clicked == True and goon.death == False:
           attack = True
           print("You attacked the goon!")
           print("Goon's Health: " + goon.current_hp)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            clicked = True
        else:
            clicked = False

    pygame.display.update()

pygame.quit()