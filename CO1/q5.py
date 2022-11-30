n=int(input("How many numbers want to insert -"))
li=[]
for i in range (n):
    t=int(input ("enter the integer :"))
    if(t>=100):
        li.append("over")
    else:
        li.append(t)
print(li)