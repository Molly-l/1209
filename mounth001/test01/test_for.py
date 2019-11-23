# list01=[]
# for i in range(101):
#     list01.append(i)
# print(list01)
# num=0
# for i in list01:
#     if i%2:
#         num+=i
# print(num)

# count=0
# while count<3:
#
#     name=input('输入用户名')
#     if name!="tarena":
#         print("用户名错误，请重新输入")
#         count += 1
#         continue
#     mima=input('输入密码')
#     if mima!="123456":
#         print('密码错误，请重新输入')
#         count += 1
#         continue
#
#     print('登录成功')


str01="welcome*to*beijing"
list01=str01.split(' ')
list02=str01.split('*')

for i in range(len(list01)):
    list01[i]=list01[i][::-1]

str1='*'.join(list01)

print(str1)
# str1=''
# for i in range(len(list01)-1):
#     str1 +=list01[i]
#     str1 +=' '
# str1 +=list01[len(list01)-1]
# print(str1)


