def square_root(number):
    if number < 0:
        raise ValueError("Cannot find square root of a negative number")

    guess = number / 2.0  # Initial guess

    for _ in range(100):  # You can adjust the number of iterations as needed
        guess = 0.5 * (guess + number / guess)

    return guess

# Example usage
number_to_find_square_root_of = 25
result = square_root(number_to_find_square_root_of)
print(f"The square root of {number_to_find_square_root_of} is approximately {result}")
