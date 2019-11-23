a = int(input(''))
b = int(input(''))
c = int(input(''))
if c < a*b:
    print('钱不够')
else:
    print(c-a*b)

a=int(input('输入单价'))
b=int(input('输入数量'))
c=int(input('输入金额'))
res=c-a*b
if res<0:
    result='金额不足'
else:
    result='应找回：'+str(res)
# print(result)





