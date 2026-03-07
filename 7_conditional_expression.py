# Conditional Expression = A one-line shortcut for the if-else statement (ternary operator)
#                          Print or assign one of two values based on a condtion
#                          X if condition else Y
#--------------------------------------------------------------------------------------------------------------------
num1 = float(input("Enter the 1st Number: "))
num2 = float(input("Enter the 2nd Number: "))

print(f"{num1} is Positive" if num1 > 0 else f"{num1} is Negative")
print(f"{num2} is Positive" if num2 > 0 else f"{num2} is Negative")

print(f"{num1} is Even" if num1 % 2 == 0 else f"{num1} is Odd")
print(f"{num2} is Even" if num2 % 2 == 0 else f"{num2} is Odd")

max_num = f"{num1} is greater than {num2}" if num1 > num2 else f"{num2} is greater than {num1}"
print(max_num)
