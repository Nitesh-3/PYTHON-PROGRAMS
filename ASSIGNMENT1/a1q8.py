num=int(input("Enter a 5 digit number to reverse its digits : "))

if len(str(num)) < 5 or len(str(num)) > 5:
    print("Enter a 5 digit number only.")

else :
    rev=0
    for i in range(1,6):
        digit=num%10
        rev=rev*10+digit
        num=num//10
    print("The reverse of given digit is ",rev)
        
    

