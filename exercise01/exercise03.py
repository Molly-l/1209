# state='偶数' if int(input('输入整数'))%2==0  else '奇数'
# print(state)

# year=int(input('输入一个年份'))
# day = 29 if year % 4 == 0 and year % 100 !=0 or year % 400==0 else 28
# print(day)


# while True:
#     dol=int(input('输入美元'))
#     print(dol*6.9)
#     if input('输入exit退出')=='exit':
#         break

# while True:
#     jidu = input('请输入一个季度')
#     if jidu == '春':
#         print('1月2月3月')
#     elif jidu == '夏':
#         print('4月5月6月')
#     elif jidu == '秋':
#         print('7月8月9月')
#     else:
#         print('10月11月12月')
#     if input('输入e退出')=='e':
#         break

# count=0
# while count<3:
#     dol=int(input('输入美元'))
#     print(dol*6.9)
#     count+=1

# count=0
# while count<6:
#     print(count)
#     count+=1

# count=2
# while count<8:
#     print(count)
#     count+=1

# count=0
# while count<=8:
#     print(count)
#     count+=2

# count=2
# while count<=20:
#     print(count)
#     count+=2
#

count =1
while count <= 20:
    if count%2==0:
        print(count)
        count += 1
