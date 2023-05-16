class Humano:  
    def saludar(self,**kwargs):
        print(kwargs)        
        print(type(kwargs))
        nombre = kwargs.get("nombre", "Dami")        
        apellido = kwargs.get("apellido", "")        
        return "Hola, soy " + nombre  + " " + apellido


newhumano = Humano()
print(newhumano.saludar())
print(newhumano.saludar(nombre="Damian",apellido="De"))