def fun(n):
    s=0
    print('Enter the numbers :')
    for i in range(n):
        n=int(input(''))
        s=s+n
    return s
n=int(input('Enter the number of numbers you want to enter :'))
print('The sum is =' ,fun(n))