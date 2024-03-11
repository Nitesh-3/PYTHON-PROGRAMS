n=int(input("Enter a 5 digit number : "))
m=n
if (m<10000 or m>99999):
    
    print("Enter a 5-digit number only.")
    

else :
    rev=0
    for i in range(1,6):
        digit=n%10
        rev=rev*10+digit
        n=n//10

    print("The reverse of entered number",m,"is",rev)

    if m==rev:
        print("The entered number and reversed numbers are equal.")
    else:
        print("The entered number and reverse number are not equal.")
