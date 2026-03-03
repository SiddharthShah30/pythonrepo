# Remove the (#) to know the output. NOTE: Don't Remove the header (#) that is "Addition:", that will through an ERROR!
price = 10

#------------------------------------------------------------------------------------------------------------------------------------------------------
# Basic Arthmetic Signs

# Addition:
# price = price + 1
# price += 1

# Subtraction:
# price = price - 2
# price -= 2

# Multiplication
# price = price * 3
# price *= price

# Devision
# price = price / 2
# price /= 2

# Exponential
# price = price ** 2
# price **= price

# print(price)

# To find the remainder called as modulas
# remainder = price % 3
# print(remainder)

#------------------------------------------------------------------------------------------------------------------------------------------------------
x = 3.14
y = - 4
z = 5

result_x = round(x) # The result would be 3
result_y = abs(y) # The result would be (+) 4
result = pow(4, 3) # The result would be 64
result_max = max(x , y, z) # Would provide you the maximum value from the given variables
result_min = min(x, y, z) # Would provide you the minimum value from the given variables

#------------------------------------------------------------------------------------------------------------------------------------------------------
import math

# print(math.pi) # Provides you with the value of PI
# print(math.e) # Provide you with the value of Exponential e

math.sqrt(z) # Provides you the Square Root of the given value/ variable(s)
math.ceil(5.5) # Provides you the highest rounded value RESULT: 6
math.floor(5.5) # Provides you the lowest rounded value RESULT: 5

#------------------------------------------------------------------------------------------------------------------------------------------------------
# Excersie: Calculating the circumference and area:
# NOTE: First import the math pacakage by typing "import math"

raidus = float(input("Enter the radius of circlet: "))
circumference = 2 * math.pi * raidus
area = math.pi * pow(raidus, 2)

print(f"The circumferecne is: {round(circumference, 2)}cm")
print(f"The area is: {round(area, 2)}cm²")