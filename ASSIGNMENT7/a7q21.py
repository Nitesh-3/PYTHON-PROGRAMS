# Checks whether a string is palindrom or not

def isStrPalindrom(st):
    revst=''
    for i in st:
        revst=i+revst
    return st==revst
st=input('Enter the string')
if isStrPalindrom(st):
    print(st,'is palindrom')
else:
    print(st,'is not palindrom')
