"""
    access modifiers  --> limit accessibility to the data

    public --> object properites
    protected ---> access object properties , in class or child class
    private ---> access object property in only the class

    no access modifiers --> naming of the object
    a--> z ---> public property
    _a-->z ---> protected

    __a-->z ----> private

"""

# class Employee:
#     def __init__(self,name, email, salary):
#         self.name= name
#         self._email = email
#         self.__salary = salary
#
#
# e = Employee("Ahmed", 'ahned@ggmail.com',20000)
# print(e.name)
# print(e._email) # will be displayed --> ethically don't do this
# # print(e.__salary)
# print(e._Employee__salary)  # scope binding  # --> ethically don't do this

""" private , protected , public ? """
""" limit accessibility
    --> access modifiers ---> do operations on the data ? 
 """


# class Employee:
#     def __init__(self, name, email, salary):
#         self.name = name
#         self._email = email
#         self.__salary = salary
#
#     def setSalary(self, salary):
#         if isinstance(salary, int) or isinstance(salary, float):
#             self.__salary = salary
#         else:
#             raise Exception("Salary should be int or float ")
#
#     def getSalary(self):
#         return self.__salary
#
#
# emp = Employee("Ahmed", 'ahmed@gmail.com', 24345)
# # emp.setSalary("iti")
# emp.setSalary(10000)
# print(emp.getSalary())

""" --------------- property decorator ------------- """
# class Employee:
#     def __init__(self, name, email, salary):
#         self.name = name
#         self._email = email
#         self.__salary = salary
#
#     # operation salary ---> set , get ?
#     def setSalary(self, salary):
#         if isinstance(salary, int) or isinstance(salary, float):
#             self.__salary = salary
#         else:
#             raise Exception("Salary should be int or float ")
#
#     def getSalary(self):
#         return self.__salary
#
#     ######
#     @property
#     def salary(self):
#         return self.__salary*.8
#
#     @salary.setter
#     def salary(self, salary):
#         if isinstance(salary, int) or isinstance(salary, float):
#             self.__salary = salary
#         else:
#             raise Exception("Salary should be int or float ")
#
# emp = Employee("Ahmed", 'ahmed@gmail.com', 24345)
# emp.setSalary(10000)
# print(emp.getSalary())
# print(emp.salary)  # you access it directly
# # emp.salary = 'iti'
# emp.salary=243546457


"""---------------------------------"""
# class Employee:
#     def __init__(self, name, email, salary):
#         self.name = name
#         self._email = email
#         # self.__salary = salary
#         # apply setter on the salary
#         if isinstance(salary, int) or isinstance(salary, float):
#             self.__salary = salary
#         else:
#             raise Exception("Salary should be int or float ")
#
#
#
#     ######
#     @property
#     def salary(self):
#         return self.__salary*.8
#
#     @salary.setter
#     def salary(self, salary):
#         if isinstance(salary, int) or isinstance(salary, float):
#             self.__salary = salary
#         else:
#             raise Exception("Salary should be int or float ")
#
# emp = Employee("Ahmed", 'ahmed@gmail.com', "iti")
#
# print(emp.salary)

""" =----> """

class Employee:
    def __init__(self, name, email, salary):
        self.name = name
        self._email = email
        # self.__salary = salary
        # apply setter on the salary
        self.salary= salary

    ######
    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary):
        if isinstance(salary, int) or isinstance(salary, float):
            self.__salary = salary
        else:
            raise Exception("Salary should be int or float ")

    @property
    def netsalary(self):
        return self.__salary*.8

emp = Employee("Ahmed", 'ahmed@gmail.com', "100")

print(emp.salary)

















