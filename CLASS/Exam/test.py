#Question 5

x1=int(input("Enter the x coordinate of first point :"))
y1=int(input("Enter the y coordinate of first point :"))

x2=int(input("Enter the x coordinate of second point :"))
y2=int(input("Enter the y coordinate of second point :"))

x3=int(input("Enter the x coordinate of third point :"))
y3=int(input("Enter the y coordinate of third point :"))

if ((y3-y2)/(y2-y1)==(x3-x2)/(x2-x1)):
    print("The entered points are in a straight line.")

else :
    print("The entered pints are not in a straight line.")

#question 1
'''
l1=[1,2,3,4,5,6]
print("Members of the first list are ",l1)
member=int(input("Enter the member to be inserted :"))
l1.append(member)
print("member after insertion are ",l1)
member1=int(input("Entered the member to be removed :"))
l1.remove(member1)
print("The list after removing member are",l1)
'''
#question 2
'''def fun(a,b) :
    c=a*b
    return c
x=int(input("Enter the first number to multiply :"))
y=int(input("Enter the second number to multiply :"))
fun(x,y)
print("The product of two numbers =",fun(x,y))
'''



















