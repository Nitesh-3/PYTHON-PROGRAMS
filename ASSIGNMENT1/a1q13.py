n=int(input("Enter a 5 digit number :"))
x=len(str(n))

if(x<5 or x>5):
       print("Enter a 5 digit number only.")

else :
       fifth=n%10
       fifth=fifth+1
       if len(str(fifth))>1:
           fifth = fifth%10
       a=n//10

       fourth=a%10
       fourth=fourth+1
       if len(str(fourth))>1:
            fourth=fourth%10
       b=a//10

       third=b%10
       third=third+1
       if len(str(third))>1:
            third=third%10
       c=b//10

       second=c%10
       second=second+1
       if len(str(second))>1:
           second=second%10
       d=c//10

       first=d+1
       if len(str(first))>1:
           first=first%10
       print("The number after adding 1 to each digit",first,second,third,fourth,fifth)
       
