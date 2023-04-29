

class Employee:
    no_of_employees= 0  # class variable
    def __init__(self,name, salary):
        self.name =name  # instance variable
        self.salary = salary
        Employee.no_of_employees +=1

    # instance method
    def display_info(self): # self  ---> you must pass instance to the function
        print(f'{self.name}, {self.salary}')

    @classmethod  # class method decorator ---> object class ---> special behaviour to the function
    def get_no_of_employees(cls):  # the first argument to the function --> represent the class
        #not the instance
        print(cls)
        # return Employee.no_of_employees
        return cls.no_of_employees
    @classmethod
    def generate_defualt_object(cls):
        return cls('', 0)

    @staticmethod  # helper method --->
    def cal_net_salary(salary):  # first argument neither self not cls
        return salary * .9

    @staticmethod
    def stripname(name):
        try:
            return name.strip()
        except:
            return None




emp = Employee("Ahmed", 1000)
emp2 = Employee("Ali", 2000)

emp3 = Employee.generate_defualt_object()
print(emp3)
emp3.salary = 2000
print(Employee.no_of_employees)

print(Employee.stripname('            Ahmed              '))

# def cal_net_salary(salary):
#     return salary*.9
#
# print(cal_net_salary(emp3.salary))
# print(cal_net_salary(100000))
# print(Employee.cal_net_salary(emp3.salary))
# print(Employee.cal_net_salary(200000))


print(Employee.stripname('           Ali           '))
print(Employee.stripname(emp.name))