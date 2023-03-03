import pygame

pygame.init()

class Path(pygame.sprite.Sprite):
    def __init__(self, coords, item):
        pygame.sprite.Sprite.__init__(self)
        self.item = item
        self.image = pygame.image.load(f"mapa/path_{item}.png")
        self.rect = self.image.get_rect()
        self.rect.x = 32*coords[0]
        self.rect.y = 32*coords[1]
        self.tick = 0

    def update_item(self, new_item):
        self.item = new_item
        self.image = pygame.image.load(f"mapa/path_{new_item}.png")

                
    def cherry(self, full_paths):
        if(self.tick % 4800 == 0):
            if(self in full_paths):
                self.update_item("circulito")
            else:
                self.update_item(None)
        elif(self.tick % 2400 == 0):
            self.update_item("cherry")
        self.tick += 1
        
