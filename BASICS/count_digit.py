
#brute force approach.
def count_digits(N):
    counter = 0
    while N > 0:
        counter += 1           
        N //= 10                 
    return counter
print(count_digits(12345))



#optimal approach
import math
def count_digits(N):
    if N == 0:
        return 1
    return math.floor(math.log10(N)) + 1

inp= int(input("Enter the number: "))
dig=count_digits(inp)
print("Number of digits is", dig)