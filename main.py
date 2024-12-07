# Importa biblioteca tkinter
from tkinter import *
from tkinter import ttk

#cores

cor1 = "#000000" # Black/Preto
cor2 = "#f7f5f5" # White/Branco
cor3 = "#858c87" # Grey/Cinza
cor4 = "#d4820f" # Orange/Laranja
cor5 = "#0d50bd" # Azul

fundo = "#202120" # Dark-light

# Janela principal
janela = Tk()
janela.title("Calculadora") # Define o titulo da janela
janela.geometry("300x400")  # Define largura e comprimento respectivamente
janela.config(bg=fundo)

# Frame - Display
frame_tela = Frame(janela,width=300,height=50)
frame_tela.grid(row=0, column=0) # posição do frame

# Frame - botões
frame_corpo = Frame(janela,width=300,height=350)
frame_corpo.grid(row=1, column=0) # posição do frame

janela.mainloop() # Executa a janela
