for i in range(5):
    num1 = int(input("Enter 1st number: "))
    num2 = int(input("Enter 2nd number: "))
    oper = input("Select the operation (+, -, *): ")

    if oper == '+':
        print(num1 + num2)
    elif oper == '-':
        print(num1 - num2)
    elif oper == '*':
        print(num1 * num2)
    else:
        print("Wrong input. Please select a valid operation.")
