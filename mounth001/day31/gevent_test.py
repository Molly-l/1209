import gevent
#导入脚本执行time模块操作
from gevent import monkey
monkey.patch_time()
from time import sleep
#协程函数
def foo(a,b):
    print('Running foo ..',a,b)
    sleep(3)
    print('Foo again')
#生成携程对象
f=gevent.spawn(foo,1,2)
gevent.joinall([f])#阻塞等待f执行完