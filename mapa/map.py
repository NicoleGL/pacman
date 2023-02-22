import pygame, sys


clock=pygame.time.Clock()
pygame.init()

yellow = (255, 255, 0)

pixel = 32

ancho = 608
alto = 384
size = (ancho, alto)

screen = pygame.display.set_mode(size)

pygame.display.set_caption("Pak-Nam")
backgroundImg = pygame.image.load("BackgroundImg.png")

class Block(pygame.sprite.Sprite):
    def __init__(self, direction):
        super().__init__()
        self.direction = direction
        self.image.set_colorkey(yellow)
    def change_direction(self, direction):
        self.direction = direction
        blockImg = pygame.image.load(f"block{direction}.png")
        self.image.set_colorkey(yellow)






def colocarObjeto(Block, x, y):
    screen.blit(backgroundImg, (x, y))


while True:
    for event in pygame.event.get():
        screen.blit(backgroundImg, (0, 0))
        if event.type == pygame.QUIT:
            sys.exit()



    pygame.display.update()
    clock.tick(120)
