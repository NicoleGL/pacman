import pygame, sys
from pygame.locals import *
from pacman import *
from board import *
from Sprites import pruebaSprites
from mapa import block
from ghost import Ghost

#Pantalla
pygame.display.init()
clock = pygame.time.Clock()
WIDTH = 608
HEIGHT = 384
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pak-Nam")
FPS = 120


esquinas = [(2,2),(2,4),(2,6),(2,8),(2,10),(4,4),(4,6),(4,8),(6,2),(6,4),(6,6),(6,10),
        (8,8),(8,10),(10,8),(10,10),(12,2),(12,4),(12,6),(12,10),(14,4),(14,6),(14,8),(16,2),
        (16,4),(16,6),(16,8),(16,10)]

#Sprites
player = Pacman(9*32,8*32)

blue = Ghost("Blue", 1, "N", 32 * 8, 32 * 6)
pink = Ghost("Pink", 1, "N", 32 * 9, 32 * 6)
orange = Ghost("Orange", 1, "N", 32 * 10, 32 * 6)
red = Ghost("Red", 1, "N", 32 * 9, 32 * 5)
phantoms = pygame.sprite.Group()
phantoms.add(blue, pink, orange, red)
all_sprite_list = pygame.sprite.Group()
all_sprite_list.add(player)
all_sprite_list.add(blue, pink, orange, red)


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
        if(phantom.scaredTime != 0): #fantasma asustado
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
                    
                    
        move_sprite(player, speed)
        
        
        if (player.rect.x, player.rect.y) in esquinas:
            pink.esquina = (player.rect.x, player.rect.y)
        if pink.posAnt in esquinas:
            pink.df.at[pink.posAnt, (player.rect.x-pink.posAnt[0], player.rect.y-pink.posAnt[1])] += 1
        pink.posAnt = (player.rect.x, player.rect.y)
        if (player.rect.x, player.rect.y) in esquinas:
            blue.esquina = (player.rect.x, player.rect.y)
        if blue.posAnt in esquinas:
            blue.df.at[blue.posAnt, (player.rect.x-blue.posAnt[0], player.rect.y-blue.posAnt[1])] += 1
        blue.posAnt = (player.rect.x, player.rect.y)
        
        for phantom in phantoms:
            phantom.animation2()
            phantom.imScared()
            phantom.moveGhost(posiciones_camino, player.rect.center)
        
        game_over(player, phantoms)
        block.Path.update_board(player, full_paths, phantoms)
        set_path(screen)

        all_sprite_list.draw(screen)
        pygame.display.update()
        clock.tick(FPS)



main()