season=input('输入一个月份')
if season=='春':
    print('1月2月3月')
if season=='春':
    print('4月5月6月')
if season=='春':
    print('7月8月9月')
if season=='春':
    print('10月11月12月')

# 老王买包子
#买4个包子
#如果看到卖西瓜的 就买一个
#输出老王买了多少包子
op=input('是否有卖西瓜的？')
if op=="是":
    count=1
elif op=="否":
    count=4
print('买了'+str(count)+'包子')


#输入一个数字
#再输入一个运算符  + - * /
#最后输入另一个数字
#根据运算符计算两个数字
#要求 如果运算符 不是加减乘除 提示 运算符有误
num1=int(input('一个数字'))
op=input('输入一个运算符')
num2=int(input('另一个数字'))
if op=='+':
    print(num1+num2)
elif op=='-':
    print(num1-num2)
elif op=='*':
    print(num1*num2)
elif op=='/':
    print(num1/num2)
else:
    print('运算符有误')


#再控制台分别输入4个数字
#打印最大的数字
num1=int(input('输入第一个数字'))
num2=int(input('输入第二个数字'))
num3=int(input('输入第三个数字'))
num4=int(input('输入第四个数字'))
max_value=num1
if max_value<num2:
    max_value=num2
if max_value<num3:
    max_value=num3
if max_value<num4:
    max_value=num4
print(max_value)


#在控制台输入一个月份 打印对应的天数
#1 3 5 7 8 10 12  --->31天
#4 6 9 11 ---> 30天
#2  ---> 28天或29天
#其它 提示输入有误
month=int(input('输入一个月份'))
if month<0 or month>12:
    print('输入有误')
elif month==2:
    year = int(input('输入年'))
    if year%4==0 and year%100!=0 or year%400==0:
        print('输出28天')
    else:
        print('输出29天')
if month==4 or 6 or 9 or 11:
    print('输出30天')
else:
    print('输出31天')


#在控制台获取一个整数
# 如果是偶数 为变量state赋值'偶数' 否则赋值 '奇数'
num=int(input('输入一个整数'))
if num%2==0:
    state='偶数'
else:
    state='奇数'
print(state)
#条件表达式
state='偶数' if num%2==0 else '奇数'
print(state)


#死循环  循环条件永远满足/直到按e键退出
#练习在控制台获取一个季度 (春夏秋冬)
#显示相应的月份
#春   1月2月3月
#夏   4 5 6
#秋   7 8 9
#冬   10 11 12
while True:
    season = input('输入一个月份')
    if season == '春':
        print('1月2月3月')
    elif season == '春':
        print('4月5月6月')
    elif season == '春':
        print('7月8月9月')
    elif season == '春':
        print('10月11月12月')
    if input('输入e退出')=='e':
        break


#在控制台输出0 1 2 3 4 5
count=0
while count<6:
    print(count)
    count +=1
#在控制台输出 1~20之间的偶数
#循环找到1～20的数字
#判断 如果是偶数就输出
count=1
while count<21:
    if count%2==0:
        print(count)
        count += 1


# 在控制台获取输入的月份 显示对应的季度 或提示月份错误
#
#
#


#猜数字 导入随机模块
#产生一个从1到100之间的随机数
import random
random_number=random.randint(1,100)
print(random_number)
#用户输入一个数字 电脑随机生成一个数字
#判断用户输入的数字和电脑随机生成的数字是否相同
  # 如果相同 提示猜对了
  # 如果用户输入的大 提示猜大了
  # 否则    提示猜小了
input_num=int(input('输入1~100的数字'))
if input_num==random_number:
    print('猜对了')
elif input_num>random_number:
    print('猜大了')
else:
    print('猜小了')
#1.重复执行以上代码 直到猜对为止
while True:
    input_num = int(input('输入1~100的数字'))
    if input_num == random_number:
        print('猜对了')
        break
    elif input_num > random_number:
        print('猜大了')
    else:
        print('猜小了')
#2.重复执行三次代码
# 如果用户猜对了 提示:“猜对了，总共猜了xx次”
# 如果用户三次没猜对 提示用户 “你输了正确的数字是xx”
#统计循环的次数
count=0
while count<3:
    count +=1
    input_num = int(input('输入1~100的数字'))
    if input_num == random_number:
        print('猜对了，总共猜了%d次'%count)
        break
    elif input_num > random_number:
        print('猜大了')
    else:
        print('猜小了')
else:
    print('你输了正确的数字是'+str(random_number))


#打印数字0 1 2 3
#for+range(次数)  执行预定的次数
for i in range(4):
    print(i)
#累加 0 1 2 3
sum_value=0
for i in range(4):
    sum_value +=i
    print(sum_value)
#累加 3 5 7 9
sum_value=3
for i in range(3,10,2):
    sum_value +=i
    print(sum_value)
#输出数字4 3 2 1 0
for i in range(4,-1,-1):
    print(i)

#假设一张纸0.0001米
#折纸10次 求厚度
#珠穆朗玛峰 8848米 求一张纸对折多少次能达到8848米
a=0.0001
for i in range(10):
    a *=2
