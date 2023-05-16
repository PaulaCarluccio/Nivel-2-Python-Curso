class Boton(object):
    def __init__(self):        
        self.mainclass = "btn"
    def renderBoton(self,texto,clase=""):        
        return (f"""<button type="button" class="{self.mainclass}{clase}">{texto}</button>""")

class BtnDanger(Boton):
    def __init__(self):
        #Boton.__init__(self)  
        super().__init__()        
        self.tipo = " btn-danger"
        self.texto = "Cuidado"
    def renderBtnDanger(self):        
        #return Boton.renderBoton(self,self.texto,self.tipo)        
        return super().renderBoton(self.texto,self.tipo)  

btn1 = Boton()
print(btn1.renderBoton("Mi boton"))

btn2 = BtnDanger()
print(btn2.renderBtnDanger())