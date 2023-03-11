import pygame
from mapa import block
from button import Button
from ghost import Ghost

#Constantes
yellow = pygame.Color(255, 242, 0)
black = pygame.Color(0, 0, 0)

posiciones_bloque_right = [(1,2),(1,3),(1,4),(1,5),(1,7),(1,8),(1,9),
                            (1,10),(3,5),(3,6),(3,7),(5,3),(5,4),(5,5),
                            (5,7),(5,8),(5,9),(7,6),(7,8),(7,9),(8,5),
                            (9,9),(9,10),(15,3),(15,5),(15,6),(15,7),(15,9),
                            (13, 4),(13, 5),(13, 7),(13, 8),
                            (11, 3),(11, 5),(11, 6),(11, 7),(11, 8),(11, 9)]

posiciones_bloque_left = [(3,3),(3,5),(3,6),(3,7),(3,9),(5, 4),(5, 5),
                            (5, 7),(5, 8),(7, 3),(7, 5),(7, 6),(7, 7),
                            (7, 8),(7, 9),(9,9),(9,10),(10,5),(17,2),
                            (17,3),(17,4),(17,5),(17,7),(17,8),(17,9),
                            (17,10),(15,5),(15,6),(15,7),(13,3),(13,4),
                            (13,5),(13,7),(13,8),(13,9),(11,6),(11,8),
                            (11,9)]

posiciones_bloque_down = [(0,5),(1,5),(2,1),(3, 1),(3, 3),(3, 7),(3, 9),
                            (4,1),(4,3),(4,9),(5,1),(5,5),(5,9),(6,1),
                            (7,1),(7,3),(7,9),(8, 1),(8, 3),(8, 5),
                            (8, 7),(9,1),(9,3),(9,7),(18,5),(17,5),(16,1),
                            (15, 1),(15, 3),(15, 7),(15, 9),
                            (14,1),(14,3),(14,9),(13,1),(13,5),(13,9),(12,1),
                            (11,1),(11,3),(11,9),(10, 1),(10, 3),(10, 5),
                            (10, 7)]

posiciones_bloque_up = [(0,7),(1,7),(2,11),(3, 3),(3, 5),(3, 9),(3, 11),
                        (4,3),(4,9),(4,11),(5,3),(5,7),(5,11),(6,11),
                        (7,3),(7,5),(7,11),(8,3),(8,5),(8,7),(8,11),
                        (9,3),(9,7),(9,9),(18,7),(17,7),(16,11),(15, 3),
                        (15, 5),(15, 9),(15, 11),
                        (14,3),(14,9),(14,11),(13,3),(13,7),(13,11),(12,11),
                        (11,3),(11,5),(11,11),(10,3),(10,5),(10,7),(10,11)]

posiciones_camino = [(0, 6) ,(1, 6), (2, 2) ,(2, 3) ,(2, 4) ,(2, 5), 
                (2, 6) ,(2, 7) ,(2, 8) ,(2, 9) ,(2, 10) ,(3, 2) ,(3, 4) ,
                (3, 8) ,(3, 10) ,(4, 2) , (4, 4), (4, 5), (4, 6), (4, 7),
                (4, 8), (4, 10), (5, 2), (5, 6), (5, 10), (6, 2), (6, 3),
                (6, 4), (6, 5), (6, 6), (6, 7), (6, 8), (6, 9), (6, 10),
                (7, 2), (7, 4), (7, 10), (8, 2), (8, 4), (8, 6), (8, 8),
                (8, 9), (8, 10), (9, 2), (9, 4), (9, 5), (9, 6), (9, 8), 
                (10, 2), (10, 4), (10, 6), (10, 8), (10, 9), (10, 10),
                (11, 2), (11, 4), (11, 10), (12, 2), (12, 3), (12, 4), 
                (12, 5), (12, 6), (12, 7), (12, 8), (12, 9), (12, 10),
                (13, 2), (13, 6), (13, 10), (14, 2) , (14, 4), (14, 5), 
                (14, 6), (14, 7), (14, 8), (14, 10), (15, 2) ,(15, 4) ,
                (15, 8) ,(15, 10), (16, 2) ,(16, 3) ,(16, 4) ,(16, 5), 
                (16, 6) ,(16, 7) ,(16, 8) ,(16, 9) ,(16, 10), (17, 6),
                (18, 6)] #el gran array de arrays

posiciones_circulito = [(2, 2) ,(2, 3) ,(2, 4) ,(2, 5), 
                (2, 6) ,(2, 7) ,(2, 8) ,(2, 9), (3, 2) ,(3, 4) ,
                (3, 8) ,(3, 10) ,(4, 2), (4, 5), (4, 6), (4, 7),
                (4, 8), (4, 10), (5, 2), (5, 6), (5, 10), (6, 2), (6, 3),
                (6, 4), (6, 5), (6, 6), (6, 7), (6, 8), (6, 9), (6, 10),
                (7, 2), (7, 4), (7, 10), (8, 2), (8, 4), (8, 8),
                (8, 9), (8, 10), (9, 2), (9, 4), (9, 8), 
                (10, 2), (10, 4), (10, 8), (10, 9), (10, 10),
                (11, 2), (11, 4), (11, 10), (12, 2), (12, 3), (12, 4), 
                (12, 5), (12, 6), (12, 7), (12, 8), (12, 9), (12, 10),
                (13, 2), (13, 6), (13, 10), (14, 2) , (14, 4), (14, 5), 
                (14, 6), (14, 7), (14, 10), (15, 2) ,(15, 4) ,
                (15, 8) ,(15, 10), (16, 3) ,(16, 4) ,(16, 5), 
                (16, 6) ,(16, 7) ,(16, 8) ,(16, 9) ,(16, 10)]

