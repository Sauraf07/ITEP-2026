age = int(input("enter your age : "))
match age:
    case x if x>1 and x<=10:print("child  ")
    case x if x>11 and x<=18:print("Teen ")
    case x if x>19 and x<=45:print("Adult ")
    case x if x>45:print("OLD IS GOLD ")