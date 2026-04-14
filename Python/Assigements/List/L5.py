li = [1,2,3,4,5]
print(li)
# found = []
find = int(input("Enter the number you want to find "))
for i in range(len(li)):
    if i == find:
        print(f"Your number is found {find}")
        break
else:
    print(f"Not found {find}")