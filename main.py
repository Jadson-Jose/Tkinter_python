from tkinter import *
from tkinter import ttk

root = Tk()
root.title("App Teste")

# dimensões da janela
largura = 500
altura = 300

# resolução do sistema
largura_screen = root.winfo_screenwidth()
altura_screen = root.winfo_screenheight()

# posição da janela
posx = largura_screen/2 - largura/2
posy = altura_screen/2 - altura/2

# definir a geometria
root.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))

label_1 = Label(root, 
                text="Este é o label um\n Frase dois",
                font="Arial 20",
                borderwidth=5,
                relief="raised").pack()




btn = Button(root, text="Executar")


# pack
btn.pack()

root.mainloop()
