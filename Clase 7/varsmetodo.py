import inspect

def funcion(a,b,c):
    d = 1
    pass

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

print(inspect.getfullargspec(funcion))
print("*********")
print(inspect.getfullargspec(Terricola.__init__))
print("*********")
print(inspect.getfullargspec(Humano.__init__))
print("*********")
print(dir(Terricola))
