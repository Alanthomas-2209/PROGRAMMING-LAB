num=int(input("Enter the base length of the pyramid :"))
mid=int(num/2)
for i in range(mid):
    for j in range(i+1):
        print("* ",end=" ")
    print()

for i in range(mid+1, 0, -1):
    for j in range(i):
        print("* ", end=" ")
    print()