from tkinter import *

def Cumprimente():
    hello.set("Olá, você!")


gui = Tk()

gui.title("Testando Melhor time")
gui.geometry("400x300")

btn = Button(gui, text="Cumprimente", command=Cumprimente)
btn.pack()

hello = StringVar()
lbl = Label(gui, textvariable=hello)
lbl.pack()

gui.mainloop()
