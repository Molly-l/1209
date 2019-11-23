class Skill:
    def __init__(self, id, name=None, atk=None, duration=None):
        self.id = id
        self.name = name
        self.atk = atk
        self.duration = duration
    def __str__(self):
        return '%s%s%s%s'%(self.id,self.name,self.atk,self.duration)

list01 = [
    Skill(101,"乾坤大挪移",8000,30),
    Skill(102,"九阳神功",9000,50),
    Skill(103,"九阴白骨爪",500,10),
    Skill(104,"黑虎掏心",9800,40),
    Skill(105,"葵花宝典",6000,2),
]


# def find():
#     for i in list01:
#         if i.duration>10:
#             yield i
#
# def find01():
#     for i in list01:
#         if 102<i.id<105:
#             yield i



def condition01(i):
    return i.duration>10
def condition02(i):
    return 102<i.id<105

def find02(func_condition):
    for i in list01:
        # if i.duration > 10:
        if func_condition(i):
            yield i

for i in find02(condition01):
    print(i)
for i in find02(condition02):
    print(i)