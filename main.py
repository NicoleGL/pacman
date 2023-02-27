import pygame, sys
from pygame.locals import *
from pacman import *
from board import *
from Sprites import pruebaSprites
from mapa import block

#Pantalla
pygame.display.init()
clock = pygame.time.Clock()
WIDTH = 608
HEIGHT = 384
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pak-Nam")
FPS = 120


#Sprites
player = Pacman(9*32,8*32)
blue = pruebaSprites.Phantom("Blue", 1, "N", 0, 0, 32 * 2, 32 * 2)
phantoms = pygame.sprite.Group()
phantoms.add(blue)
all_sprite_list = pygame.sprite.Group()
all_sprite_list.add(player)
all_sprite_list.add(blue)


#Funciones
def draw_sprite(spr):
    screen.blit(spr.image, spr.rect)
    pygame.display.update()

def move_sprite(spr, speed):
    if(spr == player):
       player.move_if_possible(speed)
       player.stop_if_wall()
    spr.rect.x += spr.speed[0]
    spr.rect.y += spr.speed[1]
    draw_sprite(spr)

def game_over(pacman, phantoms):
    phantom = pygame.sprite.spritecollideany(pacman, phantoms)
    if(phantom):
        if(phantom.scaredTime != 0 or phantom.color != "Blue"): #fantasma asustado
            phantom.rect.x = 9*32
            phantom.rect.y = 6*32
        else:
            print("Game Over")
            sys.exit()



        
set_board(screen)
all_sprite_list.draw(screen)
def main():
    run = True
    speed = 2 #Debe ser una potencia de 2
    
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
                elif event.key == K_SPACE:
                    blue.setscaredTime(9)
                    
                    
        
        
        
        #blue.animation2()
        blue.imScared()
        
        move_sprite(player, speed)
        draw_sprite(blue)
        game_over(player, phantoms)
        block.Path.update_board(player, full_paths, phantoms)
        set_path(screen)

        all_sprite_list.draw(screen)
        pygame.display.update()
        clock.tick(FPS)



main()