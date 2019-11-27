class Person:
    def say(self):
        print('balalala')

class Student(Person):
    def study(self):
        print('学习')

stu01=Student()
stu01.say()




class Zoon:
    def speak(self):
        print('balalala')
    def eat(self):
        print('food')
class Dog(Zoon):
    def run(self):
        print('run')
class Bird(Zoon):
    def fly(self):
        print('fly')

zoon=Zoon()
bird=Bird()
dog=Dog()
print(isinstance(bird,Zoon))
print(isinstance(zoon,Bird))
print(issubclass(Dog,Zoon))
print(type(dog)==Dog)






class Car:
    def __init__(self,brand,speed):
        self.brand=brand
        self.speed=speed

    def run(self):
        print('run')

class Movecar(Car):
    def __init__(self,capacity,brand,speed):
        self.capacity=capacity
        super().__init__(brand,speed)
