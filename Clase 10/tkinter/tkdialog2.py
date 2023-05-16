import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
i = 0
def mensaje(m):
    global i
    i = i+1
    tk.messagebox.showwarning(title="Cuidado!", message=m + str(i))

tk.Button(root, text="Ejemplo", fg = "black", bg = "pink", font = "Helvetica 20 bold", command=lambda: mensaje('Tenemos problemas ...')).pack() 

root.mainloop()