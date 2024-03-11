# Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.

def stringCounter(st):
    uc=0
    lc=0
    for i in st:
        if ord(i)>=65 and ord(i)<=90:
            uc+=1
        if ord(i)>=97 and ord(i)<=122:
            lc+=1
    return uc,lc
st=input('Enter the string to check:')
print(f'The number upper and lower case letters in {st} is {stringCounter(st)} respectively')
