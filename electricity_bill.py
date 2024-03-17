unit = int(input("Enter Unit : "))

if unit<=50:
    charge = unit*0.5
elif unit<=150:
    charge = 25 + (unit-50)*0.75
elif unit<=250:
    charge = 100 + (unit-150)*1.2
else:
    charge = 220 + (unit-250)*1.5

bill = charge + charge*0.2

print("Bill = ",bill)

