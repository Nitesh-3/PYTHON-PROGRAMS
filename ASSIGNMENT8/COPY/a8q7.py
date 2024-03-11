#Write a python program to get the maximum and minimum values of a dictionary.
dic={1:25,2:32,3:10,4:20,5:16,6:9}
li=list(dic.values())
li.sort()
print("The minimum value is:",li[0])
li.sort(reverse=True)
print("The maximum value is:",li[0])
