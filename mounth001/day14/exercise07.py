class Num:
    def __init__(self,x):
        self.x=x

    def __add__(self, other):
        return Num(self.x+other)
    def __str__(self):
        return str(self.x)
    def __radd__(self, other):
        return Num()
    def __iadd__(self, other):#实现在原对象基础上变化值
        self.x +=other
        return self

e01=Num(10)
print(e01,id(e01))
e01+=2
print(e01,id(e01))
print(e01+2)
print(2+e01)
# e01=Num(5)
# print(e01-2)