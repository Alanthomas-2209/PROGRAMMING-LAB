dict={}
n=int(input("how many items want to insert :",))
for i  in range(n):
    key=int(input("Enter the key value  :" ))
    data=input("Enter the data :")
    dict[key]=data
print("Before sorting :")
print(dict)
print("After sorting :")
print("Ascending",sorted(dict.items()))
print("Descending",sorted(dict.items(),reverse=True))
