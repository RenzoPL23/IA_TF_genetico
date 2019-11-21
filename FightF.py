import pygame, sys
import time as t
from pygame.locals import *
import numpy as np
import random as rnd
import time
import copy

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
        self.vidas = 4
        self.parado = 1
        self.patada = 2
        self.score = 0
        self.miss = 0
        self.acerto = 0
        self.conecto = False
        self.enemy = enemy
        self.postX = postX
        self.postY = postY
        self.kick=[0.17,0.17,0.17,0.17,0.17,0.15]
        self.punsh=[0.17,0.17,0.17,0.17,0.17,0.15]
        self.avanza=[0.17,0.17,0.17,0.17,0.17,0.15]
        self.retrocede=[0.17,0.17,0.17,0.17,0.17,0.15]
        self.agacha=[0.17,0.17,0.17,0.17,0.17,0.15]
        self.nada=[0.17,0.17,0.17,0.17,0.17,0.15]
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

    def kicks(self):
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
        if(abs(self.brazo[0] - fighterF2[0])<scale or abs(self.pierna[0] - fighterF2[0])<scale):
            self.vidas -= 1
            self.acerto += 10
            print(self.vidas)
            self.conecto = True
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
    
    def setXYVida(self,x,y,vida):
        self.postX=x
        self.postY=y
        self.vidas=vida
    
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
        self.reset(self.punsh)
        self.reset(self.avanza)
        self.reset(self.retrocede)
        self.reset(self.agacha)
        self.reset(self.nada)

        return
        


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
            luchadores[v] = copy.deepcopy(luchadores[k])
def Idoneidad(luchador):
    return (luchador.getScore())

def Cruce(luchadores):
    luchadoresAux=copy.deepcopy(luchadores.copy())
    print('-----Cruce ------')
    N=len(luchadores[0].kick)
    Pareja = Parejas(N)
    print('Parejas',Pareja)
    item = 0
    for k,v in Pareja.items():
        if item % 2 == 0:
            luchadores[k].kick,luchadores[v].kick=copy.deepcopy(CruceIndividual(N,luchadoresAux[k].kick,luchadoresAux[v].kick))
            luchadores[k].punsh,luchadores[v].punsh=copy.deepcopy(CruceIndividual(N,luchadoresAux[k].punsh,luchadoresAux[v].punsh))
            luchadores[k].avanza,luchadores[v].avanza=copy.deepcopy(CruceIndividual(N,luchadoresAux[k].avanza,luchadoresAux[v].avanza))
            luchadores[k].agacha,luchadores[v].agacha=copy.deepcopy(CruceIndividual(N,luchadoresAux[k].agacha,luchadoresAux[v].agacha))
            luchadores[k].retrocede,luchadores[v].retrocede=copy.deepcopy(CruceIndividual(N,luchadoresAux[k].retrocede,luchadoresAux[v].retrocede))
            luchadores[k].nada,luchadores[v].nada=copy.deepcopy(CruceIndividual(N,luchadoresAux[k].nada,luchadoresAux[v].nada))
        
        item = item+1
    return luchadores

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
    movimiento2 = Hijo2
    return movimiento1,movimiento2
    

def NuclearTrhone(luchadores):
    #afectados=rnd.randint(0,len(luchadores)-1)
    afectados=1
    for i in range(0,afectados):
        sujeto_prueba=rnd.randint(0,len(luchadores)-1)
        #acciones_afectadas=rnd.randint(0,5)
        acciones_afectadas=3
        if(acciones_afectadas==0):
            luchadores[sujeto_prueba].retrocede=mutate(luchadores[i].retrocede)
        elif(acciones_afectadas==1):
            luchadores[sujeto_prueba].avanza=mutate(luchadores[i].avanza)
        elif(acciones_afectadas==2):
            luchadores[sujeto_prueba].punsh=mutate(luchadores[i].punsh)
        elif(acciones_afectadas==3):
            luchadores[sujeto_prueba].kick=mutate(luchadores[i].kick)
            print(luchadores[sujeto_prueba].kick)
        elif(acciones_afectadas==4):
            luchadores[sujeto_prueba].agacha=mutate(luchadores[i].agacha)
        elif(acciones_afectadas==5):
            luchadores[sujeto_prueba].nada=mutate(luchadores[i].nada)
    return luchadores


def mutate(mutando):
    print("hi")
    print(mutando)
    intercambio1=rnd.randint(0,len(mutando)-1)
    intercambio2=rnd.randint(0,len(mutando)-1)
    while(intercambio1==intercambio2):
        intercambio2=rnd.randint(0,len(mutando)-1)
    sum_probabilidades=mutando[intercambio1]*100
    sum_probabilidades+=mutando[intercambio2]*100
    mutando[intercambio1]=rnd.randint(0,sum_probabilidades)/100
    mutando[intercambio2]=(sum_probabilidades-mutando[intercambio1]*100)/100
    return mutando


    


