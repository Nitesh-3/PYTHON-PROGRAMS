#WAP to find the lcm of two numbers

def fun(x,y):
    a=max(x,y)

    while (True):
        if(a%x==0) and (a%y==0):
            return a
            
        else :
            a=a+1

a=int(input('Enter a number :'))
b=int(input('Enter another number :'))
lcm=fun(a,b)
print('LCM =',lcm)

