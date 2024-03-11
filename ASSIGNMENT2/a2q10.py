x1=int(input("Enter the x coordinate of the first point :"))
y1=int(input("Enter the y coordinate of the first point :"))


x2=int(input("Enter the x coordinate of the second point :"))
y2=int(input("Enter the y coordinate of the second point :"))


x3=int(input("Enter the x coordinate of the third point :"))
y3=int(input("Enter the y coordinate of the third point :"))

if (y2-y1)/(x2-x1)==(y3-y2)/(x3-x2):
    print("The three points lies on a straight line .")


else :
    print("The three points doesn't lie on a srraight line")




