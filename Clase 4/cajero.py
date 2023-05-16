import math

class Cajero:
    def __init__(self):
        self.billetes1000 = 4
        self.billetes500 = 2
        self.billetes100 = 1
        self.disponible = (self.billetes1000 * 1000) + (self.billetes500 * 500) + (self.billetes100 * 100)
    
    def suficientedinero(self, retira):
        print("Hay disponible " , self.disponible)
        while self.disponible < retira or retira < 100:
            retira = int(input("Dinero insuficiente, ponga un valor menor, multiplo de 100 "))
        if self.disponible > retira:
            self.disponible = self.disponible - retira
            if banelco.entregadinero(retira) == 1:
                return ("Cantidad de billetes insuficientes, por favor volver a intentar")
            else:
                print(banelco.entregadinero(retira))
                return ("El monto " + str(retira) + " no supera el limite y quedan disponibles " + str(self.disponible) )
        
    
    def entregadinero(self, retira):
        cantidad1000 = 0
        cantidad500 = 0
        cantidad100 = 0
        backupretira = retira

        if retira >= 1000:
            cantidad1000 = math.floor(retira/1000)
            if cantidad1000 > self.billetes1000:
                retira = retira - (self.billetes1000*1000)
                cantidad1000 = self.billetes1000
            else:
                retira = retira - (cantidad1000*1000)
        if retira >= 500:
            cantidad500 = math.floor(retira/500)
            if cantidad500 > self.billetes500:
                retira = retira - (self.billetes500*500)
                cantidad500 = self.billetes500
            else:
                retira = retira - (cantidad500*500)
        if retira >= 100:
            cantidad100 = math.floor(retira/100)
            if cantidad100 > self.billetes100:
                retira = retira - (self.billetes100*100)
                cantidad100 = self.billetes100
            else:
                retira = retira - (cantidad100*100)
        
        if (cantidad100*100) + (cantidad500*500) + (cantidad1000*1000) < backupretira:
            return 1
        else:
            return ("Se le darán " + str(cantidad1000) + " billetes de 1000 " + str(cantidad500) + " billetes de 500 y " +str(cantidad100) + " billetes de 100")
            
banelco = Cajero()
multiplo = 1
while multiplo != 0:
    sacar = int(input("Cuanto quiere sacar? Multiplo de 100  "))
    multiplo = sacar % 100
print(banelco.suficientedinero(sacar))
#version by Matias D