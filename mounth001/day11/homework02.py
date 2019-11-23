class Player:
    def __init__(self,name,hp,atk):
        self.name=name
        self.hp=hp
        self.atk = atk
    def gj(self,obj):
        obj.hp=obj.hp-self.atk
        if obj.hp<=0:
           obj.die()
    def die1(self):
        print('游戏结束')


class Enemy:
    def __init__(self,name,hp,atk):
        self.name = name
        self.hp=hp
        self.atk=atk
    def gj(self,obj02):
        obj02.hp-=self.atk
        if obj02.hp<=0:
            obj02.die1()

    def die(self):
        print('播放动画')

wanjia=Player('玩家',50,30)
diren=Enemy('敌人',90,20)
wanjia.gj(diren)
print(diren.hp)
wanjia.gj(diren)

diren.gj(wanjia)
print(wanjia.hp)

wanjia.gj(diren)
print(diren.hp)




# 玩家(攻击力)攻击敌人(血量)敌人受伤(减血)可能死亡(播放动画)

# 敌人攻击玩家 玩家受伤(减血 碎屏) 可能死亡(游戏结束)

#玩家类
class Player:
    def __init__(self, hp=100, atk=10):
        self.hp=hp
        self.atk=atk
    def attack(self):

class Enemy:



