weight = float(input("Enter your weight: "))
unit = input("IS the weight in Kilogram or Pound? (K or L): ").upper()

if unit == "K":
    weight *= 2.205
    unit = "Lbs."
    metric = "Pounds"
elif unit == "L":
    weight /= 2.205
    unit = "Kgs."
    metric = "Kilograms"
else:
    print("Enter a valid unit.")

print(f"You weigth in {metric} is {round(weight, 2)} {unit}")