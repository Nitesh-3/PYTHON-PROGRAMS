#WAP to calculate the length of string,avoid space

s=input('Enter the string to count its length :')
n=0
for i in s :
    if i==' ':
        continue
    n+=1
print('The number of characters in string =',n)
