#Ejemplo by Lean
class Tarjeta():
    def __init__(self,salanual,numtarj):
        self.__pridigito = 0
        self.__minlen = 10
        self.__maxlen = 15
        self.salanual = salanual
        self.numtarj = numtarj
    
    def __Validar(self,numtarj):
        self.numtarj = numtarj
        if self.numtarj[0] == "0":
            if len(self.numtarj) < self.__maxlen and len(self.numtarj) >self.__minlen:
                return True
            else:
                return False
        else:
            return False

    def saludar(self):
        if self.__Validar(numtarj):
            if self.salanual >= 100000 and self.salanual < 200000:
                return f"Posee un credito de {(25*self.salanual)/100} disponible"
            elif self.salanual >200000:
                return f"Posee un credito de {self.salanual/2} disponible"
            else:
                return "aguarde un representante lo atendera a la brevedad"        
        else:
            return "Tarjeta No valida"


numtarj = "0542235879245"
h=Tarjeta(150000,numtarj)
print(h.saludar())