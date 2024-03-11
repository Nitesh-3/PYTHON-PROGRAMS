s=input("Enter the string:")
l=list(s)
snew=''
i=0
while i<len(l):
    k=i
    while(i<len(l) and l[i]!=' '):
        i+=1
    if (ord(l[k])>=97 and ord(l[k])<=122):
        l[k]=chr(ord(l[k])-32)
    else :
        l[k]=l[k]
    if (ord(l[i-1])>=97 and ord(l[i-1])<=122):
        l[i-1]=chr(ord(l[i-1])-32)
    else :
        l[i-1]=l[i-1]
    i+=1
for i in range(len(l)):
    snew=snew+l[i]
print(snew)
