# check a number is prime or not
from math import sqrt
def isnotprime(a):
    flag=False
    if a>1:
        for j in range(2, int(sqrt(a))+1):
            if a%j==0:
                flag=True
    return flag
num=int(input('Enter the number'))

if isnotprime(num):
    print(num,'is not a prime number')
else:
    print(num,'is a prime number')

