# Task 1: create functions for each arithmetic operation

def add(*args):
    return sum(args)

def substract(a, b): # a - b
    return a-b

def multiply(*args):
    answer = 1
    for n in args:
        answer *= n
    return answer

def divide(a, b): # a / b
    if (b == 0):
        return "You cannot divide by 0!"
    return a / b

# Task 2: User input for numbers and operator

user_num1 = int(input("Enter your first number: "))
user_num2 = int(input("Enter your second number: "))
user_operator = input("Enter +, -, *, or /: ")

if (user_operator == "+"):
    print(add(user_num1, user_num2))
elif (user_operator == "-"):
    print(substract(user_num1, user_num2))
elif (user_operator == "*"):
    print(multiply(user_num1, user_num2))
elif (user_operator == "/"):
    print(divide(user_num1, user_num2))
else:
    print("Please select one of the listed operators next time.")

# Task 3: Handle zero division and other errors