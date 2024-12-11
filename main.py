# Importações
from tkinter import Tk, Frame, Button, Label
from tkinter.constants import RAISED, RIDGE
from Style import cores

# Janela principal
janela = Tk()
janela.title("Calculadora") # Define o título da janela
janela.geometry("235x310")  # Define largura e comprimento, respectivamente
janela.config(bg=cores.fundo)

# Frame - Display
frame_tela = Frame(janela, width=235, height=60, bg=cores.cor5)
frame_tela.grid(row=0, column=0) # Posição do frame

frame_corpo = Frame(janela, width=235, height=268, bg=cores.fundo)
frame_corpo.grid(row=1, column=0) # Posição do frame

# Variável que armazena o valor exibido no display
v_display = ""

# Label para o display
display = Label(
    frame_tela,
    text="123456789",             # Valor inicial do display (vazio)
    width=15,            # Largura do display
    height=2,            # Altura do display
    padx=7,              # Espaçamento interno na horizontal
    relief="flat",       # Sem borda
    anchor="e",          # Alinha o texto à direita
    justify="right",     # Justifica o texto à direita
    font=("ivy", 18, "bold"),  # Fonte do texto
    bg=cores.cor5,       # Cor de fundo do display
    fg=cores.cor1        # Cor do texto
)
display.place(x=0, y=0)  # Posiciona o display no frame



def atualizar_display(valor):
    global valor_display
    valor_display += valor  # Adiciona o novo valor ao texto atual

# Criação de Widgets
b1 = Button(
    frame_corpo,
    text="C",
    width=11, # Largura
    height=2, # Altura
    bg=cores.cor3, # Cor de fundo
    fg=cores.cor1,  # Cor do texto
    font=("ivy", 13, "bold"), # Fonte do texto
    relief=RAISED, # Borda em relevo
    overrelief=RIDGE, # fundo ao passar mouse
    activebackground=cores.cor6, # Fundo ao clicar
    activeforeground=cores.cor1  # Texto ao clicar



)
b1.place(x=0,y=0)

b2 = Button(
    frame_corpo,
    text="%",
    width=5,
    height=2,
    bg=cores.cor3,
    font = ("ivy", 13, "bold"),  # Fonte do texto
    relief = RAISED,  # Borda em relevo
    overrelief = RIDGE,  # fundo ao passar mouse
    activebackground = cores.cor6,  # Fundo ao clicar
    activeforeground = cores.cor1,  # Texto ao clicar
    command=lambda: atualizar_display("7")
)
b2.place(x=118,y=0)

b3 = Button(
    frame_corpo,
    text="/",
    width=5,
    height=2,
    bg=cores.cor4,
    fg=cores.cor2,
    font = ("ivy", 13, "bold"),  # Fonte do texto
    relief = RAISED,  # Borda em relevo
    overrelief = RIDGE,  # fundo ao passar mouse
    activebackground = cores.cor6,  # Fundo ao clicar
    activeforeground = cores.cor1  # Texto ao clicar

)
b3.place(x=177,y=0)

b4 = Button(
    frame_corpo,
    text="7",
    width=5,
    height=2,
    bg=cores.cor3,
    font = ("ivy", 13, "bold"),  # Fonte do texto
    relief = RAISED,  # Borda em relevo
    overrelief = RIDGE,  # fundo ao passar mouse
    activebackground = cores.cor6,  # Fundo ao clicar
    activeforeground = cores.cor1  # Texto ao clicar

)
b4.place(x=0,y=51)

b5 = Button(
    frame_corpo,
    text="8",
    width=5,
    height=2,
    bg=cores.cor3,
    font = ("ivy", 13, "bold"),  # Fonte do texto
    relief = RAISED,  # Borda em relevo
    overrelief = RIDGE,  # fundo ao passar mouse
    activebackground = cores.cor6,  # Fundo ao clicar
    activeforeground = cores.cor1  # Texto ao clicar

)
b5.place(x=59,y=51)

b6 = Button(
    frame_corpo,
    text="9",
    width=5,
    height=2,
    bg=cores.cor3,
    font = ("ivy", 13, "bold"),  # Fonte do texto
    relief = RAISED,  # Borda em relevo
    overrelief = RIDGE,  # fundo ao passar mouse
    activebackground = cores.cor6,  # Fundo ao clicar
    activeforeground = cores.cor1  # Texto ao clicar

)
b6.place(x=118,y=51)

b7 =Button(
    frame_corpo,
    text="*",
    width=5,
    height=2,
    bg=cores.cor4,
    font = ("ivy", 13, "bold"),  # Fonte do texto
    relief = RAISED,  # Borda em relevo
    overrelief = RIDGE,  # fundo ao passar mouse
    activebackground = cores.cor6,  # Fundo ao clicar
    activeforeground = cores.cor1  # Texto ao clicar

)
b7.place(x=177,y=51)

