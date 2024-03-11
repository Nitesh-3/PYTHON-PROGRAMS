for i in range(1,11):
    print('Enter the working hour of employee',i)
    n=int(input())
    if n>40:
        m=n-40
        print('the overtime payment of employee =',m*12)
    else:
        print('There is no overtime payment for employee',i)
    
