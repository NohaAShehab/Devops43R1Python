"""
class method --> function represent behaviour related to the class
not the instance ---
"""

# class Employee:
#     no_of_employees= 0  # class variable
#     def __init__(self,name, salary):
#         self.name =name  # instance variable
#         self.salary = salary
#         Employee.no_of_employees +=1
#
#     # instance method
#     def display_info(self): # self  ---> you must pass instance to the function
#         print(f'{self.name}, {self.salary}')
#
#     # def get_no_of_employees(message):  # message ? self
#     #     print(message, Employee.no_of_employees)
#     #     return Employee.no_of_employees
#
#     @classmethod  # class method decorator ---> object class ---> special behaviour to the function
#     def get_no_of_employees(cls):  # the first argument to the function --> represent the class
#         #not the instance
#         print(cls)
#         # return Employee.no_of_employees
#         return cls.no_of_employees
#
#     @classmethod
#     def test(abbass):  # Usually first parameter of such methods is named 'cls'
#         print(abbass)
#
#
# emp = Employee("Ahmed", 1000)
# emp2 = Employee("Ali", 2000)
# # print(Employee.no_of_employees)
# emp2.display_info()
# print(Employee.get_no_of_employees())
#
# Employee.test()

""" class method ---> object factory ---> 
    behaviour ---> depend on the class 
    ---> return set of objects 
    --> save object in file ? 

"""

# class Employee:
#     no_of_employees= 0  # class variable
#     def __init__(self,name, salary):
#         self.name =name  # instance variable
#         self.salary = salary
#         Employee.no_of_employees +=1
#
#     # instance method
#     def display_info(self): # self  ---> you must pass instance to the function
#         print(f'{self.name}, {self.salary}')
#
#     @classmethod  # class method decorator ---> object class ---> special behaviour to the function
#     def get_no_of_employees(cls):  # the first argument to the function --> represent the class
#         #not the instance
#         print(cls)
#         # return Employee.no_of_employees
#         return cls.no_of_employees
#
#     @classmethod
#     def test(abbass):  # Usually first parameter of such methods is named 'cls'
#         print(abbass)
#
#
#     @classmethod
#     def generate_defualt_object(cls):
#         return cls('', 0)
#
#
#
#
# emp = Employee("Ahmed", 1000)
# emp2 = Employee("Ali", 2000)
#
# emp3 = Employee.generate_defualt_object()
# print(emp3)
# print(Employee.no_of_employees)

