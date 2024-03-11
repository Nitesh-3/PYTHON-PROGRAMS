s=0
f=1
for i in range(1,8):
    f=f*i
    n=i/f
    s=s+n
    n=n%n


print("Sum of the given series =",s)
