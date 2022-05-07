import pygame

class GameView():
    """
    
    """

    def __init__(self):
        """
        
        """
        self.panel_ = 614/2
        self.width = 1097
        self.height = 614 + self.panel_
        self.surface = pygame.display.set_mode([self.width, self.height])

    def starting_screen(self, image):
        """
        
        """
        title_screen = pygame.image.load(image).convert_alpha
        self.surface.bilt(title_screen,(0,0))

    def background(self, image):
        """
        
        """
        #background = pygame.image.load(image).convert_alpha()
        self.surface.blit(image,(0,0))

    def panel(self, image):
        """
        
        """
        #panel_img = pygame.image.load(image).convert_alpha()
        self.surface.blit(image, (0,self.height - self.panel_))

    def display_character(self, image, x, y):
        """
        
        """
        start_img = pygame.image.load(image).convert_alpha()
        img = pygame.transform.scale(start_img, (start_img.get_width() * 6, start_img.get_height() * 6))
        rect = img.get_rect()
        rect.center = (x, y)
        self.surface.blit(img, (rect.x, rect.y))


    def health_bar(self, character, x, y):
        """
        
        """
        font = pygame.font.Font('freesanshold.ttf', 32)
        text = font.render(f'Health: {character.current_hp}')
        # create rectangle
        textRect = text.get_rect()
        textRect.center = (x, y)

        while True:
            self.surface.blit(text, textRect)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                pygame.display.update()

    def draw_button(self, image, x, y, x_size, y_size):
        """
        
        """
        start_img = pygame.image.load(image).convert_alpha()
        img = pygame.transform.scale(start_img, (x_size, y_size))
        rect = img.get_rect()
        rect.topleft = (x, y)
        self.surface.blit(img, (rect.x, rect.y))
        return rect
        