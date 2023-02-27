import pygame

white = (255, 255, 255)
black = (0, 0, 0)
grey = (20, 20, 20)
yellow = (255, 255, 0)
pygame.init()

class Phantom(pygame.sprite.Sprite):
    def __init__(self, color, number, direction, scaredTime, waited,  x, y):
        super().__init__()
        self.number = number
        self.color = color
        self.name = self.color
        self.direction = direction
        self.waited = waited
        self.x = x
        self.y = y
        self.scaredTime = scaredTime
        name = f"Sprites/{self.color}/{self.color}Phant{number}{self.direction}.png"
        self.image = pygame.image.load(name).convert()
        self.image.set_colorkey(yellow)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def setscaredTime(self, number1):
        self.number1 = number1
        self.scaredTime = number1

    def delay(self):
        self.waited += 1
    
    def change_state(self, number2):
        self.number = number2
        name = f"Sprites/{self.color}/{self.color}Phant{self.number}{self.direction}.png"
        self.image = pygame.image.load(name).convert()
        self.image.set_colorkey(yellow)

    def change_mood(self,  mood):
        self.mood = mood
        self.color = mood
        name = f"Sprites/{self.color}/{self.color}Phant{self.number}{self.direction}.png"
        self.image = pygame.image.load(name).convert()
        self.image.set_colorkey(yellow)
        

    def animation2(self):
        self.delay()
        if (self.waited == 6):
            self.change_state((((((self.number + 1) % 5) + 1) + 1) % 5) + 1)
            self.waited = 0

    def timepassed(self):
        self.scaredTime += 1
    
    def imScared(self):
        if self.scaredTime > 0:
            self.timepassed()
            if (self.scaredTime == 360)|(self.scaredTime == 730)|(self.scaredTime == 790)|(self.scaredTime == 850):
                self.change_mood("ScaredW")
            if (self.scaredTime == 10)|(self.scaredTime == 670)|(self.scaredTime == 760)|(self.scaredTime == 820):
                self.change_mood("ScaredB")
            if self.scaredTime == 880:
                self.change_mood(self.name)
                self.scaredTime = 0


    


screen = pygame.display.set_mode([720,720])
clock = pygame.time.Clock()
done = False

all_sprite_list = pygame.sprite.Group()

for i in range(1):
    blue = Phantom("Blue", 1, "N", 0, 0, 32, 32)
    red = Phantom("Red",1,"N", 0, 0, 64, 32)
    orange = Phantom("Orange", 1, "N", 0, 0, 96, 32)
    pink = Phantom("Pink", 1, "N", 0, 0, 128, 32)

    
    all_sprite_list.add(blue)
    all_sprite_list.add(red)
    all_sprite_list.add(orange)
    all_sprite_list.add(pink)
    
""" while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                blue.setscaredTime(9)
                pink.setscaredTime(9)
                orange.setscaredTime(9)
                red.setscaredTime(9)

        

    blue.animation2()
    red.animation2()
    orange.animation2()
    pink.animation2()
    blue.imScared()
    red.imScared()
    orange.imScared()
    pink.imScared()

    screen.fill(black)
    all_sprite_list.draw(screen)
    
    pygame.display.flip()
    clock.tick(120)
    
pygame.quit()  """
