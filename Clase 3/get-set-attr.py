class Humano:  
    def __init__(self,nombre,edad):  
        self.nombre = nombre
        self.edad = edad  
  
dami = Humano("Damian",42)  
print(getattr(dami,'edad'))  
print(getattr(dami,'nombre'))  
setattr(dami,"edad",43)  
print(getattr(dami,'edad'))  
print(hasattr(dami,'nacionalidad'))