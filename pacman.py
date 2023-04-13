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
    
    def speed_near_wall(self, speed):
        chunk_x, chunk_y = self.next_chunk()
        if((self.direction == "left") and ((self.rect.x - speed) // 32) == chunk_x):
            return (self.rect.x - (chunk_x *32 + 31))
        else:
            return speed


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
                print("hola")
            elif((self.direction == "up" and self.rect.y <= ((chunk_y + 1)*32))
               or (self.direction == "down")):
                self.speed = (self.speed[0], 0)


    def move_if_possible(self, speed):
        chunk = self.next_possible_chunk()
        chunk_x, chunk_y = chunk
        path = board.posiciones_camino
        new_speed = self.speed_near_wall(speed)
        if(chunk in path and chunk != (9,5)):
            if(self.next_direction == "left" and self.rect.y <= (chunk_y*32)):
                self.direction = self.next_direction
                self.speed = (-new_speed, 0)
            elif(self.next_direction == "right" and self.rect.y <= (chunk_y*32)):
                self.direction = self.next_direction
                self.speed = (new_speed, 0)
            elif(self.next_direction == "up" and self.rect.x <= (chunk_x*32)):
                self.direction = self.next_direction
                self.speed = (0, -new_speed)
            elif(self.next_direction == "down" and self.rect.x <= (chunk_x*32)):
                self.direction = self.next_direction
                self.speed = (0, new_speed)
        self.update_img()
        
    
    def change_animation(self):
        if(self.speed != (0,0)):
            if((self.tick % 30 == 0)):
                self.animation = 2
            elif(self.tick % 15 == 0):
                self.animation = 1
            self.update_img()
            self.tick += 1