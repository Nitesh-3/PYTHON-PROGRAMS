#WAP to print even length words in a string

s=str(input('Enter the string :'))
st=s.split()
for i in st :
    if len(i)%2==0:
        print(i,end=' ')
