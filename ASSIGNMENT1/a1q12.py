a=float(input("Enter the total selling price of 15 items : "))

b=float(input("Enter the total profit earned by selling 15 items : "))

if a>b :
    tcp = a-b
    cp = tcp/15
    print("The cost price of each item = ",cp)

else :
    print("Enter the valid values .")
