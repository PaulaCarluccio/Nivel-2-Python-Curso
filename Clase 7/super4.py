class Cuadrado(object): 
    def __init__(self, lado): 
        self.lado = lado   
    def areacara(self): 
        return self.lado * self.lado 

class Cubo(Cuadrado): 
    def __init__(self, lado): 
        super().__init__(lado)
        self.lado = lado     
    def areacubo(self):          
        return super().areacara() * 6

c1 = Cuadrado(10)
print(c1.areacara())

c2 = Cubo(10)
print(c2.areacara())
print(c2.areacubo())