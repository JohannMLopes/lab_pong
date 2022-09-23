from PPlay.window import *
from PPlay.sprite import *

# Inicia recursos

janela = Window(800, 600)
janela.set_title("Pong_Lab")

teclado = Window.get_keyboard()

b1x = 200
b1y = 200

b2x = 0
b2y = 0

velp = 180

pont1 = 0
pont2 = 0

# contador colisao da bola1
contb = 0

# Esconde as bolinhas

hideb1 = False
hideb2 = True

#Inicia GameObjects

bola1 = Sprite("images/bola.png")
bola1.x = (janela.width/2) - (bola1.width/2)
bola1.y = (janela.height/2) - (bola1.height/2)

bola2 = Sprite("images/bola.png")
bola2.x = (janela.width/2) - (bola2.width/2)
bola2.y = (janela.height/2) - (bola2.height/2)

pad1 = Sprite("images/barra.png")
pad1.x = 10
pad1.y = (janela.height/2) - (pad1.height/2)

pad2 = Sprite("images/barra.png")
pad2.x = janela.width - pad2.width - 10
pad2.y = (janela.height/2) - (pad2.height/2)

# GameLoop
while 1:

    # Verifica o estado das bolinhas
    if hideb1 and hideb2:
        hideb1 = False
        contb = 0
        b1x = 200
        b1y = 200
        b2x = 0
        b2y = 0

    # IA

    if bola1.x >= janela.width/2 and bola1.y <= pad2.y + pad2.height and b1x > 0:
        pad2.y -= velp * janela.delta_time()
    if bola1.x >= janela.width/2 and bola1.y >= pad2.y and b1x > 0:
        pad2.y += velp * janela.delta_time()

    if not hideb2:
        if bola2.x >= janela.width/2 and bola2.y <= pad2.y and b2x > 0:
            pad2.y -= velp * janela.delta_time()
        if bola2.x >= janela.width/2 and bola2.y >= pad2.y + pad2.height and b2x > 0:
            pad2.y += velp * janela.delta_time()

    if bola1.x < janela.width/2 and bola2.x < janela.width/2 and pad2.y > janela.height/2 - pad2.height/2:
        pad2.y -= velp * janela.delta_time()
    if bola1.x < janela.width/2 and bola2.x < janela.width/2 and pad2.y < janela.height/2 - pad2.height/2:
        pad2.y += velp * janela.delta_time()

    # Movimento pad
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


    #Colisão pad/bola

    if bola1.collided(pad1) and b1x < 0:
        b1x = -b1x
        if contb < 3:
            contb += 1
    if bola1.collided(pad2) and b1x > 0:
        b1x = -b1x
        if contb < 3:
            contb += 1

    if bola2.collided(pad1) and b2x < 0:
        b2x = -b2x
    if bola2.collided(pad2) and b2x > 0:
        b2x = -b2x

    # Movimento bola

    if bola1.x > janela.width - bola1.width and b1x > 0:
        pont1 += 1
        hideb1 = True
        b1x = 0
        b1y = 0
        bola1.x = (janela.width/2) - (bola1.width/2)
        bola1.y = (janela.height/2) - (bola1.height/2)

    if bola1.x < 0 and b1x < 0:
        pont2 += 1
        hideb1 = True
        b1x = 0
        b1y = 0
        bola1.x = (janela.width/2) - (bola1.width/2)
        bola1.y = (janela.height/2) - (bola1.height/2)

    if bola2.x > janela.width - bola2.width and b2x > 0:
        pont1 += 1
        hideb2 = True
        b2x = 0
        b2y = 0
        bola2.x = (janela.width/2) - (bola2.width/2)
        bola2.y = (janela.height/2) - (bola2.height/2)

    if bola2.x < 0 and b2x < 0:
        pont2 += 1
        hideb2 = True
        b2x = 0
        b2y = 0
        bola2.x = (janela.width/2) - (bola2.width/2)
        bola2.y = (janela.height/2) - (bola2.height/2)

    if bola1.y > janela.height - bola1.height and b1y > 0:
        b1y = -b1y

    if bola1.y < 0 and b1y < 0:
        b1y = -b1y

    if bola2.y > janela.height - bola2.height and b2y > 0:
        b2y = -b2y

    if bola2.y < 0 and b2y < 0:
        b2y = -b2y

    bola1.x += b1x * janela.delta_time()
    bola1.y += b1y * janela.delta_time()

    bola2.x += b2x * janela.delta_time()
    bola2.y += b2y * janela.delta_time()

    # Spawna a 2 bolinha
    if contb == 3:
        hideb2 = False
        b2x = 200
        b2y = 200
        contb += 1

    # Imprime na tela

    janela.set_background_color([0, 0, 0])
    if not hideb1:
        bola1.draw()
    if not hideb2:
        bola2.draw()
    pad1.draw()
    pad2.draw()
    janela.draw_text("%d - %d" % (pont1, pont2), janela.width/2, 10, 18, (255, 255, 255), "Arial", True, False)
    janela.update()