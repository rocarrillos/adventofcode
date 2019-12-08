import csv

def csv_to_list(filename, array):
    with open(filename) as data_file:
        data_reader = csv.reader(data_file, delimiter=',')
        for row in data_reader:
            for item in row:
                array.append(item)

def csv_to_nested_list(filename, array):
    with open(filename) as data_file:
        data_reader = csv.reader(data_file, delimiter=',')
        for row in data_reader:
            childList = []
            for item in row:
                childList.append(item)
            array.append(childList)

def csv_to_tuple_list(filename, array):
    with open(filename) as data_file:
        data_reader = csv.reader(data_file, delimiter=',')
        for row in data_reader:
            array.append((row[0], row[1]))