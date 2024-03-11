s1=float(input("Enter the first side of the triangle :"))
s2=float(input("Enter the second side of the triangle :"))
s3=float(input("Enter the third side of the triangle :"))

if ((s1+s2)>s3 and (s2+s3)>s1 and (s3+s1)>s2):
    print("The values entered will make a valid triangle .")

else :
    print("The values entered will not make a valid triangle .")
