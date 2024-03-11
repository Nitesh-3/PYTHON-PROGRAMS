def addition(a,b) :
    c=a+b
    d=a-b
    e=a*b
    '''print("Sum =",c)
    print("Difference =",d)
    print("Product =",e)'''
    return c,d,e

x=int(input("Enter the value of x :"))
y=int(input("Enter the value of y :"))
sum1,sub,mul=addition(x,y)
print("Sum of two numbers =",sum1)
print("Difference of two numbers =",sub)
print("Product of two numbers =",mul)
