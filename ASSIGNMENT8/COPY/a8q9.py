#Write a python program to print dictionary in table format.

dic={(0,0):'Biswas',(0,1):23,(0,2):'Siliguri',
        (1,0):'Nitesh',(1,1):23,(1,2):'Banarhat',
        (2,0):'Avijit',(2,1):21,(2,2):'Ranchi'}
print(" Name "," Age "," Place ")

for i in range(3):
    for j in range(3):
        print(dic[(i,j)],end="   ")
    print()
