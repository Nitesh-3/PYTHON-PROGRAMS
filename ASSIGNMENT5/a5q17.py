st=input('Enter any string :')
c=0
for i in st:
    if 48>=ord(i) and ord(i)<=57 :
        continue
    elif 65<=ord(i) and ord(i)>=90 :
        continue
    elif 97<=ord(i) and ord(i)>=122:
        continue
    
    else:
        print('The special character is :',i)
        c+=1
if c!=0:
    print('The string has special characters')