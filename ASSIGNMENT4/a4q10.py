def fun(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact
    
n=int(input('Enter any number to find factorial :'))
m=fun(n)
print('The factorial is ',m)