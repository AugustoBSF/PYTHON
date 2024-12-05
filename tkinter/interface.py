from tkinter import *
from tkinter import messagebox;


janela = Tk()
janela.title ("Minha primeira janela! ") #titulo
janela.geometry("500x500+600+300") #largura X Altura + EsquerdaDireita + CimaBaixo
janela.minsize(200,200)#Tamanho minimo da janela
janela.maxsize(1000,1000)#tamanho maximo da janela
janela.resizable(False,False)# Desabilita o button "minimizar"
#janela.state("zoomed")#começa maximizada
#janela.state.state("iconic")#começa minimizada
janela['bg'] = "red"#cor da janela
def menssagem1 ():
    texto = txtNome.get()
    print(texto)

def menssagem2 ():
    messagebox.showinfo("Informação", "Turma Top")


nome = Label (janela, text = "Nome", font = "Arial 20 bold", fg = 'black', bg = "red")
nome.pack()#adiciona a caixa


txtNome  = Entry (janela, font = "Arial 20", bg = '#A9A9A9') #Adiciona caixa de texto
txtNome.pack()
 

botao1 = Button (janela,text = " Clique aqui!", font = "arial 15 bold", command = menssagem1)
botao1.pack()


botao2 = Button (janela,text = "Não Clique aqui!", font = "arial 15 bold", command = menssagem2)
botao2.pack()
janela.mainloop()
