ren=int(input("Enter any range :"))
num=[]
neg=0
pos=0
zer=0


for i in range(ren):
    num.insert(i,int(input("Enter number")))

for i in range(ren):
    if num[i]>0:
        pos += 1
    elif num[i]<0:
        neg += 1

    else:
        zer += 1

print("Negative values are",neg)
print("Positive value are",pos)
print("zero values are",zer)
    
