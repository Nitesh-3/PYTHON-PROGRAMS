import math

x=float(input("Enter the x coordinate of the centre of the circle :"))
y=float(input("Enter the y coordinate of the centre of the circle :"))

r=float(input("Enter the radius of the circle :"))

x1=float(input("Enter the x coordinate of the point :"))
y1=float(input("Enter the y coordinate of the point :"))

d = math.sqrt(math.pow(x1-x,2)+math.pow(y1-y,2))

if d<r :
    print("The point lies inside the circle.")

elif d==r :
    print("The point lies on the circle .")

else :
    print("The point lies outside the circle.")
