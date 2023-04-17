import pygame, random, time

white = (255, 255, 255)
black = (0, 0, 0)
grey = (20, 20, 20)
yellow = (255, 255, 0)
pygame.init()

class DinoAmarillo(pygame.sprite.Sprite):

    

    def  __init__(self, number, x, y):
        super().__init__()
        self.number = number
        name = f"paknamAni1{number}.png"
        self.image = pygame.image.load(name).convert()
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        
    def delay(self):
        self.waited += 1  
        
    def change_state(self, number):
        self.number = number
        name = f"paknamAni1{number}.png"
        self.image = pygame.image.load(name).convert()
        self.image.set_colorkey(yellow)

    def animation(self):
        self.change_state(((self.number) % 14) + 1)
    

screen = pygame.display.set_mode([720,720])
clock = pygame.time.Clock()
done = False

all_sprite_list = pygame.sprite.Group() 
for i in range(1):
    dinoAmarillo = DinoAmarillo(1, 32, 32)
    all_sprite_list.add(dinoAmarillo)
    
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    all_sprite_list.draw(screen)
    dinoAmarillo.animation()
    
    pygame.display.flip()
    clock.tick(10)

    
pygame.quit()