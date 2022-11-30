color1=input("Enter the colour list 1 seperated by space :").split()
color2=input("Enter the colour list 1 seperated by space :").split()
color3=set(color1)-set(color2)
print(list(color3))