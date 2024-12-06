def reverse_bits(n):
    result = 0
    for _ in range(32): 
        result = result << 1
        result = result | (n & 1) 
        n = n >> 1  
    return result

n = int(input("Enter the number: "))
reversed_n = reverse_bits(n)
print(reversed_n)  
