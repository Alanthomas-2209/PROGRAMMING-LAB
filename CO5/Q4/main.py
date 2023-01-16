import csv
import pandas as pd

# specify the column names to be read from the CSV file
# columns = ['column1', 'column2']
#
# # read the CSV file and print the contents of the selected columns
# with open('file.csv', 'r') as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         print([row[col] for col in columns])

# specify the column names to be read from the CSV file
columns = ['column1', 'column2']

# read the CSV file and print the contents of the selected columns
df = pd.read_csv('file.csv', usecols=columns)
print(df)
