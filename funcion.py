import pygame
import random
from personajes import *


#bloques arriba

Blocks_arriba1 = pygame.sprite.Group()

def cuadro():
    blo= Bloque((750, 300), 50, 50, "img/bloque.jpg" )
    blo1= Triangulo_arriba((750, 345), 50,50, "img/triu2.png")
    Blocks_arriba1.add(blo)
    Blocks_arriba1.add(blo1)

def cuadro_di():
    Blocks_arriba1.draw(ventana)
    Blocks_arriba1.update()
    
Blocks_arriba2 = pygame.sprite.Group()

def cuadro1():
    bli= Bloque((750, 300), 50, 50, "img/bloque.jpg" )
    bli1= Bloque((800, 300), 50,50, "img/bloque.jpg")
    bli2= Triangulo_arriba((750, 345), 50,50, "img/triu2.png")
    bli3= Triangulo_arriba((800, 345), 50,50, "img/triu2.png")
    Blocks_arriba2.add(bli)
    Blocks_arriba2.add(bli1)
    Blocks_arriba2.add(bli2)
    Blocks_arriba2.add(bli3)

def cuadro_di2():
    Blocks_arriba2.draw(ventana)
    Blocks_arriba2.update()


#bloques suelo

Trian = pygame.sprite.Group()

def triin1():
    trin = Triangulo((0, 470), 50,50, "img/triu.png")
    Trian.add(trin)

def trii2n():
    trin1= Triangulo((500, 470), 50,50, "img/triu.png")
    trin2= Triangulo((450, 470), 50,50, "img/triu.png")
    Trian.add(trin1)
    Trian.add(trin2)

def tri_di():
    Trian.draw(ventana)
    Trian.update()


Trian2 = pygame.sprite.Group()

def trii(): 
    ti= Triangulo((800, 470), 50,50, "img/triu.png")
    ti1= Triangulo((750, 470), 50,50, "img/triu.png")
    ti2= Triangulo((700, 470), 50,50, "img/triu.png")
    Trian2.add(ti)
    Trian2.add(ti1)
    Trian2.add(ti2)
    
def trii2():
    tri= Bloque((500,450), 50,50, "img/bloque.jpg")
    tri1= Bloque((400,450), 50,50, "img/bloque.jpg")
    tri2= Bloque((400,400), 50,50, "img/bloque.jpg")
    tri3= Triangulo((400, 355), 50,50, "img/triu.png")
    Trian2.add(tri)
    Trian2.add(tri1)
    Trian2.add(tri2)
    Trian2.add(tri3)

def tri_di2():
    Trian2.draw(ventana)
    Trian2.update()

#cierra

Cierri = pygame.sprite.Group()

def cierin1():
    cierra1= Cierra((100, 460), 80,80, "img/cierra.png")
    Cierri.add(cierra1)


def dibujo():
    Cierri.draw(ventana)
    Cierri.update()


def cierras2():
    cina= Cierra((700, 460), 80,80, "img/cierra.png")
    cien2= Cierra((730, 460), 80,80, "img/cierra.png")
    Cierri.add(cina)
    Cierri.add(cien2)


"""cierin1()
cierras2()
cuadro()
cuadro1()
triin1()
trii2()
trii()
trii2()"""