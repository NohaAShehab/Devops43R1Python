""" any variable defined in the python script , module ---> global varaible """
# course = 'python'    # global
# """ you can access it anywhere in the script"""
# print(course)
# course = 'python and django'
# print(course)
""" access global variable from inside a function """
# course = 'python'  # global
#
#
# def printcourse():
#     # you can read course variable -global- from in side the function
#     print(f"----from inside the function course ={course}")
#
#
# printcourse()

""" ------ define variable in the function """



def printcourse():
    course = 'python'  # local variable for the function
    # any variable defined in the function--> scope --> localscope
    # variable can be accessed only inside the function
    print(f"----from inside the function course ={course}")

# printcourse()
# print(course)

# for item in range(10):
#     num= item+10
#
# print(num)



""" -----> result """


# def printcourse():
#     course = 'python'  # local variable for the function
#     # any variable defined in the function--> scope --> localscope
#     # variable can be accessed only inside the function
#     print(f"----from inside the function course ={course}")
#     return course
#
# c= printcourse()


""" modify global variable from inside a function """


# course = 'python'
#
# def modifycourse():
      # "modify global variable from inside a function"
#     global course  # please don't create new local variable use the global one
#     course = input("please enter coursename")
#     print(f"course= {course}===> in the function")
#
# modifycourse()
# print(f"course= {course}===> after the function")

""""""

# course = 'python'
#
# def modifycourse():
#     course = input("please enter coursename")
#     print(f"course= {course}===> in the function")
#     return course
#
# course=modifycourse()
# print(f"course= {course}===> after the function")


# course = 'python'

# def modifycourse():
#     global course
#     course= input("please enter coursename")
#     print(f"course= {course}===> in the function")
#     return course
#
# course=modifycourse()

##################


# course = 'test'
# def modifycourse():
#     global course
#     # course= input("please enter coursename")
#     print(f"course= {course}===> in the function")
#     return course
#
# print(course)
# modifycourse()
# print(course)
""" python support function inside a function """

# def outerfunction():
#     name = 'Ali'
#     def innerfunction():
#         print(f"from inner function {name}")
#
#     innerfunction()
#
# outerfunction()


# def outerfunction():
#     name = 'Ali'
#     def innerfunction():
#         name = 'Ahmed'  # new local variable for the inner function
#         print(f"from inner function {name}")
#
#     innerfunction()
#     print(f"from outer function {name}")
#
# outerfunction()


# def outerfunction():
#     name = 'Ali'
#     def modifyname():
#         nonlocal name
#         name = 'Ahmed'
#         print(f"from inner function {name}")
#
#     modifyname()
#     print(f"from outer function {name}")
#
# outerfunction()




# def outerfunction():
#     name = 'Ali'
#     def test():
#         def modifyname():
#             nonlocal name
#             name = 'Ahmed'
#             print(f"from inner function {name}")
#
#         modifyname()
#     test()
#     print(f"from outer function {name}")
#
# outerfunction()
#
# def outerfunction():
#     def test():
#         def modifyname():
#             nonlocal name
#             name = 'Ahmed'
#             print(f"from inner function {name}")
#
#         modifyname()
#     test()
#     print(f"from outer function {name}")
#
# outerfunction()




