class Dos(object):
    def __init__(self):
        #super(Dos, self).__init__()
        self.t = "2"
        

class Tres(Dos):
    def __init__(self):
        super(Tres,self).__init__()
        #super().__init__()
        self.t += "3"
        print(self.t)

Tres()
print(Tres.__mro__)