

name = 'Ahmed'

year = 2023
""" get type of any varaible """
print(type(name))  # type string

print(type(print))  # <class 'builtin_function_or_method'>

""" conversion between types --> type casting  """

"""
    int x ;
    char [] y ; 
"""

""" convert int to string ? """
num = 10
num = str(num)
print(num)

""" convert string to int """
# year = '2023'
# year = int(year)
# print(year)
name = 'noha'
# name = int(name)  # You cannot convert string to int unless the string ---> is numeric string
# consists only from digits 0 --> 9
# ?
pii = '3.14'
# pii = int(pii)
print(pii)

""" boolean """

# focused = False
# want_to_sleep = True


# print(True and True)
#
# print(True & True)

"""------------------ Logical operators -----------------"""


print("Ahmed" and "iti")

print("Ahmed" and True and 'iti') # iti ---> represent True.
""" and ---> make sure that all the expression parts must evalutates to true ---> then return True"""

print("Ahmed" and ' ' and 10)

# '' ---> Falsy value ,  ' '---> truly value
# ("Ahmed" and '' and 10) ---> this expression will return with empty string '' --> represent false
print(bool("Ahmed" and '' and 10))
print(bool('noha'))
print(bool(''))

# return True --> return with the first value represent True
print('Mariam' or 'Noha')

print('' or None or False or 0)
