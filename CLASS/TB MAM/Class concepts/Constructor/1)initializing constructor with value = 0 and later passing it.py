#constructor is a special member method/function of a class which is automatically called when one object of a class is created/defined.
#used to initialize data members of the class
#special function(__init__)

class rectangle :
    def __init__(self):
        self.length=0
        self.breadth=0

    def putdata(self):
        print(f'The entered length is {self.length} and breadth is {self.breadth}')
        
    def setlengthbreadth(self):
        self.length=int(input("Enter the length :"))
        self.breadth=int(input("Enter the breadth :"))



r1=rectangle()
r1.putdata()
r1.setlengthbreadth()
r1.putdata()
