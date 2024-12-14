import pygame, sys
from menu import Button
from personajes import *
from funcion import *

pygame.init()
pygame.mixer.init()

pygame.display.set_caption("Menu")

x = 0
imagen = pygame.image.load("img/fondoo.jpg").convert() 

run = True
clock = pygame.time.Clock()

personaje = Cuadro(0,463)

def musica_menu(archivo):
    pygame.mixer.music.load(archivo)
    pygame.mixer.music.play(-1)
        

def musi_play(archi):
    pygame.mixer.music.load(archi)
    pygame.mixer.music.play(-1)


def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("img/font.ttf", size)

musica_menu("img/introo.mp3")
cierin1()
cierras2()
cuadro()
cuadro1()
triin1()
trii2()
trii()
trii2()

def play():
    while run:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_MENU.checkForInput(PLAY_MOUSE_POS):
                    musica_menu("img/introo.mp3")
                    main_menu()


        ventana.blit(pygame.transform.scale(imagen, (ANCHO, ALTO)),(x,0))

        PLAY_MENU = Button(image=None, pos=(60, 20), 
                            text_input="Menu", font=get_font(30), base_color="White", hovering_color="Green")

        PLAY_MENU.changeColor(PLAY_MOUSE_POS)
        PLAY_MENU.update(ventana)

        personaje.draw()
        personaje.update()

        cuadro_di()
        cuadro_di2()
        tri_di()
        tri_di2()
        dibujo()

        
        clock.tick(500)
        pygame.display.update()
    

def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        ventana.fill("white")

        OPTIONS_TEXT = get_font(45).render("vuelve a intentar", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(400, 150))
        ventana.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_MENU = Button(image=None, pos=(60, 20), 
                            text_input="Menu", font=get_font(30), base_color="Black", hovering_color="Green")

        OPTIONS_MENU.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_MENU.update(ventana)
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_MENU.checkForInput(OPTIONS_MOUSE_POS):
                    musica_menu("img/introo.mp3")
                    main_menu()

        pygame.display.update()


def main_menu():
    while True:
        
        ventana.blit(pygame.transform.scale(imagen, (ANCHO, ALTO)),(x,0))


        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(50).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(400, 50))

        img = pygame.image.load("img/button.png")
        imagen1= pygame.transform.scale(img, (200, 100))

        img2 = pygame.image.load("img/button.png")
        imagen2= pygame.transform.scale(img2, (200, 100))

        img3 = pygame.image.load("img/button.png")
        imagen3= pygame.transform.scale(img3, (200, 100))


        PLAY_BUTTON = Button(imagen1, pos=(400, 150), 
                            text_input="PLAY", font=get_font(30), base_color="#d7fcd4", hovering_color="Green")
        OPTIONS_BUTTON = Button(imagen2, pos=(400, 300), 
                            text_input="OPTIONS", font=get_font(20), base_color="#d7fcd4", hovering_color="Green")
        QUIT_BUTTON = Button(imagen3, pos=(400, 450), 
                            text_input="QUIT", font=get_font(30), base_color="#d7fcd4", hovering_color="Green")

        ventana.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(ventana)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    musi_play("img/ronda1.mp3")
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()



        clock.tick(500)
        pygame.display.update()

main_menu()