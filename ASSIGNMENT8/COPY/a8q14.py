#Write a python program to convert more than one list to a nested dictionary.
l1=['S001','S002','S003','S004']
l2=['Adina Park','Leyton Marsh','Duncan Boyle','Saim Richards']
l3=[85,98,89,92]
d1={}
d2={}
for i in range(len(l2)):
    d1[l2[i]]=l3[i]
for i,j in zip(l1,d1.items()):
    d2[i]=dict([j])
print("Nested dictionary:")
print((d2))
