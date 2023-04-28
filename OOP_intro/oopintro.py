# emp =['Ahmed', 'Microsoft', 1000]
# emp2 = {
#     "name":"Ahmed",
#     'company':"Microsoft",
#     'salary':1000
# }
#
# emp3 = {
#     "firstname":"Ahmed",
#     'work':"Microsoft",
#     'netsal':1000
# }

""" define common structure ---> describe employee

    define your own datatype  wrap data , functionality in the same component

    create class

"""

# class Employee:
#     pass
#
# "take object , instance from the class "
#
# emp = Employee()
# print(emp, type(emp))
# print(isinstance(emp, Employee))
# print(type('noha'))

""" bind data to the object """

# class Employee:
#     pass
#
# "take object , instance from the class "
#
# emp = Employee()
#
# emp.name ='Ahmed'
# emp.email= 'ahmed@gmail.com'
# emp.salary=3000
# print(emp, emp.name)
#
#
# emp2 = Employee()
#
# emp2.fullname ='Ahmed'
# print(emp2, emp2.fullname)



""" customize object creation """

# class Employee:
#     def __init__(self):  # address of the object in self
#         print(f"------{self}-------- object is being created----")
#
# "take object , instance from the class "
#
# emp = Employee()
# print(emp)
# emp2 = Employee()

""" """
# class Employee:
#     def __init__(self):  # address of the object in self
#         print(f"------{self}-------- object is being created----")
#         self.name= 'ahmed'
#         self.email = 'ahmed@gmail.com'
#
# "take object , instance from the class "
#
# emp = Employee()
# print(emp)
# emp2 = Employee()

""" customize init """

# class Employee:
#     # def __init__(self,):  # address of the object in self
#     #     print(f"------{self}-------- object is being created----")
#     #     self.name= 'ahmed'
#     #     self.email = 'ahmed@mail.com'
#
#
#     def __init__(self,name='', email=''):  # address of the object in self
#         print(f"------{self}-------- object is being created----")
#         self.name= name  # instance variables ? --> values depend on caller instance
#         self.email = email
#
# "take object , instance from the class "
# emp3 = Employee()
# emp = Employee('noha','noha@gmail.com')
# print(emp.name)
# emp2 = Employee('ahmed', 'ahmed')
# print(emp2.name)


"""add functions to the class """



# class Employee:
#     # def __init__(self,):  # address of the object in self
#     #     print(f"------{self}-------- object is being created----")
#     #     self.name= 'ahmed'
#     #     self.email = 'ahmed@mail.com'
#
#     def __init__(self,name='', email=''):  # address of the object in self
#         print(f"------{self}-------- object is being created----")
#         self.name= name  # instance variables ? --> values depend on caller instance
#         self.email = email
#
#     def printinfo(self):
#         print(f"My name is {self.name},My email{self.email}")
#
# "take object , instance from the class "
# emp3 = Employee()
# emp = Employee('noha','noha@gmail.com')
# print(emp.name)
# emp2 = Employee('ahmed', 'ahmed')
# emp.printinfo()
# emp2.printinfo() # instance method.




""" class variables """

class Employee:
    count = 0  # class variable
    """ property represnt class --> shared between instnase"""
    def __init__(self,name='', email=''):  # address of the object in self
        print(f"------{self}-------- object is being created----")
        self.name= name  # instance variables ? --> values depend on caller instance
        self.email = email
        Employee.count +=1 #

    def printinfo(self):
        print(f"My name is {self.name},My email{self.email}")

"take object , instance from the class "
emp3 = Employee()
emp = Employee('noha','noha@gmail.com')
print(emp.name)
emp2 = Employee('ahmed', 'ahmed')
emp.printinfo()
emp2.printinfo() # instance method.

print(Employee.count)





