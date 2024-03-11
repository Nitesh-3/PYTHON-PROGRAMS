# Write a python script to generate and print a dictionary that contain a number (between 1 and n)in the form (x,x*x)
num=int(input("How many number of element do you want to have in the dictionary:"))
dic=dict()
for i in range(1,num+1):
    dic[i]=i*i
print(dic)
