n=int(input("Enter the number whose factorial you want to take out :"))
fact=1
for i in range(1,n+1) :
    fact=i*fact
print("Factorial of the given number = ",fact)