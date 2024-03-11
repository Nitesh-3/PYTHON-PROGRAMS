#15. frequency of specific character in a string

s=input('Enter string:')
c=input('Enter specific character in string:')
d=0
for i in s:
    if i==c:
        d=d+1
print('Frequency of specific character in string is',d)