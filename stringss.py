

"""<---- strings - -> sequence of chars  ---> """

# name = 'Ahmed Ali Mohamed'
# "1- get no of char in string "
# print(len(name))
#
# """ string is treated like an array --> access string parts using index start from 0"""
# print(name[1])
# print(name[1:4])
# print(name[:10])
# print(name[::-1])  # reversed
#
# """ string is immutable ---> once created cannot be changed"""
# # print(name[10])
# # name[10]='@'
#
# """ count no of char in the string """
# print(name.count('a'))
# print(name.count('md'))
#
# """get index of char ?  """
# message = 'iti'
# print(message.index('i'))  # return with the first occurrence of the char in the string
#
# """ operations on the strings  ====> return new string """
#
# """ string formatting """
# template = "My name is {0} I works at {1}"
# print(template.format('Noha', 'ITI'))
# print(template.format('ITI', 'Noha'))
# "--- template ---> keyword"
# template = "My name is {name} I works at {work}"
# print(template)
# print(template.format(work='iti',name='noha'))
#
# """replace string --> part of string """
# message = 'I love iti o o o '
# print(message.replace('o', '@'))
# print(message.replace('o', '@', 2))
#
#
# """ format string ---> f-format string --> format string according to existing variables  """
# name = 'Ahmed'
# work = 'Microsoft'
# year = 32234
# temp = f"My name is {name}, I works at {work} {year}"
# print(temp)
# """ string concatenation, string interpolation """
# fname = 'Noha'
# midname = 'Abdelhady'
# lname = 'Shehab'
# test = 10
# '+ ---> valid only between values from the same type '
# # fullname = fname + midname + midname + lname
# # fullname = fname + midname + midname + lname + test # TypeError: can only concatenate str (not "int") to str
#
# fullname = fname + midname *2 + lname  # string intepolation ---> multiply string by int
# print(fullname)
# print('test'*44)
# """ ask user to enter data to the application """
#
# message = input("please enter message ")  # always returns with string
# print(message, type(message))
#
# """ format operations on the  string """
# print(message.upper())
# print(message.lower())
# print(message.capitalize())
# print(message.title())  # capitalize first char in each word
# """ examine string content ?"""
# # print(message.isupper())
# # print(message.islower())
# # print(message.isalpha())  # return True ---> if the string consists only from alphas from a -> Z
# print(message.isdigit())  #  return True ---> if the string consists only from digits from 0--> 9
#
# # age =  input("please enter age :  ")
# # if age.isdigit():
# #     age = int(age)
# #     print(age*10)
#
# deduction = input("please enter deduction percentage ")
# # d = int(deduction)  # -10
# # if deduction.isdigit():  # deosn't feel negative numbers  --> 0--->9
# #     deduction = int(deduction)
#
# # if deduction.isnumeric():  # 5 --->
# #     deduction = int(deduction)
# #
# message=  input("please enter message : ")
# print(message.isspace())

""" ====> operations on string  ---> strip string """

message = '     Nice to meet you      '
yourmessage = input("please enter message ")
print(message)
print(yourmessage)
print(yourmessage.strip())  # remove spaces from the beginning and the end of the string
print(f"{yourmessage.lstrip()}#")
print(f"{yourmessage.rstrip()}#")

""" strip pattern of chars """

print(f"#{yourmessage.strip('A i$')}#")  # remove char from the beginning and the end of the string


num = 4+5j

print(num, type(num))

numm =complex(3,45)
""" check existence """
if 'a' in 'noha':
    print('hi')