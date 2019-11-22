import csv
import pprint
import collections

list_of_data = []
with open("databases.txt") as f:
    reader = csv.reader(f, delimiter = '\n')
    for row in reader:
        list_of_data.append(row[0][:9])


#print(list_of_data)

counter = collections.Counter(list_of_data)

pprint.pprint(counter)


