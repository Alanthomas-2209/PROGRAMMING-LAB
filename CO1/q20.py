oddnum=[]
flist=[]
n=int(input("How many number wants to insert :"))
print("Enter the numbers :")

for i in range(n):
    data=int(input())
    flist.append(data)

for item in flist:
    if(item%2!=0):
        oddnum.append(item)

print("first list :",flist)
print("list after removing even numbers :",oddnum)