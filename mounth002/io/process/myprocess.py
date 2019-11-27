"""
自定义进程类
"""
from multiprocessing import Process

# 自定义类
class MyProcess(Process):
    def __init__(self,value):
        self.value = value
        super().__init__() # 加载父类init

    def f1(self):
        print("步骤1")

    def f2(self):
        print("步骤2")

    def run(self):
        self.f1()
        self.f2()

p = MyProcess(2)
p.start() # 执行run，作为一个子进程执行
p.join()