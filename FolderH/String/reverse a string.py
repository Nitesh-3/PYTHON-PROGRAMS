def fun(str1):
    reverse=''
    for i in range(len(str1)):
        reverse=str1[i]+reverse
    return reverse
a=input('Enter any string :')
st=fun(a)
print('The reverse of the entered string is',st)
