#Remove all occurances a given element from the list.
'''l=[10,20,30,10,50,10,40,80]
lnew=[]
print("The list is",l)
ele=int(input("Enter the element to be remove:"))

for i in l:
    if ele==i:
        continue
    else: 
        lnew.append(i)
print("After removing",lnew)

'''
l=[10,20,30,10,20,30,40]
print('Initial list ',l)
ele=int(input('Enter the element to remove all occurences :'))
for i in l:
    if i==ele:
        l.remove(i)
print('After removing ', l)