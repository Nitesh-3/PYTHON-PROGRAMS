#taking the length and breadth of rectangle and first printing the length and breadth without calling class method
class rectangle:
    def setdata(self):
        self.length=int(input("Enter the length of rectangle :"))
        self.breadth=int(input("Enter the breadth :"))

    def putdata(self):
        print('The entered length =',self.length)
        print('The entered breadth =',self.breadth)


r1=rectangle()
r1.setdata()
print(r1.length)
print(r1.breadth)
r1.putdata()
