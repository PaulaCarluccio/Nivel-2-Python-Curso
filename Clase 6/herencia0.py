class Humano(object):
    def __init__(self):        
        self.planeta = "Tierra"

class Programador(Humano):
    def saludar(self):
        return "Hola soy del planeta " + self.planeta

dami = Programador()
print(dami.planeta)
print(dami.saludar())