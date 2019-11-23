# a = int(input(''))
# b = int(input(''))
# c = int(input(''))
# if c < a*b:
#     print('钱不够')
# else:
#     print(c-a*b)
def pay(a,b,c):
    # a=int(input('输入单价'))
    # b=int(input('输入数量'))
    # c=int(input('输入金额'))
    return c-a*b
print(pay(10,5,80))


def money(dol):
# while True:
#     dol=int(input('输入美元'))
#     print(dol*6.9)
    # if input('输入exit退出')=='exit':
    #     break
    return dol*6.9
print(money(8))
