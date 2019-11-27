#fork進程演示
import  os
from time import sleep


pid=os.fork()

if pid<0:
    print('Error')
elif pid==0:
    print('Child process')
    print('a=',a)#從父進程空間獲取的a

else:
    print('Parent process')

print()