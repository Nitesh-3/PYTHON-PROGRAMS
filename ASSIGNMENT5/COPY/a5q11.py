s=input("Enter the string:")
snew=''
for i in s:
    if i not in snew:
        snew=snew+i
print("New string is:",snew)
