class Estudiante():
    def __init__(self, notas):
        self.notas = notas
        self.__maxmaterias = 4
        self.__minnota = 1
        self.__maxnota = 10

    def __validar(self):
        if len(self.notas) > self.__maxmaterias:
            valido = False
        else:
            valido = True        
            for x in self.notas:
                if x > self.__maxnota or x < self.__minnota:
                    valido = False
        return valido

    def mensaje(self):
        __aprobado = 7
        suma = 0
        promedio = 0
        devolucion = ""
        if self.__validar() == False:
            devolucion = "Ingresó numeros incorrectos"
        else:
            for x in self.notas:
                suma = suma + x
            promedio = suma/(len(self.notas))
            if promedio >= __aprobado:
                devolucion = "Esta aprobado. "
            else:
                devolucion = "Esta desaprobado. "
            devolucion = devolucion + f"El promedio es {promedio:.2f}"
        return devolucion

notas = [9, 5 , 9 , 10]

mati = Estudiante(notas)

print(mati.mensaje())

#Ejemplo by MatiD