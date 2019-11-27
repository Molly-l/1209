dict01={}
while True:
    list01=[]
    name=input('名字')
    if name=='':
        print(dict01)
        break
    age=input('年龄')
    list01.append(age)
    gender=input('性别')
    list01.append(gender)
    weight=input('体重')
    list01.append(weight)
    dict01[name]=list01
for item in dict01:
    print('名字是%s，年龄是%s,性别是%s,体重是%s'%
          (item,dict01[item][0],dict01[item][1],
           dict01[item][2]))
for key,value in dict01.items():
    print('名字是%s，年龄是%s,性别是%s,体重是%s'%
          (key,value[0],value[1],value[2]))




