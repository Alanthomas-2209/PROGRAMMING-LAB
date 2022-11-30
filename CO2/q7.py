str=input("Enter the string :")
l = len(str)
if (l > 2):
    if str[-3:] == 'ing':
      str += 'ly'
    else:
      str += 'ing'
print(str)
