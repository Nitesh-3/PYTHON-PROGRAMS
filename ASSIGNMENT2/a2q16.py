s1=float(input("Enter the first side of the triangle :"))
s2=float(input("Enter the second side of the triangle :"))
s3=float(input("Enter the third side of the triangle :"))

if (s1==s2 and s1!=s3) or (s2==s3 and s2!=s1) or (s3==s1 and s3!=s2)and(s1!=0 and s2!=0 and s3!=0):
         print("It is an isosceles triangle.")


elif s1==s2 and s1==s3 and(s1!=0 and s2!=0 and s3!=0):
         print("It is an equilateral triangle.")



elif (s1!=s2 and s2!=s3 and s3!=s1) and(s1!=0 and s2!=0 and s3!=0):

    if (s1**2==s2**2+s3**2) or (s2**2==s1**2+s3**2) or (s3**2==s1**2+s2**2):
         print("It is a right angled triangle as well as scalene triangle.")
    else :
         print("It is a scalene triangle.")


else :
         print("Enter valid values")
