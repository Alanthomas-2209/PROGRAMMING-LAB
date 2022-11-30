
d={"january":31,"february":28,"march":31,"april":30,"may":31,"june":30,"july":31,"august":31,"september":30,"ocotber":31,"november":30,"december":31}
mon=input(print("Enter the month"))
print(d[mon])
re=input(print("Enter the month to delete"))
del d[re]
print("The dictionary after remove is : ",d)
print(sorted(d.items(),reverse=True))
s1=input(print("Enter the montth"))
s2=int(input(print("Enter the date")))
d[s2]=s1
