import pygame
from pygame.locals import *
from pacman import *


pygame.display.init()
clock = pygame.time.Clock()
WIDTH = 700
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pak-Nam")


player = Pacman(0,0)
all_sprite_list = pygame.sprite.Group()
all_sprite_list.add(player)

def drawSprite(spr):
    screen.fill((0,0,0))
    screen.blit(spr.image, spr.rect)
    pygame.display.update()
    clock.tick(60)

#Esto está mega roto de momento pero me voy a dormir
def moveSprite(spr, direction, speed):
    if(direction == "left"):
        while spr.rect.x > 0:
            spr.rect.x -= speed
            drawSprite(spr)
    if(direction == "right"):
        while spr.rect.x <= (WIDTH - spr.rect.width):
            spr.rect.x += speed
            drawSprite(spr)
    if(direction == "up"):
        while spr.rect.y > 0:
            spr.rect.y -= speed
            drawSprite(spr)
    if(direction == "down"):
        while spr.rect.y <= (HEIGHT - spr.rect.height):
            spr.rect.y += speed
            drawSprite(spr)

def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:

                if event.key == K_UP:
                    moveSprite(player, "up", 5)
                elif event.key == K_DOWN:
                    moveSprite(player, "down", 5)
                elif event.key == K_LEFT:
                    moveSprite(player, "left", 5)
                elif event.key == K_RIGHT:
                    moveSprite(player, "right", 5)

        all_sprite_list.draw(screen)
        pygame.display.update()
        clock.tick(120)



main()