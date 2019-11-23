class EmployeeIterator:
    def __init__(self,data):
        self.__target=data
        self.__index = -1

    def __next__(self):
        if self.__index>=len(self.__target)-1:
            raise StopIteration
        self.__index +=1
        return self.__target(self.__index)



class EmployeeManager:
    def __init__(self):
        self.__employee_list=[]

    def add_employee(self,employee):
        self.__employee_list.append(employee)

    def __iter__(self):
        return EmployeeIterator()


manager=EmployeeManager()
manager.add_employee('无忌')
manager.add_employee('翠山')
manager.add_employee('三丰')

for item in manager:
    print(item)