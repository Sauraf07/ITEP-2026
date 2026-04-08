ni = int(input("enter the number of items: "))
amount = 0
for i in range(ni):
    item = int(input("Enter the amount of items: "))
    amount = item + amount
if amount > 1000:
    amount =amount -  (amount * 0.1)
    print(" You get 10 percent discount and your amount is ",amount)
else:
    print("you dont get any discount and your amount is ",amount)