import csv
import pandas as pd

# sample dictionary
data = {'name': ['John', 'Mike', 'Sarah'],
        'age': [28, 35, 19],
        'city': ['New York', 'Los Angeles', 'Chicago']}

# write the dictionary to a CSV file
with open('data.csv', 'w', newline='') as csvfile:
    fieldnames = ['name', 'age', 'city']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for i in range(len(data['name'])):
        writer.writerow({'name': data['name'][i], 'age': data['age'][i], 'city': data['city'][i]})
    
    

# read the CSV file and display its contents
with open('data.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)



# # sample dictionary
# data = {'name': ['John', 'Mike', 'Sarah'],
#         'age': [28, 35, 19],
#         'city': ['New York', 'Los Angeles', 'Chicago']}
#
# # write the dictionary to a CSV file
# df = pd.DataFrame(data)
# df.to_csv('data.csv', index=False)
#
# # read the CSV file and display its contents
# df = pd.read_csv('data.csv')
# print(df)
