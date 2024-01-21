# define function
def  calculator ():
    num1 = int(input("enter num1: "))
    num2 = int(input("enter num2: "))
    operation = (input("+,- :"))

    if operation== '+':
        print(num1+num2)
    elif operation=='-':
        print(num1-num2)
    else :
        print("wrong input")


while True:
    calculator()
    user_input= input("do you want to continue yes/no : ")
    if user_input=='no':
      break

