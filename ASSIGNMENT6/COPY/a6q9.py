#Program to print the index of first matched element of a list.
l=[10,20,30,40,10,20,30,40,50]
print('Initial list :',l)
ele=int(input('Enter the element whose first matched index is to be printed :'))
for i in l:
    if i==ele:
        print(l.index(i))
        break
    
