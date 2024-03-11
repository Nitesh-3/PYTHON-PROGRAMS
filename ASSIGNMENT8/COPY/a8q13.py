#Write a python program to filter a dictionary based on values.
dic={'Cierra Vega':175,'Alden Cantrell':180,'Kierra Gentry':165, 'Pierre Cox':190}
print("The dictionary is",dic)
print("Marks greater than 170:")
new_dic={}
for i in dic:
    if dic[i]>170:
        new_dic[i]=dic[i]
print(new_dic)
