def sum_of_digits_until_single_digit(num):
    while num >= 10:  
        num = sum(int(digit) for digit in str(num))  
    return num  

# Example usage:
number = 9875
result = sum_of_digits_until_single_digit(number)
print(f"The single-digit sum of {number} is {result}.")
