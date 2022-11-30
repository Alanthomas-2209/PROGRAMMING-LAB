s=input("Enter the string :")
a=s[0]
new=s[1:]
x=new.replace(a,'$')
a=a+x
print(a)