
""" --->
    syntax error --> interpreter (parser)
    logical error -->
    runtime error ---> exception

"""
""" test cases ---> detect logical error --> script ---> test code """

# def sumnums(num1, num2):
#     res = num1 * num2
#     print(res)

#
# sumnums(2,2)
# sumnums(3,4)


"""
runtime error: exception ?
    unexpected event caused the application to stop

"""


# print("-------- Hello world ------------")
#
# print('Ahmed')
# print(name)
# print("000000")


# num= int(input('please enter salary'))  # runtime --> valueError

"""  handle exception """

# try:
#     num = int(input("please enter num: "))
# except:
#     print("--- error happened ---")
#
# print("----------------------End of the program --------------------------")

# num = input('please enter number ')
# if num:
#     print(int(num))


""" Exception handling """
# try:
#     print(course)
# except Exception as e :
#     print(f"--- error happened  {e}---")
#
# print("---------------")




# try:
#     num = int(input('please enter number: '))
# except Exception as e :
#     print(f"--- error happened  {e}---")
#
# print("---------------")

"====================="




# try:
#     num1 = int(input('please enter number: '))
#     num2 = int(input('please enter number: '))
#     print(num1/num2)
#     print(name)
# except ValueError as ve:
#     print("----- problems with num1 or num2 ---")
# except ZeroDivisionError as ze:
#     print(f"----------------- cannot divide by zero {ze}")
# except Exception as e:
#     print(f'------------------ common exception {e}')
# print("-----------after the exception ----")


""" exception handling """

# try:
#     num1 = int(input('please enter number: '))
#     num2 = int(input('please enter number: '))
#     res = num1/ num2
# except ValueError as ve:
#     print("----- problems with num1 or num2 ---")
# except ZeroDivisionError as ze:
#     print(f"----------------- cannot divide by zero {ze}")
# except Exception as e:
#     print(f'------------------ common exception {e}')
# print("-----------after the exception ----")
# print(res)








# try:
#     num1 = int(input('please enter number: '))
#     num2 = int(input('please enter number: '))
#     res = num1/ num2
# except ValueError as ve:
#     print("----- problems with num1 or num2 ---")
#     res = 0
# except ZeroDivisionError as ze:
#     print(f"----------------- cannot divide by zero {ze}")
#     res = 0
# except Exception as e:
#     print(f'------------------ common exception {e}')
#     res = 0
# print("-----------after the exception ----")
# print(res)


""" """


# try:
#     num1 = int(input('please enter number: '))
#     num2 = int(input('please enter number: '))
#     res = num1/ num2
# except ValueError as ve:
#     print("----- problems with num1 or num2 ---")
# except ZeroDivisionError as ze:
#     print(f"----------------- cannot divide by zero {ze}")
# except Exception as e:
#     print(f'------------------ common exception {e}')
# else:
#     "this block will be executed when there is no problem "
#     print(res)


""" finally block """
#
# try:
#     num1 = int(input('please enter number: '))
#     num2 = int(input('please enter number: '))
#     res = num1/ num2
# except ValueError as ve:
#     print("----- problems with num1 or num2 ---")
# except ZeroDivisionError as ze:
#     print(f"----------------- cannot divide by zero {ze}")
# except Exception as e:
#     print(f'------------------ common exception {e}')
# finally:
#     "this block will be executed always "
#     print("------- end of the program ")

""" raising the exception """
from inputsmodule import  askforint
# def divnums():
#     num1 = askforint("please enter num1 ")
#     num2 = askforint("please enter num2 ")
#     if num2==2:
#         raise Exception('--- num2 must not be zero ')
#     print(f'num1= {num1}, num2 ={num2}')
#     res = num1/num2
#     print(res)
#
# divnums()


def sumnums(num1, num2):
    if isinstance(num1, int) and isinstance(num2, int):
        res = num1 + num2
        print(res)
        return  res

    raise Exception("num1 and num2 must be integers")

sumnums('19', '33')