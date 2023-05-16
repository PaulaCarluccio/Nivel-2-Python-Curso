import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
def saludar():
    tk.messagebox.showinfo(title="Hola título", message="Hola!")

tk.Button(root, text="Ejemplo", fg = "black", bg = "pink", font = "Helvetica 20 bold italic", command=saludar).pack() 
root.mainloop()