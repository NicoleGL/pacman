import pygame, math, random, pandas as pd

yellow = (255, 255, 0)
class Ghost(pygame.sprite.Sprite):
    def __init__(self, color, number, direction, posInicial):
        pygame.sprite.Sprite.__init__(self)
        self.number = number
        self.color = color
        self.name = color
        self.direction = direction
        name = f"Sprites/{self.color}/{self.color}Phant{number}{self.direction}.png"
        self.image = pygame.image.load(name).convert()
        self.image.set_colorkey(yellow)
        self.waited = 0
        self.scaredTime = 0
        
        self.rect = self.image.get_rect()
        self.posInicial = posInicial
        self.rect.x = posInicial[0]
        self.rect.y = posInicial[1]
        self.dire = (0,0)
        self.pospacAnt = (9,8)
        self.counter = 0

        self.df = pd.DataFrame(0, index=[(2,2),(2,4),(2,6),(2,8),(2,10),(4,4),(4,6),(4,8),(6,2),(6,4),(6,6),(6,10),
        (8,8),(8,10),(10,8),(10,10),(12,2),(12,4),(12,6),(12,10),(14,4),(14,6),(14,8),(16,2),
        (16,4),(16,6),(16,8),(16,10)], columns=[(1,0), (-1,0), (0,1), (0,-1)])
        self.esquina = (9,8)

        Ghost.level = 1
        Ghost.numero_fantasmas = -1


    def moveGhost(self, box, pospac):
        if self.color == "Red":
            if self.rect.x%32 == 0 and self.rect.y%32 == 0:
                velocity = Ghost.rojo(self.scaredTime, self.counter, self.dire, box, ((self.rect.x)//32, (self.rect.y)//32), pospac)
                self.rect.x += velocity[0]
                self.rect.y += velocity[1]
                self.dire = velocity
                self.direction = Ghost.change_direction(velocity)
            else:
                self.rect.x += self.dire[0]
                self.rect.y += self.dire[1]
            self.counter += 1
        elif self.color == "Orange":
            if self.rect.x%32 == 0 and self.rect.y%32 == 0:
                velocity = Ghost.naranja(self.scaredTime, self.counter, self.dire, box, ((self.rect.x)//32, (self.rect.y)//32), pospac)
                self.rect.x += velocity[0]
                self.rect.y += velocity[1]
                self.dire = velocity
                self.direction = Ghost.change_direction(velocity)
            else:
                self.rect.x += self.dire[0]
                self.rect.y += self.dire[1]
            self.counter += 1
        elif self.color == "Pink":
            if self.rect.x%32 == 0 and self.rect.y%32 == 0:
                velocity = Ghost.rosa(self.scaredTime, self.counter, self.dire, box, ((self.rect.x)//32, (self.rect.y)//32), self.df, pospac, self.esquina)
                self.rect.x += velocity[0]
                self.rect.y += velocity[1]
                self.dire = velocity
                self.direction = Ghost.change_direction(velocity)
            else:
                self.rect.x += self.dire[0]
                self.rect.y += self.dire[1]
            self.counter += 1
        elif self.color == "Blue":
            if self.rect.x%32 == 0 and self.rect.y%32 == 0:
                velocity = Ghost.azul(self.scaredTime, self.counter, self.dire, box, ((self.rect.x)//32, (self.rect.y)//32), self.df, pospac, self.esquina)
                self.rect.x += velocity[0]
                self.rect.y += velocity[1]
                self.dire = velocity
                self.direction = Ghost.change_direction(velocity)
            else:
                self.rect.x += self.dire[0]
                self.rect.y += self.dire[1]
            self.counter += 1
        elif self.color == "ScaredW" or self.color == "ScaredB":
            if self.rect.x%32 == 0 and self.rect.y%32 == 0:
                velocity = Ghost.asustado(box, ((self.rect.x)//32, (self.rect.y)//32), pospac)
                self.rect.x += velocity[0]
                self.rect.y += velocity[1]
                self.dire = velocity
                self.direction = Ghost.change_direction(velocity)
            else:
                self.rect.x += self.dire[0]
                self.rect.y += self.dire[1]
            self.counter += 1
        else:
            if self.rect.x%32 == 0 and self.rect.y%32 == 0:
                velocity = Ghost.muerto(self.scaredTime, self.counter, self.dire, box, ((self.rect.x)//32, (self.rect.y)//32),
                (self.posInicial[0]//32, self.posInicial[1]//32))
                self.rect.x += velocity[0]
                self.rect.y += velocity[1]
                self.dire = velocity
                self.direction = Ghost.change_direction(velocity)
            else:
                self.rect.x += self.dire[0]
                self.rect.y += self.dire[1]
            self.counter += 1


    def distance (point1, point2):
        #calcula la distancia de un punto arbitrario a otro
        return math.sqrt((point2[0]-point1[0])**2 + (point2[1]-point1[1])**2)


    def casillaFinal (pospac, dire):
        x = pospac[0]
        y = pospac[1]
        #Para rosa: calcula la casilla a la que tiene que ir (final del camino o intersección en dirección a la que va pacman)
        while (x + dire[0], y + dire[1]) in [(2,2),(2,4),(2,6),(2,8),(2,10),(4,4),(4,6),(4,8),(6,2),(6,4),(6,6),(6,10),
        (8,8),(8,10),(10,8),(10,10),(12,2),(12,4),(12,6),(12,10),(14,4),(14,6),(14,8),(16,2),
        (16,4),(16,6),(16,8),(16,10)]:
            x += dire[0]
            y += dire[1]
        return (pospac[0] + dire[0], pospac[1] + dire[1])


    def sinSalida (box, pos, dire, pospac):
        #Crea un camino imaginario en la dirección hacia la que se elige y calcula si el camino está cerrado 
        # o si hay salidas
        if ((pos in box) and ((pos[0]+dire[1], pos[1]+dire[0]) not in box) and 
            ((pos[0]-dire[1], pos[1]-dire[0]) not in box) and ((pos[0]+dire[0], pos[1]+dire[1]) == pospac)):
            return False
        elif ((pos in box) and ((pos[0]+dire[1], pos[1]+dire[0]) not in box) and
            ((pos[0]-dire[1], pos[1]-dire[0]) not in box)):
            return Ghost.sinSalida(box, (pos[0]+dire[0], pos[1]+dire[1]), dire, pospac)
        elif (pos not in box):
            return True
        else:
            return False


    def alAzar (dire, box, pos, pospac):
        velocity = (0,0)
        while True:
            while (velocity == (0,0) or velocity == (1,1) or velocity == (-1, -1) or
                velocity == (1,-1) or velocity == (-1,1)):
                velocity = (random.choice([-1,0,1]), random.choice([-1,0,1]))
            if (Ghost.sinSalida(box, (pos[0]+velocity[0], pos[1]+velocity[1]), velocity, pospac) == False) and (velocity != (-dire[0], -dire[1])):
               break
            velocity = (0,0)
        return velocity


    def rojo (scaredTime, counter, dire, box, pos, pospac):
        if scaredTime <= 3000:
            if pos == (9,6) or pos == (9,5):
                return (0,-1)
            elif pos == (9,4):
                return (random.choice([-1,1]), 0)

        if counter <= 720:
            return Ghost.alAzar(dire, box, pos, pospac)
        velocity = (0,0)
        dic = {
            (1,0): Ghost.distance((pos[0]+1, pos[1]), pospac), 
            (-1,0): Ghost.distance((pos[0]-1, pos[1]), pospac), 
            (0,1): Ghost.distance((pos[0], pos[1]+1), pospac),
            (0,-1): Ghost.distance((pos[0], pos[1]-1), pospac)}
        lista = list(dic.values())
        menor = False
        count = 0
        #Hasta que la casilla elegida sea del camino y no lleve a sinSalida busca la casilla que esté más cerca de pacman
        while True:
            for i in range(0,len(dic)):
                for k in range(-(len(dic)-1)+count,0):
                    if len(lista) == 1:
                        break
                    if lista[i-count] >= lista[i+k-count]:
                        menor = True
                        count += 1
                        break
                if menor == True:
                    lista.remove(lista[i-count+1])
                menor = False
            velocity = list(dic.keys())[list(dic.values()).index(lista[0])]
            dic.pop(velocity)
            lista = list(dic.values())
            count = 0
            if scaredTime <= 3000:
                if ((pos[0]+velocity[0], pos[1]+velocity[1]) in box and 
                    Ghost.sinSalida(box, (pos[0]+velocity[0], pos[1]+velocity[1]), velocity, pospac) == False and velocity != (-dire[0], -dire[1])):
                    break
            else:
                if ((pos[0]+velocity[0], pos[1]+velocity[1]) in box and velocity != (-dire[0], -dire[1])):
                    break
        return velocity 

    
    def naranja (scaredTime, counter, dire, box, pos, pospac):
        velocity = (0,0)
        if pos == (10,6):
            return (-1,0)
        elif pos == (9,4):
            return (random.choice([-1,1]), 0)
        elif pos == (9,6) or pos == (9,5):
            return (0,-1)

        if counter <= 720:
            return Ghost.alAzar(dire, box, pos, pospac)
        #Si la distancia a pacman es menor que 3 casillas sigue como el rojo
        if Ghost.distance(pos, pospac) <= 3:
            return Ghost.rojo (scaredTime, counter, dire, box, pos, pospac)
        #Si no, hasta que la casilla elegida sea del camino y no lleve a sinSalida, elige una dirección al azar
        else:
            return Ghost.alAzar (dire, box, pos, pospac)


    def rosa (scaredTime, counter, dire, box, pos, df, pospac, esquina):
        #Si pacman está en una de las casillas que hace esquina o intersección entre caminos
        if pos == (9,6) or pos == (9,5):
            return (0,-1)
        elif pos == (9,4):
            return (random.choice([-1,1]), 0)

        if counter <= 720:
            return Ghost.alAzar(dire, box, pos, pospac)
        if (pospac in [(2,2),(2,4),(2,6),(2,8),(2,10),(4,4),(4,6),(4,8),(6,2),(6,4),(6,6),(6,10),
        (8,8),(8,10),(10,8),(10,10),(12,2),(12,4),(12,6),(12,10),(14,4),(14,6),(14,8),(16,2),
        (16,4),(16,6),(16,8),(16,10)]):
            velocity = (0,0)
            #El diccionario contiene las veces que ha ido en cada dirección al pasar por la casilla en la que está pacman
            dic = {
                (1,0):df.at[pospac, (1,0)], 
                (-1,0):df.at[pospac, (-1,0)], 
                (0,1):df.at[pospac, (0,1)], 
                (0,-1):df.at[pospac, (0,-1)]}
            if list(dic.values()) == [0,0,0,0]:
                while True:
                    while (velocity == (0,0) or velocity == (1,1) or velocity == (-1, -1) or
                        velocity == (1,-1) or velocity == (-1,1)):
                        velocity = (random.choice([-1,0,1]), random.choice([-1,0,1]))
                    if ((pos[0]+velocity[0], pos[1]+velocity[1]) in box and 
                        Ghost.sinSalida(box, (pos[0]+velocity[0], pos[1]+velocity[1]), velocity, pospac) == False):
                        break
                    velocity = (0,0)
                if pos == Ghost.casillaFinal(pospac, velocity):
                    return (0,0)
                return Ghost.rojo(scaredTime, counter, dire, box, pos, Ghost.casillaFinal(pospac, velocity))
            else:
                lista = list(dic.values())
                menor = False
                count = 0
                #Elimina los valores menores de la lista de veces que ha tomado cada dirección y si hay repetidos en el mayor valor solo lo toma una vez
                for i in range(0,4):
                    for k in range(-3+count,0):
                        if len(lista) == 1:
                            break
                        if lista[i-count] <= lista[i+k-count]:
                            menor = True
                            count += 1
                            break
                    if menor == True:
                        lista.remove(lista[i-count+1])
                    menor = False
                if pos == Ghost.casillaFinal(pospac, list(dic.keys())[list(dic.values()).index(lista[0])]):
                    return (0,0)
                return Ghost.rojo(scaredTime, counter, dire, box, pos, Ghost.casillaFinal(pospac, list(dic.keys())[list(dic.values()).index(lista[0])]))
        else:
            return Ghost.rojo(scaredTime, counter, dire, box, pos, esquina)


    def azul (scaredTime, counter, dire, box, pos, df, pospac, esquina):
        num = random.choice([0,1,2])
        if pos == (8,6):
            return (1,0)
        elif pos == (9,4):
            return (random.choice([-1,1]), 0)
        elif pos == (9,6) or pos == (9,5):
            return (0,-1)
        if counter <= 720:
            return Ghost.alAzar(dire, box, pos, pospac)
        if num == 0:
            return Ghost.rojo(scaredTime, counter, dire, box, pos, pospac)
        elif num == 1:
            return Ghost.naranja(scaredTime, counter, dire, box, pos, pospac)
        else:
            return Ghost.rosa(scaredTime, counter, dire, box, pos, df, pospac, esquina)


    def asustado (box, pos, pospac):
        velocity = (0,0)
        dic = {
            (1,0): Ghost.distance((pos[0]+1, pos[1]), pospac), 
            (-1,0): Ghost.distance((pos[0]-1, pos[1]), pospac), 
            (0,1): Ghost.distance((pos[0], pos[1]+1), pospac),
            (0,-1): Ghost.distance((pos[0], pos[1]-1), pospac)}
        lista = list(dic.values())
        menor = False
        count = 0
        #Hasta que la casilla elegida sea del camino y no lleve a sinSalida busca la casilla que esté más cerca de pacman
        while True:
            for i in range(0,len(dic)):
                for k in range(-(len(dic)-1)+count,0):
                    if len(lista) == 1:
                        break
                    if lista[i-count] <= lista[i+k-count]:
                        menor = True
                        count += 1
                        break
                if menor == True:
                    lista.remove(lista[i-count+1])
                menor = False
            if lista == []:
                while Ghost.sinSalida(box, (pos[0]+velocity[0], pos[1]+velocity[1]), velocity, pospac):
                    velocity = list(dic.keys())[list(dic.values()).index(random.choice([dic[(1,0)], dic[(-1,0)], dic[(0,1)], dic[(0,-1)]]))]
                    break
            velocity = list(dic.keys())[list(dic.values()).index(lista[0])]
            dic.pop(velocity)
            lista = list(dic.values())
            count = 0
            if Ghost.sinSalida(box, (pos[0]+velocity[0], pos[1]+velocity[1]), velocity, pospac) == False:
                break
        return velocity 


    def muerto (scaredTime, counter, dire, box, pos, posInicial):
        return Ghost.rojo(scaredTime, counter, dire, box, pos, posInicial)
            
            
    def set_scared_time(self, number1):
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

    def change_direction(newdirection):
        if newdirection == (1,0):
            return "E"
        elif newdirection == (-1,0):
            return "W"
        elif newdirection == (0,1):
            return "S"
        else:
            return "N"

    def animation2(self):
        self.delay()
        if (self.waited == 6):
            self.change_state((((((self.number + 1) % 5) + 1) + 1) % 5) + 1)
            self.waited = 0

    def timepassed(self):
        self.scaredTime += 1
    
    def imScared(self):
        if (self.scaredTime > 0) & (self.scaredTime < 3000):
            self.timepassed()
            if (self.scaredTime == 360)|(self.scaredTime == 730)|(self.scaredTime == 790)|(self.scaredTime == 850):
                self.change_mood("ScaredW")
            if (self.scaredTime == 10)|(self.scaredTime == 670)|(self.scaredTime == 760)|(self.scaredTime == 820):
                self.change_mood("ScaredB")
            if self.scaredTime == 880:
                self.change_mood(self.name)
                self.scaredTime = 0
        elif (self.scaredTime > 3000):
            self.change_mood("Eyes")