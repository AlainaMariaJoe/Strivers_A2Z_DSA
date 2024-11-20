def pattern(n):
    for i in range(n):
        print("*" * (n - i), end="")
        # Print spaces in the middle
        print(" " * (2 * i), end="")
        # Print decreasing stars on the right
        print("*" * (n - i))

    for i in range(n):
        # Print increasing stars on the left
        print("*" * (i + 1), end="")
        # Print spaces in the middle
        print(" " * (2 * (n - i - 1)), end="")
        # Print increasing stars on the right
        print("*" * (i + 1))

inp= int(input("Enter the value of n: "))
pattern(inp)

