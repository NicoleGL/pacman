import pygame

class Button():
    def __init__(self, image, x, y):
        self.name = image
        self.image = pygame.image.load(f"mapa/{image}.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
    def hover(self, screen):
        self.image = pygame.image.load(f"mapa/{self.name}_hover.png")
        self.draw(screen)
    
    def antihover(self, screen):
        self.image = pygame.image.load(f"mapa/{self.name}.png")
        self.draw(screen)

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))