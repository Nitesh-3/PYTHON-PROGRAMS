year=int(input("Enter the year to check whether it is a leap year or not :"))

if (year%4==0 & year%100!=0) | year%400==0:
    print(year,"is a leap year.")

else :
    print(year,"is not a leap year.")
