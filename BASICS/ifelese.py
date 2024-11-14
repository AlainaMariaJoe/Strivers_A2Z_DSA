def compareNM(n,m):
    if n>m:
        return "greater"
    elif n==m:
        return "equal"
    else:
        return "lesser"
    
num1=int(input('Enter the first number: ' ))
num2=int(input('Enter the second number: ' ))
res=compareNM(num1,num2)
print(res)