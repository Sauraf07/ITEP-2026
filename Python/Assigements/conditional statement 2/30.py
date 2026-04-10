l1 = int(input("ENter the 1st sides of a triangle "))
l2 = int(input("ENter the 2nd sides of a triangle "))
l3 = int(input("ENter the 3rd sides of a triangle "))
if l1 == l2 == l3:
    print("Equilateral tringle ")
elif l1 == l2 or l2 == l3 or l1 == l3:
    print("isosceles triangle")
else:
    print("scalene triangle")