def Pattern(n): 
 for i in range(n,0,-1):
    for j in range(i):
        print("*", end=" ")
    print()

inp=int(input("Enter the number: "))
Pattern(inp)
