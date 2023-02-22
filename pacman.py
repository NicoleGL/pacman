import pygame

class Pacman(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.direction = None
        self.image = pygame.image.load(f"images/paknam_{self.direction}.png").convert()
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = (0, 0)

    def update_img(self):
        self.image = pygame.image.load(f"images/paknam_{self.direction}.png").convert()
        self.image.set_colorkey((0, 0, 0))


    def stop_if_wall(self, width, height):
        if((self.direction == "left" and self.rect.x < 3) or
          (self.direction == "right" and self.rect.x > (width - (self.rect.width + 3)))):
            self.speed = (0, self.speed[1])
        elif((self.direction == "up" and self.rect.y < 3) or
            (self.direction == "down" and self.rect.y > (height - (self.rect.height + 3)))):
            self.speed = (self.speed[0], 0)
