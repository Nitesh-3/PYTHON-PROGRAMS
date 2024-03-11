def fun(str1,str2):
    s1=str1.lower()
    s2=str2.lower()
    count=0

    for ch1 in s1:
        for ch2 in s2:
            if ch1==ch2:
                count+=1

    return count


s1=input('Enter string1 :')
s2=input('Enter string2 :')
a=fun(s1,s2)
print('The total number of matched characters= ',a)
