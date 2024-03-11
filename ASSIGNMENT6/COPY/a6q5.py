#Program to add an element at specified index in a list
l=[10,20,30,40,50]
ind=int(input(f"Enter the index between 0 to {len(l)} to insert a element:"))
ele=int(input("Enter the element to be inserted:"))
l.insert(ind,ele)
print(f"After the element{ele} at index {ind} insert",l)
