# print("------- welcome to inputs module ----------")
year = 2023
def askforint(message):
    while True:
        num = input(message)
        if num.isdigit():
            return  int(num)
        print("---please enter valid number ----")

def askforstr(message):
    while True:
        inputstr = input(message)
        if inputstr.isalpha():
            return  inputstr
        print("---please enter valid string ----")


# num = askforint("please enter salary")
# print(num)