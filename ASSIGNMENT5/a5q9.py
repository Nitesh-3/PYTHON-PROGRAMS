st=str(input('Enter a string :'))
v={'a','e','i','o','u'}
s=st.lower()
if set(v).issubset(set(s)):
    print('The given string contains all vowels.')
else :
     print('The given string does not contains all vowels.')
