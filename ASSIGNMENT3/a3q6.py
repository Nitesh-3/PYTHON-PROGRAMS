matchsticks=21
print("Number of matchsticks =",matchsticks)

while 1:

    n=int(input("Enter the number of matchsticks you want to pick :"))

    if n<=0 or n>4:
        print("Enter upto 1,2,3 or 4 matchsticks only.")

    else :
        matchsticks = matchsticks - n
        print("Number of matchticks left =",matchsticks)
        
        m=5-n
        print("Number of matchsticks computer can pick =",m)
        
        matchsticks=matchsticks-m
        print("Number of matchsticks left =",matchsticks)
        
        if matchsticks==1 :
            print("User lost the game :")
            break
