import pygame

class Pacman(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.direction = None
        self.image = pygame.image.load(f"images/paknam_{self.direction}.png").convert()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def update_img(self):
        self.image = pygame.image.load(f"images/paknam_{self.direction}.png").convert()