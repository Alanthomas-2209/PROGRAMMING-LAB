file1 = open('./football.txt', 'r')
file2 = open('file2.txt', 'w')

lines = file1.readlines()
for i in range(0, len(lines)):
    if i % 2 == 0: # array starts from 0
        file2.write(lines[i])
file1.close()
file2.close()

# opening the files and printing their content
file1 = open('football.txt', 'r')
file2 = open('file2.txt', 'r')
# reading and printing the files content
str1 = file1.read()
str2 = file2.read()
print("file1 content...")
print(str1)
print()
print("file2 content...")
print(str2)

file1.close()
file2.close()