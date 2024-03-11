no=int(input('Enter how many times you want to enter :'))
small=0
high=0
num=0
num=int(input('Enter the numberhgvyyv :'))
small=high=num
for i in range(1,no):
    num=int(input('Enter the number :'))
    if num>high:
        high=num
    elif num<small:
        small=num
range=high-small
print('The highest number is ',high)
print('The smallest number is ',small)
print('The range between two numbers is ',range)
