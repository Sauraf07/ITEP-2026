x = 500
def outer():
    x = 100
    def inner():
        x = 200
        print(f"Inside inner x {x}")
    inner()
    print(f"Inside outer x {x}")

outer()