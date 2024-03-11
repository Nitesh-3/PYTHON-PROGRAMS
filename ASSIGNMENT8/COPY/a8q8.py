#Write a python program to create a dictionary from a string.
st="MCA1stSem"
c=1
dic=dict()
for i in st:
    dic[i]=c
    c+=1
print(dic)