b8 =Button(
    frame_corpo,
    text="4",
    width=5,
    height=2,
    bg=cores.cor3,
    font = ("ivy", 13, "bold"),  # Fonte do texto
    relief = RAISED,  # Borda em relevo
    overrelief = RIDGE,  # fundo ao passar mouse
    activebackground = cores.cor6,  # Fundo ao clicar
    activeforeground = cores.cor1  # Texto ao clicar

)
b8.place(x=0,y=102)

b9 = Button(
    frame_corpo,
    text="5",
    width=5,
    height=2,
    bg=cores.cor3,
    font = ("ivy", 13, "bold"),  # Fonte do texto
    relief = RAISED,  # Borda em relevo
    overrelief = RIDGE,  # fundo ao passar mouse
    activebackground = cores.cor6,  # Fundo ao clicar
    activeforeground = cores.cor1  # Texto ao clicar

)
b9.place(x=59,y=102)

b10 = Button(
    frame_corpo,
    text="6",
    width=5,
    height=2,
    bg=cores.cor3,
    font = ("ivy", 13, "bold"),  # Fonte do texto
    relief = RAISED,  # Borda em relevo
    overrelief = RIDGE,  # fundo ao passar mouse
    activebackground = cores.cor6,  # Fundo ao clicar
    activeforeground = cores.cor1  # Texto ao clicar

)
b10.place(x=118,y=102)

b11 =Button(
    frame_corpo,
    text="-",
    width=5,
    height=2,
    bg=cores.cor4,
    font = ("ivy", 13, "bold"),  # Fonte do texto
    relief = RAISED,  # Borda em relevo
    overrelief = RIDGE,  # fundo ao passar mouse
    activebackground = cores.cor6,  # Fundo ao clicar
    activeforeground = cores.cor1  # Texto ao clicar

)
b11.place(x=177,y=102)

b12 = Button(
    frame_corpo,
    text="1",
    width=5,
    height=2,
    bg=cores.cor3,
    font = ("ivy", 13, "bold"),  # Fonte do texto
    relief = RAISED,  # Borda em relevo
    overrelief = RIDGE,  # fundo ao passar mouse
    activebackground = cores.cor6,  # Fundo ao clicar
    activeforeground = cores.cor1  # Texto ao clicar

)
b12.place(x=0,y=153)

b13 =Button(
    frame_corpo,
    text="2",
    width=5,
    height=2,
    bg=cores.cor3,
    font = ("ivy", 13, "bold"),  # Fonte do texto
    relief = RAISED,  # Borda em relevo
    overrelief = RIDGE,  # fundo ao passar mouse
    activebackground = cores.cor6,  # Fundo ao clicar
    activeforeground = cores.cor1  # Texto ao clicar

)
b13.place(x=59,y=153)

b14 = Button(
    frame_corpo,
    text="3",
    width=5,
    height=2,
    bg=cores.cor3,
    font = ("ivy", 13, "bold"),  # Fonte do texto
    relief = RAISED,  # Borda em relevo
    overrelief = RIDGE,  # fundo ao passar mouse
    activebackground = cores.cor6,  # Fundo ao clicar
    activeforeground = cores.cor1  # Texto ao clicar

)
b14.place(x=118,y=153)

b15= Button(
    frame_corpo,
    text="+",
    width=5,
    height=2,
    bg=cores.cor4,
    font = ("ivy", 13, "bold"),  # Fonte do texto
    relief = RAISED,  # Borda em relevo
    overrelief = RIDGE,  # fundo ao passar mouse
    activebackground = cores.cor6,  # Fundo ao clicar
    activeforeground = cores.cor1  # Texto ao clicar

)
b15.place(x=177,y=153)

b16= Button(
    frame_corpo,
    text="0",
    width=11, # Largura
    height=2, # Altura
    bg=cores.cor3, # Cor de fundo
    fg=cores.cor1,  # Cor do texto
    font=("ivy", 13, "bold"), # Fonte do texto
    relief=RAISED, # Borda em relevo
    overrelief=RIDGE, # fundo ao passar mouse
    activebackground=cores.cor6, # Fundo ao clicar
    activeforeground=cores.cor1  # Texto ao clicar

)
b16.place(x=0,y=204)

b17=Button(
    frame_corpo,
    text=".",
    width=5,
    height=2,
    bg=cores.cor3,
    font = ("ivy", 13, "bold"),  # Fonte do texto
    relief = RAISED,  # Borda em relevo
    overrelief = RIDGE,  # fundo ao passar mouse
    activebackground = cores.cor6,  # Fundo ao clicar
    activeforeground = cores.cor1  # Texto ao clicar

)
b17.place(x=118,y=204)

b18=Button(
    frame_corpo,
    text="=",
    width=5,
    height=2,
    bg=cores.cor4,
    font = ("ivy", 13, "bold"),  # Fonte do texto
    relief = RAISED,  # Borda em relevo
    overrelief = RIDGE,  # fundo ao passar mouse
    activebackground = cores.cor6,  # Fundo ao clicar
    activeforeground = cores.cor1  # Texto ao clicar

)
b18.place(x=177,y=204)


janela.mainloop() # Executa a janela
