class Humano():
  def __init__(self,nombre,apellido):
    self.nombre = nombre
    self.apellido = apellido

class Ubicacion():
  def __init__(self,pais):    
    self.pais = pais
    
class UsuarioGeo(Humano,Ubicacion):
  def __init__(self,nombre,apellido,pais):    
    Humano.__init__(self,nombre,apellido)
    Ubicacion.__init__(self,pais)   
  def saludar(self):
    return("Hola, mi nombre es " + self.nombre + " " + self.apellido + " y vivo en " + self.pais )

user = UsuarioGeo("Damian","DL","Argentina")
print(user.saludar())