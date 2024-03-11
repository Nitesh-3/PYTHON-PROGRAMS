#convert a string into integer list.
ch='y'
ls=[]
l=[]
while ch=='y':
    ele=input("Enter the element:")
    ls.append(ele)
    ch=input("Do you want to continue | (y/n):")
print("The list is",ls)
for i in ls:
    l.append(int(i))
print(l)


