#fibbonacci series
def fun(n):

    a=0
    b=1
    s=0
    print(a)
    print(b)
    for i in range(n-2):
        s=a+b
        a=b
        b=s
        print(s)

n=int(input('Enter a number range :'))
fun(n)