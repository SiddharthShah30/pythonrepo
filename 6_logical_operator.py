# logical operatrs = evaluate multiple conditions (or, and, not)
# Try to change the value of temp and is_raining to see the output of differnet operators and how it works

temp = 2
is_raining = True

#------------------------------------------------------------------------------------------------------------------------------------------------------
# or = at least one condition must be True
if temp > 35 or temp < 0 or is_raining: # You can also write in the following syntax: 0 > temp > 35
    print("Outdoor event is cancelled!")
else:
    print("Outdoor event is still ON!!!!")

#------------------------------------------------------------------------------------------------------------------------------------------------------
# and = both the conditions must be True
if 35 > temp and is_raining: # You can also write in the following syntax: 35 > temp > 0
    print("It is Cold!")
    print("It is raining outside!")
else:
    print("It is Warm")
    print("It is not raining outside!")

#------------------------------------------------------------------------------------------------------------------------------------------------------
# not = inverts the condition (not False, not True)
if 35 > temp > 0 and not is_raining: # You can also write in the following syntax: 35 > temp > 0
    print("It is Cold!")
    print("It is raining outside!")
else:
    print("It is Warm!")
    print("It is not raining outside!")