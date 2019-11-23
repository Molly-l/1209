class Graphics:
    def __init__(self):
        self.__list_graphic=[]
    @property
    def list_graphic(self):
        return self.__list_graphic
    def add_graphic(self,graphic):
        # if not is instance(graphic,Graphic):
        #     raise ValueError('错误')
        self.__list_graphic.append(graphic)
    def all_area(self):
        all_area=0
        for i in self.__list_graphic:
            all_area+=i.area()
        return all_area

class all_shape:
    def area(self):
        pass

class Circular(all_shape):
    def __init__(self,r):
        self.r=r
    def area(self):
        return self.r**2*3.14
class Rectangular(all_shape):
    def __init__(self,l,w):
        self.l=l
        self.w=w
    def area(self):
        return self.l*self.w
r=Circular(5)
w=Rectangular(10,20)
Meneger=Graphics()
Meneger.add_graphic(r)
Meneger.add_graphic(w)
print(Meneger.all_area())







class GraphicManager:
    def __init__(self):
        self.__graphic_list=[]
    @property
    def graphic_list(self):
        return self.__graphic_list
    def add_graphic(self,graphic):
        if not isinstance(graphic,Graphic):
            raise ValueError()#
        self.__graphic_list.append(graphic)
    def calc_total_area(self):
        total_area=0
        for i in self.__graphic_list:
            total_area+=i.area()
        return total_area



class Graphic:
    def calc_area:
        # 如果子类不重写父类的功能  异常
        raise NotImplement edError()

class Circle(Graphic):
    def __init__(self,r):
        self.r=r
    def area(self):
        return self.r**2

class Rectangle(Graphic):
    def __init__(self,l,w):
        self.l=l
        self.w=w
    def area(self):
        return self.l*self.w