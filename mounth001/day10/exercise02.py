# class Student:
#     def __init__(self,name,age,score):
#         self.name=name
#         self.age=age
#         self.score=score
#     def show_student(self):
#         print('学生%s,年龄%d,成绩%f'%
#               (self.name,self.age,self.score))
#
# list01=[
#     Student('hjl',45,95),
#     Student('赵敏',12,89),
#     Student('无忌',20,56)]
# def fun01(name):
#     for i in list01:
#         if i.name==name:
#             return i
# stu01=fun01('赵敏')
# print(stu01.age)
#
# def fun02():
#     list1=[]
#     for i in list01:
#         if i.age<30:
#             list1.append(i)
#     return list1
#
# result=fun02()
# for i in result:
#     print(i.name)
#
# def del01():
#     for i in list01:
#         if i.score<60:
#             list01.remove(i)
# del01()
# for i in list01:
#     print(i.name)

# 类方法
# @classmethod
# 保存当前类的地址





#
# class Wife:
#     w=0
#     @classmethod
#     def print_w(cls):
#         print(cls.w)
#     def __init__(self,name):
#         self.name=name
#         Wife.w +=1
#
# w1=Wife('小敏')
# w2=Wife('小红')
# w3=Wife('小芳')
# Wife.print_w()
#


class Jieq:
    def __init__(self,name,money):
        self.name=name
        self.money=money


        
    def borrow(self,obj):
        obj.money-=5000
        self.money+=5000

xiaoming=Jieq('小明',10000)
xiaobai=Jieq('小白',1000)

xiaobai.borrow(xiaoming)

print('小明剩余：',xiaoming.money)
print('小白剩余：',xiaobai.money)






