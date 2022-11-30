num=int(input("Enter the height of the pyramid :"))
for i in range(1,num+1):
    n=i
    for j in range(1,i+1):
        print(n, end=" ")
        n=n+i
    print("\n")