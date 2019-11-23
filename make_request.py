import csv
import os

def read_file(file_name):
    list_of_elements = []
    with open(file_name) as f:
        reader = csv.reader(f, delimiter = '\n')
        for row in reader:
            list_of_elements.append(row[0])
    return list_of_elements
            

def make_request_ecgiddb(database_id):
    person_id = int(database_id[7:9])
    recording_id = int(database_id[14:])
    
    output_file_name = f'person_{person_id}_rec{recording_id}.csv' 
    request = f"rdsamp -r ecgiddb/{database_id} -c -H -f 0 -t 20 -v -ps > output/{output_file_name}" 
    os.system(request)


def make_request(database_id):
    output_file_name = database_id[:-1] + ".csv"
    #request = f"rdsamp -r challange/{database_id} -c -H -f 0 -t 20 -v -ps > output/{output_file_name}"
    request = f"rdsamp -r challenge/2018/training/{database_id} -c -H -f 0 -t 60 -v -ps -s 12 >output/{output_file_name}"
    print("requesting: ", request)
    os.system(request)

list_of_databases = read_file("databases.txt")

for database in list_of_databases:
    #print(database)
    make_request(database)

