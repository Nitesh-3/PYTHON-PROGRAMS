# Get input from the user
decimal_number = int(input("Enter a decimal number: "))

# Check if the entered number is negative
if decimal_number < 0:
    print("Please enter a non-negative decimal number.")
else:
    octal_number = 0  # Initialize octal number to store the result
    position = 1  # Position represents the current place value in octal

    # Convert decimal to octal using loops
    while decimal_number > 0:
        remainder = decimal_number % 8  # Get the remainder when dividing by 8
        octal_number += remainder * position  # Add the remainder to the octal number
        position *= 10  # Update the position for the next iteration
        decimal_number //= 8  # Update the decimal number for the next iteration

    # Display the result
    print(f"The octal equivalent is {octal_number}")