def escena0(fighter_1,fighter_2):
        fighter_1.punch()
        fighter_1.kicks()
        fighter_1.PararseEn()

        fighter_2.punch()
        fighter_2.kicks()
        fighter_2.PararseEn()

        

        if(fighter_1.getX()<=0):
            fighter_1.setX(0)
        elif(fighter_1.getX()>17):
            fighter_1.setX(17)

        if(fighter_2.getX()<=0):
            fighter_2.setX(0)
        elif(fighter_2.getX()>17):
            fighter_2.setX(17)

        if(fighter_1.getX()>fighter_2.getX()-2):
            fighter_1.setX(fighter_2.getX()-2)

        fighter_1.Colision(fighter_2.fighter)
        fighter_2.Colision(fighter_1.fighter)
        
        
        
def movimientosPantalla(fighter_1,fighter_2):
    accion=5
    for event in pygame.event.get():
        
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == K_LEFT:
                fighter_1.setX(fighter_1.getX()-1)

                respuestas = [0, 1, 2, 3, 4, 5 ]
                accion=np.random.choice(respuestas, 1, fighter_1.retrocede)


            elif event.key == K_RIGHT:
                fighter_1.setX(fighter_1.getX()+1)

                respuestas = [0, 1, 2, 3, 4, 5 ]
                accion=np.random.choice(respuestas, 1, fighter_1.avanza)

            elif event.key == K_a:
                if(fighter_1.conecto is not True):
                    fighter_1.setMiss(fighter_1.getMiss()+6)
                fighter_1.setMovimientoG()

                respuestas = [0, 1, 2, 3, 4, 5 ]
                accion=np.random.choice(respuestas, 1, fighter_1.retrocede)

            elif event.key == K_s:
                print(fighter_2.vidas)
                if (fighter_1.conecto is not True):
                    fighter_1.setMiss(fighter_1.getMiss() + 6)
                fighter_1.setMovimientoP()

                respuestas = [0, 1, 2, 3, 4, 5 ]
                accion=np.random.choice(respuestas, 1, fighter_1.retrocede)

            elif event.key == K_DOWN:
                fighter_1.Agacharse()

                respuestas = [0, 1, 2, 3, 4, 5 ]
                accion=np.random.choice(respuestas, 1, fighter_1.retrocede)

    if(accion==0):
        fighter_2.setX(fighter_2.getX()-1)
        accion=5            
    elif(accion==1):
        fighter_2.setX(fighter_2.getX()+1)
        accion=5 
    elif(accion==2):
        fighter_2.setMovimientoG()
        if (fighter_2.conecto is not True):
                    fighter_2.setMiss(fighter_2.getMiss() + 6)
        accion=5 
    elif(accion==3):
        fighter_2.setMovimientoP()
        if (fighter_2.conecto is not True):
                    fighter_2.setMiss(fighter_2.getMiss() + 6)
        accion=5 
    elif(accion==4):
        fighter_2.Agacharse()
        accion=5 

def round(fighter_1,fighter_2,postX1,postY1,postX2,postY2):
    if(fighter_1.vidas==0):
        if(fighter_2.vidas==0):
            #empate
            print(0)
            fighter_1.setXYVida(postX1,postY1,4)
            fighter_2.setXYVida(postX2,postY2,4)
            #time.sleep(30)
            return 0
        else:
            #perdiste
            print(-1)
            fighter_1.setXYVida(postX1,postY1,4)
            fighter_2.setXYVida(postX2,postY2,4)
            fighter_2.acerto+=5
            #time.sleep(30)
            return -1
    elif(fighter_2.vidas==0):
        #ganaste:
        print(1)
        fighter_1.setXYVida(postX1,postY1,4)
        fighter_2.setXYVida(postX2,postY2,4)
        fighter_2.acerto-=5
        #time.sleep(30)
        return 1    


def displayW(screen):
    black = (0, 0, 0)
    scene = pygame.image.load("images\\sol's stage\\layer1.png")
    scenerescale = pygame.transform.scale(scene, screen.get_size())
    postX1 = 4
    postY1 = 8
    postX2 = 12
    postY2 = 8
    fighter_1 = Fighter(postX1, postY1,1)
    fighter_2 = Fighter(postX2, postY2,-1)

    fighters=[Fighter(postX2, postY2,-1),Fighter(postX2, postY2,-1),Fighter(postX2, postY2,-1),Fighter(postX2, postY2,-1),Fighter(postX2, postY2,-1),Fighter(postX2, postY2,-1)]
    
    ronda=0
    while True:
        fighter_2=fighters[0]
        screen.fill(black)
        screen.blit(scenerescale, (0, 0))

        fighter_1.crear(screen)
        fighters[0].crear(screen)
        mallaW(screen)

        escena0(fighter_1,fighters[0])

        movimientosPantalla(fighter_1,fighters[0])

        if(round(fighter_1,fighters[0],postX1,postY1,postX2,postY2)!=None):
            ronda+=1            

        if(ronda==5):
            for i in fighters:
                i.resetAll()
                print(i.kick)

            Seleccion(fighters)
            for i in fighters:
                print(i.kick)
            fighters = Cruce(fighters)
            for i in fighters:
                print(i.kick)
            ronda=0
            print("----Mutar----")
            fighters = NuclearTrhone(fighters)
            for i in fighters:
                print(i.kick)



        pygame.display.update()


def main():
    pygame.init()
    size = (scale * 18, scale * 12)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Guilty")

    displayW(screen)


if __name__ == '__main__':
    main()
