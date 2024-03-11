n=int(input("enter a number : "))
i=2

while i<n:
    if n%i==0:
        print("it is not a prime number")
        break
    i=i+1
else :
         print("It is a prime number")
