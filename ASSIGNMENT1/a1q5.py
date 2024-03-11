length=float(input("Enter the length of rectangle : "))
breadth=float(input("Enter the breadth of rectangle : "))
radius=float(input("Enter the radius of circle : "))

areaR=length*breadth
perimeterR=2*(length+breadth)
areaC=22/7*radius**2
perimeterC=2*22/7*radius


print("The area of rectangle = ",areaR)
print("The perimeter of rectangle = ",perimeterR)

print("The area of circle = ",areaC)
print("The perimeter of circle = ",perimeterC)
