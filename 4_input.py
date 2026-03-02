# input() = A function that prompts the user to input data, Returns the entered data as string
#           the f-string is used only when we want to input a function with the print statement

"""
name = input("What is your name: ")
your_age = int(input("How old are you: "))

your_age += 1
print(f"Hello {name}")
print("HAPPY BIRTHDAY")
print(f"{name} is {your_age} years old.")
"""

# Excerise 1: Calculating the Area of Rectangle

length = float(input("Enter the length: "))
width = float(input("Enter the width: "))
area = length * width

print(f"The area of Rectangle is {area}cm²")

"""
To get the square powered (²) do the following:
Windows: Make sure numlock is on and then Alt + 0178
Mac: Control + Commond (CMD) + Sapce
"""

# Excerise 2: Shopping Cart Program

item = input("What item would you like to buy?: ")
price = float(input("What is the price for it?: "))
quantity = int(input("How many quantity would like to buy?: "))
total = price * quantity

print(f"You have bought {quantity} x {item}/s")
print(f"Your total is: Rs.{total}")