import pygame

class Ghost(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.color = color
        self.image = pygame.image.load(f"images/{color}.png") 
        #Pongo esto pensando en que las imágenes se llamen rojo.png, etc
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y