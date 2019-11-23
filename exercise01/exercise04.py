# season=input('输入季度')
# if season=='春':
#     print('1月2月3月')
# elif season=='夏':
#     print('4月5月6月')
# elif season=='秋':
#     print('7月8月9月')
# elif season=='冬':
#     print('10月11月12月')


# num1=float(input('输入第一个数：'))
# op=input('输入运算符')
# num2=float(input('输入第二个数：'))
# if op=='+':
#     print(num1+num2)
# elif op=='-':
#     print(num1-num2)
# elif op=='*':
#     print(num1*num2)
# elif op=='/':
#     print(num1/num2)
# else:
#     print('运算符有误')

# num1=float(input('输入第一个数字：'))
# num2=float(input('输入第二个数字：'))
# num3=float(input('输入第三个数字：'))
# num4=float(input('输入第四个数字：'))
# max_value=num1
# if max_value<num2:
#     max_value=num2
# if max_value<num3:
#     max_value=num3
# if max_value<num4:
#     max_value=num4
# print(max_value)

# month=int(input('输入月份:'))
# if month<1 or month>12:
#     print('输入有误')
# elif month==4 or month==6 or month==9 or month==11:
#     print('30天')
# elif month==2:
#     print('28天')
# else:
#     print('31天')

num=int(input('输入一个整数'))
if num%2==1:
    state='奇数'
else:
    state='偶数'
