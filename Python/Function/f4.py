def modefy(a):
    a[2].append(5)
    pass

x = (1,2,[3,4])
print(f"Before modefy : {x}")
modefy(x)
print(f"After modefy : {x}")