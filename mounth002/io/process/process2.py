"""
同时创建多个子进程
"""

from multiprocessing import Process
from time import sleep
import os

def th1():
    sleep(3)
    print("吃饭")
    print(os.getppid(),'--',os.getpid())

def th2():
    # a = input()   # 不能使用标准输入
    sleep(2)
    print("睡觉")
    print(os.getppid(),'--',os.getpid())

def th3():
    sleep(4)
    print("打豆豆")
    print(os.getppid(),'--',os.getpid())

things = [th1,th2,th3]
jobs = []
for th in things:
    p = Process(target = th)
    jobs.append(p) # 列表存储一下进程对象
    p.start()#三个进程同时开启

for i in jobs:
    i.join()








