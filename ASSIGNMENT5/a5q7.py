#WAP to capitalize the first and last character of each word

s=str(input('Enter a string:'))
st= ''
l=s.split(' ')
for i in range (len(l)):
    for j in range(len(l[i])):
        if j==0 or j==len(l[i])-1:
            st=l[i][j].upper()
            print(st,end='')
        else:
            st=l[i][j]
            print(st,end='')

print(end=' ')
