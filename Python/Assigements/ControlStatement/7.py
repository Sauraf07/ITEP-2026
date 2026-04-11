num=int(input("Enter the number"))

if(num<=1):
    print("Not prime Number")
else:
  count=0

for i in range(2,num+1):
   
   if(num%i==0):
      count=count+1
   break
        
        