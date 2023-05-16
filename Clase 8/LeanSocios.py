diccsocios = {
        6000000:{"Nombre":"Alberto Mariotti","edad":67,"pais":"Argentina"},
        5000000:{"Nombre":"Matias Orozco","edad":40,"pais":"Argentina"},
        54678987:{"Nombre":"Marcelo Peretti","edad":38,"pais":"Argentina"},
        12000123:{"Nombre":"Leandro Paredes","edad":55,"pais":"Argentina"},
        24023456:{"Nombre":"Alberto Mariotti","edad":77,"pais":"Argentina"},
        8234123:{"Nombre":"Maria Alvarez","edad":25,"pais":"Argentina"},
        99674635:{"Nombre":"Wilmar Do Santos","edad":35,"pais":"Brazil"},
        99675463:{"Nombre":"Gisela  Perez","edad":28,"pais":"Peru"},
        90376231:{"Nombre":"Washington Gonzales","edad":67,"pais":"Uruguay"},
        33876543:{"Nombre":"Maria Rozetti","edad":70,"pais":"Argentina"},
        35678997:{"Nombre":"Pedro Scilensi","edad":8,"pais":"Argentina"},
        42004980:{"Nombre":"Macos Ponce","edad":42,"pais":"Argentina"}
}   

class socios():
    def __init__(self,diccsocios):
        self.diccsocios = diccsocios
        
    def orden(self):
        self.ordenados = sorted(self.diccsocios, reverse=True, key=lambda x: self.diccsocios[x]["edad"])
        return self.ordenados

    def poredad(self):
        self.listado = ""
        for x in self.orden():
            self.listado += f'Nombre: {self.diccsocios[x]["Nombre"]},  Edad: {self.diccsocios[x]["edad"]} \n'
        return self.listado 


class sociosSenior(socios):
    def obtenerNombres(self):
        self.listado =[]
        for x in super().orden():
            if self.diccsocios[x]["Nombre"] not in self.listado and self.diccsocios[x]["edad"] >= 65:
                self.listado.append(self.diccsocios[x]["Nombre"])
        return self.listado        

h=socios(diccsocios)
print(h.poredad())
i=sociosSenior(diccsocios)
print("Socios Seniors")
print(i.obtenerNombres())