# wap to odd Frequency Characters
s=input("Enter the string:")
v=''
for i in s:
    count=0
    if i in s[s[i]+1:]:
       count+=1
       print(i,count)
    if count%2==0:
        print(i)

