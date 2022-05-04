from numpy import char
import pygame

class HealthBar():
    """
    
    """
    def __init__(self, surface, x, y):
        """
        
        """
        self.surface = surface
        self.x = x
        self.y = y
        self.white = (255,255,255)
        self.green = (0, 255, 0)
        self.blue = (0, 0, 128)

    def draw(self, character):
        """
        
        """
        font = pygame.font.Font('freesanshold.ttf', 32)
        text = font.render(f'Health: {character.current_hp}')
        # create rectangle
        textRect = text.get_rect()
        textRect.center = (self.x, self.y)

        while True:
            self.surface.blit(text, textRect)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                pygame.display.update()
