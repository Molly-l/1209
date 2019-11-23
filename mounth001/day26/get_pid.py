#獲取進程PID號
import  os
from time import sleep

pid=os.fork()

if pid<0:
    print('Error')
elif pid==0:
    print('',os.getpid())
    print('',os.getpid())

else:
    print('Get child PiD:',pid)
