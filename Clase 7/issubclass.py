class Humano(object):
    def __init__(self, nombre, apellido, genero):        
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
        Humano.__init__(self, nombre, apellido, genero)        
        self.rol = rol
        self.lenguajesconocidos = ["PHP","JavaScript","Python"]

print(issubclass(Programador,Humano))
print(issubclass(Humano,object))
print(issubclass(Humano,Programador))
print(issubclass(Programador,object))