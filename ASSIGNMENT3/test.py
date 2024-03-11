
'''for i in range(1,501):
    n=i
    c=0
    armstrong_sum=0
    copy=n
    while n>0:
        a=n%10
        c=c+1
        n=n//10


    n=copy
    while n>0:
        a=n%10
        armstrong_sum=armstrong_sum + a**c
        n=n//10

    if copy==armstrong_sum:
        print(armstrong_sum)
    '''

for i in range(2,200):
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count=count+1
    if count==2:
        print(i)