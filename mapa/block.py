import pygame

yellow = (255, 255, 0)
pygame.init()

class Block(pygame.sprite.Sprite):
    def __init__(self, direction):
        pygame.sprite.Sprite.__init__(self)
        self.image.set_colorkey(yellow)
