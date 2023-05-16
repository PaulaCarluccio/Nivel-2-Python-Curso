class Persona:
    def __init__(self, nombre):
        self.nombre = nombre


class Salario:
    def __init__(self, pago):
        self.pago = pago
 
    def get_total(self):
        return (self.pago*12)
 
 
class Empleado(Persona):
    def __init__(self, pago, plus,nombre):
        super().__init__(nombre)
        self.pago = pago
        self.plus = plus
        self.obj_salario = Salario(self.pago)
 
    def salario_anual(self):
        return self.nombre + " - Total anual con el Plus: " + str(self.obj_salario.get_total() + self.plus)
 
 
empleado1 = Empleado(75000, 12000,"Clark")
print(empleado1.salario_anual())