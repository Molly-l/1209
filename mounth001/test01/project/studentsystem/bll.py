
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

