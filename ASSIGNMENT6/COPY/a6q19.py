# Create a list from the specified start to end index of another list.
li=[10,20,30,40,50,60,70,80,90]
print("The list is:",li)
start=int(input("Enter the starting index for the new list:"))
end=int(input("Enter the ending index:"))
li_new=li[start-1:end]
print("New list:",li_new)
