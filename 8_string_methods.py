# String: Just a bunch of Characters (char)
# If you want to check all the types of string functions use, print(help(str))

name = input("Enter Your Full Name: ")
phone_number = input("Enter your phone number: ")
result = len(name) # To find the lenght of the character [Includes the spaces between different string]

print(phone_number.find("-"))
print(phone_number.find(" "))
phone_result = phone_number.replace("-","").replace(" ","") # .replace() is used to replace a paticular char in string to a different char in string or even an entire string, just like find & replace in MS-OFFICE Suite
print(f"Your Phone number: {phone_result}")

o1 = input("Which character's first occurence you want to find (Use spacebar to find spaces): ")
o2 = input("Which character's last occurence you want to find (Use spacebar to find spaces): ")
find_first_occurence = name.find(o1) # To find the first position of the mentioned char in string
find_last_occurence = name.rfind(o2) # To find the last position of the mentioned char in string

print(f"Hello, {name}")
print(f"The lenght of your string is: {result}")
print(f"The first occurence of {o1} in {name} is {find_first_occurence}")
print(f"The last occurence of {o2} in {name} is {find_last_occurence}")

# If want the first letter of the string capital, use .capitalize()
capitalized = name.capitalize()
print(f"Your string in capitalized: {capitalized}")

# If want all the char in strings to be UPPER CASE, use .upper()
upper_case = name.upper()
print(f"Your string in UPPER CASE: {upper_case}")

# If want all the char in strings to be lower case, use .lower()
lower_case = name.lower()
print(f"Your string in lower case: {lower_case}")

# If want to validate if the string == strin type, use .isdigit()
validation = name.isdigit()
if validation == False:
    print("Your string is a string")
else:
    print("Your string is not a string")

# To check if there is numer of spaces in your string, use .isalpha()
validation2 = name.isalpha()
if validation2 == False:
    print("Your strings contains spaces or none aplphabatical characters")
else:
    print("Your strings DOES NOT contains spaces and is entirely an aplphabatical characters' string")
