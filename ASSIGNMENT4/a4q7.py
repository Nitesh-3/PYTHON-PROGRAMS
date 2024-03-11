def check_palindrome(n):
    t=n
    p=0
    while n>0:
        r=n%10
        p=r+p*10
        n=n//10
    if t==p:
        print('Number is palindrome')
    else:
        print('number is not palindrome')
n=int(input('Enter number:'))
check_palindrome(n)