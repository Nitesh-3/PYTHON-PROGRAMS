# WAP to use double asterick(*) character declare in a function
def person(**kwargs): # using double asterick we can pass as many argument as we want with different datatype
    for key, value in kwargs.items():
        print(f'{key}->{value}')

person(Name='Nitesh',Roll=22,Height=6)
