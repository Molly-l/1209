import time

def time1(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        func(*args,**kwargs)
        end = time.time()
        print(end - start)
    return wrapper

@time1
def fun():

    print(45+952)

# fun = time1(fun)
fun()