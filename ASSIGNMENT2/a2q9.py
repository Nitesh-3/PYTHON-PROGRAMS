l=int(input("Enter the length of the rectangle :"))
b=int(input("Enter the breadth of the retangle :"))

a=l*b
p=2*(l+b)

if a>p :
    print("Area of rectangle with lenght =",l,"and breadth =",b," is greater than its perimeter .")

else :
     print("Area of rectangle with lenght =",l,"and breadth =",b," is smaller than its perimeter .")
