def count_dig(n):
    num=n
    count=0
    while n>0:
        temp=n%10
        if temp!=0 and num%temp==0:
            count=count+1
        n=n//10
    return count

input=int(input("Enter the number:"))
print(count_dig(input))