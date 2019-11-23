class MyRangeIterator:
    def __init__(self,i):
        self.__i=i
        self.__index= -1
    def __next__(self):
        if self.__index>=self.__i-1:
            raise StopIteration
        self.__index+=1
        return self.__index
class MyRangeManager:
    def __init__(self,stop):
        self.stop=stop
    def __iter__(self):
        return MyRangeIterator(self.stop)

for item in MyRangeManager(5):
    print(item)






# w01.txt=MyRangeManager(5).__iter__()
# while True:
#     try:
#         item=w01.txt.__next__()
#         print(item)
#     except StopIteration:
#         break

