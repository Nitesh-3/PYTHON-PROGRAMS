n=input("Enter a 5 digit number to find the sum of its digits : ")
if len(n)>5 or len(n)<5 :
    print("Enter a 5 digt number only")

else :
    s=int(n)
    count=0
    for i in range (1,6) :
        x=s%10       #  12345 % 10 = 5
        y=s//10      #  12345 // 10 = 1234
        s=y
        count=count + x

    print("The sum of given 5 digit number = ",count)
