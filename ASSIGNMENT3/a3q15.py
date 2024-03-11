for i in range(0,9):
    p=float(input("Enter the value of principal :"))
    r=float(input("Enter the rate of interest :"))
    t=float(input("Enter the time :"))
    q=float(input("Enter the number of times interest neds to be calculated per year :"))

    
    a=p*(1+r/(100*q))**(t*q)
    

    print("The amount for inputted values of principal,interest,time,number of times interest calculated per year =",round(a,2))
