def pattern(n):
    for i in range(1,n+1):
        print("* " *i)
        
    for i in range(n-1,0,-1):
        print("* " *i)
        

inp=int(input("Enter the number: "))
pattern(inp)