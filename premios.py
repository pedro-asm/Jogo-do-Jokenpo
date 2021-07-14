from tkinter import *
from lista_encadeada import ListaEncadeada
premioFacil =  ListaEncadeada()
premioMedio =  ListaEncadeada()
premioDificil = ListaEncadeada()

premioFacil.adicionar("1")
premioFacil.adicionar("imagens/premio1.png")
premioFacil.adicionar("imagens/premio2.png")
premioFacil.adicionar("imagens/premio3.png")
premioFacil.adicionar("imagens/premio4.png")
premioFacil.adicionar("imagens/premio5.png")
premioFacil.adicionar("imagens/premio6.png")
premioFacil.adicionar("imagens/premio7.png")
premioFacil.adicionar("imagens/premio8.png")
premioFacil.adicionar("imagens/premio9.png")
premioFacil.adicionar("imagens/premio10.png")

premioMedio.adicionar("2")
premioMedio.adicionar("imagens/premio11.png")
premioMedio.adicionar("imagens/premio12.png")
premioMedio.adicionar("imagens/premio13.png")
premioMedio.adicionar("imagens/premio14.png")
premioMedio.adicionar("imagens/premio15.png")
premioMedio.adicionar("imagens/premio16.png")
premioMedio.adicionar("imagens/premio17.png")
premioMedio.adicionar("imagens/premio18.png")
premioMedio.adicionar("imagens/premio19.png")
premioMedio.adicionar("imagens/premio20.png")

premioDificil.adicionar("3")
premioDificil.adicionar("imagens/premio21.png")
premioDificil.adicionar("imagens/premio22.png")
premioDificil.adicionar("imagens/premio23.png")
premioDificil.adicionar("imagens/premio24.png")
premioDificil.adicionar("imagens/premio25.png")
premioDificil.adicionar("imagens/premio26.png")
premioDificil.adicionar("imagens/premio27.png")
premioDificil.adicionar("imagens/premio28.png")
premioDificil.adicionar("imagens/premio29.png")
premioDificil.adicionar("imagens/premio30.png")

def premioF(index):
    root = Tk()
    photo = PhotoImage(file=premioFacil[index])
    label = Label(root, image=photo)
    label.pack()
    root.mainloop()

def premioM(index):
    root = Tk()
    photo = PhotoImage(file=premioMedio[index])
    label = Label(root, image=photo)
    label.pack()
    root.mainloop()

def premioD(index):
    root = Tk()
    photo = PhotoImage(file=premioDificil[index])
    label = Label(root, image=photo)
    label.pack()
    root.mainloop()

def premioEspecialFacil():
    root = Tk()
    photo = PhotoImage(file="imagens/premioFacil.png")
    label = Label(root, image=photo)
    label.pack()
    root.mainloop()

def premioEspecialMedio():
    root = Tk()
    photo = PhotoImage(file="imagens/premioMedio.png")
    label = Label(root, image=photo)
    label.pack()
    root.mainloop()

def premioEspecialDificil():
    root = Tk()
    photo = PhotoImage(file="imagens/premioDificil.png")
    label = Label(root, image=photo)
    label.pack()
    root.mainloop()

def premioGeral():
    root = Tk()
    photo = PhotoImage(file="imagens/premioGeral.png")
    label = Label(root, image=photo)
    label.pack()
    root.mainloop()
