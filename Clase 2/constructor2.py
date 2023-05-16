class Hola: 
    def __init__(self,mensaje): 
        self.saludo = str(mensaje)
    def mostrarMensaje(self): 
        print(self.saludo)   
  
mundillo = Hola("Hola Mundillo") 
mundillo.mostrarMensaje() 