#WAP to check if a string has atleast on one letter and one number

st=str(input("Enter a string :"))
a=False
b=False
for i in st:
    if i.isalpha():
        a=True
    elif i.isdigit():
        b=True
if a and b :
    print("The string has atleast one letter and one number.")

else:
    print("The string doesn't has ateast one letter and one number.")
