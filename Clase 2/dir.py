import random
class Cyborg:
    bateria = 100
    encendido = False
    def saludar(self):
        print("Hola")

robotin = Cyborg()
print(dir(Cyborg))
print("***************")
print(dir(random))
print(vars(Cyborg))
