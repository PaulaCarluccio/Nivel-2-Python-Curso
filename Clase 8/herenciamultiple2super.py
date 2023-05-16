class Uno(object):
    def __init__(self):
        super(Uno, self).__init__()
        print("1")
        

class Dos(object):
    def __init__(self):
        super(Dos, self).__init__()
        print("2")
        

class Tres(Uno, Dos):
    def __init__(self):
        super(Tres, self).__init__()
        print("3")
        

Tres()