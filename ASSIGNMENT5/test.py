'''st=input('Enter a number as string :')
s=0
for i in range(len(st)):
    a=st[i]
    n=ord(a)-48
    s=s*10+n
print(s)
print(type(s))'''
'''
st=str(input('Enter the string :'))
n=int(input('Enter the idex from which you want to remove the ith character :'))
if n<=len(st) and n>0:
    s=st[0:n]+st[n+1:]
    print('The new string is ',s)
else:
    print('enter a valid index')'''
'''
st=str(input('Enter the string :'))
c=0
for i in st:
    if i==' ':
        continue
    else:
        c+=1
print('The number of characters in st =',c)
'''
'''
st=str(input('Enter the string'))
st=st.split()
for i in st:
    if len(i)%2==0:
        print(i,end=' ')
'''
'''
st=str(input('Enter the string :'))
n=len(st)
half=n//2
st1=''
st1=st[0:half+1].lower()+st[half:].upper()
print(st1)'''
'''
st=str(input('Enter a string :'))
a=False
b=False
for i in st:
    if i.isalpha():
        a=True
    if i.isdigit():
        b=True
if a and b:
    print('The string has atleast 1 alphabet and one number')
else :
    print('The string doesnt has atleast 1 alphabet and one number')
 '''   '''
st=str(input('Enter any string :'))
v={'a','e,','i','o','u'}
s=st.lower()
if set(s).issubset(set(s)):
    print('The string contains all vowels')
else:
    print('The string does not contain all vowels')
''''''
st1=str(input('Enter one string :'))
st2=str(input('Enter another input :'))
c=0
for ch1 in st1:
    for ch2 in st2:
        if ch1==ch2:
            c=c+1
print('Number of matching characters =',c)
'''
'''
st1=input('Enter any string:')
st2=''
for i in st1:
    if i not in st2:
        st2=st2+i
print('New string is',st2)
'''
'''
st=str(input('Enter any string :'))
s=str(input('Enter a specific '))
c=0
if s not in st:
    print('The character is not present in the string.')
else:
    for i in st:
        if i==s:
            c=c+1
    print(f'{s} appears {c} times in {st}')
''''''
st=str(input('Enter the string :'))
print('The odd occuring characters are :')
for i in st:
    c=0
    for j in st:
        if i==j:
            c+=1
    if c%2!=0:
        print(i)
'''
st=str(input('Enter anumber as string :'))
n=0
for i in st :
    a=ord(i)-48
    n=n*10+a

print('The number is ',n)
print(type(n))









