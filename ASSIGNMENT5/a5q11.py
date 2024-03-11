#WAP to remove all the duplicate from a given string in python.
s=str(input('Enter any string :'))
st=''
for i in s:
    if i not in st:
        st=st+i
    else:
        continue
print(st)
