# write a python function to product all the eliments in the list.

def productListEliment(list):
    product=1
    for i in list:
        product=product*i
    return product
li=[10,14,9,32,21]
print('The eliments of the list is',li)
pro=productListEliment(li)
print(f'The product of the eliments in list {li} is {pro}')
