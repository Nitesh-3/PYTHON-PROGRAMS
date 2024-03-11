# write a python program to access a function inside a function.

def outerFun():
    print('This is a outer function')
    def innerFun():
        print('This is a inner function')
    innerFun()

print('This is from main program')

outerFun()
