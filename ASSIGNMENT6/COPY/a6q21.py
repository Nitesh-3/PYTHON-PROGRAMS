# Iterate a list in reverse order.
li=[10,20,30,40,50]
l2=[]
print("The list is:",li)
for i in range(-1,-(len(li)+1),-1):
    l2.append(li[i])
print('The new list is :',l2)
