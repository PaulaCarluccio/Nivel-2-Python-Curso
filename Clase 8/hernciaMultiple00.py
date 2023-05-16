class Padre:
    nombrepadre = "" 
    def mostarPadre(self):
        print(self.nombrepadre)
 
 
# Mother class created
class Madre:
    nombremadre = "" 
    def mostrarMadre(self):
        print(self.nombremadre)
 
 
class Hijo(Padre, Madre):
    def mostrarPadres(self):
        print("Padre :", self.nombrepadre)
        print("Madre :", self.nombremadre)
 
 
s1 = Hijo() 
s1.nombrepadre = "Jose"
s1.nombremadre = "Maria"
s1.mostrarPadres()