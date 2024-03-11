# check whether a number is perfect or not.
def isPerfect(a):
    sum=0
    for i in range(1,a):
        if a%i==0:
            sum=sum+i
    return sum==a
num=int(input('Enter the number'))
if isPerfect(num):
    print("the number is perfect")
else:
    print("The number is not perfect")
