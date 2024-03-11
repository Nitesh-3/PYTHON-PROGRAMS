# Write a Python function to calculate the factorial of a number.

def fact(a):
    if a<0:
        return 'Number should be positive!!'
    elif a>0:
        fac=1
        for i in range(1,a+1):
            fac=fac*i
        return fac
    else:
        return 1

num=int(input('Enter the number'))
fac=fact(num)
print(f'The factorial of {num} is {fac}')

