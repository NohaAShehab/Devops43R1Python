

import os
print(os.getcwd())
print(os.getlogin())
print(os.getuid())

os.system('systemctl status apache2')
os.system('ls -l')

# os.chdir('/home/noha')
# print(os.getcwd())
#
# os.mkdir('devops444')

import math


import re

email = input("please enter email: ")

# regex pattern
# pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
pattern =  r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
# # check if email matches the pattern
# print(re.match(pattern, email))
# if re.match(pattern, email):
#     # match return match object if part of the  string satisfy the condition
#     print('Valid email')
# else:
#     print('invalid')

"make that all the string match the expression"

# check if email matches the pattern
print(re.fullmatch(pattern, email))  # return with match object -->all string part follows pattern
if re.fullmatch(pattern, email):
    # match return match object if part of the  string satisfy the condition
    print('Valid email')
else:
    print('invalid')

""" isalpha --> datatype of variable must be strin g"""

name='ahmed'  # name is string
print(name.isalpha())

"is instance "
print(isinstance(name, str))

x = type('noha')  # object from class str
print(x, type(x))  # x --> object from class type

# if type('noha') =='str':
#     print('hi')
# else:
#     print('bye')

if type('noha') ==str:
    print('hi')
else:
    print('bye')