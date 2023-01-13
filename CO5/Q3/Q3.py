import csv
import pandas
import os

path = os.getcwd()

# C = {'Programming language': ['Python','Java', 'C++'],
#         'Designed by': ['Guido van Rossum', 'James Gosling', 'Bjarne Stroustrup'],
#         'Appeared': ['1991', '1995', '1985'],
#         'Extension': ['.py', '.java', '.cpp'],
#     }
# path = getcwd()
# df = DataFrame(C, columns= ['Programming language', 'Designed by', 'Appeared', 'Extension'])
# export_csv = df.to_csv (r'C:\Users\Admin\Desktop\CODE\Alan\PROGRAMMING-LAB\CO5\Q3\pandaresult.csv', index = None, header=True) # here you have to write path, where result file will be stored
# print(df)

with open(path+'\writeData.csv', mode='w') as file:
    writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    # way to write to csv file
    writer.writerow(['Programming language', 'Designed by', 'Appeared', 'Extension'])
    writer.writerow(['Python', 'Guido van Rossum', '1991', '.py'])
    writer.writerow(['Java', 'James Gosling', '1995', '.java'])
    writer.writerow(['C++', 'Bjarne Stroustrup', '1985', '.cpp'])

result = pandas.read_csv(path+'\writeData.csv')
print(result)
