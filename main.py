# Importações

from tkinter import Tk, Frame, Button
from tkinter import ttk
from Style import cores

# Janela principal
janela = Tk()
janela.title("Calculadora") # Define o titulo da janela
janela.geometry("250x300")  # Define largura e comprimento respectivamente
janela.config(bg = cores.fundo)

# Frame - Display
frame_tela = Frame(janela,width=300,height=60,bg=cores.cor5)
frame_tela.grid(row=0, column=0) # posição do frame

frame_corpo = Frame(janela,width=300,height=350,bg=cores.fundo)
frame_corpo.grid(row=1, column=0) # posição do frame

# Create Widgets
b1 = Button(frame_corpo, text="C", width=11, height=2,bg=cores.cor3)
b1.place(x=0,y=0)
b2 = Button(frame_corpo, text="%",width=5, height=2,bg=cores.cor3)
b2.place(x=87,y=0)
b3 = Button(frame_corpo, text=)
b4 = Button()
b5 = Button()
b6 = Button()
b7 = Button()
b8 = Button()
b9 = Button()
b10 = Button()


janela.mainloop() # Executa a janela
