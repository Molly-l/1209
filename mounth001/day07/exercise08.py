# def add(num1,num2):
#     result=num1+num2
#     return result
# print(add(10,20))

def jia(num):
    """

    :param num:
    :return:
    """
    g=num%10
    s=num//10%10
    b=num//100%10
    q=num//1000
    he=g+s+b+q
    return he
print(jia(1234))


#
# input('输入')
# def add(num1,num2,num3,num4):
