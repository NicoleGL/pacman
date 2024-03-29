import pygame, board


class Pacman(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.direction = None
        self.next_direction = None
        self.animation = 1
        self.image = pygame.image.load(f"images/paknam_{self.direction}{self.animation}.png").convert()
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x = x
        self.y = y
        self.speed = (0, 0)
        self.tick = 0
        self.lives = 3
        self.score = -10
        self.dead = False
        self.now = False

    def update_img(self):
        self.image = pygame.image.load(f"images/paknam_{self.direction}{self.animation}.png").convert()
        self.image.set_colorkey((0, 0, 0))


    def next_chunk(self):
        chunk_x = self.rect.x // 32
        chunk_y = self.rect.y // 32
        if(self.direction == "up"):
            chunk_y -= 1
        if(self.direction == "down"):
            chunk_y += 1
        if(self.direction == "left"):
            chunk_x = (self.rect.x + 31) // 32
            chunk_x -= 1
        if(self.direction == "right"):
            chunk_x += 1
        return (chunk_x, chunk_y)
    

    def next_possible_chunk(self):
        chunk_x = self.rect.x // 32
        chunk_y = self.rect.y // 32
        if(self.next_direction == "up"):
            chunk_y -= 1
        if(self.next_direction == "down"):
            chunk_y += 1
        if(self.next_direction == "left"):
            chunk_x -= 1
        if(self.next_direction == "right"):
            chunk_x += 1
        return (chunk_x, chunk_y)

    def stop_if_wall(self):
        chunk = self.next_chunk()
        chunk_x, chunk_y = chunk
        path = board.posiciones_camino
        if(chunk == (-1, 6)):
            if(self.rect.x <= 0):
                self.rect.x = 604
        elif(chunk == (19, 6)):
            if(self.rect.x >= 604):
                self.rect.x = 0
        elif(not chunk in path or chunk == (9,5)):
            if((self.direction == "left") and (self.rect.x <= ((chunk_x + 1)*32))
               or (self.direction == "right")):
                self.speed = (0, self.speed[1])
            elif((self.direction == "up" and self.rect.y <= ((chunk_y + 1)*32))
               or (self.direction == "down")):
                self.speed = (self.speed[0], 0)


    def move_if_possible(self, speed):
        chunk = self.next_possible_chunk()
        chunk_x, chunk_y = chunk
        path = board.posiciones_camino
        if(chunk in path and chunk != (9,5)):
            if(self.dead == False):
                if(self.next_direction == "left" and self.rect.y <= (chunk_y*32)):
                    self.direction = self.next_direction
                    self.speed = (-speed, 0)
                elif(self.next_direction == "right" and self.rect.y <= (chunk_y*32)):
                    self.direction = self.next_direction
                    self.speed = (speed, 0)
                elif(self.next_direction == "up" and self.rect.x <= (chunk_x*32)):
                    self.direction = self.next_direction
                    self.speed = (0, -speed)
                elif(self.next_direction == "down" and self.rect.x <= (chunk_x*32)):
                    self.direction = self.next_direction
                    self.speed = (0, speed)
        self.update_img()
        
    
    def change_animation(self):
        if(self.dead):
            self.direction = "Ani"
            if( (self.tick == 120) | (self.tick == 240) | (self.tick == 300) | (self.tick == 360)):
                self.animation = 1
            elif((self.tick == 60) | (self.tick == 180) | (self.tick == 270) | (self.tick == 330)):
                self.animation = 2
            elif(self.tick == 380):
                self.animation = 3
            elif(self.tick == 400):
                self.animation = 4
            elif(self.tick == 420):
                self.animation = 5
            elif(self.tick == 430):
                self.animation = 1
                self.tick = 0
                self.dead = False
                self.now = True
        else:
            if(self.speed != (0,0)):
                if((self.tick % 30 == 0)):
                    self.animation = 2
                elif(self.tick % 15 == 0):
                    self.animation = 1
                self.update_img()
        self.tick += 1

    def change_speed(self, speed):
            if ((self.rect.x % speed) != 0 and (self.direction == "left" or self.direction == "right")):
                self.rect.x -= 1
            if ((self.rect.y % speed) != 0 and (self.direction == "up" or self.direction == "down")):
                self.rect.y -= 1
