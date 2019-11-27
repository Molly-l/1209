class StudentModel:
    def __init__(self,name,age,score,id=0):
        self.name=name
        self.age=age
        self.score=score
        self.id=id
class StudentManagerController:
    __stu_id=0
    def __init__(self):
        self.__stu_list=[]
    @property
    def stu_list(self):
        return self.__stu_list

    def add_student(self,stu):
        stu.id=self.gener()
        self.__stu_list.append(stu)

    def gener(self):
        StudentManagerController.__stu_id +=1
        return StudentManagerController.__stu_id

    def remove_student(self,id):
        for item in self.__stu_list:
            if item.id==id:
                self.__stu_list.remove(item)


    def update_student(self,id,name,age,score):
        for i in self.__stu_list:
            if i.id==id:
                i.name=name
                i.age=age
                i.score=score

    def order_by_score(self):
        for i in range(len(self.__stu_list)-1):
            for c in range(i+1,len(self.__stu_list)):
                if int(self.__stu_list[i].score)>int(self.__stu_list[c].score):
                    self.__stu_list[i],self.__stu_list[c]=\
                    self.__stu_list[c], self.__stu_list[i]

# c=StudentManagerController()
# stu=StudentModel(1,2,3,4)
# c.add_student(stu)
# print(c.stu_list[0].name)
class StudentManagerView:

    def __init__(self):
        self.view=StudentManagerController()
    def __display_menu(self):
        print('+---------------------+')
        print('| 1)添加学生信息        |')
        print('| 2)显示学生信息        |')
        print('| 3)删除学生信息        |')
        print('| 4)修改学生信息        |')
        print('| 5)按照成绩升序排序     |')
        print('+---------------------+')

    def __select_menu_item(self):
        qw=input('输入：')
        if qw=='1':
            self.__input_students()
        elif qw=='2':
            self.__output_students()
        elif qw=='3':
            self.__delete_student()
        elif qw=='4':
            self.__modify_student()
        elif qw=='5':
            self.__order()
    def main(self):
        while True:
            self.__display_menu()
            self.__select_menu_item()

    def __input_students(self):
        name=input('输入名字')
        age=input('输入年龄')
        score=input('输入成绩')
        stu=StudentModel(name,age,score)
        self.view.add_student(stu)
    def __output_students(self):

        for i in self.view.stu_list:
            print(i.name,i.age,i.score,i.id)

    def __delete_student(self):
        id=int(input('输入id'))
        self.view.remove_student(id)

    def __modify_student(self):
        name=input('输入名字')
        age=input('输入年龄')
        score=input('输入成绩')
        id = int(input('输入id'))

        self.view.update_student(id,name,age,score)
    def __order(self):
        self.view.order_by_score()
view=StudentManagerView()
view.main()