posiciones_bola = [(2,10), (16,2), (4,4), (14, 8)]

posiciones_none = [(9,5), (8,6), (9,6), (10,6), (0,6), (1,6), (17,6), (18, 6)]

all_paths = pygame.sprite.Group()
full_paths = pygame.sprite.Group()
currently_full_paths = pygame.sprite.Group()
special_path = block.Path((9,2), "circulito")

pygame.font.init()
arial = pygame.font.SysFont("Arial", 26)


bg_img = pygame.image.load("mapa/game_over.png")
retry_button = Button("retry", 5*32, 7*32)
exit_button = Button("exit", 11*32, 7*32)


#Funciones
def set_image(type, coord, screen):
    block_img = pygame.image.load(f"mapa/{type}.png").convert_alpha()
    block_img.set_colorkey(yellow)
    screen.blit(block_img, (coord[0] * 32, coord[1] * 32))

def set_board(screen):
    
    screen.fill(black)
    block_img = pygame.image.load(f"mapa/Bordes.png").convert_alpha()
    block_img.set_colorkey(black)
    screen.blit(block_img, (0,0))
    
    for posicion in posiciones_circulito:
        path = block.Path(posicion, "circulito")
        screen.blit(path.image, path.rect)
        full_paths.add(path)
        currently_full_paths.add(path)
        all_paths.add(path)
    for posicion in posiciones_bola:
        path = block.Path(posicion, "bola")
        screen.blit(path.image, path.rect)
        full_paths.add(path)
        currently_full_paths.add(path)
        all_paths.add(path)
    for posicion in posiciones_none:
        path = block.Path(posicion, "None")
        screen.blit(path.image, path.rect)
        all_paths.add(path)
        
    screen.blit(special_path.image, special_path.rect)
    full_paths.add(special_path)
    currently_full_paths.add(special_path)
    all_paths.add(special_path)
    
    lives_img = pygame.image.load("images/3lives.png")
    screen.blit(lives_img, (0,0))
    set_image("BlockDoor", (9,5), screen)
    
    update_level(screen)


def set_path(screen):
    for path in all_paths:
        screen.blit(path.image, path.rect)
    set_image("BlockDoor", (9,5), screen)
    
def update_level(screen):
    level_msg = arial.render(f"Lvl: {Ghost.level}", False, (255,255,255))
    screen.blit(level_msg, (70, 0))

def update_board(pacman, special_path, currently_full_paths, phantoms, screen):
    path = pygame.sprite.spritecollideany(pacman, currently_full_paths)
    if(path):
        x, y = path.rect.center
        if(pygame.Rect.collidepoint(pacman.rect, x, y)):
            if(path.item == "bola"):
                for phantom in phantoms:
                    phantom.set_scared_time(9)
            path.update_item(None)
            currently_full_paths.remove(path)
        if(len(currently_full_paths) == 0): #Has ganado el juego!!
            Ghost.level += 1
            set_board_again(screen, pacman, phantoms)
    if(pygame.sprite.collide_rect(pacman, special_path) and special_path.item == "cherry"):
        x, y = special_path.rect.center
        if(pygame.Rect.collidepoint(pacman.rect, x, y)):
            special_path.update_item(None)
    special_path.cherry(currently_full_paths)
    lives_img = pygame.image.load(f"images/{pacman.lives}lives.png")
    screen.blit(lives_img, (0,0))
    
    
def set_board_again(screen, pacman, phantoms):  
    screen.fill(black)
    block_img = pygame.image.load(f"mapa/Bordes.png").convert_alpha()
    screen.blit(block_img, (0,0))
    for path in full_paths:
        if not path in currently_full_paths:
            currently_full_paths.add(path)
            path.update_item(path.og_item)
    reset_sprites(pacman, phantoms)
    lives_img = pygame.image.load("images/3lives.png")
    screen.blit(lives_img, (0,0))
    set_image("BlockDoor", (9,5), screen)
    update_level(screen)
        
        
def reset_sprites(pacman, phantoms):
    for phantom in phantoms:
        phantom.scaredTime = 0
        phantom.rect.x = phantom.posInicial[0]
        phantom.rect.y = phantom.posInicial[1]
    pacman.direction = None
    pacman.next_direction = None
    pacman.rect.x = pacman.x
    pacman.rect.y = pacman.y
    pacman.speed = (0, 0)
        

def game_over_screen(screen):
    screen.blit(bg_img, (0,0))
    retry_button.draw(screen)
    exit_button.draw(screen)