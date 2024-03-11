#. Write a Python program to print the even numbers from a given list.

def evenlist(li):
    evenlist=[]
    for i in li:
        if i%2==0:
            evenlist.append(i)
    return evenlist
li=[11,12,13,14,99,45,62,44]
print('The list is',li)
li1=evenlist(li)
print('list with all even number->',li1)
