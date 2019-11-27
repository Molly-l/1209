class Person:
    def __init__(self,name):
        self.name=name
    def go_to(self,place):
        print(self.name,'去',place.name)
        place.take()

class Place:
    def __init__(self,name,money):
        self.name = name
        self.money=money
    def take(self):
        print('取钱')


xiaoming=Person('小明')
w02=Place('银行',10000000000000000)
xiaoming.go_to(w02)
# w02.take()



#小明去银行取钱
class Person:
    def __init__(self, name, money=None):
        self.name=name
        self.money=money
class bank:
    def __init__(self, money=None):
        self.money=money
    def draw_money(self,target,value):
        if value<=0:
            raise ValueError('value不能小于0')
        print(target.name,'在取',value,'钱')
        self.money-=value
        target.money+=value
        print('%s现在有%s钱'%(target.name,target.money))
xm=Person('小明',0)
zs=Bank(10000)
zs.draw_money(xm,1000)
print(zs.draw_money(xm,-1000))
zs.draw_money(xm,1000)

