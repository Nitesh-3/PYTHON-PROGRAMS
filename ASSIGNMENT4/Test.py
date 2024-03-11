'''def fun(n):
    a=0
    m=n
    while n>0:
        r=n%10
        a=r+a*10
        n=n//10
    if a==m:
        print('The number is palindrome')
    else:
        print('The number is not palindrome')
n=int(input('Enter the number :'))
fun(n)'''
'''
def fun(n,r):
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
n=int(input('Enter the value of n :'))
r=int(input('Enter the value of r :'))
print('The combinotric value is ',fun(n,r))
'''
'''
n=int(input('Enter a number :'))
m=int(input('Enter a number :'))
mn=min(n,m)
i=1
while i<=mn:
    if n%i==0 and m%i==0:
        hcf=i
    i=i+1
print('The HCF is ',hcf)
'''
def fun(m,n):
    a=max(m,n)
    while True:
        if a%m==0 and a%n==0:
            return a
        else :
            a=a+1

n=int(input('Enter a  number'))
m=int(input('Enter a  number'))
print('The LCM =',fun(m,n))




