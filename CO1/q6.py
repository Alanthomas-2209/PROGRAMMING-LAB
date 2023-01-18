s=[]
name=[]
n=int (input("How many names want to insert :"))
for i in range (0,n):
    name=input("Enter the name: ")
    s.append(name)
print(s)
sum=0
for join in s:
    j=join.count('a')
    sum+=j
print(sum)