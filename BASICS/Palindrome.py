# Function to check if a number is a palindrome
def is_palindrome(num):
    # Convert the number to a string
    num_str = str(num)
    
    # Reverse the string and compare with the original string
    if num_str == num_str[::-1]:
        return True  # It's a palindrome
    else:
        return False  # It's not a palindrome

# Example usage:
number = 121
if is_palindrome(number):
    print(f"{number} is a palindrome!")
else:
    print(f"{number} is not a palindrome.")
