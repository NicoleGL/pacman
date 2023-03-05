import pygame, random, time

white = (255, 255, 255)
black = (0, 0, 0)
grey = (20, 20, 20)
yellow = (255, 255, 0)
pygame.init()

class DinoAmarillo(pygame.sprite.Sprite):

    

    def  __init__(self, number, x, y,waited):
        super().__init__()
        self.number = number
        self.waited = waited
        name = f"paknamAni3{number}.png"
        self.image = pygame.image.load(name).convert()
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        
    def delay(self):
        self.waited += 1  
        
    def change_state(self, number):
        self.number = number
        name = f"paknamAni3{number}.png"
        self.image = pygame.image.load(name).convert()
        self.image.set_colorkey(yellow)

    def animation(self):
        self.change_state(((self.number + 1) % 9) + 1)

    def animation2(self):
        self.waited += 1
        if (self.waited > 0):
            if( (self.waited == 10) | (self.waited == 20) | (self.waited == 25)):
                self.change_state(1)
            elif((self.waited == 5) | (self.waited == 15) | (self.waited == 22)):
                self.change_state(2)
            elif(self.waited == 28):
                self.change_state(3)
            elif(self.waited == 31):
                self.change_state(4)
            elif(self.waited == 34):
                self.change_state(5)
                self.waited = 0
            

screen = pygame.display.set_mode([720,720])
clock = pygame.time.Clock()
done = False

all_sprite_list = pygame.sprite.Group() 
for i in range(1):
    dinoAmarillo = DinoAmarillo(1, 32, 32, 0)
    all_sprite_list.add(dinoAmarillo)
    
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    all_sprite_list.draw(screen)
    dinoAmarillo.animation2()
    
    pygame.display.flip()
    clock.tick(8)

    
pygame.quit()