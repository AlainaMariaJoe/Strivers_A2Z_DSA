def sum_of_digits_until_single_digit(num):
    # Continue summing the digits until a single-digit number is obtained
    while num >= 10:  # Keep looping as long as the number is 2 or more digits
        num = sum(int(digit) for digit in str(num))  # Sum the digits of the number
    return num  # Return the final single-digit result

# Example usage:
number = 9875
result = sum_of_digits_until_single_digit(number)
print(f"The single-digit sum of {number} is {result}.")
