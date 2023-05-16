class Uno(object):
    def __init__(self):
        super(Uno, self).__init__()
        self.nombre = "Dami"

class Dos(object):
    def __init__(self):
        super(Dos, self).__init__()
        self.nombre = "Damian"
        

class Tres(Uno, Dos):
    def __init__(self):
        super(Tres, self).__init__()
        #self.nombre = "Damian De"
        print(self.nombre)

Tres()