import csv
import pandas
import os

path = os.getcwd()

fieldnames = ['Programming language', 'Designed by', 'Appeared', 'Extension']
data = [
    {'Programming language': 'Python', 'Designed by': 'Guido van Rossum', 'Appeared': '1991', 'Extension': '.py'},
    {'Programming language': 'Java', 'Designed by': 'James Gosling', 'Appeared': '1995', 'Extension': '.java'},
    {'Programming language': 'C++', 'Designed by': 'Bjarne Stroustrup', 'Appeared': '1985', 'Extension': '.cpp'}

]
f = open("text.csv", 'w')
fileWriter = csv.DictWriter(f, fieldnames=fieldnames, delimiter=",")
fileWriter.writeheader()
fileWriter.writerows(data)
f.close()

with open('text.csv') as file:
    fileReader = csv.reader(file)
    for line in fileReader:
        print(line)

# f = open('text.csv','r')
# fileReader = csv.DictReader(f)
# for line in fileReader:
#     print(line['Appeared'])


# C = {'Programming language': ['Python','Java', 'C++'],
#         'Designed by': ['Guido van Rossum', 'James Gosling', 'Bjarne Stroustrup'],
#         'Appeared': ['1991', '1995', '1985'],
#         'Extension': ['.py', '.java', '.cpp'],
#     }
# df = DataFrame(C, columns= ['Programming language', 'Designed by', 'Appeared', 'Extension'])
# export_csv = df.to_csv (r,path + '\pandaresult.csv', index = None, header=True) # here you have to write path, where result file will be stored
# print(df)

# with open(path + '\writeData.csv', mode='w') as file:
#     writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#
#     # way to write to csv file
#     writer.writerow(['Programming language', 'Designed by', 'Appeared', 'Extension'])
#     writer.writerow(['Python', 'Guido van Rossum', '1991', '.py'])
#     writer.writerow(['Java', 'James Gosling', '1995', '.java'])
#     writer.writerow(['C++', 'Bjarne Stroustrup', '1985', '.cpp'])
#
# result = pandas.read_csv(path + '\writeData.csv')
# print(result)
