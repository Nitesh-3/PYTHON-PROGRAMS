n=("Hello!how are you ?")

#counting the number of spaces and length of string

l=0
sp=0
for ch in n:
    l+=1
    if ch ==' ':
        sp+=1

print("Spaces = ",sp)
print("Length =",l)

#counting the number of words is left


vc=0
v=["a","e","i","o","u","A","E","I","O","U"]
for ch in n :
    if ch in v :
        vc+=1
print("Vowel count = ",vc)








