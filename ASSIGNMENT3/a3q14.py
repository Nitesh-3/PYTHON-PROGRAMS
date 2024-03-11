year=0
cost=6000
am_earn=1000
salvage=2000
interest=0.12
altr=1
invest=0
while(altr>invest):
    year+=1
    altr=(1000*0.12)*year
    invest =1000*year-(6000-2000)
print('The life of machine in years is',year)