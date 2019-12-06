from csvToList import readToList
from day2puz1 import processOpcode

dataList = []
readToList('day2.csv', dataList)

def execute(valueArray):
    position = 0
    while position < len(valueArray) and processOpcode(position, valueArray):
        position += 4
    return valueArray[0]

def findMoonLanding():
    for i in range(100):
        for j in range(100):
            dataArray = dataList[:]
            dataArray[1] = i
            dataArray[2] = j
            if execute(dataArray) == '19690720':
                print(i)
                print(j)
    print('completed')


findMoonLanding()