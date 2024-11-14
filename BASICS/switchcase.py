import math
def switchCase(choice, arr):
    if choice == 1:
        return math.pi * (arr[0] ** 2)  
    elif choice == 2:
        return arr[0] * arr[1]  
    else:
        return "Invalid choice"  


choice = int(input("Enter the choice: "))
arr = list(map(int, input("Enter the inputs: ").split()))
res = switchCase(choice, arr)

if choice == 1:
    print("%.2f" % round(res, 2))  
else :
    print(int(res))  
 
