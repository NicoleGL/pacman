import pygame
from pygame.locals import *
from pacman import *


#Pantalla
pygame.display.init()
clock = pygame.time.Clock()
WIDTH = 960
HEIGHT = 544
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pak-Nam")
FPS = 120


#Sprites
player = Pacman(0,0)
all_sprite_list = pygame.sprite.Group()
all_sprite_list.add(player)


#Funciones
def draw_sprite(spr):
    screen.fill((0,0,0))
    screen.blit(spr.image, spr.rect)
    pygame.display.update()

def move_sprite(spr):
    spr.rect.x += spr.speed[0]
    spr.rect.y += spr.speed[1]
    draw_sprite(spr)

def read_chunk(spr):
    chunk_x = spr.rect.x // 32
    chunk_y = spr.rect.y // 32
    return (chunk_x, chunk_y)

def main():
    run = True
    speed = 3
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:

                if event.key == K_UP:
                    player.direction = "up"
                    player.speed = (0, -speed)
                elif event.key == K_DOWN:
                    player.direction = "down"
                    player.speed = (0, speed)
                elif event.key == K_LEFT:
                    player.direction = "left"
                    player.speed = (-speed, 0)
                elif event.key == K_RIGHT:
                    player.direction = "right"
                    player.speed = (speed, 0)
        
        
        player.update_img()
        player.stop_if_wall(WIDTH, HEIGHT)
        move_sprite(player)
        all_sprite_list.draw(screen)
        pygame.display.update()
        clock.tick(FPS)



main()