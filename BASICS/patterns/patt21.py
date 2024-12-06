def pattern(n):
    print("*"*n)
    for i in range(1,n-1):
        print("*"*1,end="")
        print(" "*(n-2),end="")
        print("*"*1,end="")
        print()
    print("*"*n)


   
inp= int(input("Enter the value of n: "))
pattern(inp)  
    
