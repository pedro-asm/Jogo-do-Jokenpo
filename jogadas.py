from tkinter import *

def empate_pedra_x_pedra():
    root = Tk()
    photo = PhotoImage(file="maos/PedraXPedra.png")
    label = Label(root, image=photo)
    label.pack()
    root.mainloop()

def empate_papel_x_papel():
    root = Tk()
    photo = PhotoImage(file="maos/PapelXPapel.png")
    label = Label(root, image=photo)
    label.pack()
    root.mainloop()

def empate_tesoura_x_tesoura():
    root = Tk()
    photo = PhotoImage(file="maos/TesouraXTesoura.png")
    label = Label(root, image=photo)
    label.pack()
    root.mainloop()

def vitoria_pedra_x_tesoura():
    root = Tk()
    photo = PhotoImage(file="maos/PedraXTesoura.png")
    label = Label(root, image=photo)
    label.pack()
    root.mainloop()

def vitoria_tesoura_x_papel():
    root = Tk()
    photo = PhotoImage(file="maos/TesouraXPapel.png")
    label = Label(root, image=photo)
    label.pack()
    root.mainloop()

def vitoria_papel_x_pedra():
    root = Tk()
    photo = PhotoImage(file="maos/PapelXPedra.png")
    label = Label(root, image=photo)
    label.pack()
    root.mainloop()

def derrota_pedra_x_papel():
    root = Tk()
    photo = PhotoImage(file="maos/PedraXPapel.png")
    label = Label(root, image=photo)
    label.pack()
    root.mainloop()

def derrota_tesoura_x_pedra():
    root = Tk()
    photo = PhotoImage(file="maos/TesouraXPedra.png")
    label = Label(root, image=photo)
    label.pack()
    root.mainloop()

def derrota_papel_x_tesoura():
    root = Tk()
    photo = PhotoImage(file="maos/PapelXTesoura.png")
    label = Label(root, image=photo)
    label.pack()
    root.mainloop()
