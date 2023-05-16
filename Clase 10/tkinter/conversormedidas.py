import tkinter as tk
import tkinter.ttk as ttk
root = tk.Tk()
root.geometry('300x120') 

def calcular():  
        try:      
                if n.get() == "pulgadas":
                        resultado = round(int(p.get()) / 2.54,2)
                elif n.get() == "metros":
                        resultado = round(int(p.get()) / 100,2)
                else:
                        resultado = round(int(p.get()) / 100000,4)    
                p.delete(first=0,last=1000)                          
                etiquetavalue.set("El resultado es " + str(resultado))
        except:
                etiquetavalue.set("Error de gravedad grave")
        

tk.Label(root, text="Escribe una cantidad de centímetros", fg = "black", font = "Helvetica 11").pack()
p = tk.Entry(root, width= 20)
p.pack()

n = ttk.Combobox(root, state="readonly", values=("pulgadas","metros", "kilómetros"))
n.set("pulgadas")
n.pack()

mibtn = ttk.Button(root, text = "Convertir", command=calcular)
mibtn.pack()

etiquetavalue = tk.StringVar()
etiqueta = ttk.Label(root,textvariable = etiquetavalue).pack()



root.mainloop()