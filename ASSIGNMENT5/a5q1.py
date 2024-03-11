s=str(input('Enter the number as string :'))
n=0
for i in range (len(s)):
    a=s[i]
    b=ord(a)-48
    n=n*10+b
    
print(n)
print(type(n))
