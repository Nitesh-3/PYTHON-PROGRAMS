ram=int(input("Enter the age of Ram :"))
shyam=int(input("Enter the age of Shyam :"))
ajay=int(input("Enter the age of Ajay :"))
if ram<(shyam and ajay):
    print('Ram is youngest')
elif shyam<(ram and ajay):
    print('Shaym is youngest')
elif ajay<(ram and shyam):
    print('Ajay is youngest')