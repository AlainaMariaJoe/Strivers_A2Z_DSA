def Pattern(n): 
 for i in range(n):
    for j in range(n):
        print("*",end=" ")
    print()

inp=int(input("Enter the number: "))
Pattern(inp)