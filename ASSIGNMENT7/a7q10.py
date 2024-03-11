# Write a python funvtion to find the max value of three number.

def maxofThree(a,b,c) :
    if a==b and b==c:
        return a
    else:
        max=a
        if b>max :
            max=b
        if c>max :
            max=c
        return max

num1=int(input('Enter the number:'))
num2=int(input('Enter the number:'))
num3=int(input('Enter the number:'))
num=maxofThree(num1,num2,num3)
print('The max of three is',num)
