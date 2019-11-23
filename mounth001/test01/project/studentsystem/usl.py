from mounth001.test01.project.studentsystem.bll import StudentManagerController
from mounth001.test01.project.studentsystem.model import StudentModel


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
