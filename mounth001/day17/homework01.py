class Enemy:
    def __init__(self,name,hp=None,atk=None,defense=None):
        self.name=name
        self.hp=hp
        self.atk=atk
        self.defense=defense
    def __str__(self):
        return "%s%s%s%s"%(self.name,
            self.hp,self.atk,self.defense)
list01=[
    Enemy('孙悟空',10,8,12),
    Enemy('鲁班七号',0,9,10),
    Enemy('后羿',45,7,9),
    Enemy('灭霸',29,4,8)
]
# def find_die():
#     for i in list01:
#         if i.hp==0:
#             yield i.name
def max_hp():
    max_hp=list01[0].hp
    max=list01[0]
    for i in list01:
        if max_hp<i.hp:
            max_hp=i.hp
            max=i
    return max

def find01():
    for i in list01:
            yield i.name,i.atk
#
def condition01(i):
    return i.hp==0
# def condition02(i,max_hp):
#     return max_hp<i.hp
# def condition03(i):
#     return i.name,i.atk

def find(func_condition):
    for i in list01:
        if func_condition(i):
            yield i

for i in find(condition01):
    print(i)

print(max_hp())

# for i in find(condition02):
#     print(i)
for i in find01():
    print(i)
# w01.txt=Enemy()
# w01.txt.max_hp(i)

# for i in max_hp:
#     print(i)
