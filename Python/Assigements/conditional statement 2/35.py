temp = int(input("Enter the degree "))
choice = input("Enter the choice in what you want to see in (f/c)")
fer = (temp*9/5)+32
cel = (5/9) * (temp-32)
if choice == 'f':
    print(fer)
else:
    print(cel)


