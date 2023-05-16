class Humano():
  def __init__(self):
    self.nombre = "Dami"
    self.apellido = "De"
    #self.pais = "Tierra"

class Ubicacion():
  def __init__(self):    
    self.pais = "Argentina"
    
class UsuarioGeolozalizado(Humano,Ubicacion):
  def __init__(self):    
    Humano.__init__(self)
    Ubicacion.__init__(self)           
  def saludar(self):
    return("Hola, mi nombre es " + self.nombre + " " + self.apellido + " y vivo en " + self.pais )

dami = UsuarioGeolozalizado()
print(dami.saludar())