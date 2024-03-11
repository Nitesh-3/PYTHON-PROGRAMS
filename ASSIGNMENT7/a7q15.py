# Write a python function to check whether a number falls in a given range.

def checkNum(upper,lower,num) :
    if num>lower and num<upper :
        print('The Number is in the given number')
    else :
        print('The Number is not in the given number')
lower=int(input('Enter lower limit'))
upper=int(input('Enter upper limit'))
num=int(input('Enter the number'))
checkNum(upper,lower,num)
