import pygame, math, random, pandas as pd

yellow = (255, 255, 0)
class Ghost(pygame.sprite.Sprite):
    def __init__(self, color, number, direction, x, y):
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
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y

        self.posAnt = (8,6)
        self.df = pd.DataFrame(0, index=[(2,2),(2,4),(2,6),(2,8),(2,10),(4,4),(4,6),(4,8),(6,2),(6,4),(6,6),(6,10),
        (8,8),(8,10),(10,8),(10,10),(12,2),(12,4),(12,6),(12,10),(14,4),(14,6),(14,8),(16,2),
        (16,4),(16,6),(16,8),(16,10)], columns=[(1,0), (-1,0), (0,1), (0,-1)])
        self.esquina = (9,8)



    def moveGhost(self, box, pospac):
        if self.color == "Red":
            print(Ghost.rojo(box, (self.rect.x//32, self.rect.y//32)))
            self.rect.x += Ghost.rojo(box, (self.rect.x//32, self.rect.y//32), pospac)[0]
            self.rect.y += Ghost.rojo(box, (self.rect.x//32, self.rect.y//32), pospac)[1]
            
        elif self.color == "Orange":
            self.rect.x += Ghost.naranja(box, (self.rect.x//32, self.rect.y//32), pospac)[0]
            self.rect.y += Ghost.naranja(box, (self.rect.x//32, self.rect.y//32), pospac)[1]
        elif self.color == "Pink":
            self.rect.x += Ghost.rosa(box, (self.rect.x//32, self.rect.y//32), self.df, pospac, self.esquina)[0]
            self.rect.y += Ghost.rosa(box, (self.rect.x//32, self.rect.y//32), self.df, pospac, self.esquina)[1]
        elif self.color == "Blue":
            self.rect.x += Ghost.azul(box, (self.rect.x//32, self.rect.y//32), self.df, pospac, self.esquina)[0]
            self.rect.y += Ghost.azul(box, (self.rect.x//32, self.rect.y//32), self.df, pospac, self.esquina)[1]
        else:
            self.rect.x += Ghost.asustado(box, (self.rect.x//32, self.rect.y//32), pospac)[0]
            self.rect.y += Ghost.asustado(box, (self.rect.x//32, self.rect.y//32), pospac)[1]



    def distance (point1, point2):
        #calcula la distancia de un punto arbitrario a otro
        return math.sqrt((point2[0]-point1[0])**2 + (point2[1]-point1[1])**2) 


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


    def rojo (box, pos, pospac):
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
            for i in range(0,4):
                for k in range(-3+count,0):
                    if len(lista) == 1:
                        break
                    if lista[i-count] >= lista[i+k-count]:
                        menor = True
                        count += 1
                        break
                    if menor == True:
                        lista.remove(lista[i-count+1])
                        menor = False
            if (pos[0]+velocity[0], pos[1]+velocity[1]) in box and Ghost.sinSalida(box, (pos[0]+velocity[0], pos[1]+velocity[1]), velocity, pospac) == False:
                break
        return velocity
    
    
    def naranja (box, pos, pospac):
        velocity = (0,0)
        #Si la distancia a pacman es menor que 3 casillas sigue como el rojo
        if Ghost.distance(pos, pospac) <= 3:
            return Ghost.rojo (box, pos, pospac)
        #Si no, hasta que la casilla elegida sea del camino y no lleve a sinSalida, elige una dirección al azar
        else:
            while True:
                while (velocity == (0,0) or velocity == (1,1) or velocity == (-1, -1) or
        		    velocity == (1,-1) or velocity == (-1,1)):
                    velocity = (random.choice([-1,0,1]), random.choice([-1,0,1]))
                if ((pos[0]+velocity[0], pos[1]+velocity[1]) in box and 
                    Ghost.sinSalida(box, (pos[0]+velocity[0], pos[1]+velocity[1]), velocity, pospac) == False):
                    break
            return velocity


    def rosa (box, pos, df, pospac, esquina):
        #Si pacman está en una de las casillas que hace esquina o intersección entre caminos
        if (pospac in [(2,2),(2,4),(2,6),(2,8),(2,10),(4,4),(4,6),(4,8),(6,2),(6,4),(6,6),(6,10),
        (8,8),(8,10),(10,8),(10,10),(12,2),(12,4),(12,6),(12,10),(14,4),(14,6),(14,8),(16,2),
        (16,4),(16,6),(16,8),(16,10)]):
            #El diccionario contiene las veces que ha ido en cada dirección al pasar por la casilla en la que está pacman
            dic = {
                (1,0):df.at[pospac, (1,0)], 
                (-1,0):df.at[pospac, (-1,0)], 
                (0,1):df.at[pospac, (0,1)], 
                (0,-1):df.at[pospac, (0,-1)]}
            if list(dic.values()) == [0,0,0,0]:
                velocity = (0,0)
                while True:
                    while (velocity == (0,0) or velocity == (1,1) or velocity == (-1, -1) or
                        velocity == (1,-1) or velocity == (-1,1)):
                        velocity = (random.choice([-1,0,1]), random.choice([-1,0,1]))
                    if ((pos[0]+velocity[0], pos[1]+velocity[1]) in box and 
                        Ghost.sinSalida(box, (pos[0]+velocity[0], pos[1]+velocity[1]), velocity, pospac) == False):
                        break
                return Ghost.rojo(box, pos, Ghost.casillaFinal(box, pospac, velocity))       
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
            return Ghost.rojo(box, pos, Ghost.casillaFinal(box, pospac, list(dic.keys())[list(dic.values()).index(lista[0])]))
        else:
            return Ghost.rojo(box, pos, esquina)


    def azul (box, pos, df, pospac, esquina):
        num = random.choice([0,1,2])
        if num == 0:
            return Ghost.rojo(box, pos, pospac)
        elif num == 1:
            return Ghost.naranja(box, pos, pospac)
        else:
            return Ghost.rosa(box, pos, df, pospac, esquina)


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
            if ((pos[0]+velocity[0], pos[1]+velocity[1]) in box and 
                Ghost.sinSalida(box, (pos[0]+velocity[0], pos[1]+velocity[1]), velocity, pospac) == False):
                break
        return velocity 


    def casillaFinal (box, pospac, dire):
        #Para rosa: calcula la casilla a la que tiene que ir (final del camino o intersección en dirección a la que va pacman)
        if pospac not in box:
            return (pospac[0] - dire[0], pospac[1] - dire[1])
        elif (((pospac[0] + dire[0], pospac[1] + dire[1]) in box) and 
            (((pospac[0] + dire[1], pospac[1] + dire[0]) in box) or 
             ((pospac[0] - dire[1], pospac[1] - dire[0]) in box))):
            return (pospac[0] + dire[0], pospac[1] + dire[1])
        else:
            return Ghost.casillaFinal(box, (pospac[0] + dire[0], pospac[1] + dire[1]), dire)
            
            
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

    def change_direction(self, newdirection):
        self.newdirection = newdirection
        self.direction = newdirection     

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