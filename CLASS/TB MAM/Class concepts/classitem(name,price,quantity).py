class item :
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity

    def purchase(self):
        print(f'The item is {self.name}')
        self.no=int(input('Enter the quantity of items purchased :'))
        self.quantity=self.quantity-self.no

        
    def increasestock(self):
        self.num=int(input('Enter the quantity of increased stock :'))
        self.quantity=self.quantity+self.num

    def display(self):
        print('The price of item is :',self.price)
        print('The name of item is :',self.name)
        print('The quantity of item is :',self.quantity)


c1=item('Laptop',70000,50)
c2=item('TV',40000,100)
c1.purchase()
c1.increasestock()
c1.display()
c2.purchase()
c2.increasestock()
c2.display()
