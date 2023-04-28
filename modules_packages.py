
"""

    any file ---> .py ---> python module

"""

""" import function from another module """
""" import all the module """
# import  inputsmodule
# def calculator():
#     num1 = inputsmodule.askforint("please enter num1: ")
#     num2 = inputsmodule.askforint('please enter num2: ')
#     res = num1 + num2
#     print(res)
#     pass
# calculator()
#
#
# inputsmodule.askforstr('please enter your name: ')

""" alias module name """



# import  inputsmodule as inmodule
# def calculator():
#     num1 = inmodule.askforint("please enter num1: ")
#     num2 = inmodule.askforint('please enter num2: ')
#     res = num1 + num2
#     print(res)
#     pass
# calculator()

# inmodule.askforstr('please enter your name: ')
#
# print(inmodule.year)
""" import part of the module """
# from inputsmodule import  askforint, askforstr, year
# def calculator():
#     num1 = askforint("please enter num1: ")
#     num2 = askforint('please enter num2: ')
#     res = num1 + num2
#     print(res)
#     pass
# calculator()
# print(year)

""" alias from """

# from inputsmodule import  askforint as getnumbers
# def calculator():
#     num1 = getnumbers("please enter num1: ")
#     num2 = getnumbers('please enter num2: ')
#     res = num1 + num2
#     print(res)
#     pass
# calculator()
#

""" package  ---> folder -> directory contains modules """

""" import module from the package 
    packagename.modulename
"""
# import iti.greetingmodule
#
# iti.greetingmodule.sayhello('Ahmed')
# iti.greetingmodule.saywelcome('Ali')

""" alais import """
#
# import iti.greetingmodule as mymodule
#
# mymodule.sayhello('Ahmed')
# mymodule.saywelcome('Ali')

""" import part of the module
    from packagename.modulename import functionname 
"""

# from iti.greetingmodule import saywelcome
#
# saywelcome('Ahmed')

""" ============================"""

# from devops.mathoperations import  sumnums
#
# sumnums(3,45)
""" import package """
import devops

devops.sumnums(445,45)


# from devops.test.testvariables import checkint
#
# print(checkint('iti'))

from devops import checkint
print(checkint('iti'))










