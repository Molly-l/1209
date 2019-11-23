# multiprocessing 模块创建进程
# 1.编写进程执行函数
# 2.创建进程对象
# 3.启动进程
# 4.回收进程
from time import sleep
import multiprocessing as mp
#进程函数
def fun(a,name):
    print('开始一个进程',a,name)
    sleep(3)
    print('进程结束')
#创建进程对象
p=mp.Process(target=fun,args=(5,),kwargs={'name':'zcc'})
p.start()#启动进程
p.join()#回收进程