n=int(input("Enter a number with upto 5 digits :"))
x=len(str(n))
if x>5 :
    print("Enter a five digit number only .")
else :
    s=0
    e=0
    rev=0

    for i in range (1,x):
        
        a=n%10
        s=s+a
        a=a//10

    print("Sum of digits = ",s)
