#Write a program to match key values in two dictionaries.
d1={'key1':1,'key2':3,'key3':2}
d2={'key1':1,'key2':2}
for i in d1:
    if i in d2:
        if d1[i]==d2[i]:
            print(f"{i}:{d1[i]} is present in both d1 and d2")
