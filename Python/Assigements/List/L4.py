l1 = [1,2,3,4,5]
ot = 0
et = 0
for i in l1:
    if i%2==0:
        et = et +i
    else:
        ot = ot +i
print(f"Total Even numbers {et}")
print(f"Total odd numbers {ot}")