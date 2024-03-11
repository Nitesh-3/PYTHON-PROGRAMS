"""Write a program to print out all Armstrong numbers between 1 and 500"""
for num in range(1, 501):
    num_copy = num
    num_digits = 0
    armstrong_sum = 0

    # Count the number of digits
    while num_copy > 0:
        num_copy //= 10
        num_digits += 1

    # Calculate the sum of each digit raised to the power of the number of digits
    num_copy = num
    while num_copy > 0:
        digit = num_copy % 10
        armstrong_sum += digit ** num_digits
        num_copy //= 10

    # Check if the number is an Armstrong number and print it
    if armstrong_sum == num:
        print(num)


