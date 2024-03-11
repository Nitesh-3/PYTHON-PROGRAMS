#output 1 2 3 4 5 6 7 8 9 10 \nout of the loop
'''
i=1
while i<=50:
    print(i,end=' ')
    if i%10==0:
        break
    i+=1
print("\nOut of the loop")
'''

#number till where you want to add odd numbers 
'''
n=int(input("Enter a number till where you want to add odd numbers :"))
i=1
a=0
while i<=n:
    if i%2!=0:
        a=a+i
    i+=1
print(a)

'''
#sum of all the odd numbers till n
'''
s=0
n=int(input("Enter a number :"))
for i in range(1,n+1):
    if i%2!=0:
        s=s+i
print("sum =",s)
'''

#program to print in the order 1 Name \n 2 Name....upto n
'''n=int(input("How many times do you want to print thr name ? "))
name='name'
for i in range(1,n+1):
    print(i,end=' ')
    print(name)
'''
#program to find the summ of all the numbers till n
'''n=int(input("Enter a number upto where you want to add the numbers :"))
s=0
i=1
while i<=n:
    s=s+i
    i+=1
print(s)
    '''
#table of a number

n=int(input("Enter the number whose table you want :"))
for i in range(1,11):
    m=n*i
    print(n,"*",i,"=",m)






