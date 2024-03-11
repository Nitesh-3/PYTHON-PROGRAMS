class person:
    count=0
    def __init__(self,name,dob,add):
        self.name = name
        self.dob=dob
        self.address=add
        person.count +=1

    def getname(self):
        print('The name of person is ',self.name)
    def getdob(self):
        print(f'The DoB of {self.name} is ',self.dob)
    def getaddress(self):
        print(f'The address of {self.name} is ',self.address)
    def setname(self):
        self.name=input('Enter the new name :')
    def setaddress(self):
        self.address=input('Enter the new address :')
    def getcount(self):
        print('The number of persons = ',person.count)

    def __str__(self):
        return f'The name is {self.name} and DoB is {self.dob} and address is {self.address}'


p1= person('Nitesh','10/08/2002','Banarhat')
p1.getname()
p1.getdob()
p1.getaddress()
p1.setname()
p1.setaddress()
p1.getcount()
print(p1.__str__())
