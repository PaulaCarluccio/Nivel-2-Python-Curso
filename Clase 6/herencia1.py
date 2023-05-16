class Humano(object):
    def __init__(self, nombre, apellido, genero):        
        self.nombre = nombre
        self.apellido = apellido
        self.genero = genero
        self.habilitado = False
    def otra(self):
        self.cualquiera = 1        
    def enable_disable(self,booleano):
        self.habilitado = booleano
        return "Ha cambiado el estado a " + str(booleano)

class Programador(Humano):
    def __init__(self, nombre, apellido, genero, rol):     
        Humano.__init__(self, nombre, apellido, genero)                
        Humano.otra(self)
        self.rol = rol        
        self.lenguajesconocidos = ["PHP","JavaScript","Python"]        

h = Humano("Pedro","Gonzalez","Masculino")
print(h.nombre)

dami = Programador("Dami","De","Masculino","Developer")
print(dami.nombre)
print(dami.rol)
print(dami.enable_disable(True))
print(dami.cualquiera)