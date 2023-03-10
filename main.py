import pygame
from pygame.locals import *
from pacman import *
from board import *
from ghost import Ghost

# Pantalla
pygame.display.init()
clock = pygame.time.Clock()
WIDTH = 608
HEIGHT = 384
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pak-Nam")
FPS = 120


GAME_OVER = pygame.USEREVENT + 1


esquinas = [(2, 2), (2, 4), (2, 6), (2, 8), (2, 10), (4, 4), (4, 6), (4, 8), (6, 2), (6, 4), (6, 6), 
            (6, 10), (8, 8), (8, 10), (10, 8), (10, 10), (12, 2), (12, 4), (12, 6), (12, 10), (14, 4), 
            (14, 6), (14, 8), (16, 2), (16, 4), (16, 6), (16, 8), (16, 10)]

# Sprites
player = Pacman(9*32, 8*32)

blue = Ghost("Blue", 1, "N", (32 * 8, 32 * 6))
pink = Ghost("Pink", 1, "N", (32 * 9, 32 * 6))
orange = Ghost("Orange", 1, "N", (32 * 10, 32 * 6))
red = Ghost("Red", 1, "N", (32 * 9, 32 * 5))
phantoms = pygame.sprite.Group()
phantoms.add(blue, pink, orange, red)
all_sprite_list = pygame.sprite.Group()
all_sprite_list.add(player)
all_sprite_list.add(blue, pink, orange, red)


# Funciones
def draw_sprite(spr):
    screen.blit(spr.image, spr.rect)
    pygame.display.update()


def move_sprite(spr, speed):
    if (spr == player):
        player.move_if_possible(speed)
        player.stop_if_wall()
    spr.rect.x += spr.speed[0]
    spr.rect.y += spr.speed[1]
    

def collision(pacman, phantoms):
    phantom = pygame.sprite.spritecollideany(pacman, phantoms)
    if (phantom):
        if (phantom.scaredTime != 0):  # fantasma asustado
            phantom.change_mood("Eyes")
            phantom.scaredTime = 3001
        else:
            if pacman.lives > 0:
                pacman.lives -= 1
            reset_sprites(pacman, phantoms)
            if(pacman.lives == 0):
                pygame.event.post(pygame.event.Event(GAME_OVER))
                


set_board(screen)
all_sprite_list.draw(screen)

def main():
    run = True
    speed = 1  # Debe ser una potencia de 2

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:

                if event.key == K_UP:
                    player.next_direction = "up"
                elif event.key == K_DOWN:
                    player.next_direction = "down"
                elif event.key == K_LEFT:
                    player.next_direction = "left"
                elif event.key == K_RIGHT:
                    player.next_direction = "right"


            if event.type == GAME_OVER:
                game_over_screen(screen)
                
            if event.type == MOUSEMOTION:
                if(player.lives == 0):
                    x, y = event.pos
                    if(pygame.Rect.collidepoint(retry_button.rect, x, y)):
                        retry_button.hover(screen)    
                    elif(pygame.Rect.collidepoint(exit_button.rect, x, y)):
                        exit_button.hover(screen)
                    else:
                        retry_button.antihover(screen)
                        exit_button.antihover(screen)
                        
            if event.type == MOUSEBUTTONDOWN:
                if(player.lives == 0):
                    x, y = event.pos
                    if(pygame.Rect.collidepoint(retry_button.rect, x, y)):
                        player.lives = 3
                        retry_button.antihover(screen)
                        set_board_again(screen, player, phantoms)
                        all_sprite_list.draw(screen)
                    elif(pygame.Rect.collidepoint(exit_button.rect, x, y)):
                        run = False
                
                
                
        move_sprite(player, speed)
        player.change_animation()

        if (player.rect.x//32, player.rect.y//32) in esquinas:
            pink.esquina = (player.rect.x//32, player.rect.y//32)
        if (player.rect.x//32, player.rect.y//32) in esquinas:
            blue.esquina = (player.rect.x//32, player.rect.y//32)
        if player.rect.x % 32 == 0 and player.rect.y % 32 == 0 and (player.rect.x//32 - blue.pospacAnt[0], player.rect.y//32 - 
            blue.pospacAnt[1]) in [(1,0), (-1,0), (0,1), (0,-1)]:
            if (pink.pospacAnt in esquinas and (player.rect.x//32, player.rect.y//32) != pink.pospacAnt):
                pink.df.at[pink.pospacAnt, (player.rect.x//32 - pink.pospacAnt[0], player.rect.y//32 - pink.pospacAnt[1])] += 1
            if (blue.pospacAnt in esquinas and (player.rect.x//32, player.rect.y//32) != blue.pospacAnt):
                blue.df.at[blue.pospacAnt, (player.rect.x//32 - blue.pospacAnt[0], player.rect.y//32 - blue.pospacAnt[1])] += 1
        pink.pospacAnt = (player.rect.x//32, player.rect.y//32)
        blue.pospacAnt = (player.rect.x//32, player.rect.y//32)
        for phantom in phantoms:
            if (phantom.rect.x, phantom.rect.y) == phantom.posInicial:
                phantom.scaredTime = 0
                phantom.change_mood(phantom.name)
        
        

        for phantom in phantoms:
            phantom.animation2()
            phantom.imScared()
            phantom.moveGhost(posiciones_camino, (player.rect.x//32, player.rect.y//32))

        collision(player, phantoms)
        if(player.lives != 0):
            draw_sprite(player)
            update_board(player, special_path, currently_full_paths, phantoms, screen)
            special_path.cherry(currently_full_paths)
            set_path(screen)
            all_sprite_list.draw(screen)
        
        pygame.display.update()
        clock.tick(FPS)


main()
