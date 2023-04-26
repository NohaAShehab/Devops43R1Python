

"""<---- listss - -> sequence of chars  ---> """
""" list ---> mutable datatype can hold different data from different data types """

"""1- define a list """
myl = []
mylist = list()
l  = [3,4,6,'iti', False, 'Ahmed', ['Ali'], 'iti', 'iti', 'iti']

"1- get len of lists "
print(len(l))
#
""" 2-lists is treated like an array --> access lists parts using index start from 0"""
print(l[1])
print(l[1:4])
print(l[:10])
print(l[::-1])  # reversed
#
""" 3- lists is mutable --->you can change its content in the runtime"""
print(l[6])
l[5]='@'
#
"""4- count no of element occurrence in the lists """
print(l.count('iti'))

#
"""5- get index of element  """

print(l.index('iti'))  # return with the first occurrence of the element in the lists
#
""" 6- lists concatenation, lists interpolation """
l1=  [4,56,66]
l2= ['Ahmed', 'ali']
l3 = l1 + l2
print(l3)

"""7- extend a list ===> mutable """
l1.extend(l2)
print(l1)

"""8- list interpolation """
myl = [4]*5
print(myl)

"""9- append element to the list"""
l.append('Ahmed')

"10- insert element in the list ? ---> insert 000> index "
l.insert(4,'inserted value')
print(l)
l[4]='Ahmed'
"""11- pop element from the list"""
popped_element=l.pop()  # pop the last element from the list
print(popped_element)

popped_element=l.pop(3)  # pop the last element from the list
print(popped_element)

"""11- remove element from the list"""
l.remove('iti')  # remove first occurrence
print(l)

"""12- sort a list ---> sorting  ---> comparing --->
 python you cannot compare different values from different datatypes"""


l = [3,56,66,-10, 5,100,30]
l.sort()# sort list itself ---> and return with None
print(l.sort()) # None
print(l)
""" sort list reversed ? """
l.sort(reverse=True)
print(l)

# sorted([4,4,5,666])  # return new list  ---> return new sorted iterable
""" reverse a list --> just  """
ll = ['Ahmed', 10 , '100', 'test', True]
ll.reverse()
print(ll)

""" check if element exists in a list """
if 'iti' in l:
    print("found")
else:
    print('not found')

""" loop over the list """
# for item in l1:
#     print(item)

"get item and index"
# for item in l1:
#     print(f"item = {item}")
enm = enumerate(l1)
print(enumerate(l1))  # enumarate object  0---> create index for the iterable
for index, item in enumerate(l1):
    print(f"item = {item}, {index}")

for index, item in enumerate('noha'):
    print(f"item = {item}, {index}")

counter = 0
for item in l:
    print(item, counter)
    counter +=1

""" cast string to list and vise versa """


name = 'noha'
print(list(name))

l=['a', 'b','c']
mystring = '_'.join(l)
print(mystring)

"split string to list "
message = 'my name is Noha'
print(message.split(' '))

print(min(l))