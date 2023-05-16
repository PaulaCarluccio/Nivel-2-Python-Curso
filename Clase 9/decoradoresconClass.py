class donacion:
    def __init__(self,monto):
        self.monto1 = monto
        
    @property
    def monto1(self):
        return self.__monto

    @monto1.setter
    def monto1(self, monto):
        if monto < 100:
            self.__monto = 100
        elif monto > 1000000:
            self.__monto = 1000000
        else:
            self.__monto = monto


donacion1 = donacion(5)
print(donacion1.monto1)
donacion1.monto1 = 1
print(donacion1.monto1)