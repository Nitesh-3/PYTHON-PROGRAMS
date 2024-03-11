n=int(input("Enter the amount required in hundreds : "))
amount=n*100

tens=amount//10
print("The number of notes of denominations 10 = ",tens)

fifties=amount//50
print("The number of notes of denominations 50 = ",fifties)

print("The number of notes of denominations 100 = ",n)
