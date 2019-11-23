a=1
def fu():
    a=100
    print(a)
    def fu1():
        a=1000
        print(a)
    fu1()
fu()
print(a)