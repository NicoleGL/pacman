import pygame, sys

pygame.init()

class Path(pygame.sprite.Sprite):
    def __init__(self, coords, item):
        pygame.sprite.Sprite.__init__(self)
        self.item = item
        self.image = pygame.image.load(f"mapa/path_{item}.png")
        self.rect = self.image.get_rect()
        self.rect.x = 32*coords[0]
        self.rect.y = 32*coords[1]

    def update_item(self, new_item):
        self.item = new_item
        self.image = pygame.image.load(f"mapa/path_{new_item}.png")

    def update_board(pacman, full_paths, phantoms):
        path = pygame.sprite.spritecollideany(pacman, full_paths)
        if(path):
            x, y = path.rect.center
            if(pygame.Rect.collidepoint(pacman.rect, x, y)):
                path.update_item(None)
                full_paths.remove(path)
            if(path.item == "bola"):
                for phantom in phantoms:
                    phantom.setscaredTime(9)
            if(len(full_paths) == 0):
                print("You won!")
                sys.exit()
