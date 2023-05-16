class Mensaje(object):
  def __init__(self, texto):
    print('Mensaje: ' + texto)

class Error(Mensaje):
  def __init__(self):    
    super().__init__('Error')    


m = Error()