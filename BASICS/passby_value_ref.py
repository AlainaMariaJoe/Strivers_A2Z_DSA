def add_values(a,b):
    a=a+1
    b[0]=b[0]+2
    return a,b[0]

num1=int(input("Enter the number1: "))
num2=list(map(int,input("Enter number2: ")))
sum=add_values(num1,num2)
print(sum)