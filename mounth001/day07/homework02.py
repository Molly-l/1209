
def max01(a,b,c,d):
    # a=int(input('输入第一个数字'))
    # b=int(input('输入第二个数字'))
    # c=int(input('输入第三个数字'))
    # d=int(input('输入第四个数字'))
    max_value=a
    if max_value<b:
        max_value=b
    if max_value<c:
        max_value=c
    if max_value<d:
        max_value=d
    # print('输出',max_value)
    return max_value
print(max01(4,6,8,3))
