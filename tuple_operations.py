

""" tuple ---> immutable datatype can hold different data from different data types """

# """1- define a tuple """
myt = ()
mytuple = tuple()
t =(3,4,6,'iti', False, 'Ahmed', ['Ali'], 'iti', 'iti', 'iti')

"1- get len of tuples "
print(len(t))
# #
""" 2-tuples is treated like an array --> access tuples parts using index start from 0"""
print(t[1])
print(t[1:4])
print(t[:10])
print(t[::-1])  # reversed --> return new tuple
# #
""" 3- tuples is immutable --->you cannot change its content in the runtime"""
# print(t[6])
# t[5]='@' #TypeError: 'tuple' object does not support item assignment
t[6].append('Ahmed')  # modify the list not the tuple
# #
"""4- count no of element occurrence in the tuples """
print(t.count('iti'))
#
# #
"""5- get index of element  """

print(t.index('iti'))  # return with the first occurrence of the element in the tuples
#
""" 6- tuples concatenation, tuples interpolation """
t1= (4,56,66)
t2= ('Ahmed', 'ali')
t3 = t1 + t2
print(t3)
#

"""8- tuple interpolation """
# tuple of one element (4,)
myt = (4,)*5
print(myt)






""" check if element exists in a tuple """
if 'iti' in t:
    print("found")
else:
    print('not found')

""" loop over the tuple """
for item in t1:
    print(item)

"get item and index"
for item in t1:
    print(f"item = {item}")
enm = enumerate(t1)
print(enumerate(t1))  # enumarate object  0---> create index for the iterable
for index, item in enumerate(t1):
    print(f"item = {item}, {index}")


#
# """ cast string to tuple and vise versa """
#
#
name = 'noha'
print(tuple(name))
#
t=('a', 'b','c')
mystring = ''.join(t)
print(mystring)
#

print(min(t1))



weekdays=('Saturday', 'Sunday','Monday') ### immutable
workdays = ['Sunday', 'Thursday']

'cast list to tuple? '
l = range(10)
l = list(l)
print(l)
t = tuple(l)
print(t)

""" note -----> """
""" remove any variable from memory ---> """
# del mystring