
"""

    ploymorphism

    overriding ---> 2 functions with the same in 2 classes ---> (inheritance relation)
    --> different implementation

    overloading

"""

class Person:
    def __init__(self,name):
        self.name= name


    def speak(self, message=''):
        print(f'My name is {self.name} ---> from the parent {message}')

p = Person("test")
p.speak()
p.speak("hello world")
class Employee(Person):
    def __init__(self, name, email):
        super().__init__(name)
        self.email = email

    def speak(self):
        super().speak()
        print(f'My name is {self.name} {self.email} ---> from the child ')

emp = Employee("Ahmed", 'ahmed@gmail.com')
emp.speak()