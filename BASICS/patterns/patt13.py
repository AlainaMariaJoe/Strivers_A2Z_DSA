def pattern(n):
    num=1
    for i in range(1, n+1):
        for j in range(i):
            print(num,end=" ")
            num+=1
        print()

inp=int(input("Enter the number: "))
pattern(inp)