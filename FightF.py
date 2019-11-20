import pygame, sys
import time as t
from pygame.locals import *
import numpy as np

scale = 50
red = pygame.Color(255, 0, 0)
blue = pygame.Color(0, 255, 0)
yellow = pygame.Color(100, 100, 0)

class Fighter:
    cont = 0
    def __init__(self, postX, postY, enemy):

        self.progreso_golpe = 0.5
        self.progreso_patada = 0.5
        self.movimientoG = 0.0
        self.movimientoP = 0.0
        self.vidas = 2
        self.parado = 1
        self.patada = 2
        self.score = 0
        self.miss = 0
        self.acerto = 0
        self.conecto = False
        self.enemy = enemy
        self.postX = postX
        self.postY = postY
        self.progreso_agacharse=0.0

    def crear(self, screen):
        self.brazo = ((self.postX + self.enemy*self.progreso_golpe) * scale, self.postY * scale,  scale, scale)
        self.pierna =((self.postX + self.enemy*self.progreso_patada) * scale, (self.postY+self.patada) * scale, scale, scale)
        self.fighter = (self.postX * scale, self.postY * scale, scale, 2 * scale + self.parado * scale)
        pygame.draw.rect(screen, blue, self.brazo)
        pygame.draw.rect(screen, red, self.pierna)
        pygame.draw.rect(screen, yellow, self.fighter)

    def punch(self):
        self.progreso_golpe += self.movimientoG
        if (self.progreso_golpe <= 0.5):
            self.movimientoG = 0.0
        if (self.progreso_golpe >= 1.2):
            self.movimientoG = self.movimientoG * -1

    def kick(self):
        self.progreso_patada +=self.movimientoP
        if (self.progreso_patada<= 0.5):
            self.movimientoP = 0.0
        if(self.progreso_patada>= 1.2):
            self.movimientoP = self.movimientoP * -1
    def Agacharse(self):
        self.setY(9)
        self.patada = 1
        self.setParado(0)
        self.progreso_agacharse=1.0
    def Pararse(self):
        self.setY(8)
        self.patada = 2
        self.setParado(1)

    def PararseEn(self):
        if(self.progreso_agacharse>0.0):
            self.progreso_agacharse-=0.01
        if(self.progreso_agacharse<0.0):
            self.Pararse()
            self.progreso_agacharse=0

    def Colision(self,fighterF2):
        if(self.brazo[0]+scale == fighterF2[0] or self.pierna[0] == fighterF2[0]):
            self.vidas -= 1
            self.acerto += 10
            print(self.vidas)
            self.conecto = True
        if( self.vidas<0):
            print("game over")
            print(self.getScore())
        self.conecto = False

    def setMiss(self, miss):
        self.miss = miss

    def getMiss(self):
        return self.miss

    def getScore(self):
        return self.acerto - self.miss

    def setX(self, postX):
        self.postX = postX

    def setY(self, postY):
        self.postY = postY

    def getX(self):
        return self.postX

    def getY(self):
        return self.postY

    def setProgreso_golpe(self,golpe):
        self.progreso_golpe = golpe

    def getProgreso_golpe(self):
        return self.progreso_golpe

    def setMovimientoG(self):
        self.movimientoG = 0.1

    def setMovimientoP(self):
        self.movimientoP = 0.1

    def setParado(self,parado):
        self.parado=parado

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



def displayW(screen):
    black = (0, 0, 0)
    scene = pygame.image.load("images\\sol's stage\\layer1.png")
    scenerescale = pygame.transform.scale(scene, screen.get_size())
    postX1 = 4
    postY1 = 8
    postX2 = 9
    postY2 = 8
    fighter_1 = Fighter(postX1, postY1,1)
    fighter_2 = Fighter(postX2, postY2,-1)

    while True:
        screen.fill(black)
        screen.blit(scenerescale, (0, 0))
        fighter_1.crear(screen)
        fighter_2.crear(screen)
        fighter_1.punch()
        fighter_1.kick()
        fighter_1.PararseEn()
        mallaW(screen)
        if(fighter_1.getX()<=0):
            fighter_1.setX(0)
        elif(fighter_1.getX()>17):
            fighter_1.setX(17)
        if(fighter_1.getX()>fighter_2.getX()-2):
            fighter_1.setX(fighter_2.getX()-2)
        fighter_1.Colision(fighter_2.fighter)
        print(fighter_1.getScore())

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == K_LEFT:
                    fighter_1.setX(fighter_1.getX()-1)
                if event.key == K_RIGHT:
                    fighter_1.setX(fighter_1.getX()+1)
                if event.key == K_a:
                    if(fighter_1.conecto is not True):
                        fighter_1.setMiss(fighter_1.getMiss()+6)
                    fighter_1.setMovimientoG()
                if event.key == K_s:
                    if (fighter_1.conecto is not True):
                        fighter_1.setMiss(fighter_1.getMiss() + 6)
                    fighter_1.setMovimientoP()
                if event.key == K_DOWN:
                    fighter_1.Agacharse()


        pygame.display.update()


def main():
    pygame.init()
    size = (scale * 18, scale * 12)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Guilty")

    displayW(screen)


if __name__ == '__main__':
    main()
