unit = int(input("ENter the unit "))
bill = 0
if unit<=50:
    bill = unit*0.5
    print("Total bill ",bill)
elif unit<=100:
    bill = unit*0.75
    print("total bill ",bill)
elif unit >= 100:
    bill = unit * 1.20
    print("total bill ",bill)
elif unit > 250:
    bill = unit * 1.50
    bill = bill + (bill*0.2)
    print("total bill ",bill)
 