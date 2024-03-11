def  fun(n,r):
    f=1
    for i in range(1,n+1):
        f=f*i
    
    g=1
    for j in range(1,r+1):
        g=g*j

    h=1
    for k in range(1,n-r+1):
        h=h*k
    
    comb=f/(g*h)
    return comb
n=int(input('enter the value of n:'))
r=int(input('enter the value of r:'))
a=fun(n,r)
print(a)
'''
import math

n = 20
r = 20

result = math.comb(n, r)
print(result)

'''