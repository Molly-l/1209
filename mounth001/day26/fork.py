#fork進程演示
import  os

pid=os.fork()
if pid<0:
    print('Create process da')
elif pid==0:
    print()
else:
    print()

print()
