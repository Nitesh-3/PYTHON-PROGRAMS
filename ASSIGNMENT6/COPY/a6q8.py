#Program to remove all elements in a range from the list.
l=[10,20,30,40,50,60,70,80,90]
print("The list is",l)
#lnew=[]
print(f"Enter the range between 1 to {len(l)} to remove")
start=int(input("Enter the starting point"))
end=int(input("Enter the ending point"))
'''
for i in range(len(l)):
    if i>=(start-1) and i<=(end-1):
        continue
    else:
        lnew.append(l[i])
print("After removing",lnew)
'''
del l[start-1:end]
print("After removing",l)
