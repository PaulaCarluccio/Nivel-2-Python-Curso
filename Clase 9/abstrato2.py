from abc import ABC, abstractmethod
class ErrorAbstracto(ABC):   
  @abstractmethod
  def test(self):
    self.mensaje = "Error"    

class ErrorInesperado(ErrorAbstracto):
  def test(self):
    super().test()
    return self.mensaje +" Inesperado"

#c = ErrorAbstracto()
c = ErrorInesperado()
print (c.test())