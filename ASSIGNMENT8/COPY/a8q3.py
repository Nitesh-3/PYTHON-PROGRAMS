dic1={1:10,2:20,4:6}
dic2={3:30,4:40,5:2}
dic3={5:50,6:60}
print("The dictionaries are:",dic1,dic2,dic3)
for i in dic3:
    if i in dic2:
        dic2[i]=dic2[i]+dic3[i]
    else:
        dic2[i]=dic3[i]
for i in dic2:
    if i in dic1:
        dic1[i]=dic1[i]+dic2[i]
    else:
        dic1[i]=dic2[i]
print("The resultant dictionary is:")
print(dic1)
