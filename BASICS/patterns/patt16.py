def pattern(n):
    for i in range(n):
        for j in range(i+1):
            print(chr(65+i),end=" ")
        print()

inp=int(input("Enter the number: "))
pattern(inp)