import csv

dataList = []
with open('day3.csv') as file:
    dataReader = csv.reader(file, delimiter=',', quotechar='"')
    for row in dataReader:
        subList = []
        for item in row:
            subList.append(item)
        dataList.append(subList)

mapArray = []
mapRow = ['.'] * 20000
for i in range(20000):
    mapArray.append(mapRow[:])

def updateBoard(circuit, position, number):
    if circuit[position[0]][position[1]] != '.' and circuit[position[0]][position[1]] != number:
        circuit[position[0]][position[1]] = 'X'
    else:
        circuit[position[0]][position[1]] = number

def processWire(circuit, wire, position, number):
    try:
        for segment in wire:
            if segment[0] == 'U':
                for i in range(int(segment[1:])):
                    position = (position[0], position[1] + 1)
                    updateBoard(circuit, position, number)
            if segment[0] == 'D':
                for i in range(int(segment[1:])):
                    position = (position[0], position[1] - 1)
                    updateBoard(circuit, position, number)
            if segment[0] == 'L':
                for i in range(int(segment[1:])):
                    position = (position[0] - 1, position[1])
                    updateBoard(circuit, position, number)
            if segment[0] == 'R':
                for i in range(int(segment[1:])):
                    position = (position[0] + 1, position[1])
                    updateBoard(circuit, position, number)
    except IndexError:
        print('IndexError')
        print(position)

for i in range(len(dataList)):
    processWire(mapArray, dataList[i], (10000, 10000), str(i))

def findMinDistance():
    distances = []
    radius = 10000
    position = (radius, radius)
    for i in range(0, radius * 2):
        if i % 2000 == 0:
            print('%s percent done' %(i/200))
        for j in range(0, radius * 2):
            if mapArray[i][j] == 'X':
                distances.append(abs(position[0] - i) + abs(position[1] - j))
    print(min(distances))

findMinDistance()