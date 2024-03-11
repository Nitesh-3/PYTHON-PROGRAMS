# Print list after removing EVEN numbers.
li=[11,12,13,14,15,16,17,18,19]
print("The list is:",li)
for i in li:
    if i%2==0:
        li.remove(i)
print("The new list is:",li)

