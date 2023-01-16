list=[]

file1 = open("file1.txt", "r")
# file2 = open("file2.txt", "w")
for line in file1.readlines():
    # file2.write(line)
    list.append(line)
file1.close()
print(list)
# file2.close()
# file2 = open("file2.txt", "r")
# for line in file1.readlines():
#     file2.write(line)
# file2.close()
 