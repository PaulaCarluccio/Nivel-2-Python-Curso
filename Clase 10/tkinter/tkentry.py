from tkinter import * 
root = Tk()

n = Entry(root, width= 70)
n.pack()

def escribir():
        etiqueta = Label(root,text = "Hola " + n.get())
        etiqueta.pack()

mibtn = Button(root, text = "Tu nombre?", command=escribir)
mibtn.pack()

root.mainloop()