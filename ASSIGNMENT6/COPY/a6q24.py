l=[10,11,12,13,14,15,16,17,18]
print('The initial list is ',l)
l_new=[]
for i in l:
    if i%2==0:
        l_new.append(i)
    else :
        continue
print('list after removing odd numbers :',l_new)