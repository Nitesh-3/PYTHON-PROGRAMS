'''def fun(st):
    st1=''
    for i in st:
        st1=i+st1

    if st1==st:
        return 'Palindrome'
    else :
        return 'Not palindrome'
    
st=input('Enter a string :')
print(fun(st))'''
def fun1(l1):
    
    for i in range(1,31):
        i=i**2
        l1.append(i)
    return l1
l1=[]
print('The list of squares is ',fun1(l1))
