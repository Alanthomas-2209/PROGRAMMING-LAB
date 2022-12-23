with open(r"file1.txt") as file1:
    lines = len(file1.readlines())
    print("Total Number of lines :", lines)

# file1 = open("file1.txt", "r")
# file2 = open("file2.txt", "w")
# for line in file1.readlines():
#     file2.write(line)
# file1.close()
# file2.close()
# file2 = open("file2.txt", "r")
# for line in file1.readlines():
#     file2.write(line)
# file2.close()
