import pygame, sys
import time as t
from pygame.locals import *
import numpy as np

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
    parado = True
    fighter_1 = Fighter(postX1, postY1)
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
