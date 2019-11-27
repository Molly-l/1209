class Person:
    def __init__(self,name):
        self.name=name
        # self.money=money
    def teach(self,other,skill):
        print(self.name,'教',other,skill)

    def work(self,money):
        print(self.name,'上班赚',money)



zwj=Person('张无忌')
zm=Person('赵敏')
zwj.teach(zm.name,'乾坤大挪移')
zm.teach(zwj.name,'化妆')