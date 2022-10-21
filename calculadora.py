from tkinter import *


janela = Tk()
janela.geometry("280x503")
janela.config(bg="white")
janela.attributes("-alpha", 0.9)
janela.resizable(False, False)

Color_body = "#FCFCFC"
Color_display = "#E3E3E3"



valor = ""
valor_  = StringVar()


# usado nas funções
tam1 = len(valor)+1
num = 1

tela = Frame(janela, width=280, height=312, background=Color_body)
tela.place(x=0, y=190)

display = Frame(janela, width=280, height=190, background=Color_display)
display.place(x=0,y=0)

tela_digito =Label(display, textvariable=valor_, background=Color_display, width=15, height=1, font=("arial 23 bold"), anchor="se",)
tela_digito.place(x=-7, y=80)

titulo = Label(janela, text='Calculator', background=Color_display, font=("italic 15 bold"))
titulo.place(x=90, y=0)

history_title = Label(janela, text='Historic', background=Color_display, font=("italic 10"))
history_title.place(x=0, y=165)


                                     ####arrumar isso ae
history = Label(janela, textvariable=valor_, width=12, height=1, justify=RIGHT, background=Color_display, fg="black", anchor="se", relief=FLAT, padx=0, pady=0)
history.place(x=190 , y=168)




def entrada_dados(tecla):
        global valor
        valor += tecla
        valor_.set(valor)
        print(valor_, valor)
       

def resultado():
        global valor
        valor_.set(eval(valor))
        valor =valor_.get()
        
def apagar_tudo():
        global valor

        valor = ""
        valor_.set(valor)
    
def apagar1():
    global  valor, num, tam1
    tam  = len(valor) - 1  
    valor = valor[:tam]
    valor_.set(valor)

    num  -=1

    if num==0:
        num = 1
    

def parentes():
    global valor, num
    

    if num % 2 !=0:
        valor += "("
        valor_.set(valor)
        
    else:
        valor += ")"
        valor_.set(valor)
    num +=  1
   
    
   
limpa = Button(janela, command=lambda: apagar_tudo(), text="C", font="arial 10 bold" ,width=7, height=3, justify=CENTER, relief=FLAT , overrelief=RIDGE, bg=Color_body)
limpa.place(x=0, y=193)

apaga = Button(janela, command=lambda: apagar1(), text="⮨", font="arial 10 bold" ,width=7, height=3, justify=CENTER, relief=FLAT, overrelief=RIDGE, bg=Color_body )
apaga.place(x=70, y=193)

porcentagem = Button(janela, command=lambda: entrada_dados("%"), text="%", font="arial 10 bold" ,width=7, height=3, justify=CENTER, relief=FLAT, overrelief=RIDGE, bg=Color_body)
porcentagem.place(x=140, y=193)

divisao = Button(janela,command=lambda: entrada_dados("/"), text="/", font="arial 10 bold" ,width=7, height=3, justify=CENTER, relief=FLAT, overrelief=RIDGE, bg=Color_body)
divisao.place(x=210, y=193)


numm_7 = Button(janela, command=lambda: entrada_dados("7"), text="7", font="arial 10 bold" ,width=7, height=3, justify=CENTER, relief=FLAT , overrelief=RIDGE, bg=Color_body)
numm_7.place(x=0, y=255)

num_8 = Button(janela, command=lambda: entrada_dados("8"), text="8", font="arial 10 bold" ,width=7, height=3, justify=CENTER, relief=FLAT , overrelief=RIDGE, bg=Color_body)
num_8.place(x=70, y=255)

num_9 = Button(janela, command=lambda: entrada_dados("9"), text="9", font="arial 10 bold" ,width=7, height=3, justify=CENTER, relief=FLAT , overrelief=RIDGE, bg=Color_body)
num_9.place(x=140, y=255)

tecla_multiplica = Button(janela, command=lambda: entrada_dados("*"), text="x", font="arial 10 bold" ,width=7, height=3, justify=CENTER, relief=FLAT , overrelief=RIDGE, bg=Color_body)
tecla_multiplica.place(x=210, y=255)


numm_4 = Button(janela, command=lambda: entrada_dados("4"), text="4", font="arial 10 bold" ,width=7, height=3, justify=CENTER, relief=FLAT , overrelief=RIDGE, bg=Color_body)
numm_4.place(x=0, y=317)

num_5 = Button(janela, command=lambda: entrada_dados("5"), text="5", font="arial 10 bold" ,width=7, height=3, justify=CENTER, relief=FLAT , overrelief=RIDGE, bg=Color_body)
num_5.place(x=70, y=317)

num_6 = Button(janela, command=lambda: entrada_dados("6"), text="6", font="arial 10 bold" ,width=7, height=3, justify=CENTER, relief=FLAT , overrelief=RIDGE, bg=Color_body)
num_6.place(x=140, y=317)

tecla_subtrai = Button(janela, command=lambda: entrada_dados("-"), text="-", font="arial 10 bold" ,width=7, height=3, justify=CENTER, relief=FLAT , overrelief=RIDGE, bg=Color_body)
tecla_subtrai.place(x=210, y=317)


numm_1 = Button(janela, command=lambda: entrada_dados("1"), text="1", font="arial 10 bold" ,width=7, height=3, justify=CENTER, relief=FLAT , overrelief=RIDGE, bg=Color_body)
numm_1.place(x=0, y=379)

num_2 = Button(janela, command=lambda: entrada_dados("2"), text="2", font="arial 10 bold" ,width=7, height=3, justify=CENTER, relief=FLAT , overrelief=RIDGE, bg=Color_body)
num_2.place(x=70, y=379)

num_3 = Button(janela, command=lambda: entrada_dados("3"), text="3", font="arial 10 bold" ,width=7, height=3, justify=CENTER, relief=FLAT , overrelief=RIDGE, bg=Color_body)
num_3.place(x=140, y=379)

tecla_soma = Button(janela, command=lambda: entrada_dados("+"), text="+", font="arial 10 bold" ,width=7, height=3, justify=CENTER, relief=FLAT , overrelief=RIDGE, bg=Color_body)
tecla_soma.place(x=210, y=379)


numm_1 = Button(janela, command=lambda: parentes(), text="()", font="arial 10 bold" ,width=7, height=3, justify=CENTER, relief=FLAT , overrelief=RIDGE, bg=Color_body)
numm_1.place(x=0, y=441)

num_0 = Button(janela, command=lambda: entrada_dados("0"), text="0", font="arial 10 bold" ,width=7, height=3, justify=CENTER, relief=FLAT , overrelief=RIDGE, bg=Color_body)
num_0.place(x=70, y=441)

tecla_ponto = Button(janela, command=lambda: entrada_dados("."), text=".", font="arial 10 bold" ,width=7, height=3, justify=CENTER, relief=FLAT , overrelief=RIDGE, bg=Color_body)
tecla_ponto.place(x=140, y=441)

tecla_resultado = Button(janela, command=lambda: resultado(), text="=", font="arial 10 bold" ,width=7, height=3, justify=CENTER, relief=FLAT , overrelief=RIDGE, bg=Color_body)
tecla_resultado.place(x=210, y=441)



janela.mainloop()