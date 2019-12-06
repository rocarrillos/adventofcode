from csvToList import readToList

dataList = []
readToList('day2.csv', dataList)

def processOpcode(position, valueArray):
    inputLocation1 = int(valueArray[position + 1])
    inputLocation2 = int(valueArray[position + 2])
    outputLocation = int(valueArray[position + 3])
    if valueArray[position] == '1':
        valueArray[outputLocation] = str(int(valueArray[inputLocation1]) + int(valueArray[inputLocation2]))
        return True
    elif valueArray[position] == '2':
        valueArray[outputLocation] = str(int(valueArray[inputLocation1]) * int(valueArray[inputLocation2]))
        return True
    elif valueArray[position] == '99':
        return False
    else:
        print('something went wrong')
        return False

position = 0
while position < len(dataList) and processOpcode(position, dataList):
    position += 4

print(dataList[0])