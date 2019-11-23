class FurnitureModel:#家居数据模型类
    def __init__(self,name,size):
        self.name=name
        self.size=size
class Controller:#房子类
    def __init__(self):
        self.__house_list=[

        ]
    @property
    def house_list(self):
        return self.__house_list
    def add_furniture(self,jiaju):
        self.__house_list.append(jiaju)

    def display_jiaju(self):
        for i in self.__house_list:
            print(i.name,i.size)

    def sum_area(self):
        area=0
        for i in self.__house_list:
            area+=int(i.size)
        return area
        # return area
xiaomingjia=Controller()

guizi=FurnitureModel('柜子','5')
guizi1=FurnitureModel('桌子','3')
guizi2=FurnitureModel('床','8')
xiaomingjia.add_furniture(guizi)
xiaomingjia.add_furniture(guizi1)
xiaomingjia.add_furniture(guizi2)

area=xiaomingjia.display_jiaju()
print(area)
print(None)