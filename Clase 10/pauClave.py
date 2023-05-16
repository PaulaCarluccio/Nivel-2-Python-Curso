import random
import tkinter as tk
from tkinter import messagebox
root = tk.Tk()

class Contrasena():
    def __init__(self, lista, titulo):
        self.titulo = titulo
        self.lista = lista                
    def clavefinal(self):
        self.clave = random.sample(self.lista, k=8)
        #self.contrasena que estaba en el init se ubica en clavefinal() porque sino no se limpia, ya que el init se llama solo una vez y la función clavefinal se llama cada vez y necesita este valor "limpio" cada vez
        self.contrasena= ""
        for x in self.clave:
            self.contrasena = self.contrasena + str(x)        
        tk.messagebox.showinfo(title=self.titulo, message=self.contrasena)
    
        

alfanum = ["a", "b","a", "c","d", "e","f", "g","h", "i","j", "k","l", "m","n", "o","p", "q","r", "s","t", "u","v", "w","x", "y","z",1, 2,3,4,5,6,7,8,9,0]

generador = Contrasena(alfanum,"Hola generamos tu clave")
tk.Button(root, text="Generar clave", fg = "white", bg = "gold", font = "Helvetica 20 bold italic", command=generador.clavefinal).pack() 

root.mainloop()

#Ejemplo de Pau - Corregido