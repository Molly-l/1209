class LittlePony:
    def __init__(self,size,color):
        self.size=size
        self.color=color
        self.vendor=Vendor()
    def sing(self):
        print('lalala')
    def speak(self):
        print('hello my name is LittlePony')

class Vendor:
    def __init__(self,email='hjkl@tedu.cn',
                 phone='400-123-8989',address='北京'):
        self.email=email
        self.phone=phone
        self.address=address
    def call(self):
        print('给%s打电话'% self.phone)

myLittlePony=LittlePony('middle','pink')
myLittlePony.vendor.call()


