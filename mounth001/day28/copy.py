"""
创建两个进程
分别复制上下两个部分
"""
from multiprocessing import Process
import os

filename = './timg.jpeg'
size = os.path.getsize(filename)

# 父进程打开文件
# fr = open(filename,'rb')
# print(fr.fileno())

# 上半部分
def top():
    fr = open(filename,'rb')
    print(fr.fileno())
    fw = open('top.jpg','wb')
    fw.write(fr.read(size//2))
    fr.close()
    fw.close()

# 下半部分
def bot():
    fr = open(filename, 'rb')
    print(fr.fileno())
    fw = open('bot.jpg', 'wb')
    fr.seek(size // 2)
    fw.write(fr.read())
    fr.close()
    fw.close()

p1 = Process(target=top)
p2 = Process(target=bot)
p2.start()
p1.start()
p1.join()
p2.join()
