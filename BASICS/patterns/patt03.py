def Pattern(n): 
 for i in range(1,n+1):
    for j in range(i):
        print(j+1,end=" ")
    print()

inp=int(input("Enter the number: "))
Pattern(inp)
