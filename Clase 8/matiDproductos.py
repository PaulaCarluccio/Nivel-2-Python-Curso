class Producto():
    def __init__(self , productos):
        self.productos = productos
    
    def mostrar(self):
        enstock = "Productos en stock: \n"
        for i in self.productos:
            if self.productos[i]["stock"] == 1:
                enstock = enstock + (f"Código : {i} - Producto: {self.productos[i]['nombre']} - Marca: {self.productos[i]['marca']}\n")
        return enstock

class Computadora(Producto):
    def __init__(self , productos , eleccion):
        Producto.__init__(self , productos)
        self.eleccion = eleccion
        self.dolar = 120

    def mostrar(self):
        elegido = "Su articulo y precio: \n"
        for id, i in self.productos.items():
            if id == self.eleccion:
                preciopesos = self.dolar * self.productos[self.eleccion]["USD"]
                elegido = elegido + (f"""{self.productos[id]["nombre"]} - {self.productos[id]['marca']} - Pesos: $ {preciopesos} \n""")
        return elegido

# stock = 1 : hay stock ; stock = 0 : no hay stock
dicproductos = {
    125 : {"nombre" : "Mother" , "marca" : "Gigabyte" , "year" : 2018 , "stock" : 1 , "USD" : 250},
    379 : {"nombre" : "RAM" , "marca" : "Kingston" , "year" : 2017 , "stock" : 1 , "USD" : 150},
    258 : {"nombre" : "Placa de video" , "marca" : "MSI GeForce" , "year" : 2020 ,  "stock" : 1 , "USD" : 400},
    501 : {"nombre" : "Monitor" , "marca" : "LG" , "year" : 2019 , "stock" : 1 , "USD" : 150},
    168 : {"nombre" : "Mouse" , "marca" : "Logitech" , "year" : 2016 , "stock" : 0 , "USD" : 10},
    465 : {"nombre" : "Teclado" , "marca" : "Logitech" , "year" : 2015 , "stock" : 0 , "USD" : 8},
    685 : {"nombre" : "Windows" , "marca" : "Windows" , "year" : 2016 , "stock" : 0 , "USD" : 65},
}

listado = Producto(dicproductos)
print(listado.mostrar())

listaenstock = []
for i in dicproductos:
    if dicproductos[i]["stock"] == 1:
        listaenstock.append(i)
articulo = int(input("Elija uno de los articulos en stock: (por código) "))
while articulo not in listaenstock:
    articulo = int(input("Elija uno de los articulos en stock: (por código) "))

venta = Computadora(dicproductos , articulo)
print(venta.mostrar())