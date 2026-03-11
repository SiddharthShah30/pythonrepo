# Rules for Validation:
# 1. Username should not be more than 15 characters
# 3. Must not contain spaces
# 3, Must not contain digits

username = input("Enter a username: ")


if len(username) > 15: # Rule 1 Completed
    print("Your username can't be more than 15 characters!")
elif username.find(" ") != -1: # Rule 2 Completed
    print("Your username can't contain spaces")
elif not username.isalpha():
    print("Your username can't contain numbers")
else:
    print(f"Welcome {username} to our portal!")
