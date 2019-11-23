import time
print(time.time())
print(time.localtime())
def fun(year,mounth,day):
    time_tuple=time.strptime\
        ('%d/%d/%d'%(year,mounth,day),'%Y/%m/%d')
    tl=time.mktime(time_tuple)
    s=time.time()-tl
    print(s/24/60/60)
fun(2019,1,1)