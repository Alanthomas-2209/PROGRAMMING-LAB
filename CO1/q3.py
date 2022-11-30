flist=[]
n=int(input("How many number wants to insert :"))
print("Enter the numbers :")

for i in range(n):
    data=int(input())
    flist.append(data)
pos=[]
for item in flist:
    if(item>0):
        pos.append(item)
print("+ve numbers in the list :",pos)

a=int(input("Enter the value of N :"))
square=[x**2 for x in  range(a+1)]
print("square upto number :",a,"is",square)

string=input("Enter a  word :")
vowel=[x for x in string if x in 'aeiouAEIOU']
print("vowels in :",string,"is",vowel)

str=input("Enter the string to find ordinal value :")
z=[ord(i) for i in str]
print("Ordinal value of :",str,"is",z)