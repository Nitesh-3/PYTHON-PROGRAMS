#Program to find the difference between two lists.
li1=[10,25,9,18,47,36]
li2=[18,10,65,9]
li3=[]
print("The lists are:",li1,"and",li2)
for i in li1:
    if i not in li2:
        li3.append(i)
print("The difference between two lists is:",li3)
