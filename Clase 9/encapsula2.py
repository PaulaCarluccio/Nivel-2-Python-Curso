class Robot:
    def __init__(self, name=None, year=1900):
        self.__name = name
        self.__build_year = year            
    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name    

    def set_build_year(self, by):
        self.__build_year = by

    def get_build_year(self):
        return self.__build_year
        
        
bender = Robot("Bender", 2978)
bender.set_build_year(2900)
print(bender.get_name())
print(bender.get_build_year())