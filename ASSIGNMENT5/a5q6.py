#WAP uppercase halfstring

#method1

s=str(input('Enter a string :'))
c=0
for i in s:
    c+=1
    a=c//2
    st=s[0:a]+s[a:c+1].upper()
print(st)



#method2
'''
s=str(input('Enter a string :'))
st=' '
for i in range(len(s)):
    n=len(s)//2
    if i >=n:
        st = st+s[i].upper()
    else:
        st=st+s[i]

print(st)
'''
