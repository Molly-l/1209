class Enemy:
    def __init__(self,name,hp,atk):
        self.name=name
        self.hp=hp
        self.atk=atk
    def __str__(self):#打印数据
        return '名字%s,血量%d,攻击力%d'%\
               (self.name,self.hp,self.atk)
    def __repr__(self):#
        return 'Enemy("%s",%d,%d)'%\
        (self.name,self.hp,self.atk)
e01=Enemy('小明',100,50)
print(e01)
e02=eval(repr(e01))
e02.name='老王'
print(e02)