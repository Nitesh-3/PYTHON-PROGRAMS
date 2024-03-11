class student :
    def setdata(self):
        self.roll=int(input("Enter the roll number :"))
        self.name=str(input("Enter your name :"))
        self.course=str(input("Enter your course :"))

    def putdata(self) :
        print("Entered roll is",self.roll)
        print("Entered name is",self.name)
        print("Entered course is",self.course)


s1=student()
s1.setdata()
s2=student()
s2.setdata()
s1.putdata()
s2.putdata()
