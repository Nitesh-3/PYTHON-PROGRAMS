#Program to create two lists with even and odd numbers from a list.
li=[]
li_odd=[]
li_even=[]
num=int(input("Enter the range:"))
for i in range(num):
    ele=int(input("Enter the element:"))
    li.append(ele)
print("Your entered list:",li)
for i in range(num):
    if li[i]%2==0:
        li_even.append(li[i])
    else:
        li_odd.append(li[i])
print("List with odd numbers:",li_odd)
print("List with even numbers:",li_even)


'''
l=[10,20,32,3,35,43,65]
l_o=[]
l_e=[]
for i in l:
    if i%2==0:
        l_e.append(i)
    else :
        l_o.append(i)
print('odd list',l_o)
print('even list',l_e)
'''