def pattern(n):
    for i in range(1,n+1):
        print("  "*(n-i),end=" ")
        print("* "*((2*i)-1))
    for i in range(n,0,-1):
        print("  " * (n - i),end=" ")
        print("* " *((2*i)- 1))

inp=int(input("enter the input: "))
pattern(inp)
