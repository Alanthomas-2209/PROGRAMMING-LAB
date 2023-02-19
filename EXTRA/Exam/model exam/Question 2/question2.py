import csv
file1=open("auto.csv","r")
file2=open("details.txt","x")
fileread=csv.DictReader(file1)
for row in fileread:
    if int(row['price']) >1000000:
        file2.write(str(row)+"\n")
file1.close()
file2.close()