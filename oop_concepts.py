

"""

    encapsulation

    inheritance

    polymorphism

    abstraction  # inherit class abc



"""



""" inheritence """


# class Person:
#     def __init__(self,name, bdate):
#         self.name = name
#         self.bdate = bdate
#
#     def speak(self):
#         print(f"My name is {self.name}")
#
# class Employee(Person):
#     pass
#
# # emp = Employee()  # TypeError: Person.__init__() missing 2 required positional arguments: 'name' and 'bdate'
# emp = Employee("ahmed", 23)
# emp.speak()


""" ===> add email to the employee class """
class Person:
    def __init__(self,name, bdate):
        self.name = name
        self.bdate = bdate

    def speak(self):
        print(f"My name is {self.name}")

# class Employee(Person):
#     def __init__(self, email):
#         self.email=email
#
# # emp = Employee("ahmed", 23, 'ahmed@gmail.com')
# emp = Employee( 'ahmed@gmail.com')
# emp.speak()


""" call parent constructor 
    use keyword super()
"""

# class Employee(Person):
#     def __init__(self, name, bdate ,email):
#         super().__init__(name, bdate)
#         self.email=email
#         # self.namee = name
#         # self.bdate= bdate
#
# emp = Employee("ahmed", 23, 'ahmed@gmail.com')
# emp.speak()

#####################3333
"""mutiple inheritence """


#
# class Parent:
#     def __init__(self):
#         print("=== parent constructor is being called ")
#         self.name = 'Ahmed'
#
#
# class A(Parent):
#     def __init__(self):
#         print("=== A constructor is being called ")
#         super(A, self).__init__()
#         self.found = True
#
#
# class B(Parent):
#     def __init__(self):
#         print("=== B constructor is being called ")
#         super().__init__()
#         self.test = 'test'
#
#
# # class Child(A, B):
# #     pass
# #
# #
# # c = Child()
#
#
# class Child(A, B):
#     def __init__(self):
#         super().__init__()
#         self.name='ahmed@gmail.com'
#
#
# c = Child()







#
#
#
# class Parent:
#     def __init__(self):
#         print("=== parent constructor is being called ")
#         self.name = 'Ahmed'
#
#
# class A(Parent):
#
#     def __init__(self):
#         # super().__init__()
#         print("=== A constructor is being called ")
#         self.found = True
#
#
# class B(Parent):
#     def __init__(self):
#         # super().__init__()
#         print("=== B constructor is being called ")
#         self.test = 'test'
#
#
#
# class Child(A, B):
#     def __init__(self):
#         super().__init__()
#         self.jj='ahmed@gmail.com'
#
#
# c = Child()


""" multiple inheritance """
#
# class A:
#     def __init__(self):
#         print("---- A constructor is called ----")
#         self.name = 'Ahmed'
#
# class B:
#     def __init__(self):
#         print("B constructor is called")
#
#     def testB_class(self):
#         print("---I being called because I am from b type")
#
#
# class C(A,B):
#     pass
#
# c = C()
#
# print(isinstance(c, A))
# print(isinstance(c, B))
# c.testB_class()

"""
 A       B
 .       . 
    .  
    c

"""
#
#
# class A:
#     # def __init__(self):
#     #     print("---- A constructor is called ----")
#     #     self.name = 'Ahmed'
#     pass
#
#
# class B:
#     def __init__(self):
#         print("B constructor is called")
#
#     def testB_class(self):
#         print("---I being called because I am from b type")

#
# class C(A,B):
#     # def __init__(self):
#     #     self.email ='ksjkldj'
#
#     pass
# c = C()

# print(isinstance(c, A))
# print(isinstance(c, B))
# c.testB_class()


""" 

all classes in python --> userdefined or builtin class -datatypes -

implicitly inherits from base class object 
"""

l = []
l.append("iti")



# class M:
#     pass
#
# m = M()

class M(object):
    def __init__(self):
        pass

m = M()