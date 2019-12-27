# add, subtract, multiply, and divide
# enter in a number
# enter in a operator they want to use
# create 3 variables and store user input values
# convert user input into a number
num1 = float(input("Enter first number: "))
op = input("Enter operator: ")
num2 = float(input("Enter second number: "))

# figure out what operator user chose
# check to see if op equals +, -, /, or *
if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("Invalid operator")