list = [1,3,5,8,6,89,100,-140]
min = float('inf')
max = float('-inf')
for element in list:
    if element >= max:
        max = element
    if element <= min:
        min = element
else:
    print(f"Max {max} and Min {min}")