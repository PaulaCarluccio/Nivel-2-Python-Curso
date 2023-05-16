class Terricola(object):
    def __init__(self):
        self.ojos = 2
    def saludar(self):
        print("Hola Mundo")

class Humano(Terricola):
    def __init__(self, nombre, apellido, genero):    
        super().__init__()    
        self.nombre = nombre
        self.apellido = apellido
        self.genero = genero
        #se crea el humano siempre habilitado
        self.habilitado = True
    def enable_disable(self,booleano):
        self.habilitado = booleano
        return "Ha cambiado el estado"


class Programador(Humano):
    def __init__(self, nombre, apellido, genero, rol):
        #Humano.__init__(self,nombre, apellido, genero)        
        super().__init__(nombre, apellido, genero)        
        self.rol = rol
        self.lenguajesconocidos = ["PHP","JavaScript","Python"]

print(Programador.__mro__)
h = Programador("Dami","De","M","Dev")
h.saludar()
print(h.ojos)
