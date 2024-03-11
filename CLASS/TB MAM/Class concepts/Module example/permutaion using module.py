import module1
n=int(input("Enter the value of n :"))
r=int(input("Enter the value of r :"))
per=module1.fact(n)/module1.fact(n-r)
print("The permutation of entered value=",per)
