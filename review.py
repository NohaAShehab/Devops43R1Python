
""" nested loop ? """


"""
3 
    [[1],[2,4],[3,6,9]]
"""

""" create 3 lists """

# num = input('please enter number: ')
## generate list of numbers ?

table =[]

count =0  # iterator --->
# range ?
# if num.isdigit():
#     num = int(num)
#     numrange = range(num)
#     print(numrange)
#     # Range object  ---> iterable object
#     for i in numrange:
#         print(i)

""" """

# if num.isdigit():
#     num = int(num)
#     numrange = range(1, num+1)
#     print(numrange)
#     # Range object  ---> iterable object
#     for i in numrange:
#         print(i)
#         newl = []
#         for j in range(1,i+1):
#             newl.append(i*j)
#
#         table.append(newl)
#
#     print(table)


""" mario pyramid """

# num = int(input("please enter num: "))
# print(num)

num = input("please enter number: ")
if num.isdigit():
    num = int(num)
    """
        *
       **
      ***
     ****
    
    """
    for i in range(1, num+1):
        print(f"{' '*(num-i)}{i*'*'}")
        # print(f"{i * '*'}")






