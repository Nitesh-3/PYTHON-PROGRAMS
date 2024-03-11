n=int(input("Enter the number of days for which your were late :"))


if n<=0:
    print("Enter the valid number of days .")
    
elif n>0 and n<=5 :
    a=.5*n
    print("Your fine is ",a)

elif n>5 and n<11:
    b=n-5
    c=b*1+2.5
    print("Your fine is ",c)
    
elif n>10 and n<=30:
    d=n-10
    e=d*5+2.5+5
    print("Your fine is ",e)

else :
    f=2.5+5+100
    print("Your membership is cancelled and fine is",f)
