def specific(pos,value):
    num=[1,2,3,4,5,6]
    num.append(None)
    print(num)
    if pos > len(num):
      print("Invalid position")
      return 
    
    for i in range(len(num)-2,pos-1,-1):
            num[i+1]=num[i]
    num[pos]=value
    print(num)

specific(2,7)