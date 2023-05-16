import random
import time

class Tensiometro:
    def __init__(self, modo, sensibilidad):
        self.modo = modo
        self.encendido = True
        self.sensimenor = modo - ((modo * sensibilidad) / 100) 
        self.sensimayor = modo + ((modo * sensibilidad) / 100) 
    
    def validador(self, t):
        tension = t
        if tension < self.sensimayor and tension > self.sensimenor:
            return (f"su tensión es " + str(tension))
        elif tension >self.sensimayor:
            return (f"su tensión es " + str(tension) + " y esta por encima del límite")
        elif tension < self.sensimenor:
            return (f"su tensión es " + str(tension) + " y esta por debajo del límite")
    
    def test(self):
        tension = random.randint(50, 300)
        while True:
            print (medir.validador(tension))
            time.sleep(1)
            if tension < medir.sensimenor or tension > medir.sensimayor:
                break
            tension = random.randint(50, 300)

modo = input("Elija uno de los modos (220 ó 110): ")

opcion = input("Desea modificar la sensibilidad por defecto? (20%) s/n: " ).lower()
if opcion == "s":
    sensibilidad = input("Elija porcentaje de sensibildiad (20% por defecto): ")
else:
    sensibilidad = 20

medir = Tensiometro(int(modo), int(sensibilidad))

medir.test()
#Ejercicio by Matid