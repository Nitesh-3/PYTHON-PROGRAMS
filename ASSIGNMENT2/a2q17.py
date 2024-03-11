n=float(input("Enter the time required by the worker to complete a particular job:"))

if 2<=n and 3>=n :
    print("You are highly efficient.")

elif 3<n and 4>=n :
    print("You must improve your speed.")

elif 4<n and 5>=n :
    print("Take training to improve your speed.")

elif n>5 :
    print("Kindly leave the company.")
else :
    print("Enter a valid time.")
