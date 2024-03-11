# Write a Python function to create and print a list where the values are square of numbers between 1 and 30 (both included)

def sqrlist(li):
    sqrli=[]
    for i in li:
        sqrli.append(i**2)
    print("the new list is",sqrli)
def li_init(li):
    for i in range(1,31):
        li.append(i)
    print('The list is',li)
    sqrlist(li)
li=[]
li_init(li)
