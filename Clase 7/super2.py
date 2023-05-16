class Humano:
    def __init__(self):
        self.nombre=str(input("Dime tu Nombre: "))
        self.edad=str(input("Dime tu Edad: "))
    def imprimir(self):
        print("Nombre: " + self.nombre)
        print("Edad: " + self.edad)

class Empleado(Humano):
    def __init__(self):
        super().__init__()
        self.sueldo=int(input("Dime tu Sueldo:"))
    def imprimir(self):
        super().imprimir()
        print("Sueldo:",self.sueldo)       
    def tributar(self):
        if self.sueldo>50000:
            print("Paga el impuesto")
        else:
            print("NO debes pagar el impuesto")         

#humano1 = Humano()
#humano1.imprimir()

empleado1 = Empleado()
empleado1.imprimir()
empleado1.tributar()