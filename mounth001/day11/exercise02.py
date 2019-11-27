class Dr:
    def __init__(self,name,xl):
        self.name=name
        # self.__xl=xl
        # self.set_xl(xl)
        self.xl=xl
    def print_dr(self):
        print(self.name,self.__xl)

    def get_xl(self):
        return self.__xl
    def set_xl(self,value):
        if 0<value<100:
            self.__xl=value
        else:
            raise ValueError('xlyc')
    xl=property(get_xl,set_xl)
a=Dr('孙悟空',65)



class Dr:
    def __init__(self,name,xl):
        self.name=name
        self.xl=xl
    def print_dr(self):
        print(self.name,self.__xl)
    @property
    def xl(self):
        return self.__xl
    @xl.setter
    def xl(self,value):
        if 0<value<100:
            self.__xl=value
        else:
            raise ValueError('xlyc')
    # xl=property(get_xl,set_xl)
a=Dr('孙悟空',65)




class Wife:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    
    def age(self):
        return self.__age
    def age(self,value):
        if 25<=value<=30:
            self.__age=value
        else:
            raise ValueError