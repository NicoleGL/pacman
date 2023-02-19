import pygame, random

white = (255, 255, 255)
black = (0, 0, 0)
grey = (20, 20, 20)
yellow = (255, 255, 0)
pygame.init()

class Phantom(pygame.sprite.Sprite):
<<<<<<< HEAD

    def  __init__(self, color, number, x, y):
        super().__init__()
        self.color = color
        self.number = number
        name = f"{color}Phant{number}.png"
        self.image = pygame.image.load(name).convert()
        self.image.set_colorkey(yellow)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def change_state(self, number):
        self.number = number
        name = f"{self.color}Phant{number}.png"
        self.image = pygame.image.load(name).convert()
        self.image.set_colorkey(yellow)

    def animation(self):
        self.change_state(((self.number + 1) % 12) + 1)

=======
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
<<<<<<< HEAD
all_sprite_list = pygame.sprite.Group() 
for i in range(1):
    phant = Phantom("Pink", 1, 200, 300)
=======
all_sprite_list = pygame.sprite.Group()
for i in range(2):
    phant = Phantom()
    phant.rect.x = random.randrange(900)
    phant.rect.y = random.randrange(600)
>>>>>>> 4e0cfdb (Añadir sprites de fantasmas y las pruebas)
    
    phant_list.add(phant)
    all_sprite_list.add(phant)

jugador = Jugador()
all_sprite_list.add(jugador)  
    
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    mouse_pos = pygame.mouse.get_pos()
<<<<<<< HEAD
    phant.rect.x = mouse_pos[0]
    phant.rect.y = mouse_pos[1]
    
    screen.fill(black)
    phant.animation()

    all_sprite_list.draw(screen)
    
    pygame.display.flip()
    clock.tick(12)
=======
    jugador.rect.x = mouse_pos[0]
    jugador.rect.y = mouse_pos[1]
    
    screen.fill(black)
    
    all_sprite_list.draw(screen)
    
    pygame.display.flip()
    clock.tick(60)
>>>>>>> 4e0cfdb (Añadir sprites de fantasmas y las pruebas)
    
pygame.quit()
