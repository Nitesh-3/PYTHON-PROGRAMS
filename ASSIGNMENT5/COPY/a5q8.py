#wap to check if a string has at least one letter and one number
char_flag=False
num_flag=False

s=input("Enter the string to check:")
print("checking, whether the string has at least one letter and one number")
for i in s:
    if i.isalpha() :
        char_flag=True
    if i.isdigit() :
        num_flag=True
if char_flag and num_flag :
    print("true")
else :
    print("false")

