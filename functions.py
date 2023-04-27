

# print("hello world")
#
#
# print('Ahmed'.upper())
"""
create our own function
    function name ---> inputs
    --> return result ?
"""
# l=[4,5,6,43]
# print(l.sort())

""" functions with known number of arguments """
# """ define function """
#
# def myfunction():
#     pass
#
# """ call the function """
# res=myfunction()
# print(res)

""" implement the function """
# def sayhello():
#     name = input("please enter name : ")
#     print(f"---- Hello {name}")
#
# x= sayhello()
# print(x)
#
# sayhello()
#
# sayhello()
#
# sayhello()

""""""
# def sayhello():
#     name = input("please enter name : ")
#     print(f"---- Hello {name}")
#     return
#
# x= sayhello()
# print(x)

""""""
#
# def askforfullname():
#     fname = input("please enter first name : ")
#     lname = input("please enter last name : ")
#     print(f"---- Hello {fname}{lname}")
#     return f"{fname}{lname}"
#
# x= askforfullname()
# print(x)


""" loosely dynamically typed lang. --> detect datatype in the runtime """
# def askforfullname() ->str:
#     fname = input("please enter first name : ")
#     lname = input("please enter last name : ")
#     print(f"---- Hello {fname}{lname}")
#     return len(f"{fname}{lname}")
#
# x= askforfullname()
# print(x)


"""  --- return type """
# def askforfullname():
#     fname = input("please enter first name : ")
#     lname = input("please enter last name : ")
#     print(f"---- Hello {fname}{lname}")
#     return fname, lname  # tuple
#
# x= askforfullname()
# print(x)

""" ----> """
# def askforfullname():
#     fname = input("please enter first name : ")
#     lname = input("please enter last name : ")
#     print(f"---- Hello {fname}{lname}")
#     return [fname, lname]  # list
#
# x= askforfullname()
# x.append('Ahmed')
# print(x)


"functions special variable "

" function accept arguments "


# def sumnum(num1,num2):
#     print(f"num1={num1}, num2={num2}")
#     res = num1 + num2
#     print(res)
#     return res
#
# r= sumnum(4,3)
# print(r)

'-------------- problems with functions ----'

# def sumnum(num1,num2):
#     print(f"num1={num1}, num2={num2}")
#     res = num1 + num2
#     print(res)
#     return res
# sumnum(3,45)
# r= sumnum("4","3")
# mm = sumnum('Ahmed', 'Ali')  #concate num1 , num2
# sumnum(10 , '100')

""" customize argument type ---> type hint """

# def sumnum(num1 :int,num2: int):
#     print(f"num1={num1}, num2={num2}")
#     res = num1 + num2
#     print(res)
#     return res
# sumnum(3,45)
# r= sumnum("4","3")
# mm = sumnum('Ahmed', 'Ali')  #concate num1 , num2
# sumnum(10 , '100')

""" """


# def sumnum(num1 :int,num2: int):
#     if not num1.isdigit():  # with string
#         print("---- error ---")
#         return
#     print(f"num1={num1}, num2={num2}")
#     res = num1 + num2
#     print(res)
#     return res
# sumnum(3,45)

"""  --------> """

# print(isinstance(10 , int))
# print(isinstance(10, float))
# print(isinstance('ahmed', int))
# def sumnum(num1 :int,num2: int) ->int :
#     if isinstance(num1, int) and isinstance(num2, int):
#         print(f"num1={num1}, num2={num2}")
#         res = num1 + num2
#         print(res)
#         return res
#     print("-------- not valid parameters ------")
# sumnum(3,45)
# sumnum('Ahmed', 'Ali')


""" functions with default arguments  """
# def sumnum(num1=5 ,num2=10) ->int :
#     if isinstance(num1, int) and isinstance(num2, int):
#         print(f"num1={num1}, num2={num2}")
#         res = num1 + num2
#         print(res)
#         return res
#     print("-------- not valid parameters ------")
# sumnum(3,45)
# sumnum('Ahmed', 'Ali')
# sumnum()
# sumnum(3)

# print("Ahmed", end='')
# print("Ali")
#
# print("Ahmed", 'ali', 'iti', 234, sep='||')




# def sumnum(num1=5 ,num2=10) ->int :
#     if isinstance(num1, int) and isinstance(num2, int):
#         print(f"num1={num1}, num2={num2}")
#         res = num1 + num2
#         print(res)
#         return res
#     print("-------- not valid parameters ------")
# sumnum(3,45)
# sumnum('Ahmed', 'Ali')
# sumnum(3)













""" function with unknown number of arguments """

# print()
# print('ahmed', 10)
# print(35,566,56,546,34,35,35,35)


# def askforstudents(*students):  # * ==> zero or more ?
#     print(students)  # accept arguments tuple --->
#
# askforstudents()
# askforstudents('Ahmed')
# askforstudents('Ahmed', 'ali', 'Mohamed')


# template = 'My name is {0}'
# print(template.format('Ahmed'))

""" ----> keyword arguments """

def introduceyourself(**info): # ** --> arguments --> keyword arguments
    print(info)

introduceyourself(name='noha', work='iti', study='engineering')
introduceyourself(lname='Ali')
introduceyourself()



template = 'My name is {username}'
print(template.format(username='Ahmed'))




