Physics = int(input("Enter the marks of Physics: "))
Chemistry = int(input("Enter the marks of Chemistry: "))
Biology = int(input("Enter the marks of Biology: "))
Mathematics = int(input("Enter the marks of Mathematics: "))
Computer = int(input("Enter the marks of Computer: "))
total_marks = Physics+Chemistry+Mathematics+Biology+Computer
percantage = (total_marks/500)*100
if percantage>=90:
    print("Grade A ",percantage)
elif percantage>=80:
     print("Grade B ",percantage)
elif percantage>=70:
     print("Grade C ",percantage)
elif percantage>=60:
     print("Grade D ",percantage)
elif percantage>=40:
     print("Grade E ",percantage)
elif percantage<40:
     print("Grade F ",percantage)