#input comma separated elements, convert into list and print
s=input("Enter elements separated by commas:")

print("Entered string:",s)

l=s.split(',')
print(l)
lnew=[]
for i in l:
    lnew.append(i)
print("The new list is:",lnew)

