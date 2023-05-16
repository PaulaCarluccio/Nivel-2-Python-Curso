class Cantante:
  def __init__(self): 
    self.name = 'Freddie'
    #Atributo privado
    self.__lastname = 'Mercury'
    
  def PrintName(self):
    return self.name +' ' + self.__lastname
    
P = Cantante()
print(P.name)
print(P.PrintName())
#print(P.__lastname)