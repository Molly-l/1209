# yuefen=int(input('输入月份'))
# if yuefen==1 or yuefen==2 or yuefen==3:
#     print('春')
# elif yuefen==4 or yuefen==5 or yuefen==6:
#     print('夏')
# elif yuefen==7 or yuefen==8 or yuefen==9:
#     print('秋')
# elif yuefen==10 or yuefen==11 or yuefen==12:
#     print('冬')
#
# # nl=int(input('输入年龄'))
# # if nl<0:
# #     print('输入错误')
# # elif 2<nl<13:
# #     print('儿童')
# # elif 13<nl<20:
# #     print('青年')
# # elif 20<nl<65:
# #     print('成年人')
# # elif 65<nl<130:
# #     print('老年人')
# # elif 130<nl:
# #     print('不可能')
#
# # m=float(input('输入身高'))
# # kg=float(input('输入体重'))
# # bmi=kg/m**2
# # if bmi<18.5:
# #     print('体重过低')
# # elif 18.5<=bmi<24:
# #     print('正常')
# # elif 24<=bmi<28:
# #     print('超重')
# # elif 28<=bmi<30:
# #     print('I度肥胖')
#
#
#
#
#
# I=float(input('输入利润'))
# money=0
# while money>0:
#     if I<=10:
#         money +=I*0.1
#
#     if 10<I<20:
#         if I<10:
#             money +=I*0.1
#         else:
#             money +=I*0.075
#     if 20<I<40:
#         if I>20:
#             money +=I*0.05
#     if 40<I<60:
#         if I>40:
#             money +=I*0.03
#     if 60<I<100:
#         if I>60:
#             money +=I*0.15
#     if I>100:
#         money +=I*0.01
#
# money +=money
# print(money)


# n=int(input('输入年'))
# y=int(input('输入月'))
# r=int(input('输入日'))
# month=1
# tian=0
# while month < y:
#     if month<1 or month>12:
#         print('输入有误')
#     elif month==4 or month==6 or month==9 or month==11:
#         tian +=30
#     elif month==2:
#         if n%4==0 and n%100!=0 or n%400==0:
#             tian += 29
#         else:
#             tian += 28
#     else:
#         tian +=31
#     month +=1
# tian +=r
# print(tian)



# num=100
# while num<1000:
#     g=num%10
#     s=num//10%10
#     b=num//100
#     if num==b**3+s**3+g**3:
#         print('输出',num)
#     num +=1











num=100
while num<1000:
    num+=1
    g=num%10
    s=num//10%10
    b=num//100
    if num==g**3+s**3+b**3:
        print('水花闲数是%d'%num)
set.

for i in range(100,1001):
    g = i% 10
    s = i // 10 % 10
    b = i // 100
    if i==g**3+s**3+b**3:
        print('')



n=int(input('输入'))
y=int(input('输入'))
t=int(input('输入'))
tian=0
for i in range(1,y):
    if i in [4,6,9,11]:
        tian +=30
    elif i==2:
        if n%4==0 and n%100!=0 or n%400==0:
            tian+=29
        else:
            tian+=28
    else:
        tian+=31

print(tian)





