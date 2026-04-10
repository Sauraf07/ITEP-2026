salary = int(input("Enter your salary: "))
if salary<=10000:
    print("HRA = 20%, DA = 80%")
elif salary <= 20000:
    print(" HRA = 25%, DA = 90% ")
elif salary > 20000:
    print(" HRA = 30%, DA = 95% ")