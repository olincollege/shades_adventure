import pygame

class Button():

    def __init__(self, surface, rect):
        #self.image = pygame.transform.scale(image, (x_size, y_size))
        #self.rect = self.image.get_rect()
        self.rect = rect
        #self.rect.topleft = (x,y)
        self.clicked = False
        self.surface = surface

    def get_button(self):
        action = False
        mouse_pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                action = True
                self.clicked = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        #self.surface.blit(self.image, (self.rect.x, self.rect.y))
        return action