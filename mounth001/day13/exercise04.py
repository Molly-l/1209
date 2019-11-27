class StudentModel:#数据模型类
    def __init__(self,name,age,score,id=0):
        self.id=id
        self.name=name
        self.age=age
        self.score=score
class StudenManagerController:#逻辑控制类
    __stu_id=1000
    def __init__(self):
        self.__stu_list=[]

    @property
    def stu_list(self):#返回列表
        return self.__stu_list


    def add_student(self,stu):#为学生设置id 递增
        stu.id=self.__generate_id()
        self.__stu_list.append(stu)

    def __generate_id(self):#将学生添加到学生列表
        StudenManagerController.__stu_id += 1
        return StudenManagerController.__stu_id



    def remove_student(self,id):#根据id删除学生
        for item in self.__stu_list:
            if item.id==id:
                self.__stu_list.remove(item)



    def update_student(self,stu):#更新
        for item in self.__stu_list:
            if stu.id==item.id:
                item.name=stu.name
                item.age=stu.age
                item.score=stu.score





    def order_by_score(self):# 根据成绩排序
        for i in range(len(self.__stu_list)-1):
            for c in range(i+1,len(self.__stu_list)):
                if self.__stu_list[i]>self.__stu_list[c]:
                    self.__stu_list[i],self.__stu_list[c]=\
                    self.__stu_list[c], self.__stu_list[i]




class StudentManagerView:#界面视图类

    def __init__(self):
        self.contro=StudenManagerController()

    def __display_menu(self):#显示菜单
        print('+---------------------+')
        print('| 1)添加学生信息        |')
        print('| 2)显示学生信息        |')
        print('| 3)删除学生信息        |')
        print('| 4)修改学生信息        |')
        print('| 5)按照成绩升序排序     |')
        print('+---------------------+')

    def __select_menu(self):#选择菜单

        s01=input('请输入:')
        if s01=="1":
            self.__input_students()
        elif s01=='2':
            self.__output_students()
        elif s01 == '3':
            self.__delete_student()
        elif s01 == '4':
            self.__modify_student()
        elif s01 == '5':
            self.__output_student_by_socre()
    def main(self):#主入口
        while True:
            self.__display_menu()
            self.__select_menu()

    def __input_students(self):# 输入学生
        name=input('输入学生姓名')
        age=input('输入学生年龄')
        score = input('输入学生成绩')
        stu=StudentModel(name,age,score)
        self.contro.add_student(stu)
    def __output_students(self):# 输出学生
        for i in self.contro.stu_list:
            print(i.name,i.age,i.score,i.id)
    def __delete_student(self): # 删除学生
        id=input('输入id')
        self.contro.remove_student(id)
    def __modify_student(self):#修改学生信息
        name=input('输入学生姓名')
        age=input('输入学生年龄')
        score = input('输入学生成绩')
        id=int(input('输入id'))
        stu=StudentModel(name,age,score,id)
        self.contro.update_student(stu)

    def __output_student_by_socre(self):#
        self.contro.order_by_score()
view=StudentManagerView()
view.main()