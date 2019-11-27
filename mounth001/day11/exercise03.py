class Skill:
    def __init__(self,name,gjbl,time,xhfl):
        self.name=name
        self.gjbl=gjbl
        self.time=time
        self.xhfl=xhfl
    def print_all(self):
        print(self.name,self.gjbl,self.time,self.xhfl)

    @property
    def gjbl(self):
        return self.__gjbl
    @gjbl.setter
    def gjbl(self,value):
        if 0.1<value<5:
            self.__gjbl=value
        else:
            raise ValueError('输入错误')

    @property
    def time(self):
        return self.__time
    @time.setter
    def time(self,value):
        if 0.1<value<10:
            self.__time=value
        else:
            raise ValueError('输入错误')

    @property
    def xhfl(self):
        return self.__xhfl
    @xhfl.setter
    def xhfl(self,value):
        if 0<value<100:
            self.__xhfl=value
        else:
            raise ValueError('输入错误')

list01=[
    Skill('降龙十八掌',0.2,4,65),
    Skill('神功',3,0.5,70),
    Skill('漂移',2,3,85),
    Skill('七十二变',4,6.5,10)
]

def find_name():
    for i in list01:
       if i.name=='降龙十八掌':
           return i


def del_xhfl():
    count=0
    for item in range(len(list01)-1,-1,-1):
        if list01[item].xhfl==0:
            del list01[item]
            count+=1
        return count

def name_time():
    # dict01={}
    # for i in list01:
    #     dict01[i.name]=i.time
    # return dict01
    return {i.name:i.time for i in list01}

def max_gjbl():
    max_gjbl=list01[0]
    for i in list01:
        if i.gjbl>max_gjbl.gjbl:
            max_gjbl=i
    return i
print('*')
max_gjbl().print_all()

def time_list():
    for j in range(len(list01)-1):
        for i in range(len(list01)-1-j):
            if list01[i].time>list01[i+1].time:
                list01[i],list01[i+1]=\
                    list01[i + 1],list01[i]

time_list()
for i in list01:
    i.print_all()
