import pygame

white = (255, 255, 255)
black = (0, 0, 0)
grey = (20, 20, 20)
yellow = (255, 255, 0)
pygame.init()

class Phantom(pygame.sprite.Sprite):

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
<<<<<<< HEAD
        self.change_state(((self.number + 1) % 3) + 1)
=======
        self.change_state(((self.number + 1) % 12) + 1)
>>>>>>> af05c58 (Soy Bruno 2.0)


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
for i in range(1):
    phant = Phantom("Pink", 1, 200, 300)
    
    phant_list.add(phant)
    all_sprite_list.add(phant)

jugador = Jugador()
all_sprite_list.add(jugador)  
    
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    mouse_pos = pygame.mouse.get_pos()
    phant.rect.x = mouse_pos[0]
    phant.rect.y = mouse_pos[1]
    
    screen.fill(black)
    phant.animation()

    all_sprite_list.draw(screen)
    
    pygame.display.flip()
<<<<<<< HEAD
    clock.tick(6)
=======
    clock.tick(12)
>>>>>>> af05c58 (Soy Bruno 2.0)
    
pygame.quit()
