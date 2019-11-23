from mounth001.day18.list_helper import ListHelper


class Skill:
    def __init__(self, id, name=None, atk=None, duration=None):
        self.id = id
        self.name = name
        self.atk = atk
        self.duration = duration

    # 对象 --》 字符串
    def __str__(self):
        return self.name

list01 = [
    Skill(101,"乾坤大挪移",0,30),
    Skill(102,"九阳神功",0,50),
    Skill(103,"九阴白骨爪",500,10),
    Skill(104,"黑虎掏心",9800,40),
    Skill(105,"葵花宝典",6000,2),
]

def find01():
    for i in list01:
        if i.id==102:
            yield i
def find02():
    for i in list01:
        if i.name =="九阳神功":
            yield i
def sum(list):
    sum=0
    for i in list:
            sum+=i.atk
            yield i


#封装
# def condition01(i):
#     return i.id==102
# def condition02(i):
#     return i.name =="九阳神功"
# def find(func_condition):i.id==102
#     for item in list01:
#         if func_condition(item):
#             yield item


print(ListHelper.find(list01,lambda i:i.id==102).name)

print(ListHelper.find(list01,lambda i:i.name =="九阳神功").name)


# print(ListHelper.name_atk(list01,lambda i:(i.name,i.atk)).__next__())
for i in ListHelper.name_atk(list01,lambda item:(item.name,item.duration)):
    print(i)



re = ListHelper.find03(list01,lambda i:i.atk)
print(re.name)

ListHelper.order(list01,lambda i:i.atk)

for i in list01:
    print(i.name)
ListHelper.order(list01,lambda i:i.duration)
for i in list01:
    print(i)

ListHelper.pour_order(list01,lambda i:i.id)
for i in list01:
    print(i.id)

ListHelper.delete_atk(list01,lambda i:i.atk)
for i in list01:
    print(i)

