def pattern(n):
    size = 2 * n - 1  # Grid size
    for i in range(size):
        for j in range(size):
            value = n - min(i, j, size - i - 1, size - j - 1)
            print(value, end=" ")
        print()  

inp =int(input("Enter the value: "))
pattern(inp)  

