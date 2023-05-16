class Humano(object):
    def __init__(self,planeta):        
        self.planeta = planeta

class Programador(Humano):
    def __init__(self):       
        Humano.__init__(self,"Vulcano")         
        self.test = True    
    def saludar(self):
        return "Hola soy del planeta " + self.planeta

dami = Programador()
print(dami.planeta)
print(dami.saludar())