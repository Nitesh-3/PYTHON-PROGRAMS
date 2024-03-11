# write a python function to sum all the elements in the list.

def sumListEliment(li):
    sum=0
    for i in li:
        sum=sum+i
    return sum
li=[10,14,9,32,21]
print('The eliments of the list is',li)
sum=sumListEliment(li)
print(f'The sum of the eliments in list {li} is {sum}')
