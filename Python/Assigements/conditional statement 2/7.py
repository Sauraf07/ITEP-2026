nch = int(input("Number of classes held"))
nca = int(input("Number of classes attended."))
if (nca/nch)*100 >= 75:
    print("You are eligible to sit in the exam ")
else:
    print("you are not eligible to sit in the exam")