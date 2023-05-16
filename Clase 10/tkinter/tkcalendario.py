import tkinter as tk
from tkinter import ttk

from tkcalendar import Calendar

def abrirCal():
    def mostrar():
        etiquetavalue.set("El resultado es " + str(cal.selection_get()))  
        top.destroy()

    top = tk.Toplevel(root)

    cal = Calendar(top,
                   font="Helvetica 18", selectmode='day',
                   cursor="hand1", year=2020, month=6, day=16)
    cal.pack(fill="both", expand=True)
    ttk.Button(top, text="ok", command=mostrar).pack()


root = tk.Tk()
root.geometry('300x120') 
s = ttk.Style(root)
s.theme_use('clam')

ttk.Button(root, text='Abrir calendario', command=abrirCal).pack(padx=10, pady=10)
etiquetavalue = tk.StringVar()
etiqueta = ttk.Label(root,textvariable = etiquetavalue).pack()

root.mainloop()