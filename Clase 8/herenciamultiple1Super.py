class Humano():
  def __init__(self):
    super(Humano, self).__init__()
    self.nombre = "Dami"
    self.apellido = "De"

class Ubicacion():
  def __init__(self):    
    super(Ubicacion, self).__init__()
    self.pais = "Argentina"
    self.nombre = "Damian"

class OtraClase():
  def __init__(self):    
    super(OtraClase, self).__init__() 
    self.pais = "Otro pais"     

class UsuarioGeolocalizado(Humano,Ubicacion,OtraClase):  
  def saludar(self):
    return("Hola, mi nombre es " + self.nombre + " " + self.apellido + " y vivo en " + self.pais )

dami = UsuarioGeolocalizado()
print(dami.saludar())