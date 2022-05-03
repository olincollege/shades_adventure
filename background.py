import pygame

pygame.init()

#Game window
width = 800
height = 400

screen = pygame.display.set_mode([width, height])
pygame.display.set_caption("Shades's Adventure")

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
pygame.quit()
