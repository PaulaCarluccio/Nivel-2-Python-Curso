import tkinter as tk
import tkinter.ttk as ttk
root = tk.Tk()

p = tk.Entry(root, width= 70)
p.pack()

n = ttk.Combobox(root, values=("1", "2", "3", "4", "5"))
n.set("1")
n.pack()

def escribir():
        etiqueta = ttk.Label(root,text = "Elegiste " + p.get() + " ("+n.get()+")")
        etiqueta.pack()
mibtn = ttk.Button(root, text = "Elige producto y cantidad", command=escribir)
mibtn.pack()

root.mainloop()