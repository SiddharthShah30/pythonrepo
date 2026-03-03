temp = float(input("Enter the temperature: "))
unit = input("Is this temperature in Celsius or Fahrenheit (C/F): ").upper()

if unit == "C":
    temp = round((9 * temp) / 5 + 32, 2)
    unit = "F"
    metric = "Fahrenheit"
elif unit == "F":
    temp = round((temp - 32) * 5 / 9, 2)
    unit = "C"
    metric = "Celsius"
else:
    print(f"{unit} is an invalid unit of measurement.")

print(f"Your temperature in {metric} is {temp}°{unit}")