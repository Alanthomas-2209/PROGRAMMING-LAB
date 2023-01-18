dict1={}
dict2={}
n=int(input("how many items want to insert in first dictionary :",))
for i  in range(n):
    key=int(input("Enter the key value  :" ))
    data=input("Enter the data :")
    dict1[key]=data

n = int(input("how many items want to insert in second dictionary :", ))
for i  in range(n):
    key=int(input("Enter the key value  :" ))
    data=input("Enter the data :")
    dict2[key]=data
print("\n",dict1)
print("\n",dict2)

def merge(dict1, dict2):
    for i in dict2.keys():
        dict1[i]=dict2[i]
    return dict1
print("\nafter merging :")
dict3=merge(dict1,dict2)
# dict4={**dict1,**dict2}
# print(dict4)
print(dict3)
