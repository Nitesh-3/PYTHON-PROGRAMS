class rectangle :
    def setdata(self):
        self.length=int(input('Enter the length of the rectangle :'))
        self.breadth=int(input('Enter the breadth of rectangle :'))

    def putdata(self) :
        print('Entered length =',self.length)
        print('Entered breadth =',self.breadth)

    def area(self):
        a=self.length*self.breadth
        return print('Area =',a)

    def perimeter(self):
        p=2*(self.length+self.breadth)
        return  print('Perimeter =',p)

    def setlength(self):
        self.length=input("Enter your new length :")

d=rectangle()
d.setdata()
d.putdata()
d.area()
d.perimeter()
d.setlength()
d.putdata()
