#WAP to print odd frequency characters in a string

s=str(input('Enter string from which odd frequency characters will be printed :'))
print('odd frequency character is :')
for i in range(97,123):
    c=0
    j=chr(i)
    for k in s :
        if k==j:
            c=c+1
    if c%2!=0:
        print(j)
