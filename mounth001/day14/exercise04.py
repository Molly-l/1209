class EmployeeManager:
    def __init__(self):
        self.__emp_list=[]
    @property
    def position_list(self):
        return self.__emp_list
    def add_emp(self,emp):
        self.__emp_list.append(emp)
    def all_wage(self):
        all_wage=0
        for i in self.__emp_list:
            all_wage +=i.wage()
        return all_wage

class Employee:
    def __init__(self,base_wage):
        self.base_wage=base_wage
    def calc_wage(self):
        pass
class Programmer(Employee):
    def __init__(self,base_wage,commission):
        self.commission=commission
        super().__init__(base_wage)#
    def wage(self):
        return self.base_wage+self.commission

class Sales(Employee):
    def __init__(self,base_wage,commission):
        super().__init__(base_wage)
        self.commission = commission
    def wage(self):
        return self.base_wage+self.commission*0.05
M01=EmployeeManager()
programmer=Programmer(4000,10000)
Sales=Sales(5000,30000)
M01.add_emp(programmer)
M01.add_emp(Sales)
print(M01.all_wage())
