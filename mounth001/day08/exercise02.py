def num(list):

    for i in range(len(list)-1):
        for a in range(i+1,len(list)):
            if list[i]>list[a]:
                list[i],list[a]=list[a],list[i]
    # return
list = [1, 5, 13, 2, 4]
num(list)
print(list)


def fun01(row,col,char='*'):
    for r in range(row):
        for c in range(col):
            print(char,end='')
        print()
fun01(3,3)
fun01(3,3'-')