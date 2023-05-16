class Cajero():
    def __init__(self,tipousuario):
        self.tipousr = tipousuario # 1 es admin y 2 es usr final
    def agregarDinero(self,monto,store):
        if self.tipousr == 1:
            store.agregar(monto)
            return store.dinero
        else:
            return "Error"
    def retirarDinero(self,monto,store):
        if self.tipousr == 2:
            if store.dinero - monto >= 0:
                store.quitar(monto)
                return "Le entregamos "+str(monto)
            else:
                return "No hay suficiente dinero para entregar"
        else:
            return "Error"         

class Store():
    def __init__(self):
        self.dinero = 0
    def agregar(self,newdinero):
        self.dinero += int(newdinero)
    def quitar(self,newdinero):
        self.dinero = self.dinero-int(newdinero)        


s = Store()
agente = Cajero(1) 
print(agente.agregarDinero(2500,s))
print("*******")
print(s.dinero)
usuario = Cajero(2) 
print(usuario.retirarDinero(1000,s))
print("*******")
print(s.dinero)