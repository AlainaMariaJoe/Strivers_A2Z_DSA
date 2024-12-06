def pattern(n):
    x=1
    for i in range(1,n+1):
        if i%2==0:
            x=0
        else:
            x=1
        for j in range(i):
            print(x, end=" ")
            x=1-x
        print()
inp=int(input("Enter the number"))
pattern(inp)
