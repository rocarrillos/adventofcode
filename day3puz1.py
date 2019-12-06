from csvToList import readToNestedList

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

def findMinDistance(radius, mapArray):
    distances = []
    position = (radius, radius)
    for i in range(0, radius * 2):
        if i % (radius / 5) == 0:
            print('%s percent done' %(i/(radius / 50)))
        for j in range(0, radius * 2):
            if mapArray[i][j] == 'X':
                distances.append(abs(position[0] - i) + abs(position[1] - j))
    return min(distances)

def execute():
    dataList = []
    readToNestedList('day3.csv', dataList)

    radius = 10000
    mapArray = []
    mapRow = ['.'] * 2 * radius
    for i in range(2 * radius):
        mapArray.append(mapRow[:])
    for i in range(len(dataList)):
        processWire(mapArray, dataList[i], (radius, radius), str(i))
    print(findMinDistance(radius, mapArray))

execute()