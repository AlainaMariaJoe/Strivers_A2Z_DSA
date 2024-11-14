def data_size(x):
    if x== "character":
     return 1
    elif x== "integer" or x== "float":
     return 4
    elif x== "long" or x== "double":
     return 8
    else:
      return("Invalid data type")

inp=input("Enter the data type: ").lower()
size=data_size(inp)
print(size)
