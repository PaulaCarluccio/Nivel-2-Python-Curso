from abc import ABC, abstractmethod
class Abstracto(ABC):   
  @abstractmethod
  def test(self):
        return "Prueba"

class Abstractito(Abstracto):   
  #@abstractmethod
  def test(self):
        return "Prueba"

c = Abstractito()
print (c.test())