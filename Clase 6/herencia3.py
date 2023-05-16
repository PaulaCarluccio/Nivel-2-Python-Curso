class Dispositivo:
    def __init__(self):
        self.encendido = False     
        self.testing = 1   
    def encender(self,**kwargs):
        if self.encendido == False:
            self.encendido = True      
            dispositivo = kwargs.get('dispositivo', "Dispositivo Genérico")      
            return "Mensaje: se ha encencido con éxito: " + dispositivo + "."
        else:
            return "Mensaje: ya estaba encendido"
            self.encendido = False
    def apagar(self):
        if self.encendido:
            self.encendido = False
            return "Mensaje: se ha apagado con éxito"
        else:
            return "Mensaje: ya estaba apagado"    
            self.encendido = True

class Cajero(Dispositivo):  
    def __init__(self):        
        Dispositivo.__init__(self)        
        self.nombre_dispositivo = "Cajero"
        self.cantidad_dinero = 1000
        self.mensaje = ""
    def test(self):
        return "Test"
    def informardinero(self):
        if(self.encendido == False):
            self.mensaje = Dispositivo.encender(self,dispositivo=self.nombre_dispositivo) 
        return self.mensaje + " En stock $" + str(self.cantidad_dinero)

lavarropas = Dispositivo()
print(lavarropas.encender(dispositivo="Lavarropas"))

c = Cajero()
print(c.encendido) 
print(c.informardinero())
print(c.encendido) 
print(Dispositivo().encendido)

print(dir(Cajero()))

d = Cajero()
print(d.encendido) 