class Str01(str):
    def __sub__(self, other):
        return self.replace(other,'')

s1=Str01(123456)
s2=Str01(123)
print(s1-s2)



print(,mro())