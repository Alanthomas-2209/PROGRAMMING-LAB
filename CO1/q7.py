list1=[]
list2=[]
flag=0
str=input("Enter the integers in the first list seperated by space :")
list1=str.split()
str=input("Enter the integers in the second list seperated by space :")
list2=str.split()
if(len(list1)==len(list2)):
    print("list1 and list2 are equal in length")
else:
    print("list1 and list2 are not equal in length")
sum1=0
sum2=0
for i in list1:
    a=int(i)
    sum1+=a
for i in list2:
    a=int(i)
    sum2+=a
for x in list1:
    for y in list2:
        if x == y:
            print("atleast one value occur in both")
            flag=1
            break
    if(flag==1):
        break
if(flag==0):
    print(":value not occur in both")
if(sum1==sum2):
    print(":value not occur in both")
else:
    print("sums are not equal")