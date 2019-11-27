import time
from multiprocessing import Process
def my_time(f):
    def wrapper(*args,**kwargs):
        start_time=time.time()
        res=f(*args,**kwargs)
        end_time=time.time()
        print('%s函数执行时长:%.6f'%(f.__name__,end_time-start_time))
        return res
    return wrapper

# 判断一个数是否是质数
def isPrime(n):
    if n<=1:
        return False
    for i in range(2,int(n)):
        if n%i==0:
            return False
    return True
#自定义进程类
class Prime(Process):
    def __init__(self,prime,begin,end):
        super().__init__()
        self.prime=prime
        self.begin=begin
        self.end=end
    def run(self):
        for i in range(self.begin,self.end):
            if isPrime(i):
                self.prime.append(i)
            sum(self,prime)
@timeit
def use_10_process():
    prime = []
    jobs = []
    for i in range(1,100001,10000):
        p = Prime(prime,i,i+10000)
        jobs.append(p)
        p.start()
    [i.join() for i in jobs] # 回收进程

use_10_process()