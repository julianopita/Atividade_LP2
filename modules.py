from tkinter import *
from tkinter import messagebox

class Window:
  def __init__(self, master):
    self.master = master

    self.Main = Frame(self.master)

    self.L0 = Label(self.Main, text = "Bem vindo ao sistema de geração de médias de cinco notas!")
    self.L0.grid(row = 0, column = 1, padx = 5, pady = 5, columnspan = 2)

    #Notas
    self.L1 = Label(self.Main, text = "Insira a nota 1: ")
    self.L1.grid(row = 1, column = 0, padx = 5, pady = 5)

    self.E1 = Entry(self.Main, width = 2)
    self.E1.grid(row = 1, column = 1, padx = 5, pady = 5)

    self.L2 = Label(self.Main, text = "Insira a nota 2: ")
    self.L2.grid(row = 2, column = 0, padx = 5, pady = 5)

    self.E2 = Entry(self.Main, width = 2)
    self.E2.grid(row = 2, column = 1, padx = 5, pady = 5)

    self.L3 = Label(self.Main, text = "Insira a nota 3: ")
    self.L3.grid(row = 3, column = 0, padx = 5, pady = 5)

    self.E3 = Entry(self.Main, width = 2)
    self.E3.grid(row = 3, column = 1, padx = 5, pady = 5)

    self.L4 = Label(self.Main, text = "Insira a nota 4: ")
    self.L4.grid(row = 4, column = 0, padx = 5, pady = 5)

    self.E4 = Entry(self.Main, width = 2)
    self.E4.grid(row = 4, column = 1, padx = 5, pady = 5)

    self.L5 = Label(self.Main, text = "Insira a nota 5: ")
    self.L5.grid(row = 5, column = 0, padx = 5, pady = 5)

    self.E5 = Entry(self.Main, width = 2)
    self.E5.grid(row = 5, column = 1, padx = 5, pady = 5)

    self.Main.pack(padx = 5, pady = 5)

    #Botões
    self.B1 = Button(self.Main, text = "Enviar", command = self.media)
    self.B1.grid(row = 7, column = 2, padx = 5, pady = 5, sticky = "e")

    self.B2 = Button(self.Main, text = "Clear", command = self.clear)
    self.B2.grid(row = 7, column = 3, padx = 5, pady = 5)

  def clear(self):
    self.E1.delete(0, 'end')
    self.E2.delete(0, 'end')
    self.E3.delete(0, 'end')
    self.E4.delete(0, 'end')
    self.E5.delete(0, 'end')

  def media(self):
    n1 = float(self.E1.get())
    n2 = float(self.E2.get())
    n3 = float(self.E3.get())
    n4 = float(self.E4.get())
    n5 = float(self.E5.get())

    md1 = (n1+n2+n3+n4+n5)/5

    for widget in self.Main.winfo_children():
      widget.destroy()
    
    self.LR = Label(self.Main, text = f"Média = {md1:.2f}")
    self.LR.grid(row = 3, column = 0, padx = 5, pady = 5)
   
