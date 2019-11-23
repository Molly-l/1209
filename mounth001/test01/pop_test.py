list01=[1,2,3,4,7,6,6,8,54,78,57]
# a=list01.pop(3)
# print(a,list01)
# my_pop(list,n)
# for i in range(len(list01))
# my_del(list01,n)
def my_del(list01,n):
    for i in range(n,len(list01)-1):
        list01[i],list01[i+1]=list01[i+1],list01[i]
    # list[::-1],
    list02=list01[:len(list01)-1]
    return list02

print(my_del(list01,4))