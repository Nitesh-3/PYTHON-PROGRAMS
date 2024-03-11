#Write a python program to access the fifth value of each key from the dictionary.
dic={'x':[11,12,13,14,15,16,17,18,19],
        'y':[21,22,23,24,25,26,27,28,29],
        'z':[31,32,33,34,35,36,37,38,39]}
for i in dic:
    for j in range(9):
        if j==4:
            print(dic[i][j])
