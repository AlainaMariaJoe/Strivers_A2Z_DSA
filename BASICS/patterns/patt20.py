def pattern(n):
    for i in range(1,n+1):
            print("*"*i,end="")
            print(" "*(2*(n-i)),end="")
            print("*"*i,end="")
            print()
    for i in range(n,0,-1):
            print("*"*(i-1),end="")
            print(" "*(2*(n-i+1)),end="")
            print("*"*(i-1),end="")
            print()

inp= int(input("Enter the value of n: "))
pattern(inp)  
