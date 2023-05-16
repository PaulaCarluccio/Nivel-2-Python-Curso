from tkinter import * 
root = Tk()

n = Entry(root, width= 70)
n.pack()
a = Entry(root, width= 70)
a.pack()

def escribir():
        nombreyapellido = str(n.get()) + " " + str(a.get())
        etiqueta = Label(root,text = "Hola " + nombreyapellido)
        etiqueta.pack()

mibtn = Button(root, text = "Tu nombre y apellido", command=escribir)
mibtn.pack()

root.mainloop()