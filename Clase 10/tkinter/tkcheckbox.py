import tkinter as tk

app = tk.Tk()
app.title('Me gusta')
app.geometry('150x150')
 
l = tk.Label(app, bg='orange', width=25)
l.pack()
 
def elegir():
    if (var1.get() == 1) & (var2.get() == 0):
        l.config(text='Me gusta la Asado')
    elif (var1.get() == 0) & (var2.get() == 1):
        l.config(text='Me gusta el Pizza')
    elif (var1.get() == 0) & (var2.get() == 0):
        l.config(text='Prefiero otra cosa')
    else:
        l.config(text='En ese orden')
 
var1 = tk.IntVar()
var2 = tk.IntVar()
c1 = tk.Checkbutton(app, text='Asado',variable=var1, onvalue=1, offvalue=0, command=elegir)
c1.pack()
c2 = tk.Checkbutton(app, text='Pizza',variable=var2, onvalue=1, offvalue=0, command=elegir)
c2.pack()
 
app.mainloop()