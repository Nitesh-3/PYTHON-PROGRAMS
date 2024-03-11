x=int(input("Enter the x coordinate :"))
y=int(input("Enter the y coordinate :"))

if x==0 and y==0 :
    print("The point with given coordinates (0,0) lies on origin .")

elif (x>0 or x<0) and y==0 :
    print("The point with given coordinates (",x,", 0 )lies on x axis .")

elif (y>0 or y<0) and x==0 :
    print("The point with given coordinates ( 0 ,",y,")lies on y axis .")

else :
    print("The point with given cooordinates (",x,",",y,") doesn't lie on any of - x-axis,y-axis or origin.")
