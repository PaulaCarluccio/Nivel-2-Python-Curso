class Humano:  
    def __init__(self,nombre,edad):  
        self.nombre = nombre;          
        self.edad = edad  
  
dami = Humano("Damian",42)  
print(getattr(dami,'nombre'))  
setattr(dami,"edad",43)  
print(getattr(dami,'edad'))  
print(hasattr(dami,'nacionalidad'))  
delattr(dami,'edad')  
print(hasattr(dami,'edad'))  
#print(dami.edad) 

pedro = Humano("Pedro",12) 
print(getattr(pedro,'edad')) 