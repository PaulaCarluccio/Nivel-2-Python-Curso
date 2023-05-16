class Humano:  
    def saludar(self,*args):
        nombre = " "

        for x in args:
            nombre += str(x) + " "
        return "Hola" + nombre

newhumano = Humano()
print(newhumano.saludar("Dami","De"))