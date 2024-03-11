l=[1,2,3,4,5]
l_square=[]
l_cube=[]
print('The initial list is',l)
for i in l:
    a=i**2
    l_square.append(a)
    b=i**3
    l_cube.append(b)
print('The list of squares is :',l_square)
print('The list of cubes is :',l_cube)