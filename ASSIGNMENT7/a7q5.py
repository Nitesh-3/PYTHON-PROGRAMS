# Write a Python program to understand the use of global and nonlocal variables declared in a function
def outer():
    x='Hello'

    def inner():
        nonlocal x
        x='People'
        
    inner()
    print(a)
    print(x)
a=10
outer()
