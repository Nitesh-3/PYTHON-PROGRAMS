s=input('Enter string:')
d={}
for i in s:
    if i==" ":
        continue
    elif i in d.keys():
        d[i]=d[i]+1
    else:
        d[i]=1

m=d
n=list(m.values())
min=n[0]
for j in n[1: ]:
    if j<min:
        min=j

for k in m.keys():
    if d[k]==min:
        print('least frequent character in string is :',k)
