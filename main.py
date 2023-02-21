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

def move_sprite(spr, movement):
    spr.rect.x += movement[0]
    spr.rect.y += movement[1]
    draw_sprite(spr)

def stop_at_wall(spr, xvel, yvel):
    if((spr.direction == "left" and spr.rect.x < 3) or
      (spr.direction == "right" and spr.rect.x > (WIDTH - (spr.rect.width + 3)))):
        return(0, yvel)
    elif((spr.direction == "up" and spr.rect.y < 3) or
        (spr.direction == "down" and spr.rect.y > (HEIGHT - (spr.rect.height + 3)))):
        return(xvel, 0)
    else:
        return(xvel,yvel)



def main():
    run = True
    xvel = 0
    yvel = 0
    speed = 3
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:

                if event.key == K_UP:
                    player.direction = "up"
                    xvel = 0
                    yvel = -speed
                elif event.key == K_DOWN:
                    player.direction = "down"
                    xvel = 0
                    yvel = speed
                elif event.key == K_LEFT:
                    player.direction = "left"
                    xvel = -speed
                    yvel = 0
                elif event.key == K_RIGHT:
                    player.direction = "right"
                    xvel = speed
                    yvel = 0
        
        
        player.update_img()
        move_sprite(player, stop_at_wall(player, xvel, yvel))
        all_sprite_list.draw(screen)
        pygame.display.update()
        clock.tick(FPS)



main()