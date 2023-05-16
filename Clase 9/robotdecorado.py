class Robot(object):
    def __init__(self, name, by):
        self.name = name
        self.build_year = by

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, newname):
        self._name = newname

    @property
    def build_year(self):
        return self._build_year

    @build_year.setter
    def build_year(self, y):
        self._build_year = "El año: " +str(y)
        
x = Robot("Mazinger", 1972)
#x.build_year = 1993
print(x.build_year)
print(x.name)