import pygame, sys
import time as t
from pygame.locals import *
import numpy as np
import random as rnd

scale = 50
red = pygame.Color(255, 0, 0)
blue = pygame.Color(0, 255, 0)
yellow = pygame.Color(100, 100, 0)


class Axl:

    def __init__(self, positionX, positionY):
        self.positionX = positionX
        self.positionY = positionY
        # self.sprite = "images\\axl_complete_v2\\t%s.png"

    def Staticmove(self, screen, n):
        staticAxl = self.sprite % n
        axl = pygame.image.load(staticAxl)
        return axl

    def animate(self, screen, n):
        return screen.blit(self.Staticmove(screen, n), (scale * self.positionX, scale * self.positionY))

    def setX(self, positionX):
        self.positionX = positionX

    def setY(self, positionY):
        self.positionY = positionY

    def getY(self):
        return self.getY()

    def getX(self):
        return self.getX()


class Fighter:
    def __init__(self, postX, postY):
        self.postX = postX
        self.postY = postY
        self.kick=[0.17,0.17,0.17,0.17,0.17,0.15]
        self.punsh=[0.17,0.17,0.17,0.17,0.17,0.15]
        self.avanza=[0.17,0.17,0.17,0.17,0.17,0.15]
        self.retrocede=[0.17,0.17,0.17,0.17,0.17,0.15]
        self.agacha=[0.17,0.17,0.17,0.17,0.17,0.15]
        self.nada=[0.17,0.17,0.17,0.17,0.17,0.15]
        self.pushEsquivados=0
        self.punsh

    def crear(self, screen, parado, postX, postY):
        fighter_1 = (postX * scale, postY * scale, scale, 2 * scale + parado * scale)
        return pygame.draw.rect(screen, yellow, fighter_1)

    def setX(self, postX):
        self.postX = postX

    def setY(self, postY):
        self.postY = postY

    def getX(self):
        return self.postX

    def getY(self):
        return self.postY
    
    def reset(self,reseteando):
        probabilidadRestante=100
        for i in range(len(reseteando)-1):
            if(probabilidadRestante>=60):
                reseteando[i]=rnd.randint(0,40)/100
            else:
                if(probabilidadRestante>=40):
                    reseteando[i]=rnd.randint(0,40)/100
                else:
                    reseteando[i]=rnd.randint(0,probabilidadRestante)/100
            probabilidadRestante-=int(reseteando[i]*100)
        if(probabilidadRestante>0):
            reseteando[-1]=probabilidadRestante/100    
        else:
            reseteando=0.0
        return
    def resetAll(self):
        self.reset(self.kick)
        return
        



malla = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


def mallaW(window):
    for i in range(18):
        pygame.draw.line(window, red, (scale * i, 0), (scale * i, scale * 12))
        pygame.draw.line(window, red, (0, scale * i), (scale * 18, scale * i))

def Parejas(N):
        Aleatorio = rnd.sample(range(int(N/2),N),int(N/2))
        Pareja = {}
        for i in range(int(N/2)):
            Pareja[i] = Aleatorio[i]
            Pareja[Aleatorio[i]] = i
        return Pareja
def Seleccion(luchadores):
    print('---Seleccion----')
    Pareja = Parejas(len(luchadores[0].kick))
    print('Parejas',Pareja)
    for k,v in Pareja.items():
        if Idoneidad(luchadores[k]) >= Idoneidad(luchadores[v]):
            luchadores[v] = luchadores[k]
def Idoneidad(luchador):
    return (luchador.kick[0])

def Cruce(luchadores):
    print('-----Cruce ------')
    N=len(luchadores[0].kick)
    Pareja = Parejas(N)
    print('Parejas',Pareja)
    item = 0
    for k,v in Pareja.items():
        if item % 2 == 0:
            luchadores[k].kick,luchadores[v].kick=CruceIndividual(N,luchadores[k].kick,luchadores[v].kick)
            print(luchadores[k].kick)
        item = item+1

def CruceIndividual(N,movimiento1, movimiento2):
    Punto = rnd.randint(1,N-2)
    Hijo1 = []
    Hijo2 = []
    Padre1 = movimiento1
    Padre2 = movimiento2
    Hijo1.extend(Padre1[0:Punto])
    Hijo1.extend(Padre2[Punto:])
    Hijo2.extend(Padre2[0:Punto])
    Hijo2.extend(Padre1[Punto:])
    movimiento1 = Hijo1
    print(movimiento1)
    movimiento2 = Hijo2
    return movimiento1,movimiento2



def displayW(screen):
    black = (0, 0, 0)
    scene = pygame.image.load("images\\sol's stage\\layer1.png")
    scenerescale = pygame.transform.scale(scene, screen.get_size())
    postX1 = 4
    postY1 = 8
    postX2 = 9
    postY2 = 8
    parado = True
    fighters=[Fighter(postX1, postY2),Fighter(postX1, postY2),Fighter(postX1, postY2),Fighter(postX1, postY2),Fighter(postX1, postY2),Fighter(postX1, postY2)]
    for i in fighters:
        i.resetAll()
        print(i.kick)
    Seleccion(fighters)
    for i in fighters:
        print(i.kick)
    Cruce(fighters)
   # for i in fighters:
    #    print(i.kick)
    fighter_1 = Fighter(postX1, postY1)
    fighter_1.resetAll()
    fighter_2 = Fighter(postX1, postY2)
    while True:
        screen.fill(black)
        screen.blit(scenerescale, (0, 0))
        fighter_1.crear(screen, parado, postX1, postY1)
        fighter_2.crear(screen, parado, postX2, postY2)

        mallaW(screen)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()


def main():
    pygame.init()
    size = (scale * 18, scale * 12)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Guilty")

    displayW(screen)


if __name__ == '__main__':
    main()
