class Cajero():
    def __init__(self,tipousuario):
        self.dinero = 5000
        self.tipousr = tipousuario # 1 es admin y 2 es usr final
    def agregarDinero(self,monto):
        if self.tipousr == 1:
            return self.dinero + monto
        else:
            return "Error"
    def retirarDinero(self,monto):
        if self.tipousr == 2:
            if self.dinero - monto >= 0:
                return "Le entregamos "+str(monto)
            else:
                return "No hay suficiente dinero para entregar"
        else:
            return "Error"            

agente = Cajero(1) 
print(agente.agregarDinero(10000))

usuario = Cajero(2) 
print(usuario.retirarDinero(1000))