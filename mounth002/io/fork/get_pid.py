#獲取進程PID號
import  os
from time import sleep

pid=os.fork()

if pid<0:
    print('Error')
elif pid==0:
    print('',os.getpid())#获取当前进程的进程号
    print('',os.getppid())#获取父进程的进程号

else:
    print('Get child PiD:',pid,os.getpid())#子进程,父进程
