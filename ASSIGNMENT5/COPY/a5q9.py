s=input("Enter the string:")
v='aeiou'
vnew=''
s=s.lower()
for i in s:
    if i in v:
        vnew=vnew+i
print(vnew,len(v),len(vnew))
if len(v)==len(vnew):
    print("True")
else :
    print("Not allowed")
        
