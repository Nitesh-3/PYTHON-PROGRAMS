st=str(input('enter any string'))
c=0
for i in st:
    if ord(i)>=48 and ord(i)<=57:
        c+=1
print(f'The numbers occurs {c} times')