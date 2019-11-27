"""
queue_0.py  消息队列演示
注意 : 通过一个对象操作队列，满足先进先出原则
"""

from multiprocessing import Queue,Process
from time import sleep
from random import randint

# 创建消息队列
q = Queue(5)

# 请求进程
def request():
    for i in range(10):
        sleep(0.5)
        t = (randint(1,100),randint(1,100))
        q.put(t)
        print("=====================")

# 数据处理进程
def handle():
    while True:
        sleep(2)
        x,y = q.get()
        print("数据处理结果 x + y=",x + y)

p1 = Process(target=request)
p2 = Process(target=handle)
p1.start()
p2.start()
p1.join()
p2.join()


