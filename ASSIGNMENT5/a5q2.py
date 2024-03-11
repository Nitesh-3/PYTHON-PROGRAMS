s=input('Enter a binary number:')
n=0
for i in range(len(s)):
    r=s[i]
    m=ord(r)-48
    n=n*10+m

t=n
i=0
b=0
while t>0:
    r=t%10
    b=b+r*(2**i)
    t=t//10
    i=i+1
print('Integer value is :',b)