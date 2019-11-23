import time
def fun(year,mounth,day):
    time_tuple=time.strptime('%d/%d/%d'%\
                  (year,mounth,day),'%Y/%m/%d')




if __name__=='__main__':
    print(fun(2019,8,3))
# def fun01(year,mounth,day):


try:
except ValueError:
    print('人数必须为整数')

else:
    print('没有异常发生')
finally:
