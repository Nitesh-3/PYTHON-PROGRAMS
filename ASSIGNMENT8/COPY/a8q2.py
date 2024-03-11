dic1={'name':'Nitesh', 'age':23, 'address':'Siliguri'}
key=input("Enter the key you want to search:")
key=key.lower()
if key in dic1:
    print(f"'{key}' present in the dictionary")
    print(f"The value of the '{key}' is:",dic1[key])
else:
    print("The key is not present in the dictionary")
