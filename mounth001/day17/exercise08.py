class Skill:
    def __init__(self, id, name=None, atk=None, duration=None):
        self.id = id
        self.name = name
        self.atk = atk
        self.duration = duration
    def __str__(self):
        return self.name

list01 = [
    Skill(101,"乾坤大挪移",8000,30),
    Skill(102,"九阳神功",9000,50),
    Skill(103,"九阴白骨爪",500,10),
    Skill(104,"黑虎掏心",9800,40),
    Skill(105,"葵花宝典",6000,2),
]
# for i in (i for i in list01 if i.id==103):
#     print(i)

def find03():
    for i in list01:
        yield i.name#返回多个结果


for i in (i.name for i in list01):
     print(i)
