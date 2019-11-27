class Dr:
    def __init__(self,name,xl,fl,jcgj,fyl):
        self.name=name
        self.xl=xl
        self.fl=fl
        self.jcgj=jcgj
        self.fyl=fyl
    def print_dr(self):
        print(self.name,self.xl,self.fl,self)


list01=[
Dr('孙悟空',0,8,6,7),
Dr('鲁班七号',36,2,4,3),
Dr('后羿',45,7,3,4),
Dr('灭霸',29,4,8,6)
]
def find():
    for i in list01:
        if i.name=='灭霸':
            print(i.name)
find()

def died():
    for i in list01:
        if i.xl==0:
            print(i.name)
died()
def pj():
    sum=0
    for i in list01:
        sum+=i.jcgj
    return sum/len(list01)

print(pj())
# def min_10():
#     for i in list01[::-1]:
#         if i.fyl<10:
#             list01.remove(i)
def min_10():
    for item in range(len(list01)-1,-1,-1):
        if list01[item].fyl<10:
            # list01.remove(list01[item])
            del list01[item]
def add():
    for i in list01:
        i.jcgj+=50
