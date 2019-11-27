# 进程
# 线程
# 锁
# 队列
# cookie,session,token

def fu(a=5,b=2):
    return a+b
print(fu(6))

a=[1,2,3]
b=a.__iter__()
for i in a:
    b.__next__()
    print(i)
while True:
    pass
b=a
c=b
d=c
a=c


# del a
a.remove(1)
print(b)
