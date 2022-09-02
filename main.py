from PPlay.window import *

# I/O
janela = Window(800, 600)
janela.set_title("window")
janela.set_background_color([0, 0, 0])

# GameLoop
while True:
    
    janela.update()
