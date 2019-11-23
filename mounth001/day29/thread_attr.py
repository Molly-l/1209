from threading import Thread
from time import sleep


def fun():
    sleep(3)
    print('进程属性设置')

t=Thread(target=fun,name="AID")
t=Thread(target=fun)

t.setName()
print('name:',t.getName())

print('is alive:',t.is_alive())