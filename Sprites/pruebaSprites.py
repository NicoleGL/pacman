import pygame, random

white = (255, 255, 255)
black = (0, 0, 0)
grey = (20, 20, 20)
yellow = (255, 255, 0)
pygame.init()
<<<<<<< HEAD
class Phantom(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
<<<<<<< HEAD
        self1.image = pygame.image.load("PinkPhant1.png").convert()
        self1.image.set_colorkey(yellow)
        self1.rect = self1.image.get_rect()
=======
        self.image = pygame.image.load("PinkPhant1.png").convert()
        self.image.set_colorkey(yellow)
        self.rect = self.image.get_rect()
    
>>>>>>> af05c58 (Soy Bruno 2.0)
=======

class Phantom(pygame.sprite.Sprite):
    def __init__(self1):
        super().__init__()
        self1.image = pygame.image.load("PinkPhant1.png").convert()
        self1.image.set_colorkey(yellow)
        self1.rect = self1.image.get_rect()
    def __init__(self2):
        super().__init__()
        self2.image = pygame.image.load("PinkPhant2.png").convert()
        self2.image.set_colorkey(yellow)
        self2.rect = self2.image.get_rect()
    def __init__(self3):
        super().__init__()
        self3.image = pygame.image.load("PinkPhant3.png").convert()
        self3.image.set_colorkey(yellow)
        self3.rect = self3.image.get_rect()
>>>>>>> 4e0cfdb (Añadir sprites de fantasmas y las pruebas)

class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("OrangePhant1.png").convert()
        self.image.set_colorkey(yellow)
        self.rect = self.image.get_rect()

screen = pygame.display.set_mode([720,720])
clock = pygame.time.Clock()
done = False

phant_list = pygame.sprite.Group()
all_sprite_list = pygame.sprite.Group()

for i in range(2):
<<<<<<< HEAD
    phant = Phantom()
=======
    phant = Phantom(self2)
>>>>>>> 4e0cfdb (Añadir sprites de fantasmas y las pruebas)
    phant.rect.x = random.randrange(900)
    phant.rect.y = random.randrange(600)
    
    phant_list.add(phant)
    all_sprite_list.add(phant)

jugador = Jugador()
all_sprite_list.add(jugador)  
    
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    mouse_pos = pygame.mouse.get_pos()
    jugador.rect.x = mouse_pos[0]
    jugador.rect.y = mouse_pos[1]
    
    screen.fill(black)
    
    all_sprite_list.draw(screen)
    
    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()
