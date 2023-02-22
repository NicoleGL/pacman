import pygame
from pygame.locals import *
from pacman import *
from board import set_board

#Pantalla
pygame.display.init()
clock = pygame.time.Clock()
WIDTH = 608
HEIGHT = 384
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pak-Nam")
FPS = 120


#Sprites
player = Pacman(0,192)
all_sprite_list = pygame.sprite.Group()
all_sprite_list.add(player)


#Funciones
def draw_sprite(spr):
    screen.blit(spr.image, spr.rect)
    pygame.display.update()

def move_sprite(spr):
    spr.rect.x += spr.speed[0]
    spr.rect.y += spr.speed[1]
    draw_sprite(spr)



        

def main():
    run = True
    speed = 4
    
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:

                if event.key == K_UP:
                    player.next_direction = "up"
                elif event.key == K_DOWN:
                    player.next_direction = "down"
                elif event.key == K_LEFT:
                    player.next_direction = "left"
                elif event.key == K_RIGHT:
                    player.next_direction = "right"
        
        set_board(screen)

        player.move_if_possible(speed)
        player.stop_if_wall()
        move_sprite(player)

        all_sprite_list.draw(screen)
        pygame.display.update()
        clock.tick(FPS)



main()