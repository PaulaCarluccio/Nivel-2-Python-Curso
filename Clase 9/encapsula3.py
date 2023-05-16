class Electrodomestico:
    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Precio máximo: "+str(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

c = Electrodomestico()
c.sell()

c.__maxprice = 1200
c.sell()

c.setMaxPrice(1000)
c.sell()