n=int(input("Enter a four digit number to find the sum of its first and last digits : "))

if len(str(n))<4 or len(str(n))>4 :
    print("Enter a 4 digit number only .")

else :
   ''' a=str(n)

    x=int(a[0])
    y=int(a[3])

    sum=x+y

    print("The sum of first and last digits = ",sum)

'''
   x=n
   a=n%10
   b=n//1000
   c=a+b
   print("The sum of first and fourth digit of ",x,"=",c)
