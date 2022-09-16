from PPlay.window import *
from PPlay.sprite import *

#Inicia recursos

janela = Window(800, 600)
janela.set_title("Pong")

teclado = Window.get_keyboard()

velx = 180
vely = 180

velp = 180

pont1 = 0
pont2 = 0

#Inicia GameObjects

bola = Sprite("images/bola.png", 1)
bola.x = (janela.width/2) - (bola.width/2)
bola.y = (janela.height/2) - (bola.height/2)

pad1 = Sprite("images/barra.png", 1)
pad1.x = 10
pad1.y = janela.height/2 - pad1.height/2

pad2 = Sprite("images/barra.png")
pad2.x = janela.width - pad1.width - 10
pad2.y = janela.height/2 - pad2.height/2

#GameLoop
while True:

    #Movimento Pad
    if pad1.y < 0:
        pad1.y = 0
    if pad1.y > janela.height - pad1.height:
        pad1.y = janela.height - pad1.height
    if pad2.y < 0:
        pad2.y = 0
    if pad2.y > janela.height - pad2.height:
        pad2.y = janela.height - pad2.height

    if teclado.key_pressed("w"):
        pad1.y -= velp * janela.delta_time()
    if teclado.key_pressed("s"):
        pad1.y += velp * janela.delta_time()
    if teclado.key_pressed("up"):
        pad2.y -= velp * janela.delta_time()
    if teclado.key_pressed("down"):
        pad2.y += velp * janela.delta_time()

    #Colisao pad/bola
    if bola.collided(pad1) and velx < 0:
        velx = -velx
    if bola.collided(pad2) and velx > 0:
        velx = -velx

    #Movimento Bola
    if bola.x > janela.width - bola.width and velx > 0:
        pont1 += 1
        velx = -velx
        bola.x = (janela.width / 2) - (bola.width / 2)
        bola.y = (janela.height / 2) - (bola.height / 2)
        pad1.y = janela.height / 2 - pad1.height / 2
        pad2.y = janela.height / 2 - pad2.height / 2
    if bola.x < 0 and velx < 0:
        pont2 += 1
        velx = -velx
        bola.x = (janela.width / 2) - (bola.width / 2)
        bola.y = (janela.height / 2) - (bola.height / 2)
        pad1.y = janela.height / 2 - pad1.height / 2
        pad2.y = janela.height / 2 - pad2.height / 2
    if bola.y > janela.height - bola.height and vely > 0:
        vely = -vely
    if bola.y < 0 and vely < 0:
        vely = -vely

    bola.x += velx * janela.delta_time()
    bola.y += vely * janela.delta_time()


    #Imprime na tela
    janela.set_background_color([0, 0, 0])
    bola.draw()
    pad1.draw()
    pad2.draw()
    janela.draw_text("%d - %d" % (pont1, pont2), janela.width/2, 10, 18, (255, 255, 255), "Arial", True, False)
    janela.update()