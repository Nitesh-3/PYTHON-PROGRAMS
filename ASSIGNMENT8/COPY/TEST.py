'''dic1={'name':'Nitesh','age':23,'address':'Siliguri'}
key=input('Enter a key to check :')
key.lower()
for i in dic1:
    if key==i:
        print('The key is present')
        print(f'the key is {key} and its value is {dic1[i]}')'''
'''
d1={1:10,2:20,3:6}
d2={3:30,4:40,5:2}
d3={5:50,6:60}
for i in d3 :
    if i in d2:
        d2[i]=d2[i]+d3[i]
    else:
        d2[i]=d3[i]
for i in d2:
    if i in d1:
        d1[i]=d1[i]+d2[i]
    else:
        d1[i]=d2[i]

print(d1)''''''
d={'Name':'Nitesh','age':23,'department':'MCA'}
for i in d:
    print(i,':',d[i])
''''''
n=int(input('Enter the range of numbers :'))
d={}
for i in range (1,n+1):
    d[i]=i**2

print(d)
''''''
l1=[1,2,3,4]
l2=['Jan','Feb','March','April']
l3=dict(zip(l1,l2))
print(l3)
'''
d1={'Ram':20,'Shyam':21,'Ravi':32,'Govind':40}
l1=list(d1.values())
l1.sort()
print('The minimum element is',l1[0])
l1.sort(reverse=True)
print('The maximum element is',l1[0])
















