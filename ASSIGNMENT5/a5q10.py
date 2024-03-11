#WAP to find the number of matching characters in a string



st1=str(input('Enter the first string :'))
st2=str(input('Enter the second string :' ))
n=0
for ch1 in st1:
    for ch2 in st2:
        if ch1==ch2:
            n+=1
            print('Matching character is :',ch2)
print("Number of matching characters =",n)

