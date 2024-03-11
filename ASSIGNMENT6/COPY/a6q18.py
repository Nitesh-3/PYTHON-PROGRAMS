# Program to remove duplicate elements from the list.
li=[10,20,30,10,20,50,60]
li_new=[]
print("The initial list is:",li)
for i in li:
    if i not in li_new:
        li_new.append(i)
print("The list after removing duplicates:",li_new)
