# Write a program to map two lists into a dictionary.
key=['Name','Age','Address']
value=['Nitesh',23,'Siliguri']
print("Lists are",key,',',value)
dic=dict(zip(key,value))
print("After mapping======>")
print(dic)
