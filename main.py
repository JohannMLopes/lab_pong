from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *

# Inicia recursos

janela = Window(800, 600)
janela.set_title("Pong_Lab")

teclado = Window.get_keyboard()

bx = 200
by = 200

velp = 180

pont1 = 0
pont2 = 0

isGamePaused = True

# Inicia GameObjects

fundo = GameImage("images/fundo.png")

bola = Sprite("images/bola.png")
bola.x = (janela.width/2) - (bola.width/2)
bola.y = (janela.height/2) - (bola.height/2)

pad1 = Sprite("images/barra.png")
pad1.x = 10
pad1.y = (janela.height/2) - (pad1.height/2)

pad2 = Sprite("images/barra.png")
pad2.x = janela.width - pad2.width - 10
pad2.y = (janela.height/2) - (pad2.height/2)

# GameLoop
while 1:

    # Inicio de jogo

    if isGamePaused:
        bx = 0
        by = 0
        velp = 0
        if teclado.key_pressed("space"):
            isGamePaused = False
            bx = 200
            by = 200
            velp = 180

    # IA

    if bola.x >= janela.width/2 and bx > 0:
        if bola.y <= pad2.y + pad2.height:
            pad2.y -= velp * janela.delta_time()
        elif bola.y >= pad2.y:
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

    # Colisão pad/bola

    if bola.collided(pad1) or bola.collided(pad2):
        if bola.collided(pad1) and bx < 0:
            bx = -bx
        elif bola.collided(pad2) and bx > 0:
            bx = -bx

    # Movimento bola

    if bola.x > janela.width - bola.width or bola.x < 0:
        if bola.x > janela.width - bola.width and bx > 0:
            pont1 += 1
            pad1 = Sprite("images/barra.png")
            pad2 = Sprite("images/barra_metade.png")
            bx = -bx
            bola.x = (janela.width/2) - (bola.width/2)
            bola.y = (janela.height/2) - (bola.height/2)
            pad1.x = 10
            pad1.y = (janela.height / 2) - (pad1.height / 2)
            pad2.x = janela.width - pad2.width - 10
            pad2.y = (janela.height / 2) - (pad2.height / 2)
            isGamePaused = True
        elif bola.x < 0 and bx < 0:
            pont2 += 1
            pad2 = Sprite("images/barra.png")
            pad1 = Sprite("images/barra_metade.png")
            bx = -bx
            bola.x = (janela.width/2) - (bola.width/2)
            bola.y = (janela.height/2) - (bola.height/2)
            pad1.x = 10
            pad1.y = (janela.height / 2) - (pad1.height / 2)
            pad2.x = janela.width - pad2.width - 10
            pad2.y = (janela.height / 2) - (pad2.height / 2)
            isGamePaused = True

    if bola.y > janela.height - bola.height or bola.y < 0:
        if bola.y > janela.height - bola.height and by > 0:
            by = -by
        elif bola.y < 0 and by < 0:
            by = -by

    bola.x += bx * janela.delta_time()
    bola.y += by * janela.delta_time()

    # Imprime na tela

    fundo.draw()
    bola.draw()
    pad1.draw()
    pad2.draw()
    janela.draw_text("%d - %d" % (pont1, pont2), janela.width/2, 10, 18, (255, 0, 0), "Arial", True, False)
    janela.update()
