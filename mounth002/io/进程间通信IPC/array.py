"""
array.py 存放一组数据
"""

from multiprocessing import Process,Array

# 共享内存，初始[1,2,3,4,5]
# shm = Array('i',[1,2,3,4,5])
# shm = Array('i',4) #共享内存，初始[0,0,0,0]
shm = Array('c',b'Hello')

def fun():
    # 迭代获取共享内存值
    for i in shm:
        print(i)
    shm[0] = b'h'

p = Process(target = fun)
p.start()
p.join()
# for i in shm:
#     print(i)
print(shm.value)  # 用于打印共享内存字节串