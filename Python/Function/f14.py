def outer():
    x = 100
    def inner():
        print(f"Inside inner x {x}")

    print(f"Inside outer x : {x}")
    inner()

outer()