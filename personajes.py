import pygame 


ANCHO= 800
ALTO = 600

ventana = pygame.display.set_mode((ANCHO,ALTO))
pygame.display.set_caption("Geometry Dash") 
icon= pygame.image.load("img/iconn.png") 
pygame.display.set_icon(icon)


#clase de mi personaje

class Cuadro():
    def __init__(self, x, y ):
        self.x = x
        self.y = y
        self.ancho = 30
        self.direccion = 1
        self.alto = 30
        self.muerte = 0
        self.velocidad = 1
        self.imagen = pygame.image.load("img/cuadrado.jpeg")


    def draw(self):
        ventana.blit(self.imagen , (self.x , self.y))

    def Saltar(self,ventana):
        self.imagen2= pygame.image.load("img/cuadrado.jpeg")
        pygame.draw.rect(ventana, self.imagen, (self.x,self.y, 50,50))
        


    def update(self):
        self.x += self.velocidad * self.direccion
        if self.x + 55 == ANCHO / 2:
            self.direccion= 0



#ENEMIGOS!!
#clase de bloque 

def load_image(path, size=None):
    img = pygame.image.load("img/bloque.jpg")
    if size:
        img = pygame.transform.scale(img, size)
    return img


class Bloque(pygame.sprite.Sprite):
    def __init__(self, pos, width, height, img_path ):
        super().__init__()
        self.image = load_image(img_path, (width, height))
        self.rect = self.image.get_rect(topleft = pos)
        self.speed = 5
        self.activo = False


    def update(self):
        self.rect.x -= self.speed
        if self.rect.x == -795:
            self.rect.right= 800


#clase de triangulo

def load_imagen(path, size=None):
    img = pygame.image.load("img/triu.png")
    if size:
        img = pygame.transform.scale(img, size)
    return img

class Triangulo(Bloque):
    def __init__(self, pos, width, height, img_path):
        super().__init__(pos, width, height, img_path)
        self.image = load_imagen(img_path, (width, height))
        self.rect = self.image.get_rect(topleft = pos)
        self.speed = 5
        self.activo = False


    def update(self):

        self.rect.x -= self.speed
        if self.rect.x == -795:
            self.rect.right= 800


#clase de triangulo invertido

def load_imageen(path, size=None):
    img = pygame.image.load("img/triu2.png")
    if size:
        img = pygame.transform.scale(img, size)
    return img


class Triangulo_arriba(Triangulo):
    def __init__(self, pos, width, height, img_path):
        super().__init__(pos, width, height, img_path)
        self.image = load_imageen(img_path, (width, height))
        self.rect = self.image.get_rect(topleft = pos)
        self.speed = 5


    def update(self):
        self.rect.x -= self.speed
        if self.rect.x == -795:
            self.rect.right= 800


#clase de la cierra

def load_imagenn(path, size=None):
    img = pygame.image.load("img/cierra.png")
    if size:
        img = pygame.transform.scale(img, size)
    return img


class Cierra(Bloque):
    def __init__(self, pos, width, height, img_path):
        super().__init__(pos, width, height, img_path)
        self.image = load_imagenn(img_path, (width, height))
        self.rect = self.image.get_rect(topleft = pos)
        self.speed = 5


    def update(self):
        self.rect.x -= self.speed
        if self.rect.x == -795:
            self.rect.right= 800