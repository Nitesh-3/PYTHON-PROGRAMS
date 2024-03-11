# Program to print all numbers which are divisible by M and N in the list.
li=[4,6,8,10,12,14]
print("List is:",li)
num1=int(input("Enter the first divisor:"))
num2=int(input("Enter the second divisor:"))
print(f"Numbers which are divisible by {num1} and {num2} are:")
for i in li:
    if i%num1==0 and i%num2==0 :
        print(i)