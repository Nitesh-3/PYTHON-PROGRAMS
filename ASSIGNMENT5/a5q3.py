#WAP to remove i th caharracter from the string

s=str(input('Enter a string :'))
n=int(input('enter the index from which you want to remove the string :'))
if n>=0 and n <=len(s)-1:
    st=s[0:n]+s[n+1:]
    print('The new string is',st)
