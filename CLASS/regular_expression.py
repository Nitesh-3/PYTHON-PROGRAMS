import re

check=re.search(r'my name','Hello my name is Nitesh')
print(check)
print(check.group())
print('starting index :',check.start())
print('ending index :',check.end())



print(re.findall(r'[Mm]y','Hello My name is nitesh, my home is in Banarhat'))
print('Range',re.search(r'[a-zA-Z]','home'))
