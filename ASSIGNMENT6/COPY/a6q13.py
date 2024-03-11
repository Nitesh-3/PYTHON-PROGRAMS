#Program to input ,append and print the list element.
l=[]
num=int(input("How many elements you want to enter:"))
for i in range(num):
    ele=int(input("Enter the element:"))
    l.append(ele)

print("Your list element is:",l)
