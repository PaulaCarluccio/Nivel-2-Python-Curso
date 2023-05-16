import tkinter as tk
import tkinter.ttk as ttk
root = tk.Tk()

n = ttk.Combobox(root, values=("1", "2", "3", "4", "5"))
n.set("1")
n.pack()

def escribir():
        etiqueta = ttk.Label(root,text = "Elegiste " + n.get())
        etiqueta.pack()
mibtn = ttk.Button(root, text = "Elige", command=escribir)
mibtn.pack()

root.mainloop()