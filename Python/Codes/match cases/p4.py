n = int(input("Enter number  : "))
match n:
    case x if x%2==0:print(f"{x} is even ")
    case _ :print(f"{x} is odd ")