class user():
    def __init__(self):
        self.levels ={
            "nivel 0":{"puntos":0,"descuento":0},
            "nivel 1":{"puntos":100,"descuento":10},
            "nivel 2":{"puntos":200,"descuento":20},
            "nivel 3":{"puntos":300,"descuento":30},
            "nivel 4":{"puntos":400,"descuento":40},
            "nivel 5":{"puntos":500,"descuento":50}
            }
    def calcularnivel(self,puntos):
        ordenados = sorted(self.levels,reverse=True, key = lambda x:(self.levels[x]["puntos"]))
        nivel =""
        if puntos > 500:
            nivel ="nivel 5"
        else:
            for x in ordenados:
                if puntos <= self.levels[x]["puntos"]:
                    nivel = x
        return nivel
    def calcularpago(self,puntos,importe):
        pagar = importe - ((self.levels[self.calcularnivel(puntos)]["descuento"]*importe)/100)
        return f"se realiza descuendo del {self.levels[self.calcularnivel(puntos)]['descuento']}% se debe abonar {round(pagar)}"

usuario=user()
print(usuario.calcularpago(0,2000))
#Ejercicio by Lean