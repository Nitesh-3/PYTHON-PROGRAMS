#program 1

'''a=10
b=int(input('Enter the divisor :'))
try :
    s=a/b
    print(s)
except ZeroDivisionError :
    print('Exception caught')
print('End of program..')
'''
#program 2
'''
def valueat(s,ind):
    return s[ind]
s='MCASIT'
print(valueat(s,3))
print('End of the loop')
'''


#program3

print('')
def valueat(s,ind):
    try :
        return s[ind]
    except IndexError:
        print('Index error encountered')
s='MCASIT'
print(valueat(s,4))
print('End of the program.')


