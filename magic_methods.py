
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
        return self.__salary *.8

    def __str__(self):
        "must retrurn with string "
        return self.name

    def __len__(self):
        "must return with number"
        return len(self.__dict__)

    def __call__(self, *args, **kwargs):
        print("object is being called ")

    def __repr__(self):
        return f"Employee({self.name}, {self._email}, {self.__salary})"


emp = Employee("Ahmed", 'ahmed@gmail.com', 94934)
print(emp)
print(emp.__repr__())

# print(emp.__dict__)

print(len(emp))

emp()