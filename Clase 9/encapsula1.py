class Persona:
    def __init__(self, nombre, edad=0):
        self.nombre = nombre
        self.__edad = edad
 
    def mostrar(self):
        print(self.nombre)
        print(self.__edad)
 
personita = Persona('Dami', 43)
personita.mostrar()
print('Intentando acceder x afuera')
print(personita.nombre)
#print(personita.__edad)
#print(Persona().__edad)