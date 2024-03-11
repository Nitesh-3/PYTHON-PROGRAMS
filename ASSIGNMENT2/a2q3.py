n=int(input("Enter any year to find whether it is leap year or not :"))

if (n%4==0 and n%100!=0)or n%400==0 :
    print(n,"is a leap year.")

else :
    print(n,"is a non leap year.")
