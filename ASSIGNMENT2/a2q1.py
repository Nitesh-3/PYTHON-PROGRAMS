cp=float(input("Enter the cost price of the item : "))
sp=float(input("Enter the selling price of the item : "))

if sp>cp :
    p=sp-cp
    print("There is a profit of ",p,"rupees while selling the item.")

else :
    l=cp-sp
    print("There is a loss of ",l,"rupees while selling the item.")
