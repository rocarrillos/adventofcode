import csv

def readToList(filename, array):
    with open(filename) as dataFile:
        dataReader = csv.reader(dataFile, delimiter=',')
        for row in dataReader:
            for item in row:
                array.append(item)

def readToNestedList(filename, array):
    with open(filename) as dataFile:
        dataReader = csv.reader(dataFile, delimiter=',')
        for row in dataReader:
            childList = []
            for item in row:
                childList.append(item)
            array.append(childList)

def readToTupleList(filename, array):
    with open(filename) as dataFile:
        dataReader = csv.reader(dataFile, delimiter=',')
        for row in dataReader:
            array.append((row[0], row[1]))