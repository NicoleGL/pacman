import pygame, random, time

white = (255, 255, 255)
black = (0, 0, 0)
grey = (20, 20, 20)
yellow = (255, 255, 0)
pygame.init()

class Phantom(pygame.sprite.Sprite):

    

    def  __init__(self, color, number, x, y, waited, direction):
        super().__init__()
        self.direction = direction
        self.waited = waited
        self.color = color
        self.number = number
        name = f"{color}/{color}Phant{number}{direction}.png"
        self.image = pygame.image.load(name).convert()
        self.image.set_colorkey(yellow)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        
    def delay(self):
        self.waited += 1  
        
    def change_state(self, number):
        self.number = number
        name = f"{self.color}/{self.color}Phant{number}{self.direction}.png"
        self.image = pygame.image.load(name).convert()
        self.image.set_colorkey(yellow)

    def animation(self):
        self.change_state(((self.number + 1) % 5) + 1)
        
    def animation2(self):
        self.delay()
        if (self.waited == 6):
            self.change_state((((((self.number + 1) % 5) + 1) + 1) % 5) + 1)
            self.waited = 0
       # pygame.time.wait(100)
    

screen = pygame.display.set_mode([720,720])
clock = pygame.time.Clock()
done = False

all_sprite_list = pygame.sprite.Group() 
for i in range(1):
    phant = Phantom("ScaredB", 1, 32, 0,0, "N")
    phont = Phantom("ScaredB", 1, 64, 0,0, "S")
    phent = Phantom("ScaredB", 1, 96, 0,0, "E")
    phunt = Phantom("ScaredB", 1, 128, 0,0, "W")
    phant2 = Phantom("ScaredW", 1, 32, 32,0, "N")
    phont2 = Phantom("ScaredW", 1, 64, 32,0, "S")
    phent2 = Phantom("ScaredW", 1, 96, 32,0, "E")
    phunt2 = Phantom("ScaredW", 1, 128, 32,0, "W")
    phant3 = Phantom("Pink", 1, 32, 64,0, "N")
    phont3 = Phantom("Pink", 1, 64, 64, 0,"S")
    phent3 = Phantom("Pink", 1, 96, 64,0, "E")
    phunt3 = Phantom("Pink", 1, 128, 64,0, "W")
    phant4 = Phantom("Orange", 1, 32, 96,0, "N")
    phont4 = Phantom("Orange", 1, 64, 96,0, "S")
    phent4 = Phantom("Orange", 1, 96, 96,0, "E")
    phunt4 = Phantom("Orange", 1, 128, 96,0, "W")
    scared = Phantom("ScaredB", 1,160, 0, 0,"N" )
all_sprite_list = pygame.sprite.Group()
all_sprite_list.add(phant)
all_sprite_list.add(phont)
all_sprite_list.add(phent)
all_sprite_list.add(phunt)
all_sprite_list.add(phant2)
all_sprite_list.add(phont2)
all_sprite_list.add(phent2)
all_sprite_list.add(phunt2)
all_sprite_list.add(phant3)
all_sprite_list.add(phont3)
all_sprite_list.add(phent3)
all_sprite_list.add(phunt3)
all_sprite_list.add(phant4)
all_sprite_list.add(phont4)
all_sprite_list.add(phent4)
all_sprite_list.add(phunt4)
all_sprite_list.add(scared)
#jugador = Jugador()
# all_sprite_list.add(jugador)  
    
""" while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

  #  mouse_pos = pygame.mouse.get_pos()

  #  phant.rect.x = mouse_pos[0]
  #  phant.rect.y = mouse_pos[1]
    
    screen.fill(black)
    phant.animation2()
    phont.animation2()
    phent.animation2()
    phunt.animation2()
    phant2.animation2()
    phont2.animation2()
    phent2.animation2()
    phunt2.animation2()
    phant3.animation2()
    phont3.animation2()
    phent3.animation2()
    phunt3.animation2()
    phant4.animation2()
    phont4.animation2()
    phent4.animation2()
    phunt4.animation2()
    scared.animation2()

    all_sprite_list.draw(screen)
    
    
    pygame.display.flip()
    clock.tick(120)

    
pygame.quit() """
