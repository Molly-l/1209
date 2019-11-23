#
# def len_my(list):
#     len01=0
#     for i in list:
#         len01+=1
#     return len01
#
# list01=[1,2,3,4]
# str01='hhhuyg'
# tuple01=('s','f','g')
# print(len_my(list01))
# print(len_my(str01))
# print(len_my(tuple01))


def min_01(list):
    min_value=list[0]
    for i in range(1,len(list)):
        if min_value>list[i]:
            min_value=list[i]
    return min_value
list01=[1,2,3,4,7,6,6,8,54,78,57]
print(min_01(list01))
def my_sum(list):
    sum_value=0
    # for i in range(len(list)):
    #     sum_value +=list[i]
    for i in list:
        sum_value+=i
    return sum_value
print(my_sum(list01))
# list01.insert(3,888)
# print(list01)
# def my_insert(list)
# k l
list01=[1,2,3,4,7,6,6,8,54,78,57]
# list01[3]=888
# list01[5]=list01[4]
def my_insert(list01,n,m):
    list01.append('')
    for i in range(len(list01)-1,n,-1):
        list01[i],list01[i-1]=list01[i-1],list01[i]
    list01[n]=m

my_insert(list01,5,888)
print(list01)
# print(list01)

def add(m,n):
    return m+n
# add(1,2)
add(2,5)