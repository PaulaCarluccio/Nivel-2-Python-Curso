class Humano:
    nombre = None
    #lenguajes = "Español"

class Programador:
    lenguajes = ["JavaScript","Python","PHP"]

class WebDev(Humano, Programador):
    especialidad = "Front-End"
    lenguajes = "Python"

persona = WebDev()
persona.nombre = "Dami"

print(persona.nombre)
print(persona.lenguajes)
print(persona.especialidad)