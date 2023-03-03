import pygame, sys


clock=pygame.time.Clock()
pygame.init()

yellow = pygame.Color(255, 242, 0)

chunk = 32

ancho = 608
alto = 384
size = (ancho, alto)

screen = pygame.display.set_mode(size)

pygame.display.set_caption("Pak-Nam")
backgroundImg = pygame.image.load("BackgroundImg.png")

def colocarObjeto(direction, coord):
    blockImg = pygame.image.load(f"block{direction}.png").convert_alpha()
    blockImg.set_colorkey(yellow)
    screen.blit(blockImg, (coord[0] * chunk, coord[1] * chunk))
    
  #  print(blockImg.get_at((0, 0))) mr pinturitas me ayuda ;)

def colocarDoor(x, y):
    blockImg = pygame.image.load("blockDoor.png").convert_alpha()
    blockImg.set_colorkey(yellow)
    screen.blit(blockImg, (x * chunk, y * chunk))
    
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

def ponerBloques():
    right = posiciones_bloque_right
    left = posiciones_bloque_left
    down = posiciones_bloque_down
    up = posiciones_bloque_up
    for posicion in right:
        colocarObjeto("Right",posicion)
    for posicion in left:
        colocarObjeto("Left",posicion)
    for posicion in down:
        colocarObjeto("Down",posicion)
    for posicion in up:
        colocarObjeto("Up",posicion)

def colocarCamino(coord):
    blockImg = pygame.image.load("path.png").convert_alpha()
    blockImg.set_colorkey(yellow)
    screen.blit(blockImg, (coord[0] * chunk, coord[1] * chunk))

posiciones_camino_public = [(0, 6) ,(1, 6), (2, 2) ,(2, 3) ,(2, 4) ,(2, 5), 
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

def ponerCaminos():
    posiciones_camino = posiciones_camino_public
    for posicion in posiciones_camino:
        colocarCamino(posicion)


while True:
    for event in pygame.event.get():
        screen.blit(backgroundImg, (0, 0))
        if event.type == pygame.QUIT:
            sys.exit()
        
    #ponerCaminos()
    ponerBloques()
    #colocarDoor(9, 5)
    

    pygame.display.update()
    clock.tick(120) 