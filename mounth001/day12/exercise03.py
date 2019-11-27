 # Student_manager_system
class StudentModel:
    def __init__(self,name,age,score,id=0):
        self.id = id
        self.name=name
        self.age=age
        self.score=score
    def print_list(self):
        print(self.id,self.name,self.score,self.age)

class StudentManagerController:
    __stu_id=1001
    def __init__(self):
        self.__stu_list=[]

    @property
    def stu_list(self):
        return self.__stu_list

    def add_student(self,stu):
        stu.id=self.__generate_id()
        self.__stu_list.append(stu)

    def __generate_id(self):
        StudentManagerController.__stu_id+= 1
        return StudentManagerController.__stu_id

    # def remove_student(self,stu):
    #     count=0
    #     for item in range(len(self.__stu_list)-1,-1,-1):
    #         if self.__stu_list[item].id==stu.id:
    #             del self.__stu_list[item]
    #             count+=1
    #     if count:
    #         return True
    #     else:
    #         return False
    def remove_student(self, id):
        for item in self.__stu_list:
            if item.id==id:
                self.__stu_list.remove(item)
                return   True
        return False

    def update_student(self,stu):
        for item in self.__stu_list:
             if item.id==stu.id:
                 item.name=stu.name
                 item.age = stu.age
                 item.score = stu.score
                 return True
        raise ValueError('未找到对应的学员！')

    def order_by_score(self):

        for i in range(len(self.__stu_list)-1):
            for c in range(len(self.__stu_list)-1-i):
                if self.__stu_list[c].score>self.__stu_list[c+1].score:
                    self.__stu_list[c],self.__stu_list[c+1]=\
                    self.__stu_list[c+1], self.__stu_list[c]






manager=StudentManagerController()
s01=StudentModel('zs',18,50)
s02=StudentModel('lj',18,68)
s03=StudentModel('vb',18,90)
s04=StudentModel('ty',18,78)


manager.add_student(s01)
manager.add_student(s02)
manager.add_student(s03)
manager.add_student(s04)
print(manager.stu_list[0].name)
print(len(manager.stu_list))
# print(manager.remove_student(s01))
manager.order_by_score()

for i in manager.stu_list:
    i.print_list()



class StudentManagerView:
    def __init__(self):
        self.__manager=StudentManagerController()
    def main(self):

    def __input_student(self):
        name=input('输入姓名')
        age = input('输入年龄')
        score = input('输入成绩')
        stu=StudentModel(name,age,score)
        # manager=StudentManagerController()
        # manager.add_student(stu)
        self.__manager.add_student(stu)
    def __delete_student(self):
        id=int(input())
        self.__manager.remove_student(id)


    def __modify_student(self):
        id=int(input(''))
        name=int(input(''))
        =int(input(''))
        =int(input(''))
        stu=




