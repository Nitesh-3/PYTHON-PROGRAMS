class mydate:
    def setdate(self):
       self.date=int(input('Enter the day :'))
       self.month=int(input("Enter the month :"))
       self.year=int(input('Enter the year :'))
        
    def checkdate(self):
        if (1<=self.date<=30) and (1<=self.month<=12) and (1<=self.year):
            print(f"The entered date is {self.date}/{self.month}/{self.year}")
        else :
            print("Enter valid date.")
    def adddays(self):
        self.d=int(input('Enter the days you want to add :'))
        if self.d+self.date>30:
            self.m=(self.date+self.d)//30
            self.date=(self.d+self.date)%30
            self.month+=self.m
        else:
            self.date+=self.d
    def addmonths(self):
        self.m=int(input("Enter the months you want to add :"))
        if (self.month+self.m)>12:
            self.y=(self.month+self.m)//12
            self.month=(self.month+self.m)%12
            self.year+=self.y
        else:
            self.month+=self.m
    def addyears(self):
        self.y=int(input('Enter the years you want to add :'))
        self.year+=self.y
    def display(self):
        print(f'The date after adding n years to date is {self.date}/{self.month}/{self.year}')


d1=mydate()
d1.setdate()        
d1.checkdate()        
d1.adddays()        
d1.addmonths()        
d1.addyears()        
d1.display()        
