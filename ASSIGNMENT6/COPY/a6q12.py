#Program to find the position of minimum and maximum elements of a list.
li=[]
num=int(input("Enter the number of elements you want to insert:"))
for i in range(num):
    ele=int(input("Enter the element:"))
    li.append(ele)
print("Your entered elements:",li)
min_ele=min(li)
min_ind=li.index(min_ele)
max_ele=max(li)
max_ind=li.index(max_ele)
print(f"The minimum element is {min_ele} at {(min_ind)+1} in {li}")
print(f"The maximum element is {max_ele} at {(max_ind)+1} in {li}")
