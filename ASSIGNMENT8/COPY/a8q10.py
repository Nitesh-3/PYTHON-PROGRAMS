#Write a python program to get the top three items in terms of cost in a shop.
d1={'dress':23,'pant':45,'shoe':12,'bungle':55,'book':8}
c=0
x=list(d1.values())
x.sort(reverse=True)
x=x[:3]
for i in x:
    for j in d1.keys():
        if (d1[j]==i):
            print(str(j)+":"+str(d1[j]))
