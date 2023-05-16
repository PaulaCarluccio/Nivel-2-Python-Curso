class Terricola(object):
    def __init__(self):
        pass

class Humano(Terricola):
    def __init__(self, nombre, apellido, genero):        
        self.nombre = nombre
        self.apellido = apellido
        self.genero = genero
        #se crea el humano siempre habilitado
        self.habilitado = True
    def enable_disable(self,booleano):
        self.habilitado = booleano
        return "Ha cambiado el estado"


class Robot(object):
    def __init__(self):
        pass 


class SuperRobot(Robot):
    def __init__(self):
        pass    


class Programador(Humano,SuperRobot):
    def __init__(self, nombre, apellido, genero, rol):
        Humano.__init__(self, nombre, apellido, genero)        
        #super().__init__(self, nombre, apellido, genero)        
        self.rol = rol
        self.lenguajesconocidos = ["PHP","JavaScript","Python"]

print(Programador.__mro__)