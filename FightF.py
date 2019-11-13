import pygame, sys
import time as t
from pygame.locals import *

scale = 50
class Axl():

    def __init__(self, positionX, positionY):
        self.positionX = positionX
        self.positionY = positionY
        self.sprite = "images\\axl_complete_v2\\t%s.png"
    def Staticmove(self, screen, n):
        staticAxl = self.sprite % n
        axl = pygame.image.load(staticAxl)
        return axl
    def animate(self, screen, n):
        return screen.blit(self.Staticmove(screen, n), (scale * self.positionX, scale * self.positionY))
    def setX(self,positionX):
        self.positionX = positionX
    def setY(self,positionY):
        self.positionY = positionY
    def getY(self):
        return self.getY()
    def getX(self):
        return self.getX()



def displayW(screen):
    black = (0, 0, 0)
    scene = pygame.image.load("images\\sol's stage\\layer1.png")
    nSpriteAxl = 0
    axlY = 6
    axlX = 12
    player1 = Axl(axlX, axlY)
    static = True
    scenerescale = pygame.transform.scale(scene, screen.get_size())
    while True:
        screen.fill(black)
        screen.blit(scenerescale, (0, 0))

        player1.animate(screen, nSpriteAxl)
        if static:
            if nSpriteAxl > 11:
                nSpriteAxl = 0
            else:
                t.sleep(0.05)
                nSpriteAxl += 1
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYUP:
                if event.key == K_RIGHT or event.key == K_LEFT or event.key == K_UP:
                    static = True
                    nSpriteAxl = 0
                    player1.setY(6)

            elif event.type == pygame.KEYDOWN:
                static = False
                if event.key == K_RIGHT:
                    nSpriteAxl = 17
                elif event.key == K_LEFT:
                    nSpriteAxl = 25
                elif event.key == K_UP:
                    nSpriteAxl = 44
                elif event.key == K_a:
                    nSpriteAxl = 63

        key_press = pygame.key.get_pressed()
        if  key_press[K_RIGHT]:
            if nSpriteAxl >23:
                nSpriteAxl = 17
            else:
                t.sleep(0.05)
                axlX += 0.5
                player1.setX(axlX)
                nSpriteAxl += 1
        elif key_press[K_LEFT]:
            if nSpriteAxl >31:
                nSpriteAxl = 25
            else:
                t.sleep(0.05)
                axlX -= 0.5
                player1.setX(axlX)
                nSpriteAxl += 1
        elif key_press[K_UP]:
            cont = 1
            if nSpriteAxl > 50:
                nSpriteAxl = 44
            else:
                t.sleep(0.05)
                player1.setY(axlY-1)
                nSpriteAxl += cont
        elif key_press[K_a]:
            if nSpriteAxl> 68:
                nSpriteAxl = 63
            else:
                t.sleep(0.05)
                player1.setX(axlX-3)
                nSpriteAxl += 1


        pygame.display.update()

def main():
    pygame.init()
    size = (scale*18, scale*12)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Guilty")
    displayW(screen)

if __name__ == '__main__':
    main()