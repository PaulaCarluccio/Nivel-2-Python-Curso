class Persona:
    def __init__(self, nombre):
        self.__nombre = nombre


class SalarioAnual(Persona):
    def __init__(self, pago,nombre):
        #Persona.__init__(self,nombre)
        self.__pago = pago
        #self.nombre = nombre
        self.__nombre = nombre
    def __get_total(self):
        return (self.__pago*12)
    def mensaje(self):
        return self.__nombre + " cobra anualmente: " + str(self.__get_total())
 

 
empleado1 = SalarioAnual(50000,"Joaquín")
#print(empleado1.nombre)
#print(empleado1.__pago)
#print(empleado1.__get_total())
print(empleado1.mensaje())