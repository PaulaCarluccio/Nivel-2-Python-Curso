#Martin última versión
class Estudiante(object):
    def __init__(self, nombre, notas):
        self.__nombre = nombre
        self.notas = notas
        self.__maxmaterias = 4
        self.__min_nota = 1
        self.__max_nota = 10
    @property #
    def notas(self):
        return self.__notas
    @notas.setter #
    def notas(self, notas):
        notas_Ok = 0
        Len_notas = len(notas)
        self.__notas = notas
        if Len_notas == 4:
            for x in notas:
                if x >= 1 and x <=10:
                    notas_Ok = notas_Ok +1
            if notas_Ok == 4:
                self.__notas = notas
            else:
                self.__notas.clear()
                return print("Una o varias de las notas, son incorrectas")
        else:
            self.__notas.clear()
            return print("Cantidad de notas incorrectas")
    def get_Notas(self): #
        return self.__notas
    def get_Nombre(self): #
        return self.__nombre
    def get_Promedio(self): #
        prom = 0
        cant_notas = len(self.notas)
        for nota in self.notas:
            prom = prom + nota
        prom = round((prom /cant_notas), 2)
        return str(prom)
#Ejecución
notas_E = []
num_nota = 1
nombre_Est = input("Nombre del Estudiante al que se ingresarán notas: ")
try:
    for x in range(0,4):
        nota = int(input("Ingrese la nota "+str(num_nota)+": "))
        num_nota = num_nota+1
        notas_E.append(int(nota))
    est = Estudiante(nombre_Est, notas_E)
    print(est.get_Nombre(),": Notas-> ",est.get_Notas()," | Promedio-> ",est.get_Promedio())
except:
    print("No ha ingresado un número de nota válido: Deben ser números enteros, entre '1' y '10',incluidos estos)")