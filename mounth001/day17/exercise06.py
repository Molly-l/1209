list01=['无忌','翠山','翠翠']
def my_enumerate(l):
    w01=0
    for i in l:
        yield (w01,i)
        w01 +=1




for i in my_enumerate(list01):
    print(i)

