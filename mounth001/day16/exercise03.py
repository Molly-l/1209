class AtkError(Exception):
    def __init__(self,id,code,message):
        self.id=id
        self.code=code
        self.message=message
class Enemy:
    def __init__(self,atk=0):
        self.atk=atk
    @property
    def atk(self):
        return self.__atk
    @atk.setter
    def atk(self,value):
        try:
            if 0<value<100:
                self.__atk=value
            else:
                raise AtkError(101,\
                    "0<value<100",'攻击力错误')
        except AtkError as e:
            print(e.id, e.code, e.message)

if __name__ == '__main__':
    # try:
    #     w01.txt = Enemy(800)
    #
    # except AtkError as e:
    #     print(e.id,e.code,e.message)
    w01 = Enemy(800)