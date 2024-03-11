s=input('Enter string:')
d={}
for i in s:
    if i==' ':
        continue
    elif i in d.keys():
        d[i]=d[i]+1
    else:
        d[i]=1
m=d
max=0
for i in m.keys():
    if m[i]>max:
        max=m[i]
for j in m.keys():
    if m[j]==max:
        print('maximum frequent character in string is:',j)