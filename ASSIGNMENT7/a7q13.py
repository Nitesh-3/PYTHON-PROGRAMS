# Write a python program to reverse a string.

def reverseString(st):
    st2=""
    for i in st:
        st2=i+st2
    return st2

st=input('Enter the string:')
st1=reverseString(st)
print(f'Reverse of {st} is {st1}')
