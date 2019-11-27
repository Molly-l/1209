
#生成worker 消费者
from celery import Celery


#初始化celery对象
app=Celery('guo',broker='redis://@127.0.0.1:6379/1')

#创建消费者具体执行的内容
@app.task
def test_task():
    print('-----is runing----')