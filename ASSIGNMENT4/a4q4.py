#WAP to calculate the HFC of given two numbers.

def fun(x,y):
    mn=min(x,y)
    i=1
    while i<=mn:
        if x%i==0 and y%i==0:
            hcf=i
        i+=1
    return hcf


n=int(input('enter a number :'))
m=int(input('Enter another number :'))
hcf=fun(n,m)
print(hcf)
