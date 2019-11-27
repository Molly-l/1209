class Airplany:

    
    class Person:
        def __init__(self, name):
            self.name = name

        def go_to(self, position, type):

            print('去：' + position)
            type.run()

    class Car:
        def run(self):
            print('走你～')

    c01 = Car()
    lz = Person('老张')
    lz.go_to('东北', c01)
