class HandGrenades:
    def __init__(self,atk):
        self.atk=atk
    def explode(self,target):
        if not isinstance(target,Life):
            raise ValueError('对象不能受伤')
        print('手雷爆炸啦')
        target.damage(self.atk)

class Life:
    def damage(self):
        pass

class Enemy(Life):
    def __init__(self,hp):
        self.hp=hp
    def damage(self,value):
        print('敌人受伤了')
        self.hp-=value
        if self.hp<=0:
            print('敌人死了')

class Player(Life):
    def __init__(self,hp):
        self.hp=hp
    def damage(self,value):
        print('玩家受伤了')
        self.hp-=value
        if self.hp<=0:
            print('玩家死了')


class Animal:
    def damage(self,value):
        print('小动物受伤啦')


a01=HandGrenades(100)
a02=Enemy(200)
a01.explode(a02)
