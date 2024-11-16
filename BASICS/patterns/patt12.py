def pattern(n):
    for i in range(1,n+1):
        for j in range(i):
           print(j+1,end=" ")

        for j in range(2*(n-i)):
            print("  ",end="")
            
        for j in range(i, 0, -1):
            print(j,end=" ")
        print()

inp=int(input("Enter the number: "))
pattern(inp)

