from threading import Thread
from time import sleep,ctime

class MyClass(Thread):
    #
    def __init__(self):
        super().__init__()

def player(sec,song):
    for i in range(3):
        print('playing %s:%s'%9)