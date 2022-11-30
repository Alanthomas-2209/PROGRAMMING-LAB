num=int(input("How many data wants to insert "))
l=[]
total=0
for i in range(num):
    data=int(input("Enter the element :"))
    l.append(data)
    total=total+l[i]
print(total)