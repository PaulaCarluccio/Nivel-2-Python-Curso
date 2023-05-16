class Personaje:
    def __init__(self, velocidad, edad, genero, activo, comic):
        self.velocidad = int(velocidad)
        self.edad = int(edad)
        self.genero = genero
        self.activo = activo
        self.comic = comic
    def listarcaracteristicas(self):
        return "Velocidad: "+ str(self.velocidad) + "\n" + "Edad: "+ str(self.edad) + "\n" + "Genero: "+ str(self.genero) + "\n" + "Activo: "+ str(self.activo) + "\n"
    def listarpubs(self):
        acumula = "Aparece en los siguientes comics: "
        orden = input("Quiere orden ascendente (A) o descendente (D) ? : ").lower()
        ordenacomics = {}
        while orden != "a" and orden != "d":
            orden = input("Quiere orden ascendente (A) o descendente (D) ? : ").lower()
        if orden == "a":
            ordenacomics = sorted(self.comic.items() , key = lambda x : x [1])
        elif orden == "d":
            ordenacomics = sorted(self.comic.items() , key = lambda x : x [1] , reverse = True)                
        for id, x in ordenacomics:
            acumula = acumula + id + ": " + str(x) + ", "
        return acumula        

class Superheroe(Personaje):
    def __init__(self, velocidad, edad , genero , activo , comic, superpoderes):
        Personaje.__init__(self, velocidad, edad, genero, activo, comic)
        self.superpoderes = superpoderes
    def listarsuper(self):
        acumula = "Tiene los siguientes superpoderes: "
        for x in self.superpoderes:
            acumula = acumula + str(x) + "\n"
        return acumula

    def listartodo(self):
        acumula = "Todos los datos son : "
        acumula = acumula + self.listarcaracteristicas() + self.listarpubs() + '\n' + self.listarsuper()
        return (f"{acumula}")

supermancomics = { "Action comics 1" : 1938 ,  "El hombre de acero" : 1986 , "Para el hombre que lo tiene todo" : 1985}
poderessuperman = ["volar","superfuerza","supervista","superfume"]
luisa = Personaje(10, 40, "femenino", "activo", supermancomics)
print(luisa.listarpubs())
print(luisa.listarcaracteristicas())
print("*********************")
superman = Superheroe(15, 42, "masculino", "activo", supermancomics , poderessuperman)
print(superman.listartodo())
#Basado en la versión de MatiD