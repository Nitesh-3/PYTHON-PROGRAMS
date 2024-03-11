#method 1
'''n=int(input("Enter any number to check whether it is prime or not :"))
count=0
for i in  range (2,n):

    if n%i==0:
        
        print(n,"is not a prime number.")
        break
        
    else :
        print(n,"is a prime number.")
        break
'''

#wrong
n=int(input("Enter any number to check whether it is prime or not :"))

check=True
for div in range(2,n):
        if n%div==0:
            check ==False
            break

if check == False:
    prime(n,"is a not prime number .")

else :
    prime(n,"is a prime number")
