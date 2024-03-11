#Write a Python function that takes a list and returns a new list with unique elements of the first list.

def unique(li):
    unique_list=[]
    for i in li:
        if i not in unique_list:
            unique_list.append(i)
    return unique_list
li=[10,20,30,10,10,40,30,30,30,80,80]
print('The list is',li)

unique=unique(li)

print(f'list of all unique eliments is {unique}')



