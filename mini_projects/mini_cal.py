operator = input("Enter an Operator (+ - * /): ")
num1 = float(input("Enter Your 1st Number: "))
num2 = float(input("Enter Your 2nd Number: "))

if operator == '+':
     print(num1 + num2)
elif operator == '-':
     print(num1 - num2)
elif operator == '*':
     print(num1 * num2)
elif operator == '/':
     print(num1 / num2)
else:
     print("Please Enter A Valid Operator from the List.")