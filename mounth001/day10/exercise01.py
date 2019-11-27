# 类：
class Wife:
    # 数据成员
    # 身高 体重 姓名
    def __init__(self):#双下划线
        self.height=2.2
        self.weight=90
        self.name='翠花'
    # 行为成员
    # 唱歌 玩

    pass
# 创建对象
w01=Wife()
print(w01)
# w01的身高 为 2.2
# w01.txt.height=2.2
print(w01.height)
# w01.txt.weight=90
print(w01.weight)
# w01.txt.name='翠花'
print(w01.name)
w02=Wife()
print(w02.name)

def sing(self):
    print('%s正在唱歌'% self.name)
def play(self,game):
    print('%s正在玩游戏'% (self.name,game))


class Wife2:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def print_self(self):


class Dog:
    def __init__(self,name,kinds,color):
        self.name=name
        self.kinds=kinds
        self.color=color
    def eat(self,food):
        print('%s正在吃xx'% (self.name,food))
    def run(self,speed):
        print('%s%s正在以%skm/h的速度飞奔'%
              (self.color,self.kinds,speed))

wangcai=Dog('旺财','中华田园犬','黄色')
wangcai.eat('骨头')
wangcai.run(40)
dou=wangcai
dou.eat('狗粮')