print(a)
count=0
while a<8848:
    count +=1
    a *=2
print(count)


#随机加法考试
# import random
#随机生成两个数字
#在控制台获取用户输入的两个数字相加的结果
   #3+2=？  5
   #8+5=？  3  x
#如果用户输入正确得20分
# 共5道题
# 保存分数
import random
score=0
for i in range(5):
    random_num01=random.randint(0,100)
    random_num02=random.randint(0,100)
    prompt=str(random_num01)+'+'+str(random_num02)+'=?'
    input_num=int(input(prompt))
    if input_num==random_num01+random_num02:
        score +=20
print(score)


#累加10~50之间的个位不是3 6 9的数字
#10+11+12+14+15+17+18+20...

#获取所有10~50的数字
#获取数字的个位 如果是 3 6 9 跳过
#如果不是 累加
#输出结果
sum_number=0
# for i in range(10,51):
#     unit=i%10
#     if unit==3 or unit==6 or unit==9:
#         continue
#     sum_number +=i
n=10
while n<51:
    unit=n%10
    if unit == 3 or unit == 6 or unit == 9:
        n += 1
        continue
    sum_number +=n
    n +=1
print(sum_number)

# 在控制台输入整数作为边长 打印如下
# 如果输入4
# ****
# *  *
# *  *
# ****
# 如果输入 5
# *****
# *   *
# *   *
# *   *
# *****
num=int(input('输入一个整数'))
print('*'*num)
for i in range(num-2):
    # print('*'+(num-2)+'*')
    print('*%s'%(' '(num-2)))
print('*'*num)

# 2.在控制台输入一个字符串 判断是否为回文
# 判断规则正向与反向相同
# 上海自来水来自海上
zfc=input('输入字符串')
if zfc==zfc[::-1]:
    print('是回文')
else:
    print('不是回文')


#在控制台输入一个字符串
#打印  第一个字符是xx
#打印  倒数第二个字符是xx
#打印  前2个字符是xx
#倒序打印所有字符串
#打印所有正向索引是奇数的字符
# 0 1 2 3 4 5
#如果字符串的长度是奇数 则打印中间的字符
#  如 12345 ———> 3
zfc=input('输入字符串')
print('第一个字符是%s'%zfc[0])
print('倒数第二个字符是%s' % zfc[-2])
print('前2个字符是%s' % zfc[:2])
print(zfc[::-1])
print(zfc[1::2])
length=len(zfc)
if length%2==1:
    print(zfc[length//2])

'''列表的索引赋值'''
list01 = ['a','b','c']
#['a','b'] = [0,1,2]
list01[0:2] = [0,1,2]
print(list01)#[0, 1, 2, 'c']
#通过切片获取到三个元素 修改为0个元素（删除）
list01[:3] = []
print(list01)

#定义列表 存储八大行星
#水 金 地 火 木 土 天王 海王
#打印 距离太阳最近的行星是xx
#打印 距离太阳最远的行星是xx
#打印 太阳到地球之间的行星
#倒序打印 八大行星(从又向左 一行一个)
list_planets = ['水星','金星','地球','火星','木星','土星','天王星','海王星']
print('距离太阳最近的行星是%s' % list_planets[0] )
print('距离太阳最远的行星是%s' % list_planets[-1] )
print(list_planets[0:2])
#打印 八大行星(一行一个)
for item in list_planets:
    print(item)
#如果采用切片的方式 会重新创建新列表 不建议
for i in list_planets[::-1]:
    print(item)
#建议通过索引 在原列表直接查找对应位置的值
for i in range(len(list_planets)-1,-1,-1):
    print(list_planets[item])


#在控制台获取学生姓名 (循环输入 一个一个录入)
#将输入结果保存到列表
#如果输入的是空字符串  则停止录入
#打印所有学生姓名
name_list=[]
while True:
    name=input('输入姓名')
    if name=='':
        break
    name_list.append(name)
# 打印列表的每一个元素
for name in name_list:
    print(name)

#在控制台获取所有学生的成绩(循环 一个一个录入)
#如果录入空字符串 停止
#输出最高分 最低分 和平均分
score_list=[]
while True:
    str=input('输入字符串')
    if str=='':
        break
    score=int(str)
    score_list.append(score)
print(max(score_list))
print(min(score_list))
print(sum(score_list)/len(score_list))


list01 = [3,45,8,12,36,7,3]
#         0  1 2 3  4  5 6
#把list01中大于10的数字存入另一个列表
result_list=[]
for i in list01:
    if i>10:
        result_list.append(i)
print(result_list)

# 获取list01中最大的数 不使用max()
#假设最大值为列表的第一个数
max_value=list01[0]
for item in list01:
    if i>max_value:
        max_value=item

for i in range(1,len(list01)):
    if list01[i]>max_value:
        max_value=list01[i]
print(max_value)

#删除列表list01中所有的奇数
for item in list01:
    if item%2:
        list01.remove(item)
print(list01)
# 倒序删除
for i in range(len(list01)-1,-1,-1):
    if list01[i]%2:
        # list01.remove(list01[i])
        del list01[i]
print(list01)

list01=[]
for i in range(101):
    list01.append(i)
