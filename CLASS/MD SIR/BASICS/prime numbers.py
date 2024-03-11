n=int(input("Enter any number to check whether it is prime or not :"))
count=0
for i in  range (2,n):

    if n%i==0:
        
        print(n,"is not a prime number.")
        break
        
    else :
        print(n,"is a prime number.")
        break
