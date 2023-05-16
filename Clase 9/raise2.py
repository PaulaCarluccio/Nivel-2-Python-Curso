class SalarioRango(Exception):
    def __init__(self, sueldo, mensaje="Fuera de rango"):
        self.sueldo = sueldo
        self.mensaje = mensaje
        super().__init__(self.mensaje)


sueldo = int(input("Ingresa tu sueldo: "))
if not 10000 < sueldo < 150000:
    raise SalarioRango(sueldo)
else:
    print("Sueldo: " + str(sueldo))

print(SalarioRango.__mro__)
