s1=input("Enter the first string:")
s2=input("Enter the second string:")
s1new=s1.lower()
s2new=s2.lower()
count=0
for i in s1new :
    if i in s2new :
        count+=1
print("The number of matching characters are",count)
