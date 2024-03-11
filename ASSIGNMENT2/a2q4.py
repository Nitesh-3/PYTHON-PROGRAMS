a=1900
s=int(input("Enter any year after 1900 to find the day on 1st January of that year :"))
count=0

if a>=s :
    print("Enter the year after 1900")


else :
    n=s-a

    leap=n//4
    non_leap=n-leap
    days = leap*366  +  non_leap*365
    count=days%7

 

if count==0 : print("The day is Monday")

if count==1 : print("The day is Tuesday")

if count==2 : print("The day is Wednesday")

if count==3 : print("The day is Thursday")

if count==4 : print("The day is Friday")

if count==5 : print("The day is Saturday")

if count==6 : print("The day is Sunday")

