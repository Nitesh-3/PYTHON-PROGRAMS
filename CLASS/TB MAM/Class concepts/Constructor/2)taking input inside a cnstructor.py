class rectangle :
    def __init__(self):
        self.length=int(input('Enter the length of the rectangle :'))
        self.breadth=int(input('Enter the breadth of the rectangle :'))
    def area(self):
        self.a=self.length*self.breadth
        print(f"The area of the rectangle is {self.a}")

    def perimeter(self):
        self.perimeter=2*(self.length+self.breadth)
        print(f'The perimeter of the rectangle is {self.perimeter}')


r1=rectangle()
r1.area()
r1.perimeter()
