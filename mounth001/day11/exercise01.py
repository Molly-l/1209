# class Wife:
#     def __init__(self, name, age):
#         self.name=name
#         self.__age=age
#     def get_age(self):
#         return self.__age
#     def __set__(self,value):
#         if 25<=value<=30:
#             self.__age=value
#         else:
#             raise ValueError



class Dr:
    def __init__(self,name,xl,jcgj):
        self.name=name
        self.__xl=xl
        self.jcgj=jcgj
    def print_dr(self):
        print(self.name,self.__xl,self.jcgj)
    def get_xl(self):
        return self.__xl

    def set_xl(self,value):
        if 0<value<100:
            self.__xl=value
        else:
            raise ValueError('xlyc')
a=Dr('孙悟空',10,8)
# Dr('鲁班七号',36,2),
# Dr('后羿',45,7),
# Dr('灭霸',29,4)
a.set_xl(110)



