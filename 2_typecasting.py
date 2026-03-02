# Typecasting: The process of converting a variable into different kind of form using: str(), int(), float(), bool()
# Can use type() to know the type of variable
name = "Bro"
age = 23
gpa = 3.1
is_a_student = True

# Typecasting for gpa:
print(int(gpa))

# Typecasting for age:
print(float(age))

# Typecasting age from a string would result into the following:
age = str(age)
age += "1"
print(age) # prints out "23" + "1" = "231"
