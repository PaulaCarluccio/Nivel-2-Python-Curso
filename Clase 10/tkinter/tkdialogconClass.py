import tkinter as tk
from tkinter import messagebox
root = tk.Tk()

class Saludo():
    def __init__(self,titulo,mensaje):
        self.titulo = titulo
        self.mensaje = mensaje
    def saludar(self):
        tk.messagebox.showinfo(title=self.titulo, message=self.mensaje)

misaludo = Saludo("Hola título","Hola!")
tk.Button(root, text="Ejemplo", fg = "black", bg = "pink", font = "Helvetica 20 bold italic", command=misaludo.saludar).pack() 
root.mainloop()