def outer():
    x = 100
    def inner():
        print(f"Inside inner x {x}")

    print(f"Outer function  x {x}")
    return inner

Inner = outer()
print("Hello..")
print("Hi  ")
Inner()