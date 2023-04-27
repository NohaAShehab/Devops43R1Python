""""""

myinfo = ['noha', 'iti', 30]

"""
    descriptive data ? 
    
    instead of indicies  --> key:value pairs ?
"""
"""1- to define a dict """
d = {}
myinfo = dict()

""" dict --> comma seperated keyvalue pair """
myinfo = {"name": "Noha", 'age': 30, 'work': "ITI"}
print(myinfo)

""" access elements using key """
print(myinfo['name'])

""" dict --> is mutable datatype"""
myinfo['name'] = 'Noha Shehab'
print(myinfo)

"""dict ---> allow only unique keys """
myinfo = {'name': 'Noha Shehab', 'age': 30, 'work': 'ITI', 'name': "Ali"}
print(myinfo)

"get len of the dict "
print(len(myinfo))
print(myinfo.__len__())

myinfo['age'] = 'Thirty'  # update exisiting values

"""add new element to the dict  """
myinfo['city'] = 'Cairo'
print(myinfo)

# myinfo.city = 'cairo'

myinfo['courses'] = ['python', 'django', 'flask']
print(myinfo)

""" pop pair the dict ? """

# popped_value=myinfo.pop("name")
# print(popped_value)
# print(myinfo)

""" check if item exists in the dict ? """
print(myinfo)
print('Ali' in myinfo)  # in operator --> check if element exists in the dict keys
print('name' in myinfo)

""" get dict keys, dict values , dict items"""
# keys = myinfo.keys()
# print(keys, type(keys))  # dict_keys  -> iterable object can be casted to list / tuple
# print('name' in keys)
# keys_list = list(keys)
# print(keys_list)

values = myinfo.values()
print(values, type(values))  # dict_values  -> iterable object can be casted to list / tuple
print('Ali' in values)
values_list = list(values)
print(values_list)

items = myinfo.items()
print(items, type(items))  # dict_items  -> iterable object can be casted to list / tuple
print('Ali' in items)
items_list = list(items)
print(items_list)


""" loop over the dict """
""" print('Ali' in myinfo)"""
# for item in myinfo:
#     # print(item)
#     print(f"key={item}, value={myinfo[item]}")

for v in myinfo.values():
    print(v)


# for item in myinfo.items():
#     print(item)

# for key, value in myinfo.items():
#     print(f"key={key}, value={value}")

# for index, key in enumerate(myinfo.items()):
#     print(key)
#     print(f"{index}: key={key[0]}, value={key[1]}")

for index, (key, value) in enumerate(myinfo.items()):
    print(f"{index}: key={key}, value={value}")

""" update dict ? """
courses = {
    'name':"Mariam",
    'devops':['python'],
    'ai':['linux', 'python'],
    'gis':['mongo']
}

myinfo.update(courses)
print(myinfo)


""" clear key, value pair ---> """
# myinfo.clear()

###
